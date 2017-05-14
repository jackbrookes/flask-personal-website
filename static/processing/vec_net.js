var particles = [];
var hw;
var hh;

function setup(){
  frameRate(24);
  max_dist = 50;
  var prnt = document.getElementById('p5-container');
  var positionInfo = prnt.getBoundingClientRect();
  canvas = createCanvas(positionInfo.width, positionInfo.height);
  canvas.parent('p5-container');

  // allows for different screen sizes to get same particle density
  var density = 0.0005;
  var area = positionInfo.width * positionInfo.height;


  colorMode(RGB, 255, 255, 255, 1)
  for (var i=0; i<area*density; i++)  {
    particles.push(new Particle());
  }

  hw = width/2;
  hh = height/2;

}

function draw() {
    t = millis()/(1000 / -3)
    for (var i=0; i<particles.length; i++)  {
      var exy = 0.2*Math.sin(t + particles[i].x/500);
      particles[i].move(exy);
    }

    background('#0B0E31');

    for (var i=0; i<particles.length; i++)  {
      particles[i].display();
    }
}

function Particle() {

  this.x = random(width);
  this.y = random(height);
  this.r = random(4, 8);
  this.bi = random(0, 0.3);
  this.bj = random(0, 0.3);
  this.i = this.bi * (Math.random() < 0.5 ? -1 : 1);
  this.j = this.bj * (Math.random() < 0.5 ? -1 : 1);

  var rng = Math.floor(random(0, 4));
  if (rng==0)
  {
    this.c = '#F74553';
  }
  if (rng==1)
  {
    this.c = '#7F9CA0';
  }
  if (rng==2)
  {
    this.c = '#FFAB98';
  }
  if (rng==3)
  {
    this.c = '#E5DBC0';
  }

  this.display = function()
  {
    noStroke();
    fill(this.c);
    ellipse(this.x, this.y, this.r, this.r);
  }

  this.move = function(ei2)
  {

    var xr = this.x - hw;
    var yr = this.y - hh;
    var theta = Math.atan2(xr, yr);

    var ej = 0.4 * Math.cos(theta);
    var ei = 0.4 * -Math.sin(theta);

    if (this.y > height+10){
      this.i = -this.bi;
      ei = -1;
      ei2 = 0;
    }

    if (this.y < -10){
      this.i = this.bi;
      ei = 1;
      ei2 = 0;
    }

    if (this.x > width+10){
      this.j = -this.bj;
      ej = -1;

    }

    if (this.x < -10){
      this.j = this.bj;
      ej = 1;

    }

    this.x = this.x + this.j + ej;
    this.y = this.y + this.i + ei + ei2;

  }

 }

function compare(a,b) {
  if (typeof a == 'undefined' && typeof b == 'undefined')
    return 0;
  if (typeof a == 'undefined')
    return 1;
  if (typeof b == 'undefined')
    return -1;
  if (a.tempdist > b.tempdist)
    return -1;
  if (a.tempdist < b.tempdist)
    return 1;
  return 0;
}

 function colorAlpha(aColor, alpha) {
  var c = color(aColor);
  return color('rgba(' +  [red(c), green(c), blue(c), alpha].join(',') + ')');
}
