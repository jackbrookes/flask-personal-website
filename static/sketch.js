let x = 1;
let y = 1;
let easing = 0.1;
let nextBlink = 0;
let innerColor = 'cyan';

function setup() {
  var canvas = createCanvas(320, 150);
  rectMode(CENTER);
  canvas.parent('sketch-holder');
}

function draw() {

  background(51);
  fill(51);
  strokeWeight(3);
  stroke(255);

  headSize = min(width / 2, height / 2);
  line(width / 2 - headSize / 2, height / 2, width / 2 - headSize / 2, height);
  line(width / 2 + headSize / 2, height / 2, width / 2 + headSize / 2, height);
  arc(width / 2, height / 2, headSize, headSize, PI, 2 * PI);

  push();

  let targetX = mouseX;
  let dx = targetX - x;
  x += dx * easing;

  let targetY = mouseY;
  let dy = targetY - y;
  y += dy * easing;

  mX = min(x, width * 2.5) - width / 2;
  mY = min(y, width * 2.5) - height / 2;
  ipd = headSize / 4;
  pupilSize = 8;

  translate(width / 2, height / 2);

  translate(mX * 0.025, mY * 0.025);
  rect(0, 0, ipd * 4, pupilSize * 5);
  stroke(innerColor);
  rect(0, 0, ipd * 4 - 10, pupilSize * 5 - 10);

  // eyes
  stroke(255);
  translate(mX * -0.005, mY * -0.005);
  blink = millis() > nextBlink;

  if (blink) {
    line(-ipd / 2 - 1, 0, -ipd / 2 + 1, 0);
    line(ipd / 2 - 1, 0, ipd / 2 + 1, 0);
    if (millis() > nextBlink + 100) {
      nextBlink = millis() + random() * 3000;
      innerColor = random(['cyan', 'magenta', 'yellow'])
    }
  } else {
    line(-ipd / 2, pupilSize / 2, -ipd / 2, -pupilSize / 2);
    line(ipd / 2, pupilSize / 2, ipd / 2, -pupilSize / 2);
  }

  noFill();
  translate(mX * 0.005, mY * 0.005);

  offset = -(millis() % 1000) / 1000;
  translate(offset * mX * 0.01, offset * mY * 0.01);

  for (let i = 3 + offset; i < 9; i++) {
    stroke(255, 255, 255, 255 - (i - 1) * 255 / 8);
    translate(mX * 0.01, mY * 0.01);
    rect(0, 0, ipd * 4 * i / 2, pupilSize * 5 * i / 2);
  }


  pop();
}