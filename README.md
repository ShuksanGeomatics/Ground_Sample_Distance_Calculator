# Ground_Sample_Distance_Calculator
##Calculates the pixel spatial resolution and image footprint from common drone cameras at different heights above ground.

This script calculates the pixel spatial resolution (in cm) and the resulting image footprint width (in meters) and height (in meters) 
for a  drone camera capturing a vertical image.  
Input parameters can be manually set in main() or the script can be executed from the command line.

##Parameters
0.  the drone model.  Valid inputs include 'P3P', 'P4P'(includes P4P Advanced, P4Pv2, P4PRTK, or Mavic Pro),'Sequoia Monochrome', 'REDEDGE-M, or 'Sequoia RGB'
1. The height above ground in meters
2. The output image width in pixels
3. The output image height in pixels
4. camera focal length

##Example of a command line option and output:   $ python gsd.py 'REDEDGE-M' 120 1280 960 5.5



Or better still, execute from your IDE and manually set the parameters in main() yourself.
