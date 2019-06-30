import os
import glob
import errno
from CONFIG import *




changeFragment=len(DIR_LIST_MERGE[INITIAL_CLOUD:LAST_CLOUD])/NUM_FRAG

os.chdir("/")

#Check if we need to create the container folder for the results
try:
    # Create target Directory
    os.mkdir("clouds")
    print("Directory " , dirName ,  " Created ")
except OSError as e:
    if e.errno == errno.EEXIST:
        print "Directory clouds already exists"



actualFragment=0
#Loop over the clouds merging it  
for i,v in enumerate(DIR_LIST_MERGE[INITIAL_CLOUD:LAST_CLOUD]):
    if(i%changeFragment==0 and actualFragment<=NUM_FRAG):
        actualFragment+=1
    #Needed to check if DS_Store isnt in the folder
    if v!=".DS_Store" and "REGISTRATION" not in v:
        #Need to use the first to clouds
        if i%changeFragment==0 or( i==1 and v[0]!=".DS_Store" ) or i+INITIAL_CLOUD==INITIAL_CLOUD:
            fullComand="sudo "+ path_cc+" -SILENT  -AUTO_SAVE OFF -o "+path_f+DIR_LIST_MERGE[i+INITIAL_CLOUD]+" -o "+path_f+DIR_LIST_MERGE[i+1+INITIAL_CLOUD]+" -ICP -RANDOM_SAMPLING_LIMIT 45000  -MERGE_CLOUDS -C_EXPORT_FMT PLY -PLY_EXPORT_FMT BINARY_BE -SAVE_CLOUDS FILE ./clouds/mergedX"+str(actualFragment)+".ply"
            os.system(fullComand)
        #From iter 2 to N uses the merged cloud made it before
        else:
            fullComand="sudo "+ path_cc+" -SILENT  -AUTO_SAVE OFF -o "+"./clouds/mergedX"+str(actualFragment)+".ply"+" -o "+path_f+DIR_LIST_MERGE[i+INITIAL_CLOUD]+" -ICP -RANDOM_SAMPLING_LIMIT 45000  -MERGE_CLOUDS  -C_EXPORT_FMT PLY -PLY_EXPORT_FMT BINARY_BE  -SAVE_CLOUDS FILE ./clouds/mergedX"+str(actualFragment)+".ply"
            os.system(fullComand)



if CLEAN_FOLDERS:
    r = [f for f in glob.glob("./clouds/*.ply") if "REGISTRATION" in f]
    for f in r:
        os.remove(f)

    r = [f for f in glob.glob("./clouds/*.ply") if "NORMS" in f]
    for f in r:
        os.remove(f)



if NEED_SUBSAMPLING:
    for i in range(1,NUM_FRAG+1):
        fullComand="sudo "+ path_cc+" -SILENT  -AUTO_SAVE OFF -o "+"./clouds/mergedX"+str(i)+".ply -SS OCTREE "+SUBSAMPLING_OCTREE_DEPTH+"  -C_EXPORT_FMT PLY -PLY_EXPORT_FMT BINARY_BE -SAVE_CLOUDS FILE ./clouds/mergedX"+str(i)+".ply"
        os.system(fullComand)




if NEED_NORMALS:
    for i in xrange(1,NUM_FRAG+1):
        os.system("sudo "+path_cc+" -SILENT  -AUTO_SAVE OFF -o ./clouds/mergedX"+str(i)+".ply  -OCTREE_NORMALS 0.18 -ORIENT_NORMS_MST 6  -C_EXPORT_FMT PLY  -PLY_EXPORT_FMT BINARY_BE -SAVE_CLOUDS FILE ./clouds/mergedX"+str(i)+".ply" )

if NEED_MERGES:
    for i in range(2,NUM_FRAG+1):
        if i==2:
            fullComand="sudo "+ path_cc+" -SILENT  -AUTO_SAVE OFF -o ./clouds/mergedX1.ply -o ./clouds/mergedX2.ply  -MERGE_CLOUDS -C_EXPORT_FMT PLY -PLY_EXPORT_FMT BINARY_BE -SAVE_CLOUDS FILE ./clouds/merged_FINAL.ply"
            os.system(fullComand)
        #From iter 2 to N uses the merged cloud made it before
        else:
            fullComand="sudo "+ path_cc+" -SILENT  -AUTO_SAVE OFF -o ./clouds/merged_FINAL.ply -o ./clouds/mergedX"+str(i)+".ply  -MERGE_CLOUDS  -C_EXPORT_FMT PLY -PLY_EXPORT_FMT BINARY_BE  -SAVE_CLOUDS FILE ./clouds/merged_FINAL.ply"
            os.system(fullComand)
