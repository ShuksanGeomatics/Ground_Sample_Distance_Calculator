#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch/Shuksan Geomatics'
__date__ = 'April 2022'
__copyright__ = '(C) 2022, Gerry Gabrisch'

'''returns ground sampling distance(image spatial resolutionas cm / pixel), image width m, and image height m.
    This all assumes the image is a vertical image.'''

import sys
import traceback
try:
    #For P4P, P4P Advanced, P4Pv2, or P4P RTK use P4P
    
    def get_sensor_size(camera):
        #{'camera_id:(sensorbx in mm,  sensor y in mm, focal length in mm, image x in pixels, image y in pixels)
        cameras = {'P3P':(6.16, 4.62, 3.6, 4000, 3000),\
                   'P4P':(13.2, 8, 8.8, 5472, 3648),\
                   'Sequoia Monochrome':(4.8, 3.6, 3.89, 1280, 960 ),\
                   'Sequoia RGB':(6.175, 4.531, 4.88, 4608, 3456),\
                   'RedEdge-M':(4.8, 3.6, 5.5, 1280, 960),\
                   'ZenmuseP1-24':(35.9, 24, 24, 8192, 5460),\
                   'ZenmuseP1-35':(35.9, 24, 35, 8192, 5460),\
                   'ZenmuseP1-50':(35.9, 24, 50, 8192, 5460), \
                   'MotoG3':(5.05,3.744,2.5,3264,2448),\
                   'Hero5Black':(6.17, 3.47, 3, 2016, 1128),\
                   'SamsungS22Ultra':(96, 72, 6.4, 12000, 9000)}        
        
        
        if camera in cameras:
            camera = cameras[camera]
            return camera
        
        else:
            sys.exit('Unknown camera type - and unknown sensor size. Check camera_type input parameter for correct spelling')
        
       
    
    def get_ground_sampling_distance(camera_stats, AOG):
        
        sensor_width = camera_stats[0]
        sensor_height = camera_stats[1]
        focal_length = camera_stats[2]
        image_width = camera_stats[3]
        image_height = camera_stats[4]
        gsdw = ((sensor_width*AOG)/(focal_length*image_width))
        gsdh = ((sensor_height*AOG)/(focal_length*image_height))
        
        #gsdw and gsdh are in meters so convert that to cm.
        gsd = round(max([gsdw, gsdh])*100,3)
        
        #widths and heights are in cm so convert that to meters.
        ground_width = (gsd*image_width)/100
        ground_height = (gsd*image_height)/100
        return (gsd, ground_width, ground_height)
    
    
    def main():
        
        #####              USER-DEFINED INPUT PARAMETERS              #################
        
        camera = 'P3P'
        
        #camera altitude in meters above ground
        AOG = 300  
        
        
        
        
        #Get the sensor sizes, focal lenght, and image sizes for the input camera.
        camera_stats = get_sensor_size(camera)
        #Calculate GSD
        gsd = get_ground_sampling_distance(camera_stats, AOG)
        print('pixel resolution in cm = ', round(gsd[0],2))
        print ('ground footprint width in meters = ', round(gsd[1],1))
        print ('ground footprint height in meters = ', round(gsd[2],1))
        
        
        

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))
    
if __name__ == "__main__":
    main()