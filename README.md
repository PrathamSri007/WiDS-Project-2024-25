# WiDS Project 2024-25: Enabling Gesture Control using Computer Vision
This is my report on the project that I took up under the "Winter in Data Science" program conducted by the Analytics Club, IIT Bombay.  
Duration: 10th December '24 - 25th January '25  
Link to project report: [WiDS Project Report](https://1drv.ms/b/c/0eae334f927a8cd3/ESDAduJdmXVHn03TX5V0m-sBsYBtvV85HWzi14vjV-4vcg?e=g3Jme7)

## Introduction
In this winter project, I have used the 'Hands' module of the library- Mediapipe to create cool projects enabling system control using hand gestures. These include volume control and mouse control using hands movements that would be captured using live video input stream.   

MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame. What this means is that if you supply a hand image to this module, it will return a 21 point vector showing the coordinates of 21 important landmarks present on your hand. To add, it is backed up by Google, so this gives another reason to use this library.  
Further information can be found on its [documentation page](https://mediapipe.readthedocs.io/en/latest/solutions/hands.html) .

## Determining the Hand Landmarks
Mediapipe Hands represents a 'hand' as a list of 21 hand landmarks, where each landmark is composed of x, y and z. x and y are normalized to [0.0, 1.0] by the image width and height respectively. z represents the landmark depth with the depth at the wrist being the origin, and the smaller the value the closer the landmark is to the camera.These landmarks are used to locate various points on our hand in the input video stream, and their variation would be used to command virtual control over our system.  

To ensure code reusability, I have created a module (HandTrackingModule.py) that contains all the important methods needed for hand detection and locating hand landmarks. I would be importing this module in my projects.

## Implementing Volume Control and Mouse Control
To implement volume control using our code, we need to install an external python package- pycaw. Pycaw is a Python library designed exclusively for controlling audio devices on Windows systems. It allows programmatic access to audio sessions, volume control, and sound device management on the Windows platform. This library will handle the controlling of our system volume. The documentation for the same can be found [here](https://github.com/AndreMiras/pycaw) .

For implementing virtual mouse control, we would be using the Mouse python library. The Mouse Module enables us to fully control our mouse through a variety of features, including hooking global events, registering hotkeys, simulating mouse movement and clicks, and much more. The documentation for the same could be found [here](https://github.com/boppreh/mouse#api) .

## My Learning Experience and Takeaways
This project broadened my horizons about the implementations of Computer Vision- especially gesture control. This project is a mere simplified implementation of virtual system control, which finds immense application in robotics, VR and AR, home automation systems, smart multimedia devices and much more. With the completion of this project, I am now capable of implementing gesture control for basic controls on my device. I am looking forward to learn more about this domain of study and build on technologies that could be used on a larger scale over larger systems with much more efficient application to simplify our day-to-day life activities.  

_Vision realized, with more to come._
