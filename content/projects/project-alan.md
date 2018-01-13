title: Project ALAN
date: 2016-08-16
tags:
  - Presentation
  - Engineering
  - LabVIEW
short_description: >
  A project on developing tools to help make commercial rehabilitation robots viable.
pin_rank: 5
meta_image: blog-images/alan-banner.png

[NI Community Page](https://decibel.ni.com/content/docs/DOC-46580)

## Background

Project Advanced upper-Limb Autonomous Neuro-rehabilitation (ALAN) was part of a multidisciplinary Master's project a Leeds University. ALAN was tasked with bringing rehabilitation robotics to the mainstream. This would be achieved with the creation of two devices.

## MyPAM

Rehabilitation robotics has the potential to save huge amounts of time and money by providing physical assistance during the re-learning of motor skills in post-stroke patients. The MyPAM is an attempt at a home-based device, which includes a 2DOF robotic arm, and a PC & Monitor which can be used to play games and activities. These games and activities provide incentives for patients to continue to play and improve their skill.

![MyPAM]({{ url_for('static', filename='blog-images/mypam.jpg') }})  

### My contributions

* Local database of user's progress in the rehabilitation program. This database fetches tasks from a http JSON API which can allow physiotherapists to assign targets for patients.
* Inverse kinematics for the robot
* PID tuning for the robot
* Partial programming of FPGA controller
* Standard communication protocol between the robot controller and Unity3D based games
* Implementation of a basic game "Snake"

## ALAN-Arm

Robotic rehabilitation devices are often developed in a research setting, and unproven in terms of safety and reliability in the healthcare setting. The ALAN arm is a robotic arm device built to automate and standardise the testing procedure of devices like the MyPAM. The device can autonomously play Unity games developed for the MyPAM protocol to stress-test software and hardware of the devices. It can also be used to accurately re-trace a movement path, allowing for benchmarking of measurement systems of rehab robots. It features 3 independent 2DOF robots in a "puppet" form factor. 

![ALAN Arm]({{ url_for('static', filename='blog-images/alan-arm.jpg') }})  

### My contributions

* Inverse kinematics for shoulder, wrist & elbow
* Developed a biologically inspired human-arm model which generates plausible joint configurations for demand positions
* Implementation of master-slave control scheme where the shoulder and elbow are driven by hand/wrist position 
* PID tuning for the 3 robots
* Partial programming of FPGA controller
* Implementation of communication with Unity3D game
* Thorough testing of path reproducibility and frequency response

## Result

From this project I achieved a 1st class honours in MEng Mechanical Engineering. The project was recognised by National Instruments and awarded 1st place in their annual student competition. We were invited to present our devices in the expo hall and on stage at NIWeek 2016. 

[Watch the presentation on YouTube](https://www.youtube.com/watch?v=8WbgjWfF17g)

I also published a paper detailing the Alan-Arm design.

* **J. Brookes**, M. Kuznecovs, M. Kanakis, A. Grigals, M. Narvidas, J. Gallagher, M. Levesley, *"Robots testing robots: ALAN-Arm, a humanoid arm for the testing of robotic rehabilitation systems"* 2017 International Conference on Rehabilitation Robotics (ICORR), London, 2017, pp. 676-681. <http://doi.org/10.1109/ICORR.2017.8009326>