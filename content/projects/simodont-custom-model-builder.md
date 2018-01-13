title: Simodont Custom Model Builder GUI
date: 2017-09-17
tags:
  - Python
pin_rank: 10
short_description: >
  A user friendly Python 3 application for developing models for use in the
  Simodont VR dental simulator.
meta_image: blog-images/smb-banner.png


*Note: This software is not in any way affiliated with MOOG.*

## Background

The Simodont system (MOOG) is an educational virtual reality dentistry simulator. It has a 3D display and high resolution haptics, allowing the user to use tools to interact with virtual tooth models in the virtual space. The haptic technology of the system allows for models to have varying ‘density’ – which changes the feeling of the interaction between the tool and the tooth. Parts of a model with low density feel soft and are more easily removed (less force required) using the drill – high density materials are harder and require more force from the user to remove. If one were to try to create custom models for the Simodont system for use in research or education, it involves a monotonous and technical processes. The Simodont Model Builder (SMB) presented here is a piece of software that has been developed which aims to streamline the process of creating models for use in the Simodont systems.

## The Simodont Model Builder

The SMB is a piece of software I developed in Python. It has been designed to be cross platform, fast, and scalable. It uses a GUI to allow researchers to create models while viewing the results in real-time. The nature of the models, being 3D, with multiple channels, makes creating an intuitive user-friendly interface for interacting with the data a significant challenge.

![Simodont model builder]({{ url_for('static', filename='blog-images/smb-ss.png') }})
*Above: Screenshot of the Simodont model builder GUI. Here we see a noise layer, masked with a cross shape (from a bitmap), overlaid on a rainbow bitmap applied to the top view.*

The image above is annotated to highlight the main features of the application:

A.	Model viewer – allows the user to view the models they are creating from the top, front or right side. This is done in such a way to replicate third angle orthographic projection, a commonly used standard for representing 3D objects in 2D.
B.	Model viewer controls – allows for manipulation of the way the data is displayed in the three views. The channel selector at the top changes which channel of data is currently displayed in the model viewer. The sliders are linked to the colour-coded dashed lines, which indicate the 2D ‘slice’ of voxels currently displayed. A slider for the zoom level can magnify of the views.
C.	Model settings and information – Allows the user to change the model name, model size and voxel size.
D.	Generators – Mini-programs used to generate data for use in the model. When clicked, the generator launches its own mini-application with its own settings and interface. See Generators section.
E.	Layers – When data is created using a generator, it creates a layer. Layers are composited on top of each other, from bottom to top, a common feature in creative software suites such as photoshop. Here we can delete and reorder layers, and can change the opacity, and the blend mode of the layers – which determines how the layer data interacts with the data in the layers below.

After the user creates a model, they can output the model into a .zip file containing all the necessary files for the Simodont systems, no files need to be manually edited. The generated zip file can then be uploaded to the Simodont system for use in research or education.

## Generators

Within the data for a model include the colour of each voxel, as well as the density of the voxel. Generators are mini-applications which create these data in whichever way they wish, which are then converted into a layer.
Currently, three generators are implemented, which allow for building basic models:

1.	Bitmap – Generates data from a 2D image. Images will be resized and stacked in a selected direction to make them three-dimensional.
2.	Noise – Generates 3D fractal noise using a perlin noise algorithm. Many parameters can be changed including the feature size and min/max value.
3.	Solid – Generates data based on a user selectable solid colour that is used for all voxels in the ‘color’ channel.

The Generator system is designed to be fundamentally flexible. In the future, if a researcher cannot create a model that suits their needs using the above tools alone, creating a new generator is a relatively simple task. If a newly created generator found is installed and passes validation checks a new button for that generator will appear.  An example of where this functionality may be if in the future there is a need to generate a realistic looking 3D tooth object. An algorithm that generates the necessary structure and converts it into voxels could be packaged in a generator, making the software a platform for development simple 3D data generation algorithms.

## Layering system

The layering system is a feature of the SMB which makes the application much more powerful. It allows users to combine data created by generators (‘layers’) to create a complex model. This also makes development of models less cumbersome, as individual layers can be deleted or tweaked without the need to start from scratch.

![Simodont model builder]({{ url_for('static', filename='blog-images/smb-layering.png') }})
*Diagram showing an example of the layering system, viewing the density channel. Left shows three layers, (1) from the solid generator, (2) from the noise generator, and (3) a mask layer from the bitmap generator. Result is Layer 2, masked by Layer 3, overlaid on Layer 1.*

## Future development

* Release software as open-source with developer guidelines
* Ability to render the model in isometric 3D for easier visualisation
* Improve clarity and user experience of layer system.
* Develop a custom file format for models, including layer data, that can be saved and edited later.


## Availability

The software is for use in my PhD but I will release the source code if requested - contact me.
