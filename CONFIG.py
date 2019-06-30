import os

########################################################################
#CONFIGURATION OF SCENE GENERATOR (scene_creator.py)
PATH_F="/Users/nildomene/Downloads/dataset/poses/"
FILENAME="04.txt"
USE_ORB_SLAM2=False
PATH_SEQUENCE_ORB="PATH_TO_DATASET_FOLDER/dataset/sequences/SEQUENCE_NUMBER"
#Same as specified in file kitti_orbslam2
PATH_FILE_ORBSLAM2="EXAMPLE.txt"
PATH_S="/Users/nildomene/Documents/GitHub/TFG/"
PATH_OBJ="./test.obj"
########################################################################


########################################################################
#CONFIGURATION OF VIDEO SEQUENCE CREATOR (create_video.py)
#Configuration info for creating the video from image sequence
PATH_IN= '/Users/nildomene/Downloads/2011_09_30-2/2011_09_30_drive_0016_extract/image_01/data/'
PATH_OUT = 'prueba.avi'
FPS =  25.0

########################################################################

########################################################################
#CONFIGURATION OF MERGE CLOUDS FILE (merge_clouds.py)

#Location of CloudCompare in the system
path_cc="./Applications/CloudCompare.app/Contents/MacOS/CloudCompare"
#Location of the sequence of velodyne points that want to merge
path_f="/Users/nildomene/Downloads/2011_09_30-2/2011_09_30_drive_0016_extract/velodyne_points/data/"
#Path where files will be saved
path_s="/Users/nildomene/Documents/"


#Subsampling needed for slower computers (steps will be N size ex. cloud_0,cloud_6,cloud_12,...)
#If you dont want to apply a sumbsampling set this to false
NEED_SUBSAMPLING=False
SUBSAMPLING_OCTREE_DEPTH=10


#Assign this to true if you want the normals of the merged cloud (needed for 3D surface reconstruction )
NEED_NORMALS=False

NEED_MERGES=True

#Assign true if you want to delete all previous files stored in the folder (that are related to clouds
# like transformation matrix, or norms previously calculated)
CLEAN_FOLDERS=True


#Total clouds that will be merged from 0 to AMOUNT_OF_CLOUDS (assign -1 if you want all clouds)
INITIAL_CLOUD=0
LAST_CLOUD=280
DIR_LIST_MERGE = sorted(os.listdir(path_f))

NUM_FRAG=40
########################################################################
