title: BounceBeat - Free VR Music Game
date: 2017-06-24
tags:
  - Unity
  - C#
short_description: >
  Virtual reality musical physics-based sandbox game, made in Unity, free and open source
pin_rank: 45
github_link: https://github.com/jackbrookes/bouncebeat
meta_image: blog-images/bouncebeat-logo.png

{% from 'macros.html' import vimeo %}
{{ vimeo('223177181') }}

## Information

![BounceBeat logo]({{ url_for('static', filename='blog-images/bouncebeat-logo.png') }})


I've been recently hacked together a new VR game. Its a musical sandbox game,
the idea is you can place "Spawners" in the world which will output beads. These
beads will make a sound when they hit a "BouncePad", the pitch of the sound being
dependent on the velocity. You can create as many as you like and move them around,
and theoretically create complex songs if you chain together sounds by changing the
tempo and instrument of the sounds.

* You can spawn objects by picking them up from your wrists
* You can snap objects rotationally using the index finger trigger
* There are two objects:
  * Spawner, which outputs beads
  * BouncePad
* Velocity scales the pitch of the sound when a bead hits a bouncepad
* You can change the tempo of a spawner using the thumbstick up/down while held
  * Left/right will cycle the instrument
* Supports Oculus Rift only (probably works with Vive via ReVive)

## Download

You can download the latest build zip file [here](https://github.com/jackbrookes/bouncebeat/releases)

And view the source code [on GitHub](https://github.com/jackbrookes/bouncebeat)
