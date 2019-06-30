import os

#Check the comment inside if doesn't work and comment this line
os.system("python create_video.py")

#Reconstruct the scene using LIDAR data
os.system("python merge_clouds.py")

#Reconstruct the trajectory of the camera
os.system("python scene_creator.py")

