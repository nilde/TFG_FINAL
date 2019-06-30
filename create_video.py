import cv2
import numpy as np
import os
from CONFIG import *
 
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
 
def main():
    convert_frames_to_video(PATH_IN, PATH_OUT, FPS)


#If report some kind of error justo open a terminal and type:
#
# ffmpeg -framerate 25 -pattern_type glob -i '*.png' \ -c:v libx264 -pix_fmt yuv420p out.mp4
#
#And will do exactly the same
if __name__=="__main__":
    main()
