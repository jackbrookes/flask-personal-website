title: UXF - Unity Experiment Framework 
date: 2017-10-01
tags:
  - Unity
  - C#
  - VR
short_description: >
  A set of C# scripts which simplifies management of human-based experiments developed in Unity.
github_link: https://github.com/jackbrookes/uxf-unity-experiment-framework
pin_rank: 30
meta_image: blog-images/uxf-banner.png

This is a beefed-up version of my more simple [CSV logger](/posts/unity-csv-logger-for-experiments/) package I previously released, focusing on doing the difficult management of different stages of an experiment that are usually cumbersome. It also crucially allows for multithreaded File I/O which is especially important in VR applications where we can not afford for frame times to exceed the target.

## Features

* UI to load participant data from file (or add new participant data)
* Classes for common experimental concepts such as `Session`, `Block` & `Trial`
* Saves behavioural data to `.CSV` file, automatically handling file & directory naming
* Allows for tracking of position/rotation of any objects in the scene and writes to `.CSV`
* Writes files in a separate thread to avoid frame drops
* Cascading settings system, allowing setting independent variables at a Session, Block, or Trial level.
* Serialises and saves information to `JSON` files
* Helps create maintainable code using an Object-Oriented Programming style

## UI Screenshot

![User interface]({{ url_for('static', filename='blog-images/uxf-ss.png') }})

## Example

    :::csharp
    class ExperimentBuilder : Monobehaviour
    {
      // set this to your ExperimentSession instance in the inspector
      public ExpMngr.ExperimentSession exp;
      
      // call this function from ExperimentSession OnSessionStart UnityEvent in its inspector
      public void GenerateAndRun() 
      {
          // Creating a block
          var myBlock = new ExpMngr.Block(exp); 

          // Creating 10 trials within our block
          for (int i = 0; i < 10; i++)
              new ExpMngr.Trial(exp, myBlock);

          // Add a new setting to trial 1
          var firstTrial = myBlock.GetTrial(1);//trial number not 0 indexed
          firstTrial.settings["color"] = "red";

          // Run first trial
          exp.nextTrial.Begin();
      }

      ...

    }

See `Assets/ExpMngr/ExampleScript.cs` for another simple example.

## Documentation

[http://jackbrookes.github.io/unity-experiment-manager](http://jackbrookes.github.io/unity-experiment-manager)

## Usage

Download the project and open in Unity. Alternatively import the ```.unitypackage``` file to your existing Unity project.

Note: Users must change API Compatibility Level to .NET 2.0 in Unity player settings. 

See the full project on [GitHub](https://github.com/jackbrookes/unity-experiment-manager).  
