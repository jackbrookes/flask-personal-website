title: Geometric ripples in p5js
date: 2017-05-15
tags:
  - Processing
  - JavaScript
  - Mathematics
short_description: >
  Inspired by openprocessing.org, I made a looping geometric animation in p5js.  

{% include 'vec-net.html' %}

Source code:

    :::javascript
    var funkyBoxes = [[]];
    var ps;
    var ox;
    var oy;

    function setup(){

      // Allows canvas to scale to screen size
      var prnt = document.getElementById('p5-container');
      var positionInfo = prnt.getBoundingClientRect();
      canvas = createCanvas(positionInfo.width, positionInfo.height);
      canvas.parent('p5-container');
      //

      ps = 30; // element size
      var nx = Math.floor(width/ps) - 2;
      var ny = Math.floor(height/ps) - 2;
      noiseDetail(1,1);
      colorMode(HSB, 360, 100, 100);
      for (var i=0; i<nx; i++) {
        funkyBoxes[i] = [];
        for (var j=0; j<ny; j++)  {
          funkyBoxes[i][j] = new FunkyBox(i, j);
        }
      }
      ox = (width - (ps * nx))/2;
      oy = (height - (ps * ny))/2;
    }

    function draw() {

        background('#0B0E31');

        t = millis()/(1000);
        for (var i=0; i<funkyBoxes.length; i++)  {
          for (var j=0; j<funkyBoxes[i].length; j++)  {

            var v = 2*t + i + j + 5 * 2*noise(i/5,j/5,t/5);
            var st = 0.5 + 0.5 * spacedSin(v);
            var op = 1-st;

            push();
            translate(i*ps+ox, j*ps+oy);
            c = color(360 * noise(i/6,j/6,t), 25, 100);
            funkyBoxes[i][j].draw(st, c, op);
            pop();
          }
        }

    }

    function FunkyBox(i, j) {
      this.draw = function(st, c, op)
      {
        stroke(c);
        fill(0,0,0,0)
        var t = -8;
        var ips = ps-2*t;
        beginShape();
        vertex(t+st*ips, t+st*ips);
        vertex(ps-t, t);
        vertex(t+(1-st)*ips, t+(1-st)*ips);
        vertex(t, ps-t);
        vertex(t+st*ips, t+st*ips);
        endShape();
        stroke(c);
        var d = ps - 15;
        ellipse(ps/2, ps/2, d, d);
        fill(c);
        ellipse(ps/2, ps/2, d*op, d*op);
      }

    }

    function spacedSin(x){
      var xn = Math.abs(x % (2*Math.PI));
      if (xn < Math.PI/2){
        return Math.sin(x);
      } else if (xn > 3 * Math.PI/2) {
        return Math.sin(x - Math.PI);
      } else {
        return 1;
      }
    }
