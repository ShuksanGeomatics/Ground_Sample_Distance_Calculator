#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch/Shuksan Geomatics'
__date__ = 'April 2022'
__copyright__ = '(C) 2022, Gerry Gabrisch'

'''returns ground sampling distance(image spatial resolutionas cm / pixel), image width m, and image height m.
    This all assumes the image is a vertical image.'''

import sys
import traceback
try:

    def get_sensor_size(camera_type):
        '''Different cameras have different sensors so return the correct sensor size.(W, H, focal length)'''
        if camera_type == 'P3P':
            sensor_size = (6.16, 4.62, 3.75)
        
        elif camera_type == 'P4P' or camera_type == 'Mavic Pro':
            #For P4P, P4P Advanced, P4Pv2, or P4P RTK use P4P
            sensor_size = (13.2, 8, 8.8)
        
        elif camera_type == 'Sequoia Monochrome':
            sensor_size = (4.8, 3.6, 4.0 )
        
        elif camera_type == 'Sequoia RGB':
            sensor_size = (6.175, 4.531, 4.0)
        
        elif camera_type == 'RedEdge-M':
            sensor_size = (4.8, 3.6, 5.5)
        
        elif type(camera_type) == tuple:
            sensor_size = camera_type
        
        else:
            sys.exit('Unknown camera type - and unknown sensor size. Check camera_type input parameter for correct spelling')
        
        return sensor_size
    
    def get_ground_sampling_distance(sensor_size, AOG, image_width, image_height):
        
        sensor_width = float(sensor_size[0])#mm
        sensor_height = float(sensor_size[1])
        focal_length = float(sensor_size[2])
        gsdw = ((sensor_width*AOG)/(focal_length*image_width))
        gsdh = ((sensor_height*AOG)/(focal_length*image_height))
        
        #gsdw and gsdh are in meters so convert that to cm.
        gsd = round(max([gsdw, gsdh])*100,3)
        
        #widths and heights are in cm so convert that to meters.
        ground_width = (gsd*image_width)/100
        ground_height = (gsd*image_height)/100
        return (gsd, ground_width, ground_height)
    
    
    def main():
           
        camera_type = str(sys.argv[1])
        AOG = float(sys.argv[2])
        image_width = float(sys.argv[3])
        image_height = float(sys.argv[4])
        sensor_size = get_sensor_size(camera_type)
        
        gsd = get_ground_sampling_distance(sensor_size, AOG, image_width, image_height)
        print('pixel resolution in cm = ', gsd[0])
        print ('ground footprint width in meters = ', round(gsd[1],1))
        print ('ground footprint height in meters = ', round(gsd[2],1))

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
    
if __name__ == "__main__":
    main()