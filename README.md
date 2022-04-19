# Ground_Sample_Distance_Calculator
## Calculates the pixel spatial resolution and image footprint from common drone cameras at different heights above ground.

This script estimates the pixel spatial resolution (in cm) and the resulting image footprint on land with width (in meters) and height (in meters) 
for a  drone camera capturing a vertical image.  

## Parameters
0.  the drone model.  Valid inputs include 'P3P', 'P4P'(includes P4P Advanced, P4Pv2, P4PRTK, or Mavic Pro),'Sequoia Monochrome', 'REDEDGE-M, or 'Sequoia RGB, 
1. The height above ground in meters
2. The output image width in pixels
3. The output image height in pixels


## Example of a command line option and output:   $ python gsd.py 'P4P' 120.1 5472 3648

![image](https://user-images.githubusercontent.com/71470542/164117821-89942935-676f-49eb-9e08-4d6be2138663.png)
