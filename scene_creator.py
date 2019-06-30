import os
from math import cos,sin,pi,radians,acos
from pyephem_sunpath.sunpath import sunpos,_calc_xyz
from datetime import datetime
from CONFIG import *



if USE_ORB_SLAM2:
    os.system("./kitti_orbslam2 DICTIONARY_ORB.txt CAMERA_CONFIG.yaml "+PATH_SEQUENCE_ORB)

#dirlist = os.listdir(path_f)
#dirlist_points = os.listdir(path_f_points)
#dirlist=sorted(dirlist)
os.chdir("/")
allPositions={}
allContent=[]
if not USE_ORB_SLAM2:
    #Read all contents from specified file
    with open(PATH_F+FILENAME, 'r') as fp:
        line = fp.readline()
        cnt = 1
        while line:
            allContent.append([line])
            line = fp.readline()
            cnt += 1
else:
    #Read all contents from specified file
    with open(PATH_FILE_ORBSLAM2, 'r') as fp:  
        line = fp.readline()
        cnt = 1
        while line:
            allContent.append([line])
            line = fp.readline()
            cnt += 1



#Extract all x,y,z positions readed from files
cleanXYZ=[]
for i in allContent:
    cleanXYZ.append([i[0].split(' ')[3].rstrip(),i[0].split(' ')[7].rstrip(),i[0].split(' ')[11].rstrip()])


#Extract all rotations positions readed from files
cleanRot=[]
for i in allContent:
    cleanRot.append([i[0].split(' ')[0].rstrip(),i[0].split(' ')[1].rstrip(),i[0].split(' ')[2].rstrip()])

print cleanXYZ

YEAR=2011
MONTH=9
DAY=30
HOUR=12
lat = 49.03
lon = 8.39
tz = 2

#Create datetime variable for calc the current sun position
thetime = datetime(YEAR, MONTH, DAY, HOUR)
alt, azm = sunpos(thetime, lat, lon, tz, dst=False)

#Transform to achive the truly position in x,y,z coords.
radius=100
inclination=(acos(alt/radius))
x=radius*sin(inclination)*cos(azm)
y=radius*sin(inclination)*sin(azm)
z=radius*cos(inclination)

print ("Sun position (x,y,z): ")
print(x,y,z)


scale=1
initFrame=0
finalFrame=2000
resolution_x=1252
resolution_y=525
numFrames=25

#Creation of the file that will import in Blender
with open(PATH_S+"importThis.py", "w") as f1:


    f1.write("import bpy\nimport sys\nfrom math import pi\nimport math\n")
    #Need for insert automatically object in the scene

    f1.write("bpy.data.objects['Camera'].select_set(True)\n")
    f1.write("bpy.data.objects['Cube'].select_set(True)\n")
    f1.write("bpy.ops.object.delete()\n")

    f1.write("bpy.context.preferences.themes[0].view_3d.space.gradients.high_gradient = [0.0,0.0,0.0]\n")
    f1.write("bpy.data.scenes[0].render.alpha_mode = 'TRANSPARENT'\n")

    f1.write("bpy.ops.import_scene.obj(filepath='"+PATH_OBJ+"')\n")
    f1.write("bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))\n")
    f1.write("bpy.ops.transform.translate( value = ( 40, -2.5, -1.4 ))\n")
    #Adding some object from default to our scene    
    f1.write("bpy.ops.object.light_add(type='SUN',location=("+str(x)+","+str(y)+","+str(z)+"))\n")
    f1.write("bpy.ops.object.camera_add(view_align=False,location=[0, 0, 0],rotation=[90,180,0])\n")
    f1.write("context = bpy.context\ncamera = context.object\n")
    f1.write("o = bpy.data.objects.new( 'empty', None )\n")
    f1.write("bpy.context.scene.collection.objects.link( o )\n")
    f1.write("o.empty_display_size = 2\n")
    f1.write("o.empty_display_type = 'PLAIN_AXES'\n")

    #Miscellaneous configs
    f1.write("camera.name = 'Camera_car'\n")
    f1.write("bpy.data.scenes[0].render.engine = 'BLENDER_EEVEE'\n")
    f1.write("bpy.data.scenes[0].render.resolution_x ="+str(resolution_x) +"\n")
    f1.write("bpy.data.scenes[0].render.resolution_y ="+str(resolution_y) +"\n")
    f1.write("bpy.data.scenes[0].frame_start = "+str(initFrame)+"\n")
    f1.write("bpy.data.scenes[0].frame_start = "+str(initFrame)+"\n")
    f1.write("bpy.data.scenes[0].frame_end = "+str(finalFrame)+"\n")
    f1.write("bpy.data.scenes[0].render.fps = "+str(numFrames)+"\n")


    counter=0
    initialZOffset=0

    
    for v,x in zip(cleanXYZ,cleanRot):

        #Unwind x,y,z rotations
        rotX=float(x[0])
        rotY=float(x[1])
        rotZ=float(x[2])
        #Unwind x,y,z rotations
        posX=float(v[0])
        posY=float(v[1])
        posZ=float(v[2])

        #Assignation of the x,y,z position in the current frame
        f1.write("camera.location.x = "+str(float(posZ)/scale) +"\n")
        f1.write("camera.location.y = "+str(-1*float(posX)/scale)+"\n")
        f1.write("camera.location.z = "+str(float(posY)/scale)+"\n")

        #Assignation of the euler rotation to the object
        f1.write("camera.rotation_euler = ("+str(radians(270)+rotZ) +","+str(-1*rotY+radians(180)) +","+str(-1.82*(pi)+ rotX)+")\n")

        #Binding between the previous definitions and the actual frame
        f1.write('camera.keyframe_insert(data_path="rotation_euler",frame='+str(3*counter)+'.0)\n')
        f1.write('camera.keyframe_insert(data_path="location", frame='+str(3*counter)+'.0)\n')
        counter+=1
    
