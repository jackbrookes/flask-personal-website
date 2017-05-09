title: LabVIEW smooth interpolation/filtering
date: 2016-10-01
tech:
  - LabVIEW
  - LabVIEW
short_description: Labview library that allows smooth filtering and interpolation for a discrete input, even with irregular timing.
github_link: https://github.com/jackbrookes/LabVIEW-smooth-interpolation

LabVIEW library that allows smooth filtering and interpolation for a discrete input, even with irregular timing.

The system uses a weighted moving average. It can be used with step inputs (for example the target position of an end effector robotic applications) and it will generate smooth a sinusoidal movement profile, ensuring no harsh spike in demand position. You can also set a velocity cap.

![alt tag](https://github.com/jackbrookes/LabVIEW-smooth-interpolation/blob/master/example_image.png?raw=true)
