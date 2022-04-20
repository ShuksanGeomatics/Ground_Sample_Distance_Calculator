# Ground_Sample_Distance_Calculator
## Calculates the pixel spatial resolution and image footprint from common drone cameras at different heights above ground.

This script estimates the pixel spatial resolution (in cm) and the resulting image footprint on land with width (in meters) and height (in meters) 
for common  drone cameras capturing a vertical image.  

## Parameters
0.  the drone model.  Some valid inputs include 'P3P', 'P4P'(includes P4P Advanced, P4Pv2, and P4PRTK),'Sequoia Monochrome', 'REDEDGE-M, or 'Sequoia RGB
1. The height above ground in meters

## Example of a command line option and output:   $ python gsd.py 'P4P' 120.1 5472 3648

![image](https://user-images.githubusercontent.com/71470542/164295754-b2f62e01-38e0-4214-9893-f51ca8c40d02.png)

If your camera is not listed you can add it to dictionary as 'YourName':(sensorwidth, sensorhight, focallength, imagewidth, imageheight)
Propeller Aero has a nice online calculator with many more drone camera models listed but sometimes you just need to do the calculation off line.
https://www.propelleraero.com/gsd-calculator/
