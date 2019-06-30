import bpy
import sys
from math import pi
import math
bpy.data.objects['Camera'].select_set(True)
bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()
bpy.context.preferences.themes[0].view_3d.space.gradients.high_gradient = [0.0,0.0,0.0]
bpy.data.scenes[0].render.alpha_mode = 'TRANSPARENT'
bpy.ops.import_scene.obj(filepath='./test.obj')
bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))
bpy.ops.transform.translate( value = ( 10, -2.5, -1.4 ))
bpy.ops.object.light_add(type='SUN',location=(62.2559849845,-69.6629273213,35.6548578827))
bpy.ops.object.camera_add(view_align=False,location=[0, 0, 0],rotation=[90,180,0])
context = bpy.context
camera = context.object
o = bpy.data.objects.new( 'empty', None )
bpy.context.scene.collection.objects.link( o )
o.empty_display_size = 2
o.empty_display_type = 'PLAIN_AXES'
camera.name = 'Camera_car'
bpy.data.scenes[0].render.engine = 'BLENDER_EEVEE'
bpy.data.scenes[0].render.resolution_x =1252
bpy.data.scenes[0].render.resolution_y =525
bpy.data.scenes[0].frame_start = 0
bpy.data.scenes[0].frame_start = 0
bpy.data.scenes[0].frame_end = 2000
bpy.data.scenes[0].render.fps = 25
camera.location.x = 2.220446e-16
camera.location.y = 5.551115e-17
camera.location.z = 0.0
camera.rotation_euler = (4.71238898056,3.14159265358,-4.71769862953)
camera.keyframe_insert(data_path="rotation_euler",frame=0.0)
camera.keyframe_insert(data_path="location", frame=0.0)
camera.location.x = 1.310643
camera.location.y = -0.001289128
camera.location.z = -0.01821616
camera.rotation_euler = (4.71217886348,3.14249617209,-4.71769902953)
camera.keyframe_insert(data_path="rotation_euler",frame=3.0)
camera.keyframe_insert(data_path="location", frame=3.0)
camera.location.x = 2.625299
camera.location.y = -0.0004448326
camera.location.z = -0.04203318
camera.rotation_euler = (4.71183515988,3.14323900059,-4.71770012953)
camera.keyframe_insert(data_path="rotation_euler",frame=6.0)
camera.keyframe_insert(data_path="location", frame=6.0)
camera.location.x = 3.94173
camera.location.y = -0.002037581
camera.location.z = -0.06302801
camera.rotation_euler = (4.71165776068,3.14500610759,-4.71770472953)
camera.keyframe_insert(data_path="rotation_euler",frame=9.0)
camera.keyframe_insert(data_path="location", frame=9.0)
camera.location.x = 5.261017
camera.location.y = -0.002777892
camera.location.z = -0.08483761
camera.rotation_euler = (4.71174558008,3.14522800159,-4.71770542953)
camera.keyframe_insert(data_path="rotation_euler",frame=12.0)
camera.keyframe_insert(data_path="location", frame=12.0)
camera.location.x = 6.581638
camera.location.y = -0.004157928
camera.location.z = -0.1014678
camera.rotation_euler = (4.71187275638,3.14551787259,-4.71770642953)
camera.keyframe_insert(data_path="rotation_euler",frame=15.0)
camera.keyframe_insert(data_path="location", frame=15.0)
camera.location.x = 7.908775
camera.location.y = -0.007571022
camera.location.z = -0.1165874
camera.rotation_euler = (4.71197199418,3.14709670559,-4.71771382953)
camera.keyframe_insert(data_path="rotation_euler",frame=18.0)
camera.keyframe_insert(data_path="location", frame=18.0)
camera.location.x = 9.238962
camera.location.y = -0.008323818
camera.location.z = -0.1328035
camera.rotation_euler = (4.71179142078,3.14677720559,-4.71771222953)
camera.keyframe_insert(data_path="rotation_euler",frame=21.0)
camera.keyframe_insert(data_path="location", frame=21.0)
camera.location.x = 10.56963
camera.location.y = -0.007728339
camera.location.z = -0.1497649
camera.rotation_euler = (4.71152850978,3.14622352359,-4.71770972953)
camera.keyframe_insert(data_path="rotation_euler",frame=24.0)
camera.keyframe_insert(data_path="location", frame=24.0)
camera.location.x = 11.90426
camera.location.y = -0.006780918
camera.location.z = -0.1634547
camera.rotation_euler = (4.71142887578,3.14349346059,-4.71770092953)
camera.keyframe_insert(data_path="rotation_euler",frame=27.0)
camera.keyframe_insert(data_path="location", frame=27.0)
camera.location.x = 13.24208
camera.location.y = -0.003419395
camera.location.z = -0.176748
camera.rotation_euler = (4.71176711338,3.14004906559,-4.71770002953)
camera.keyframe_insert(data_path="rotation_euler",frame=30.0)
camera.keyframe_insert(data_path="location", frame=30.0)
camera.location.x = 14.58048
camera.location.y = 0.001862182
camera.location.z = -0.1959202
camera.rotation_euler = (4.71185850068,3.13763009959,-4.71770662953)
camera.keyframe_insert(data_path="rotation_euler",frame=33.0)
camera.keyframe_insert(data_path="location", frame=33.0)
camera.location.x = 15.93066
camera.location.y = 0.005851755
camera.location.z = -0.2177602
camera.rotation_euler = (4.71200203698,3.13640284059,-4.71771212953)
camera.keyframe_insert(data_path="rotation_euler",frame=36.0)
camera.keyframe_insert(data_path="location", frame=36.0)
camera.location.x = 17.28222
camera.location.y = 0.004267715
camera.location.z = -0.236414
camera.rotation_euler = (4.71241774799,3.13859956359,-4.71770312953)
camera.keyframe_insert(data_path="rotation_euler",frame=39.0)
camera.keyframe_insert(data_path="location", frame=39.0)
camera.location.x = 18.63469
camera.location.y = -0.000482789
camera.location.z = -0.2537475
camera.rotation_euler = (4.71264147078,3.14249203919,-4.71769902953)
camera.keyframe_insert(data_path="rotation_euler",frame=42.0)
camera.keyframe_insert(data_path="location", frame=42.0)
camera.location.x = 19.9867
camera.location.y = -0.005006086
camera.location.z = -0.2699101
camera.rotation_euler = (4.71234938823,3.14523129459,-4.71770522953)
camera.keyframe_insert(data_path="rotation_euler",frame=45.0)
camera.keyframe_insert(data_path="location", frame=45.0)
camera.location.x = 21.34127
camera.location.y = -0.004134686
camera.location.z = -0.2931092
camera.rotation_euler = (4.71215694478,3.14671191559,-4.71771172953)
camera.keyframe_insert(data_path="rotation_euler",frame=48.0)
camera.keyframe_insert(data_path="location", frame=48.0)
camera.location.x = 22.70575
camera.location.y = 0.0007654745
camera.location.z = -0.3222297
camera.rotation_euler = (4.71281524188,3.14444142759,-4.71770272953)
camera.keyframe_insert(data_path="rotation_euler",frame=51.0)
camera.keyframe_insert(data_path="location", frame=51.0)
camera.location.x = 24.0721
camera.location.y = 0.007369324
camera.location.z = -0.3468119
camera.rotation_euler = (4.71363440538,3.14145016829,-4.71769942953)
camera.keyframe_insert(data_path="rotation_euler",frame=54.0)
camera.keyframe_insert(data_path="location", frame=54.0)
camera.location.x = 25.44868
camera.location.y = 0.009719264
camera.location.z = -0.3687424
camera.rotation_euler = (4.71433103838,3.14015201959,-4.71770152953)
camera.keyframe_insert(data_path="rotation_euler",frame=57.0)
camera.keyframe_insert(data_path="location", frame=57.0)
camera.location.x = 26.8203
camera.location.y = 0.005061181
camera.location.z = -0.3871399
camera.rotation_euler = (4.71475821838,3.14264354459,-4.71770202953)
camera.keyframe_insert(data_path="rotation_euler",frame=60.0)
camera.keyframe_insert(data_path="location", frame=60.0)
camera.location.x = 28.19472
camera.location.y = -0.001962273
camera.location.z = -0.4099385
camera.rotation_euler = (4.71434029538,3.14693166059,-4.71771472953)
camera.keyframe_insert(data_path="rotation_euler",frame=63.0)
camera.keyframe_insert(data_path="location", frame=63.0)
camera.location.x = 29.57012
camera.location.y = -0.005281593
camera.location.z = -0.4328977
camera.rotation_euler = (4.71437387238,3.14752588259,-4.71771822953)
camera.keyframe_insert(data_path="rotation_euler",frame=66.0)
camera.keyframe_insert(data_path="location", frame=66.0)
camera.location.x = 30.94984
camera.location.y = -0.007939024
camera.location.z = -0.4591179
camera.rotation_euler = (4.71478567638,3.14776994259,-4.71772052953)
camera.keyframe_insert(data_path="rotation_euler",frame=69.0)
camera.keyframe_insert(data_path="location", frame=69.0)
camera.location.x = 32.33531
camera.location.y = -0.006827076
camera.location.z = -0.4850133
camera.rotation_euler = (4.71556225538,3.14445691659,-4.71770772953)
camera.keyframe_insert(data_path="rotation_euler",frame=72.0)
camera.keyframe_insert(data_path="location", frame=72.0)
camera.location.x = 33.7178
camera.location.y = -0.008305167
camera.location.z = -0.5122367
camera.rotation_euler = (4.71595881238,3.14350925759,-4.71770682953)
camera.keyframe_insert(data_path="rotation_euler",frame=75.0)
camera.keyframe_insert(data_path="location", frame=75.0)
camera.location.x = 35.11083
camera.location.y = -0.0101734
camera.location.z = -0.543116
camera.rotation_euler = (4.71588740738,3.14261410259,-4.71770522953)
camera.keyframe_insert(data_path="rotation_euler",frame=78.0)
camera.keyframe_insert(data_path="location", frame=78.0)
camera.location.x = 36.50789
camera.location.y = -0.0121194
camera.location.z = -0.5746233
camera.rotation_euler = (4.71579794238,3.14254895019,-4.71770492953)
camera.keyframe_insert(data_path="rotation_euler",frame=81.0)
camera.keyframe_insert(data_path="location", frame=81.0)
camera.location.x = 37.90589
camera.location.y = -0.01511478
camera.location.z = -0.5999006
camera.rotation_euler = (4.71537512438,3.14178161029,-4.71770312953)
camera.keyframe_insert(data_path="rotation_euler",frame=84.0)
camera.keyframe_insert(data_path="location", frame=84.0)
camera.location.x = 39.30156
camera.location.y = -0.01696851
camera.location.z = -0.6238526
camera.rotation_euler = (4.71535165138,3.13907811759,-4.71770612953)
camera.keyframe_insert(data_path="rotation_euler",frame=87.0)
camera.keyframe_insert(data_path="location", frame=87.0)
camera.location.x = 40.70437
camera.location.y = -0.01942949
camera.location.z = -0.643712
camera.rotation_euler = (4.71549039038,3.13654110259,-4.71771622953)
camera.keyframe_insert(data_path="rotation_euler",frame=90.0)
camera.keyframe_insert(data_path="location", frame=90.0)
camera.location.x = 42.111
camera.location.y = -0.01916344
camera.location.z = -0.6707246
camera.rotation_euler = (4.71550002738,3.13438900159,-4.71772942953)
camera.keyframe_insert(data_path="rotation_euler",frame=93.0)
camera.keyframe_insert(data_path="location", frame=93.0)
camera.location.x = 43.51858
camera.location.y = -0.02134431
camera.location.z = -0.694132
camera.rotation_euler = (4.71523260138,3.13328434259,-4.71773712953)
camera.keyframe_insert(data_path="rotation_euler",frame=96.0)
camera.keyframe_insert(data_path="location", frame=96.0)
camera.location.x = 44.92821
camera.location.y = -0.02622364
camera.location.z = -0.7178581
camera.rotation_euler = (4.71480123938,3.13433293759,-4.71772792953)
camera.keyframe_insert(data_path="rotation_euler",frame=99.0)
camera.keyframe_insert(data_path="location", frame=99.0)
camera.location.x = 46.34127
camera.location.y = -0.03086036
camera.location.z = -0.739025
camera.rotation_euler = (4.71410991338,3.13516641559,-4.71772072953)
camera.keyframe_insert(data_path="rotation_euler",frame=102.0)
camera.keyframe_insert(data_path="location", frame=102.0)
camera.location.x = 47.75704
camera.location.y = -0.03408031
camera.location.z = -0.7610315
camera.rotation_euler = (4.71315059948,3.13579248459,-4.71771572953)
camera.keyframe_insert(data_path="rotation_euler",frame=105.0)
camera.keyframe_insert(data_path="location", frame=105.0)
camera.location.x = 49.17963
camera.location.y = -0.03359221
camera.location.z = -0.7839856
camera.rotation_euler = (4.71214778518,3.13558208859,-4.71771672953)
camera.keyframe_insert(data_path="rotation_euler",frame=108.0)
camera.keyframe_insert(data_path="location", frame=108.0)
camera.location.x = 50.60218
camera.location.y = -0.03175532
camera.location.z = -0.805635
camera.rotation_euler = (4.71108516338,3.13494374359,-4.71772152953)
camera.keyframe_insert(data_path="rotation_euler",frame=111.0)
camera.keyframe_insert(data_path="location", frame=111.0)
camera.location.x = 52.02831
camera.location.y = -0.02895795
camera.location.z = -0.8265408
camera.rotation_euler = (4.70990950038,3.13495440259,-4.71772372953)
camera.keyframe_insert(data_path="rotation_euler",frame=114.0)
camera.keyframe_insert(data_path="location", frame=114.0)
camera.location.x = 53.45716
camera.location.y = -0.02536977
camera.location.z = -0.8453836
camera.rotation_euler = (4.70880067938,3.13470987759,-4.71772872953)
camera.keyframe_insert(data_path="rotation_euler",frame=117.0)
camera.keyframe_insert(data_path="location", frame=117.0)
camera.location.x = 54.88464
camera.location.y = -0.02082938
camera.location.z = -0.8668316
camera.rotation_euler = (4.70800157438,3.13609556159,-4.71772332953)
camera.keyframe_insert(data_path="rotation_euler",frame=120.0)
camera.keyframe_insert(data_path="location", frame=120.0)
camera.location.x = 56.3166
camera.location.y = -0.0168087
camera.location.z = -0.88688
camera.rotation_euler = (4.70736040238,3.13758953859,-4.71771922953)
camera.keyframe_insert(data_path="rotation_euler",frame=123.0)
camera.keyframe_insert(data_path="location", frame=123.0)
camera.location.x = 57.7455
camera.location.y = -0.0132291
camera.location.z = -0.9072442
camera.rotation_euler = (4.70673453738,3.13987327659,-4.71771612953)
camera.keyframe_insert(data_path="rotation_euler",frame=126.0)
camera.keyframe_insert(data_path="location", frame=126.0)
camera.location.x = 59.17365
camera.location.y = -0.01007535
camera.location.z = -0.9249469
camera.rotation_euler = (4.70665821138,3.14121771399,-4.71771512953)
camera.keyframe_insert(data_path="rotation_euler",frame=129.0)
camera.keyframe_insert(data_path="location", frame=129.0)
camera.location.x = 60.60318
camera.location.y = -0.006524255
camera.location.z = -0.9446035
camera.rotation_euler = (4.70708819138,3.14242914419,-4.71771302953)
camera.keyframe_insert(data_path="rotation_euler",frame=132.0)
camera.keyframe_insert(data_path="location", frame=132.0)
camera.location.x = 62.02795
camera.location.y = -0.00276421
camera.location.z = -0.9647484
camera.rotation_euler = (4.70747104938,3.14345144459,-4.71771242953)
camera.keyframe_insert(data_path="rotation_euler",frame=135.0)
camera.keyframe_insert(data_path="location", frame=135.0)
camera.location.x = 63.45198
camera.location.y = 0.001308243
camera.location.z = -0.98781
camera.rotation_euler = (4.70790019038,3.14538520259,-4.71771592953)
camera.keyframe_insert(data_path="rotation_euler",frame=138.0)
camera.keyframe_insert(data_path="location", frame=138.0)
camera.location.x = 64.87187
camera.location.y = 0.002873604
camera.location.z = -1.008175
camera.rotation_euler = (4.70838078238,3.14688884959,-4.71772062953)
camera.keyframe_insert(data_path="rotation_euler",frame=141.0)
camera.keyframe_insert(data_path="location", frame=141.0)
camera.location.x = 66.2894
camera.location.y = 0.005953934
camera.location.z = -1.0297
camera.rotation_euler = (4.70902938538,3.14681311759,-4.71771792953)
camera.keyframe_insert(data_path="rotation_euler",frame=144.0)
camera.keyframe_insert(data_path="location", frame=144.0)
camera.location.x = 67.70311
camera.location.y = 0.01002031
camera.location.z = -1.050203
camera.rotation_euler = (4.70983584538,3.14507511559,-4.71770792953)
camera.keyframe_insert(data_path="rotation_euler",frame=147.0)
camera.keyframe_insert(data_path="location", frame=147.0)
camera.location.x = 69.11593
camera.location.y = 0.0193644
camera.location.z = -1.076075
camera.rotation_euler = (4.71032020838,3.14224078969,-4.71770092953)
camera.keyframe_insert(data_path="rotation_euler",frame=150.0)
camera.keyframe_insert(data_path="location", frame=150.0)
camera.location.x = 70.53
camera.location.y = 0.02702275
camera.location.z = -1.097831
camera.rotation_euler = (4.71110100938,3.13857978859,-4.71770402953)
camera.keyframe_insert(data_path="rotation_euler",frame=153.0)
camera.keyframe_insert(data_path="location", frame=153.0)
camera.location.x = 71.93978
camera.location.y = 0.03513442
camera.location.z = -1.118231
camera.rotation_euler = (4.71186023908,3.13493272059,-4.71772092953)
camera.keyframe_insert(data_path="rotation_euler",frame=156.0)
camera.keyframe_insert(data_path="location", frame=156.0)
camera.location.x = 73.33986
camera.location.y = 0.0421465
camera.location.z = -1.135987
camera.rotation_euler = (4.71252486368,3.13044118359,-4.71776082953)
camera.keyframe_insert(data_path="rotation_euler",frame=159.0)
camera.keyframe_insert(data_path="location", frame=159.0)
camera.location.x = 74.74245
camera.location.y = 0.04677589
camera.location.z = -1.153311
camera.rotation_euler = (4.71323930438,3.12737574359,-4.71780002953)
camera.keyframe_insert(data_path="rotation_euler",frame=162.0)
camera.keyframe_insert(data_path="location", frame=162.0)
camera.location.x = 76.1445
camera.location.y = 0.05327678
camera.location.z = -1.177226
camera.rotation_euler = (4.71393393838,3.12522667359,-4.71783372953)
camera.keyframe_insert(data_path="rotation_euler",frame=165.0)
camera.keyframe_insert(data_path="location", frame=165.0)
camera.location.x = 77.54079
camera.location.y = 0.05458511
camera.location.z = -1.197942
camera.rotation_euler = (4.71427260138,3.12495499359,-4.71783882953)
camera.keyframe_insert(data_path="rotation_euler",frame=168.0)
camera.keyframe_insert(data_path="location", frame=168.0)
camera.location.x = 78.93496
camera.location.y = 0.05287325
camera.location.z = -1.218035
camera.rotation_euler = (4.71442949038,3.12619073359,-4.71781932953)
camera.keyframe_insert(data_path="rotation_euler",frame=171.0)
camera.keyframe_insert(data_path="location", frame=171.0)
camera.location.x = 80.32545
camera.location.y = 0.0495425
camera.location.z = -1.236655
camera.rotation_euler = (4.71434834938,3.12735635359,-4.71780192953)
camera.keyframe_insert(data_path="rotation_euler",frame=174.0)
camera.keyframe_insert(data_path="location", frame=174.0)
camera.location.x = 81.71095
camera.location.y = 0.04883212
camera.location.z = -1.258287
camera.rotation_euler = (4.71406619538,3.12810278359,-4.71779102953)
camera.keyframe_insert(data_path="rotation_euler",frame=177.0)
camera.keyframe_insert(data_path="location", frame=177.0)
camera.location.x = 83.09721
camera.location.y = 0.04838807
camera.location.z = -1.278676
camera.rotation_euler = (4.71383744338,3.12805849359,-4.71779122953)
camera.keyframe_insert(data_path="rotation_euler",frame=180.0)
camera.keyframe_insert(data_path="location", frame=180.0)
camera.location.x = 84.48367
camera.location.y = 0.05269073
camera.location.z = -1.300031
camera.rotation_euler = (4.71329751478,3.12851255359,-4.71778462953)
camera.keyframe_insert(data_path="rotation_euler",frame=183.0)
camera.keyframe_insert(data_path="location", frame=183.0)
camera.location.x = 85.86562
camera.location.y = 0.06072004
camera.location.z = -1.320245
camera.rotation_euler = (4.71257602768,3.12815787359,-4.71778892953)
camera.keyframe_insert(data_path="rotation_euler",frame=186.0)
camera.keyframe_insert(data_path="location", frame=186.0)
camera.location.x = 87.25015
camera.location.y = 0.07518042
camera.location.z = -1.343695
camera.rotation_euler = (4.71164353118,3.12853856359,-4.71778412953)
camera.keyframe_insert(data_path="rotation_euler",frame=189.0)
camera.keyframe_insert(data_path="location", frame=189.0)
camera.location.x = 88.62909
camera.location.y = 0.0843762
camera.location.z = -1.362982
camera.rotation_euler = (4.71051100538,3.13066201359,-4.71776012953)
camera.keyframe_insert(data_path="rotation_euler",frame=192.0)
camera.keyframe_insert(data_path="location", frame=192.0)
camera.location.x = 90.00634
camera.location.y = 0.09813229
camera.location.z = -1.38264
camera.rotation_euler = (4.70930233338,3.13280192259,-4.71774202953)
camera.keyframe_insert(data_path="rotation_euler",frame=195.0)
camera.keyframe_insert(data_path="location", frame=195.0)
camera.location.x = 91.37524
camera.location.y = 0.1110475
camera.location.z = -1.399781
camera.rotation_euler = (4.70867734338,3.13478939359,-4.71772862953)
camera.keyframe_insert(data_path="rotation_euler",frame=198.0)
camera.keyframe_insert(data_path="location", frame=198.0)
camera.location.x = 92.74128
camera.location.y = 0.1283351
camera.location.z = -1.418059
camera.rotation_euler = (4.70820020038,3.13608290159,-4.71772252953)
camera.keyframe_insert(data_path="rotation_euler",frame=201.0)
camera.keyframe_insert(data_path="location", frame=201.0)
camera.location.x = 94.10339
camera.location.y = 0.1454603
camera.location.z = -1.435964
camera.rotation_euler = (4.70792048838,3.13731043659,-4.71771772953)
camera.keyframe_insert(data_path="rotation_euler",frame=204.0)
camera.keyframe_insert(data_path="location", frame=204.0)
camera.location.x = 95.46076
camera.location.y = 0.1697048
camera.location.z = -1.45619
camera.rotation_euler = (4.70778421238,3.13665119859,-4.71772142953)
camera.keyframe_insert(data_path="rotation_euler",frame=207.0)
camera.keyframe_insert(data_path="location", frame=207.0)
camera.location.x = 96.81382
camera.location.y = 0.1913409
camera.location.z = -1.476213
camera.rotation_euler = (4.70790157038,3.13685407859,-4.71771992953)
camera.keyframe_insert(data_path="rotation_euler",frame=210.0)
camera.keyframe_insert(data_path="location", frame=210.0)
camera.location.x = 98.16545
camera.location.y = 0.2120314
camera.location.z = -1.496478
camera.rotation_euler = (4.70814272038,3.13613062259,-4.71772252953)
camera.keyframe_insert(data_path="rotation_euler",frame=213.0)
camera.keyframe_insert(data_path="location", frame=213.0)
camera.location.x = 99.51513
camera.location.y = 0.2344056
camera.location.z = -1.517683
camera.rotation_euler = (4.70851203138,3.13453181359,-4.71773102953)
camera.keyframe_insert(data_path="rotation_euler",frame=216.0)
camera.keyframe_insert(data_path="location", frame=216.0)
camera.location.x = 100.8603
camera.location.y = 0.2485715
camera.location.z = -1.534999
camera.rotation_euler = (4.70876177338,3.13406339359,-4.71773352953)
camera.keyframe_insert(data_path="rotation_euler",frame=219.0)
camera.keyframe_insert(data_path="location", frame=219.0)
camera.location.x = 102.2054
camera.location.y = 0.2694021
camera.location.z = -1.556018
camera.rotation_euler = (4.70893068238,3.13275884259,-4.71774362953)
camera.keyframe_insert(data_path="rotation_euler",frame=222.0)
camera.keyframe_insert(data_path="location", frame=222.0)
camera.location.x = 103.5459
camera.location.y = 0.2867601
camera.location.z = -1.575247
camera.rotation_euler = (4.70897569138,3.13329039959,-4.71773892953)
camera.keyframe_insert(data_path="rotation_euler",frame=225.0)
camera.keyframe_insert(data_path="location", frame=225.0)
camera.location.x = 104.8845
camera.location.y = 0.3053256
camera.location.z = -1.596046
camera.rotation_euler = (4.70905077538,3.13341878259,-4.71773762953)
camera.keyframe_insert(data_path="rotation_euler",frame=228.0)
camera.keyframe_insert(data_path="location", frame=228.0)
camera.location.x = 106.2208
camera.location.y = 0.3153955
camera.location.z = -1.613299
camera.rotation_euler = (4.70900162438,3.13395937959,-4.71773352953)
camera.keyframe_insert(data_path="rotation_euler",frame=231.0)
camera.keyframe_insert(data_path="location", frame=231.0)
camera.location.x = 107.5653
camera.location.y = 0.3343086
camera.location.z = -1.638432
camera.rotation_euler = (4.70914993238,3.13608772559,-4.71771902953)
camera.keyframe_insert(data_path="rotation_euler",frame=234.0)
camera.keyframe_insert(data_path="location", frame=234.0)
camera.location.x = 108.9064
camera.location.y = 0.3508131
camera.location.z = -1.661275
camera.rotation_euler = (4.70976309738,3.13845054859,-4.71770702953)
camera.keyframe_insert(data_path="rotation_euler",frame=237.0)
camera.keyframe_insert(data_path="location", frame=237.0)
camera.location.x = 110.2446
camera.location.y = 0.3737761
camera.location.z = -1.686739
camera.rotation_euler = (4.71067946138,3.14003118859,-4.71770132953)
camera.keyframe_insert(data_path="rotation_euler",frame=240.0)
camera.keyframe_insert(data_path="location", frame=240.0)
camera.location.x = 111.5766
camera.location.y = 0.3943149
camera.location.z = -1.710102
camera.rotation_euler = (4.71138879238,3.14091648869,-4.71769932953)
camera.keyframe_insert(data_path="rotation_euler",frame=243.0)
camera.keyframe_insert(data_path="location", frame=243.0)
camera.location.x = 112.905
camera.location.y = 0.4137129
camera.location.z = -1.733997
camera.rotation_euler = (4.71205522628,3.13901145359,-4.71770202953)
camera.keyframe_insert(data_path="rotation_euler",frame=246.0)
camera.keyframe_insert(data_path="location", frame=246.0)
camera.location.x = 114.2286
camera.location.y = 0.4219683
camera.location.z = -1.753986
camera.rotation_euler = (4.71313726308,3.13705998359,-4.71770912953)
camera.keyframe_insert(data_path="rotation_euler",frame=249.0)
camera.keyframe_insert(data_path="location", frame=249.0)
camera.location.x = 115.5601
camera.location.y = 0.4295899
camera.location.z = -1.775004
camera.rotation_euler = (4.71455026238,3.13402245659,-4.71772962953)
camera.keyframe_insert(data_path="rotation_euler",frame=252.0)
camera.keyframe_insert(data_path="location", frame=252.0)
camera.location.x = 116.893
camera.location.y = 0.4334779
camera.location.z = -1.79423
camera.rotation_euler = (4.71598592538,3.13259592959,-4.71774552953)
camera.keyframe_insert(data_path="rotation_euler",frame=255.0)
camera.keyframe_insert(data_path="location", frame=255.0)
camera.location.x = 118.2274
camera.location.y = 0.4334151
camera.location.z = -1.811794
camera.rotation_euler = (4.71705629338,3.13251276559,-4.71775072953)
camera.keyframe_insert(data_path="rotation_euler",frame=258.0)
camera.keyframe_insert(data_path="location", frame=258.0)
camera.location.x = 119.5613
camera.location.y = 0.4306137
camera.location.z = -1.825847
camera.rotation_euler = (4.71783852038,3.13351477459,-4.71774612953)
camera.keyframe_insert(data_path="rotation_euler",frame=261.0)
camera.keyframe_insert(data_path="location", frame=261.0)
camera.location.x = 120.9045
camera.location.y = 0.4334146
camera.location.z = -1.846322
camera.rotation_euler = (4.71885791938,3.13300549159,-4.71775642953)
camera.keyframe_insert(data_path="rotation_euler",frame=264.0)
camera.keyframe_insert(data_path="location", frame=264.0)
camera.location.x = 122.2684
camera.location.y = 0.4472932
camera.location.z = -1.880929
camera.rotation_euler = (4.72009822738,3.13124234359,-4.71778192953)
camera.keyframe_insert(data_path="rotation_euler",frame=267.0)
camera.keyframe_insert(data_path="location", frame=267.0)
camera.location.x = 123.6242
camera.location.y = 0.4560744
camera.location.z = -1.91003
camera.rotation_euler = (4.72123870038,3.12921241359,-4.71781442953)
camera.keyframe_insert(data_path="rotation_euler",frame=270.0)
camera.keyframe_insert(data_path="location", frame=270.0)
camera.location.x = 124.9835
camera.location.y = 0.4622549
camera.location.z = -1.940325
camera.rotation_euler = (4.72235209938,3.12845537359,-4.71783452953)
camera.keyframe_insert(data_path="rotation_euler",frame=273.0)
camera.keyframe_insert(data_path="location", frame=273.0)
camera.location.x = 126.3371
camera.location.y = 0.4641329
camera.location.z = -1.966295
camera.rotation_euler = (4.72343992038,3.12736064359,-4.71786092953)
camera.keyframe_insert(data_path="rotation_euler",frame=276.0)
camera.keyframe_insert(data_path="location", frame=276.0)
camera.location.x = 127.6925
camera.location.y = 0.4708495
camera.location.z = -2.006026
camera.rotation_euler = (4.72434652038,3.12819784359,-4.71785982953)
camera.keyframe_insert(data_path="rotation_euler",frame=279.0)
camera.keyframe_insert(data_path="location", frame=279.0)
camera.location.x = 129.0496
camera.location.y = 0.4718094
camera.location.z = -2.038343
camera.rotation_euler = (4.72511893038,3.12872810359,-4.71786242953)
camera.keyframe_insert(data_path="rotation_euler",frame=282.0)
camera.keyframe_insert(data_path="location", frame=282.0)
camera.location.x = 130.407
camera.location.y = 0.47428
camera.location.z = -2.073189
camera.rotation_euler = (4.72596638038,3.12970307359,-4.71786152953)
camera.keyframe_insert(data_path="rotation_euler",frame=285.0)
camera.keyframe_insert(data_path="location", frame=285.0)
camera.location.x = 131.7557
camera.location.y = 0.4701254
camera.location.z = -2.099489
camera.rotation_euler = (4.72628521038,3.13070095359,-4.71785452953)
camera.keyframe_insert(data_path="rotation_euler",frame=288.0)
camera.keyframe_insert(data_path="location", frame=288.0)
camera.location.x = 133.1097
camera.location.y = 0.4656937
camera.location.z = -2.127702
camera.rotation_euler = (4.72626155038,3.13278010859,-4.71783372953)
camera.keyframe_insert(data_path="rotation_euler",frame=291.0)
camera.keyframe_insert(data_path="location", frame=291.0)
camera.location.x = 134.4614
camera.location.y = 0.4651028
camera.location.z = -2.162932
camera.rotation_euler = (4.72593732038,3.13444988059,-4.71781592953)
camera.keyframe_insert(data_path="rotation_euler",frame=294.0)
camera.keyframe_insert(data_path="location", frame=294.0)
camera.location.x = 135.8146
camera.location.y = 0.4661197
camera.location.z = -2.198388
camera.rotation_euler = (4.72539397038,3.13595603959,-4.71779902953)
camera.keyframe_insert(data_path="rotation_euler",frame=297.0)
camera.keyframe_insert(data_path="location", frame=297.0)
camera.location.x = 137.1606
camera.location.y = 0.4644953
camera.location.z = -2.226309
camera.rotation_euler = (4.72413833038,3.13754401059,-4.71777582953)
camera.keyframe_insert(data_path="rotation_euler",frame=300.0)
camera.keyframe_insert(data_path="location", frame=300.0)
camera.location.x = 138.5124
camera.location.y = 0.4645723
camera.location.z = -2.254854
camera.rotation_euler = (4.72306735038,3.13880092659,-4.71775952953)
camera.keyframe_insert(data_path="rotation_euler",frame=303.0)
camera.keyframe_insert(data_path="location", frame=303.0)
camera.location.x = 139.8626
camera.location.y = 0.4641807
camera.location.z = -2.281749
camera.rotation_euler = (4.72204556138,3.14036459459,-4.71774602953)
camera.keyframe_insert(data_path="rotation_euler",frame=306.0)
camera.keyframe_insert(data_path="location", frame=306.0)
camera.location.x = 141.2129
camera.location.y = 0.4674418
camera.location.z = -2.314866
camera.rotation_euler = (4.72074417138,3.14110726839,-4.71773362953)
camera.keyframe_insert(data_path="rotation_euler",frame=309.0)
camera.keyframe_insert(data_path="location", frame=309.0)
camera.location.x = 142.5622
camera.location.y = 0.4704574
camera.location.z = -2.341886
camera.rotation_euler = (4.71949112438,3.14136337899,-4.71772382953)
camera.keyframe_insert(data_path="rotation_euler",frame=312.0)
camera.keyframe_insert(data_path="location", frame=312.0)
camera.location.x = 143.9099
camera.location.y = 0.474702
camera.location.z = -2.367455
camera.rotation_euler = (4.71845009338,3.14173883619,-4.71771702953)
camera.keyframe_insert(data_path="rotation_euler",frame=315.0)
camera.keyframe_insert(data_path="location", frame=315.0)
camera.location.x = 145.2578
camera.location.y = 0.4789013
camera.location.z = -2.395024
camera.rotation_euler = (4.71746383638,3.14336690059,-4.71771302953)
camera.keyframe_insert(data_path="rotation_euler",frame=318.0)
camera.keyframe_insert(data_path="location", frame=318.0)
camera.location.x = 146.6011
camera.location.y = 0.4813925
camera.location.z = -2.426593
camera.rotation_euler = (4.71633638438,3.14889126759,-4.71773302953)
camera.keyframe_insert(data_path="rotation_euler",frame=321.0)
camera.keyframe_insert(data_path="location", frame=321.0)
camera.location.x = 147.9538
camera.location.y = 0.484415
camera.location.z = -2.462969
camera.rotation_euler = (4.71519182238,3.15568833359,-4.71780192953)
camera.keyframe_insert(data_path="rotation_euler",frame=324.0)
camera.keyframe_insert(data_path="location", frame=324.0)
camera.location.x = 149.303
camera.location.y = 0.4832843
camera.location.z = -2.489366
camera.rotation_euler = (4.71370916138,3.16332345359,-4.71793562953)
camera.keyframe_insert(data_path="rotation_euler",frame=327.0)
camera.keyframe_insert(data_path="location", frame=327.0)
camera.location.x = 150.6481
camera.location.y = 0.4887986
camera.location.z = -2.518617
camera.rotation_euler = (4.71252222408,3.16664212359,-4.71801242953)
camera.keyframe_insert(data_path="rotation_euler",frame=330.0)
camera.keyframe_insert(data_path="location", frame=330.0)
camera.location.x = 151.9917
camera.location.y = 0.4979854
camera.location.z = -2.545628
camera.rotation_euler = (4.71276972258,3.16672517359,-4.71801452953)
camera.keyframe_insert(data_path="rotation_euler",frame=333.0)
camera.keyframe_insert(data_path="location", frame=333.0)
camera.location.x = 153.3373
camera.location.y = 0.5139897
camera.location.z = -2.581792
camera.rotation_euler = (4.71363780238,3.16318014359,-4.71793242953)
camera.keyframe_insert(data_path="rotation_euler",frame=336.0)
camera.keyframe_insert(data_path="location", frame=336.0)
camera.location.x = 154.6843
camera.location.y = 0.5203405
camera.location.z = -2.611885
camera.rotation_euler = (4.71439091938,3.16292452359,-4.71792812953)
camera.keyframe_insert(data_path="rotation_euler",frame=339.0)
camera.keyframe_insert(data_path="location", frame=339.0)
camera.location.x = 156.0329
camera.location.y = 0.5188374
camera.location.z = -2.641449
camera.rotation_euler = (4.71499826938,3.16565203359,-4.71799152953)
camera.keyframe_insert(data_path="rotation_euler",frame=342.0)
camera.keyframe_insert(data_path="location", frame=342.0)
camera.location.x = 157.3829
camera.location.y = 0.510487
camera.location.z = -2.666163
camera.rotation_euler = (4.71547078538,3.17110482359,-4.71813892953)
camera.keyframe_insert(data_path="rotation_euler",frame=345.0)
camera.keyframe_insert(data_path="location", frame=345.0)
camera.location.x = 158.7319
camera.location.y = 0.4996047
camera.location.z = -2.68915
camera.rotation_euler = (4.71545969838,3.17525964359,-4.71827022953)
camera.keyframe_insert(data_path="rotation_euler",frame=348.0)
camera.keyframe_insert(data_path="location", frame=348.0)
camera.location.x = 160.0786
camera.location.y = 0.4908894
camera.location.z = -2.711383
camera.rotation_euler = (4.71539578438,3.17705507359,-4.71833212953)
camera.keyframe_insert(data_path="rotation_euler",frame=351.0)
camera.keyframe_insert(data_path="location", frame=351.0)
camera.location.x = 161.429
camera.location.y = 0.4848759
camera.location.z = -2.73678
camera.rotation_euler = (4.71621089338,3.17550376359,-4.71828102953)
camera.keyframe_insert(data_path="rotation_euler",frame=354.0)
camera.keyframe_insert(data_path="location", frame=354.0)
camera.location.x = 162.7788
camera.location.y = 0.4836516
camera.location.z = -2.760604
camera.rotation_euler = (4.71743267638,3.17156969359,-4.71816072953)
camera.keyframe_insert(data_path="rotation_euler",frame=357.0)
camera.keyframe_insert(data_path="location", frame=357.0)
camera.location.x = 164.1295
camera.location.y = 0.4767803
camera.location.z = -2.787254
camera.rotation_euler = (4.71838130638,3.16813612359,-4.71806892953)
camera.keyframe_insert(data_path="rotation_euler",frame=360.0)
camera.keyframe_insert(data_path="location", frame=360.0)
camera.location.x = 165.4807
camera.location.y = 0.468784
camera.location.z = -2.810667
camera.rotation_euler = (4.71913920738,3.16529572359,-4.71800232953)
camera.keyframe_insert(data_path="rotation_euler",frame=363.0)
camera.keyframe_insert(data_path="location", frame=363.0)
camera.location.x = 166.839
camera.location.y = 0.4599264
camera.location.z = -2.835558
camera.rotation_euler = (4.71953440138,3.16329363359,-4.71795962953)
camera.keyframe_insert(data_path="rotation_euler",frame=366.0)
camera.keyframe_insert(data_path="location", frame=366.0)
camera.location.x = 168.2
camera.location.y = 0.449484
camera.location.z = -2.861986
camera.rotation_euler = (4.71930836938,3.16165454359,-4.71792382953)
camera.keyframe_insert(data_path="rotation_euler",frame=369.0)
camera.keyframe_insert(data_path="location", frame=369.0)
camera.location.x = 169.5602
camera.location.y = 0.4424438
camera.location.z = -2.88656
camera.rotation_euler = (4.71882339238,3.15972564359,-4.71788372953)
camera.keyframe_insert(data_path="rotation_euler",frame=372.0)
camera.keyframe_insert(data_path="location", frame=372.0)
camera.location.x = 170.9198
camera.location.y = 0.4389717
camera.location.z = -2.91424
camera.rotation_euler = (4.71832206938,3.15622731359,-4.71782332953)
camera.keyframe_insert(data_path="rotation_euler",frame=375.0)
camera.keyframe_insert(data_path="location", frame=375.0)
camera.location.x = 172.2841
camera.location.y = 0.4111543
camera.location.z = -2.932731
camera.rotation_euler = (4.71812923138,3.15132594759,-4.71776242953)
camera.keyframe_insert(data_path="rotation_euler",frame=378.0)
camera.keyframe_insert(data_path="location", frame=378.0)
camera.location.x = 173.6528
camera.location.y = 0.388112
camera.location.z = -2.960771
camera.rotation_euler = (4.71842598738,3.14673579959,-4.71773002953)
camera.keyframe_insert(data_path="rotation_euler",frame=381.0)
camera.keyframe_insert(data_path="location", frame=381.0)
camera.location.x = 175.0291
camera.location.y = 0.3779301
camera.location.z = -2.986448
camera.rotation_euler = (4.71895621438,3.14342076159,-4.71772182953)
camera.keyframe_insert(data_path="rotation_euler",frame=384.0)
camera.keyframe_insert(data_path="location", frame=384.0)
camera.location.x = 176.4086
camera.location.y = 0.3588782
camera.location.z = -3.008539
camera.rotation_euler = (4.71908500138,3.14307026359,-4.71772212953)
camera.keyframe_insert(data_path="rotation_euler",frame=387.0)
camera.keyframe_insert(data_path="location", frame=387.0)
camera.location.x = 177.7852
camera.location.y = 0.3405308
camera.location.z = -3.013913
camera.rotation_euler = (4.71829847038,3.14593224659,-4.71772552953)
camera.keyframe_insert(data_path="rotation_euler",frame=390.0)
camera.keyframe_insert(data_path="location", frame=390.0)
camera.location.x = 179.1607
camera.location.y = 0.3214042
camera.location.z = -3.022953
camera.rotation_euler = (4.71662095438,3.14848545259,-4.71773132953)
camera.keyframe_insert(data_path="rotation_euler",frame=393.0)
camera.keyframe_insert(data_path="location", frame=393.0)
camera.location.x = 180.542
camera.location.y = 0.3136545
camera.location.z = -3.041123
camera.rotation_euler = (4.71455912738,3.14890195059,-4.71772772953)
camera.keyframe_insert(data_path="rotation_euler",frame=396.0)
camera.keyframe_insert(data_path="location", frame=396.0)
camera.location.x = 181.9214
camera.location.y = 0.3089995
camera.location.z = -3.0621
camera.rotation_euler = (4.71306525278,3.14784181159,-4.71771832953)
camera.keyframe_insert(data_path="rotation_euler",frame=399.0)
camera.keyframe_insert(data_path="location", frame=399.0)
camera.location.x = 183.3098
camera.location.y = 0.3140564
camera.location.z = -3.088158
camera.rotation_euler = (4.71246523182,3.14306466359,-4.71769972953)
camera.keyframe_insert(data_path="rotation_euler",frame=402.0)
camera.keyframe_insert(data_path="location", frame=402.0)
camera.location.x = 184.7039
camera.location.y = 0.3186558
camera.location.z = -3.114466
camera.rotation_euler = (4.71233912467,3.13899942259,-4.71770202953)
camera.keyframe_insert(data_path="rotation_euler",frame=405.0)
camera.keyframe_insert(data_path="location", frame=405.0)
camera.location.x = 186.0994
camera.location.y = 0.3141305
camera.location.z = -3.137555
camera.rotation_euler = (4.71262240638,3.13728912059,-4.71770792953)
camera.keyframe_insert(data_path="rotation_euler",frame=408.0)
camera.keyframe_insert(data_path="location", frame=408.0)
camera.location.x = 187.4988
camera.location.y = 0.3087277
camera.location.z = -3.164478
camera.rotation_euler = (4.71304026868,3.13650162559,-4.71771182953)
camera.keyframe_insert(data_path="rotation_euler",frame=411.0)
camera.keyframe_insert(data_path="location", frame=411.0)
camera.location.x = 188.9003
camera.location.y = 0.3089327
camera.location.z = -3.193945
camera.rotation_euler = (4.71312206668,3.13714393159,-4.71770882953)
camera.keyframe_insert(data_path="rotation_euler",frame=414.0)
camera.keyframe_insert(data_path="location", frame=414.0)
camera.location.x = 190.3048
camera.location.y = 0.3070211
camera.location.z = -3.221858
camera.rotation_euler = (4.71306452958,3.13863864359,-4.71770322953)
camera.keyframe_insert(data_path="rotation_euler",frame=417.0)
camera.keyframe_insert(data_path="location", frame=417.0)
camera.location.x = 191.7128
camera.location.y = 0.3030042
camera.location.z = -3.25053
camera.rotation_euler = (4.71305228338,3.14122592819,-4.71769892953)
camera.keyframe_insert(data_path="rotation_euler",frame=420.0)
camera.keyframe_insert(data_path="location", frame=420.0)
camera.location.x = 193.1213
camera.location.y = 0.3007558
camera.location.z = -3.281162
camera.rotation_euler = (4.71342851038,3.14388943959,-4.71770182953)
camera.keyframe_insert(data_path="rotation_euler",frame=423.0)
camera.keyframe_insert(data_path="location", frame=423.0)
camera.location.x = 194.5397
camera.location.y = 0.2979338
camera.location.z = -3.314135
camera.rotation_euler = (4.71375853738,3.14688697659,-4.71771352953)
camera.keyframe_insert(data_path="rotation_euler",frame=426.0)
camera.keyframe_insert(data_path="location", frame=426.0)
camera.location.x = 195.9592
camera.location.y = 0.2945301
camera.location.z = -3.344375
camera.rotation_euler = (4.71416056738,3.15096126059,-4.71774402953)
camera.keyframe_insert(data_path="rotation_euler",frame=429.0)
camera.keyframe_insert(data_path="location", frame=429.0)
camera.location.x = 197.3809
camera.location.y = 0.2955048
camera.location.z = -3.384557
camera.rotation_euler = (4.71438633738,3.15439752359,-4.71778262953)
camera.keyframe_insert(data_path="rotation_euler",frame=432.0)
camera.keyframe_insert(data_path="location", frame=432.0)
camera.location.x = 198.8011
camera.location.y = 0.2998637
camera.location.z = -3.419365
camera.rotation_euler = (4.71462233638,3.15253612359,-4.71776102953)
camera.keyframe_insert(data_path="rotation_euler",frame=435.0)
camera.keyframe_insert(data_path="location", frame=435.0)
camera.location.x = 200.2242
camera.location.y = 0.3150034
camera.location.z = -3.471363
camera.rotation_euler = (4.71509475738,3.14599741359,-4.71771202953)
camera.keyframe_insert(data_path="rotation_euler",frame=438.0)
camera.keyframe_insert(data_path="location", frame=438.0)
camera.location.x = 201.6573
camera.location.y = 0.3321987
camera.location.z = -3.515079
camera.rotation_euler = (4.71625598538,3.13665497459,-4.71771832953)
camera.keyframe_insert(data_path="rotation_euler",frame=441.0)
camera.keyframe_insert(data_path="location", frame=441.0)
camera.location.x = 203.0948
camera.location.y = 0.3485808
camera.location.z = -3.555576
camera.rotation_euler = (4.71769210138,3.12840136359,-4.71779972953)
camera.keyframe_insert(data_path="rotation_euler",frame=444.0)
camera.keyframe_insert(data_path="location", frame=444.0)
camera.location.x = 204.5325
camera.location.y = 0.3518432
camera.location.z = -3.580327
camera.rotation_euler = (4.71847821238,3.12693116359,-4.71782462953)
camera.keyframe_insert(data_path="rotation_euler",frame=447.0)
camera.keyframe_insert(data_path="location", frame=447.0)
camera.location.x = 205.9704
camera.location.y = 0.3481359
camera.location.z = -3.604083
camera.rotation_euler = (4.71794548838,3.12896637359,-4.71779372953)
camera.keyframe_insert(data_path="rotation_euler",frame=450.0)
camera.keyframe_insert(data_path="location", frame=450.0)
camera.location.x = 207.4183
camera.location.y = 0.3438313
camera.location.z = -3.628674
camera.rotation_euler = (4.71677925238,3.13205732059,-4.71775372953)
camera.keyframe_insert(data_path="rotation_euler",frame=453.0)
camera.keyframe_insert(data_path="location", frame=453.0)
camera.location.x = 208.8679
camera.location.y = 0.342198
camera.location.z = -3.650886
camera.rotation_euler = (4.71565433738,3.13453594459,-4.71772882953)
camera.keyframe_insert(data_path="rotation_euler",frame=456.0)
camera.keyframe_insert(data_path="location", frame=456.0)
camera.location.x = 210.3232
camera.location.y = 0.3429638
camera.location.z = -3.67436
camera.rotation_euler = (4.71513534838,3.13417144659,-4.71772992953)
camera.keyframe_insert(data_path="rotation_euler",frame=459.0)
camera.keyframe_insert(data_path="location", frame=459.0)
camera.location.x = 211.7849
camera.location.y = 0.347951
camera.location.z = -3.708945
camera.rotation_euler = (4.71502884838,3.13272668559,-4.71774142953)
camera.keyframe_insert(data_path="rotation_euler",frame=462.0)
camera.keyframe_insert(data_path="location", frame=462.0)
camera.location.x = 213.2453
camera.location.y = 0.3533161
camera.location.z = -3.741769
camera.rotation_euler = (4.71491347838,3.13147658359,-4.71775292953)
camera.keyframe_insert(data_path="rotation_euler",frame=465.0)
camera.keyframe_insert(data_path="location", frame=465.0)
camera.location.x = 214.7142
camera.location.y = 0.3575809
camera.location.z = -3.778065
camera.rotation_euler = (4.71467661738,3.13206445759,-4.71774662953)
camera.keyframe_insert(data_path="rotation_euler",frame=468.0)
camera.keyframe_insert(data_path="location", frame=468.0)
camera.location.x = 216.1864
camera.location.y = 0.3574839
camera.location.z = -3.809987
camera.rotation_euler = (4.71427107838,3.13248315459,-4.71774192953)
camera.keyframe_insert(data_path="rotation_euler",frame=471.0)
camera.keyframe_insert(data_path="location", frame=471.0)
camera.location.x = 217.6615
camera.location.y = 0.3559812
camera.location.z = -3.837087
camera.rotation_euler = (4.71407665638,3.13323343859,-4.71773502953)
camera.keyframe_insert(data_path="rotation_euler",frame=474.0)
camera.keyframe_insert(data_path="location", frame=474.0)
camera.location.x = 219.1419
camera.location.y = 0.3604882
camera.location.z = -3.867619
camera.rotation_euler = (4.71362970638,3.13288174459,-4.71773732953)
camera.keyframe_insert(data_path="rotation_euler",frame=477.0)
camera.keyframe_insert(data_path="location", frame=477.0)
camera.location.x = 220.6192
camera.location.y = 0.3669047
camera.location.z = -3.899694
camera.rotation_euler = (4.71328290218,3.13284901859,-4.71773722953)
camera.keyframe_insert(data_path="rotation_euler",frame=480.0)
camera.keyframe_insert(data_path="location", frame=480.0)
camera.location.x = 222.1053
camera.location.y = 0.3711882
camera.location.z = -3.93317
camera.rotation_euler = (4.71308269948,3.13279844859,-4.71773752953)
camera.keyframe_insert(data_path="rotation_euler",frame=483.0)
camera.keyframe_insert(data_path="location", frame=483.0)
camera.location.x = 223.5894
camera.location.y = 0.3755068
camera.location.z = -3.961696
camera.rotation_euler = (4.71273701548,3.13169995259,-4.71774762953)
camera.keyframe_insert(data_path="rotation_euler",frame=486.0)
camera.keyframe_insert(data_path="location", frame=486.0)
camera.location.x = 225.0789
camera.location.y = 0.3771503
camera.location.z = -3.990503
camera.rotation_euler = (4.71239204115,3.13205738259,-4.71774412953)
camera.keyframe_insert(data_path="rotation_euler",frame=489.0)
camera.keyframe_insert(data_path="location", frame=489.0)
camera.location.x = 226.5691
camera.location.y = 0.3787707
camera.location.z = -4.017067
camera.rotation_euler = (4.71212852698,3.13155453359,-4.71774902953)
camera.keyframe_insert(data_path="rotation_euler",frame=492.0)
camera.keyframe_insert(data_path="location", frame=492.0)
camera.location.x = 228.0602
camera.location.y = 0.3785266
camera.location.z = -4.048136
camera.rotation_euler = (4.71202388898,3.13249804759,-4.71774002953)
camera.keyframe_insert(data_path="rotation_euler",frame=495.0)
camera.keyframe_insert(data_path="location", frame=495.0)
camera.location.x = 229.5511
camera.location.y = 0.3786614
camera.location.z = -4.075078
camera.rotation_euler = (4.71213129428,3.13375233159,-4.71772942953)
camera.keyframe_insert(data_path="rotation_euler",frame=498.0)
camera.keyframe_insert(data_path="location", frame=498.0)
camera.location.x = 231.0454
camera.location.y = 0.3766086
camera.location.z = -4.099044
camera.rotation_euler = (4.71229997373,3.13488370959,-4.71772112953)
camera.keyframe_insert(data_path="rotation_euler",frame=501.0)
camera.keyframe_insert(data_path="location", frame=501.0)
camera.location.x = 232.5421
camera.location.y = 0.3745701
camera.location.z = -4.124994
camera.rotation_euler = (4.71250182568,3.13647233159,-4.71771172953)
camera.keyframe_insert(data_path="rotation_euler",frame=504.0)
camera.keyframe_insert(data_path="location", frame=504.0)
camera.location.x = 234.0378
camera.location.y = 0.3739626
camera.location.z = -4.153624
camera.rotation_euler = (4.71249386258,3.13663081959,-4.71771092953)
camera.keyframe_insert(data_path="rotation_euler",frame=507.0)
camera.keyframe_insert(data_path="location", frame=507.0)
camera.location.x = 235.539
camera.location.y = 0.3764692
camera.location.z = -4.186333
camera.rotation_euler = (4.71240920197,3.13625467859,-4.71771282953)
camera.keyframe_insert(data_path="rotation_euler",frame=510.0)
camera.keyframe_insert(data_path="location", frame=510.0)
camera.location.x = 237.0446
camera.location.y = 0.3784077
camera.location.z = -4.220226
camera.rotation_euler = (4.71262532488,3.13556446659,-4.71771682953)
camera.keyframe_insert(data_path="rotation_euler",frame=513.0)
camera.keyframe_insert(data_path="location", frame=513.0)
camera.location.x = 238.5499
camera.location.y = 0.3814943
camera.location.z = -4.253315
camera.rotation_euler = (4.71315700808,3.13429189259,-4.71772552953)
camera.keyframe_insert(data_path="rotation_euler",frame=516.0)
camera.keyframe_insert(data_path="location", frame=516.0)
camera.location.x = 240.0603
camera.location.y = 0.3829065
camera.location.z = -4.285388
camera.rotation_euler = (4.71381061738,3.13397759759,-4.71772862953)
camera.keyframe_insert(data_path="rotation_euler",frame=519.0)
camera.keyframe_insert(data_path="location", frame=519.0)
camera.location.x = 241.5712
camera.location.y = 0.3820924
camera.location.z = -4.315103
camera.rotation_euler = (4.71432394238,3.13424747059,-4.71772742953)
camera.keyframe_insert(data_path="rotation_euler",frame=522.0)
camera.keyframe_insert(data_path="location", frame=522.0)
camera.location.x = 243.0873
camera.location.y = 0.3818797
camera.location.z = -4.347138
camera.rotation_euler = (4.71479321638,3.13399628259,-4.71773032953)
camera.keyframe_insert(data_path="rotation_euler",frame=525.0)
camera.keyframe_insert(data_path="location", frame=525.0)
camera.location.x = 244.602
camera.location.y = 0.3796393
camera.location.z = -4.377646
camera.rotation_euler = (4.71533937838,3.13402766259,-4.71773162953)
camera.keyframe_insert(data_path="rotation_euler",frame=528.0)
camera.keyframe_insert(data_path="location", frame=528.0)
camera.location.x = 246.1231
camera.location.y = 0.377078
camera.location.z = -4.404696
camera.rotation_euler = (4.71564941738,3.13299842959,-4.71774082953)
camera.keyframe_insert(data_path="rotation_euler",frame=531.0)
camera.keyframe_insert(data_path="location", frame=531.0)
camera.location.x = 247.6477
camera.location.y = 0.3721572
camera.location.z = -4.432022
camera.rotation_euler = (4.71571582038,3.13349096659,-4.71773692953)
camera.keyframe_insert(data_path="rotation_euler",frame=534.0)
camera.keyframe_insert(data_path="location", frame=534.0)
camera.location.x = 249.1682
camera.location.y = 0.3683885
camera.location.z = -4.458219
camera.rotation_euler = (4.71541154438,3.13341302159,-4.71773662953)
camera.keyframe_insert(data_path="rotation_euler",frame=537.0)
camera.keyframe_insert(data_path="location", frame=537.0)
camera.location.x = 250.6964
camera.location.y = 0.3658944
camera.location.z = -4.487063
camera.rotation_euler = (4.71518709838,3.13308682959,-4.71773872953)
camera.keyframe_insert(data_path="rotation_euler",frame=540.0)
camera.keyframe_insert(data_path="location", frame=540.0)
camera.location.x = 252.2241
camera.location.y = 0.3629857
camera.location.z = -4.511301
camera.rotation_euler = (4.71522851238,3.13162118559,-4.71775232953)
camera.keyframe_insert(data_path="rotation_euler",frame=543.0)
camera.keyframe_insert(data_path="location", frame=543.0)
camera.location.x = 253.757
camera.location.y = 0.3598899
camera.location.z = -4.535745
camera.rotation_euler = (4.71543324838,3.13064144359,-4.71776322953)
camera.keyframe_insert(data_path="rotation_euler",frame=546.0)
camera.keyframe_insert(data_path="location", frame=546.0)
camera.location.x = 255.2885
camera.location.y = 0.3565283
camera.location.z = -4.558441
camera.rotation_euler = (4.71532091438,3.13004108359,-4.71776962953)
camera.keyframe_insert(data_path="rotation_euler",frame=549.0)
camera.keyframe_insert(data_path="location", frame=549.0)
camera.location.x = 256.823
camera.location.y = 0.3518994
camera.location.z = -4.58494
camera.rotation_euler = (4.71533348438,3.13161975059,-4.71775272953)
camera.keyframe_insert(data_path="rotation_euler",frame=552.0)
camera.keyframe_insert(data_path="location", frame=552.0)
camera.location.x = 258.3612
camera.location.y = 0.3474488
camera.location.z = -4.611578
camera.rotation_euler = (4.71523860438,3.13311881959,-4.71773862953)
camera.keyframe_insert(data_path="rotation_euler",frame=555.0)
camera.keyframe_insert(data_path="location", frame=555.0)
camera.location.x = 259.9003
camera.location.y = 0.3407995
camera.location.z = -4.637604
camera.rotation_euler = (4.71530059838,3.13594362459,-4.71771882953)
camera.keyframe_insert(data_path="rotation_euler",frame=558.0)
camera.keyframe_insert(data_path="location", frame=558.0)
camera.location.x = 261.4352
camera.location.y = 0.3346776
camera.location.z = -4.662237
camera.rotation_euler = (4.71497894238,3.13748131959,-4.71771042953)
camera.keyframe_insert(data_path="rotation_euler",frame=561.0)
camera.keyframe_insert(data_path="location", frame=561.0)
camera.location.x = 262.9731
camera.location.y = 0.3291338
camera.location.z = -4.686551
camera.rotation_euler = (4.71469647238,3.13870518259,-4.71770542953)
camera.keyframe_insert(data_path="rotation_euler",frame=564.0)
camera.keyframe_insert(data_path="location", frame=564.0)
camera.location.x = 264.5113
camera.location.y = 0.3253738
camera.location.z = -4.715745
camera.rotation_euler = (4.71527264238,3.14065708849,-4.71770322953)
camera.keyframe_insert(data_path="rotation_euler",frame=567.0)
camera.keyframe_insert(data_path="location", frame=567.0)
camera.location.x = 266.0572
camera.location.y = 0.3249046
camera.location.z = -4.748173
camera.rotation_euler = (4.71571814338,3.14171606749,-4.71770412953)
camera.keyframe_insert(data_path="rotation_euler",frame=570.0)
camera.keyframe_insert(data_path="location", frame=570.0)
camera.location.x = 267.5981
camera.location.y = 0.3208179
camera.location.z = -4.788372
camera.rotation_euler = (4.71584839438,3.14365875859,-4.71770672953)
camera.keyframe_insert(data_path="rotation_euler",frame=573.0)
camera.keyframe_insert(data_path="location", frame=573.0)
camera.location.x = 269.1377
camera.location.y = 0.3173943
camera.location.z = -4.824679
camera.rotation_euler = (4.71613985638,3.14450134359,-4.71770992953)
camera.keyframe_insert(data_path="rotation_euler",frame=576.0)
camera.keyframe_insert(data_path="location", frame=576.0)
camera.location.x = 270.6771
camera.location.y = 0.3166024
camera.location.z = -4.866052
camera.rotation_euler = (4.71678497438,3.14353068459,-4.71771012953)
camera.keyframe_insert(data_path="rotation_euler",frame=579.0)
camera.keyframe_insert(data_path="location", frame=579.0)
camera.location.x = 272.2185
camera.location.y = 0.3155943
camera.location.z = -4.906588
camera.rotation_euler = (4.71786878338,3.14205878599,-4.71771372953)
camera.keyframe_insert(data_path="rotation_euler",frame=582.0)
camera.keyframe_insert(data_path="location", frame=582.0)
camera.location.x = 273.7649
camera.location.y = 0.3140401
camera.location.z = -4.950219
camera.rotation_euler = (4.71882918338,3.14035972059,-4.71772012953)
camera.keyframe_insert(data_path="rotation_euler",frame=585.0)
camera.keyframe_insert(data_path="location", frame=585.0)
camera.location.x = 275.3072
camera.location.y = 0.3112309
camera.location.z = -4.987626
camera.rotation_euler = (4.71979162238,3.13916806459,-4.71772892953)
camera.keyframe_insert(data_path="rotation_euler",frame=588.0)
camera.keyframe_insert(data_path="location", frame=588.0)
camera.location.x = 276.8535
camera.location.y = 0.3114206
camera.location.z = -5.039836
camera.rotation_euler = (4.72058212938,3.13840992459,-4.71773722953)
camera.keyframe_insert(data_path="rotation_euler",frame=591.0)
camera.keyframe_insert(data_path="location", frame=591.0)
camera.location.x = 278.3952
camera.location.y = 0.3062026
camera.location.z = -5.082755
camera.rotation_euler = (4.72141860338,3.13805241159,-4.71774562953)
camera.keyframe_insert(data_path="rotation_euler",frame=594.0)
camera.keyframe_insert(data_path="location", frame=594.0)
camera.location.x = 279.9451
camera.location.y = 0.3011292
camera.location.z = -5.134136
camera.rotation_euler = (4.72232439738,3.13859032759,-4.71775252953)
camera.keyframe_insert(data_path="rotation_euler",frame=597.0)
camera.keyframe_insert(data_path="location", frame=597.0)
camera.location.x = 281.4958
camera.location.y = 0.2897536
camera.location.z = -5.172038
camera.rotation_euler = (4.72316352038,3.13918057159,-4.71775952953)
camera.keyframe_insert(data_path="rotation_euler",frame=600.0)
camera.keyframe_insert(data_path="location", frame=600.0)
camera.location.x = 283.0498
camera.location.y = 0.2764899
camera.location.z = -5.210037
camera.rotation_euler = (4.72391055038,3.14010203859,-4.71776612953)
camera.keyframe_insert(data_path="rotation_euler",frame=603.0)
camera.keyframe_insert(data_path="location", frame=603.0)
camera.location.x = 284.6005
camera.location.y = 0.2599233
camera.location.z = -5.24169
camera.rotation_euler = (4.72425339038,3.14152270375,-4.71776902953)
camera.keyframe_insert(data_path="rotation_euler",frame=606.0)
camera.keyframe_insert(data_path="location", frame=606.0)
camera.location.x = 286.1454
camera.location.y = 0.2447296
camera.location.z = -5.277598
camera.rotation_euler = (4.72431578038,3.14217095899,-4.71776992953)
camera.keyframe_insert(data_path="rotation_euler",frame=609.0)
camera.keyframe_insert(data_path="location", frame=609.0)
camera.location.x = 287.6999
camera.location.y = 0.2301583
camera.location.z = -5.316244
camera.rotation_euler = (4.72396135038,3.14308494859,-4.71776672953)
camera.keyframe_insert(data_path="rotation_euler",frame=612.0)
camera.keyframe_insert(data_path="location", frame=612.0)
camera.location.x = 289.2536
camera.location.y = 0.2170805
camera.location.z = -5.355148
camera.rotation_euler = (4.72311846038,3.14276446659,-4.71775682953)
camera.keyframe_insert(data_path="rotation_euler",frame=615.0)
camera.keyframe_insert(data_path="location", frame=615.0)
camera.location.x = 290.8103
camera.location.y = 0.2045251
camera.location.z = -5.390475
camera.rotation_euler = (4.72241035038,3.14437604159,-4.71775272953)
camera.keyframe_insert(data_path="rotation_euler",frame=618.0)
camera.keyframe_insert(data_path="location", frame=618.0)
camera.location.x = 292.3692
camera.location.y = 0.1926927
camera.location.z = -5.424878
camera.rotation_euler = (4.72139685138,3.14427444059,-4.71774282953)
camera.keyframe_insert(data_path="rotation_euler",frame=621.0)
camera.keyframe_insert(data_path="location", frame=621.0)
camera.location.x = 293.9316
camera.location.y = 0.1828271
camera.location.z = -5.462578
camera.rotation_euler = (4.72083621338,3.14400468759,-4.71773722953)
camera.keyframe_insert(data_path="rotation_euler",frame=624.0)
camera.keyframe_insert(data_path="location", frame=624.0)
camera.location.x = 295.5007
camera.location.y = 0.1753107
camera.location.z = -5.502144
camera.rotation_euler = (4.72012654538,3.14396614059,-4.71773132953)
camera.keyframe_insert(data_path="rotation_euler",frame=627.0)
camera.keyframe_insert(data_path="location", frame=627.0)
camera.location.x = 297.0723
camera.location.y = 0.1681708
camera.location.z = -5.542654
camera.rotation_euler = (4.71927618938,3.14441226559,-4.71772632953)
camera.keyframe_insert(data_path="rotation_euler",frame=630.0)
camera.keyframe_insert(data_path="location", frame=630.0)
camera.location.x = 298.6502
camera.location.y = 0.1571664
camera.location.z = -5.573209
camera.rotation_euler = (4.71824035938,3.14505949059,-4.71772172953)
camera.keyframe_insert(data_path="rotation_euler",frame=633.0)
camera.keyframe_insert(data_path="location", frame=633.0)
camera.location.x = 300.2367
camera.location.y = 0.1498301
camera.location.z = -5.605662
camera.rotation_euler = (4.71768046938,3.14347740159,-4.71771442953)
camera.keyframe_insert(data_path="rotation_euler",frame=636.0)
camera.keyframe_insert(data_path="location", frame=636.0)
camera.location.x = 301.8211
camera.location.y = 0.1436567
camera.location.z = -5.638056
camera.rotation_euler = (4.71831213338,3.14295078859,-4.71771712953)
camera.keyframe_insert(data_path="rotation_euler",frame=639.0)
camera.keyframe_insert(data_path="location", frame=639.0)
camera.location.x = 303.413
camera.location.y = 0.1362308
camera.location.z = -5.674045
camera.rotation_euler = (4.71928384838,3.14237438909,-4.71772272953)
camera.keyframe_insert(data_path="rotation_euler",frame=642.0)
camera.keyframe_insert(data_path="location", frame=642.0)
camera.location.x = 305.0095
camera.location.y = 0.1245796
camera.location.z = -5.704927
camera.rotation_euler = (4.71966536838,3.14365882459,-4.71772722953)
camera.keyframe_insert(data_path="rotation_euler",frame=645.0)
camera.keyframe_insert(data_path="location", frame=645.0)
camera.location.x = 306.6086
camera.location.y = 0.1113075
camera.location.z = -5.740563
camera.rotation_euler = (4.71984204638,3.14537696059,-4.71773352953)
camera.keyframe_insert(data_path="rotation_euler",frame=648.0)
camera.keyframe_insert(data_path="location", frame=648.0)
camera.location.x = 308.2116
camera.location.y = 0.1009905
camera.location.z = -5.775938
camera.rotation_euler = (4.72014724138,3.14702133059,-4.71774342953)
camera.keyframe_insert(data_path="rotation_euler",frame=651.0)
camera.keyframe_insert(data_path="location", frame=651.0)
camera.location.x = 309.8189
camera.location.y = 0.0964999
camera.location.z = -5.821106
camera.rotation_euler = (4.72015246938,3.14727997859,-4.71774492953)
camera.keyframe_insert(data_path="rotation_euler",frame=654.0)
camera.keyframe_insert(data_path="location", frame=654.0)
camera.location.x = 311.4331
camera.location.y = 0.09324941
camera.location.z = -5.863046
camera.rotation_euler = (4.71803337738,3.14673974759,-4.71772782953)
camera.keyframe_insert(data_path="rotation_euler",frame=657.0)
camera.keyframe_insert(data_path="location", frame=657.0)
camera.location.x = 313.0445
camera.location.y = 0.09658434
camera.location.z = -5.907766
camera.rotation_euler = (4.71588565038,3.14581396959,-4.71771362953)
camera.keyframe_insert(data_path="rotation_euler",frame=660.0)
camera.keyframe_insert(data_path="location", frame=660.0)
camera.location.x = 314.6682
camera.location.y = 0.106523
camera.location.z = -5.952029
camera.rotation_euler = (4.71547311038,3.14407742159,-4.71770642953)
camera.keyframe_insert(data_path="rotation_euler",frame=663.0)
camera.keyframe_insert(data_path="location", frame=663.0)
camera.location.x = 316.2953
camera.location.y = 0.1079811
camera.location.z = -5.990688
camera.rotation_euler = (4.71597296338,3.14530961459,-4.71771192953)
camera.keyframe_insert(data_path="rotation_euler",frame=666.0)
camera.keyframe_insert(data_path="location", frame=666.0)
camera.location.x = 317.9241
camera.location.y = 0.1086696
camera.location.z = -6.032426
camera.rotation_euler = (4.71617922738,3.14635974759,-4.71771712953)
camera.keyframe_insert(data_path="rotation_euler",frame=669.0)
camera.keyframe_insert(data_path="location", frame=669.0)
camera.location.x = 319.5525
camera.location.y = 0.1058419
camera.location.z = -6.068362
camera.rotation_euler = (4.71646136338,3.14778747159,-4.71772612953)
camera.keyframe_insert(data_path="rotation_euler",frame=672.0)
camera.keyframe_insert(data_path="location", frame=672.0)
camera.location.x = 321.1823
camera.location.y = 0.1039698
camera.location.z = -6.106845
camera.rotation_euler = (4.71680114338,3.14855751459,-4.71773262953)
camera.keyframe_insert(data_path="rotation_euler",frame=675.0)
camera.keyframe_insert(data_path="location", frame=675.0)
camera.location.x = 322.8139
camera.location.y = 0.1009179
camera.location.z = -6.143404
camera.rotation_euler = (4.71699827138,3.14843383359,-4.71773262953)
camera.keyframe_insert(data_path="rotation_euler",frame=678.0)
camera.keyframe_insert(data_path="location", frame=678.0)
camera.location.x = 324.4397
camera.location.y = 0.09883113
camera.location.z = -6.185282
camera.rotation_euler = (4.71748771338,3.14856880759,-4.71773592953)
camera.keyframe_insert(data_path="rotation_euler",frame=681.0)
camera.keyframe_insert(data_path="location", frame=681.0)
camera.location.x = 326.0682
camera.location.y = 0.09648438
camera.location.z = -6.224088
camera.rotation_euler = (4.71797153738,3.14712451159,-4.71772952953)
camera.keyframe_insert(data_path="rotation_euler",frame=684.0)
camera.keyframe_insert(data_path="location", frame=684.0)
camera.location.x = 327.6976
camera.location.y = 0.09411052
camera.location.z = -6.268819
camera.rotation_euler = (4.71864380338,3.14633256659,-4.71772942953)
camera.keyframe_insert(data_path="rotation_euler",frame=687.0)
camera.keyframe_insert(data_path="location", frame=687.0)
camera.location.x = 329.3242
camera.location.y = 0.08496956
camera.location.z = -6.305428
camera.rotation_euler = (4.71948501838,3.14745986659,-4.71774102953)
camera.keyframe_insert(data_path="rotation_euler",frame=690.0)
camera.keyframe_insert(data_path="location", frame=690.0)
camera.location.x = 330.9508
camera.location.y = 0.07442718
camera.location.z = -6.342113
camera.rotation_euler = (4.71961303738,3.14835943159,-4.71774762953)
camera.keyframe_insert(data_path="rotation_euler",frame=693.0)
camera.keyframe_insert(data_path="location", frame=693.0)
camera.location.x = 332.5694
camera.location.y = 0.06421231
camera.location.z = -6.372244
camera.rotation_euler = (4.71931158138,3.14958119159,-4.71775452953)
camera.keyframe_insert(data_path="rotation_euler",frame=696.0)
camera.keyframe_insert(data_path="location", frame=696.0)
camera.location.x = 334.1893
camera.location.y = 0.05844895
camera.location.z = -6.413497
camera.rotation_euler = (4.71932370938,3.14877647259,-4.71774842953)
camera.keyframe_insert(data_path="rotation_euler",frame=699.0)
camera.keyframe_insert(data_path="location", frame=699.0)
camera.location.x = 335.8024
camera.location.y = 0.05434961
camera.location.z = -6.45078
camera.rotation_euler = (4.71922229638,3.14638008759,-4.71773342953)
camera.keyframe_insert(data_path="rotation_euler",frame=702.0)
camera.keyframe_insert(data_path="location", frame=702.0)
camera.location.x = 337.4097
camera.location.y = 0.04949748
camera.location.z = -6.492551
camera.rotation_euler = (4.71849827938,3.14516461259,-4.71772362953)
camera.keyframe_insert(data_path="rotation_euler",frame=705.0)
camera.keyframe_insert(data_path="location", frame=705.0)
camera.location.x = 339.0211
camera.location.y = 0.04548042
camera.location.z = -6.532188
camera.rotation_euler = (4.71762310038,3.14358683659,-4.71771432953)
camera.keyframe_insert(data_path="rotation_euler",frame=708.0)
camera.keyframe_insert(data_path="location", frame=708.0)
camera.location.x = 340.6287
camera.location.y = 0.04257007
camera.location.z = -6.571397
camera.rotation_euler = (4.71675126438,3.14305495459,-4.71770922953)
camera.keyframe_insert(data_path="rotation_euler",frame=711.0)
camera.keyframe_insert(data_path="location", frame=711.0)
camera.location.x = 342.2462
camera.location.y = 0.03930296
camera.location.z = -6.601811
camera.rotation_euler = (4.71568840638,3.14187531759,-4.71770412953)
camera.keyframe_insert(data_path="rotation_euler",frame=714.0)
camera.keyframe_insert(data_path="location", frame=714.0)
camera.location.x = 343.8528
camera.location.y = 0.03681003
camera.location.z = -6.628918
camera.rotation_euler = (4.71448068038,3.14138641189,-4.71770082953)
camera.keyframe_insert(data_path="rotation_euler",frame=717.0)
camera.keyframe_insert(data_path="location", frame=717.0)
camera.location.x = 345.4525
camera.location.y = 0.03514659
camera.location.z = -6.652782
camera.rotation_euler = (4.71266063718,3.14203676419,-4.71769872953)
camera.keyframe_insert(data_path="rotation_euler",frame=720.0)
camera.keyframe_insert(data_path="location", frame=720.0)
camera.location.x = 347.0554
camera.location.y = 0.0345479
camera.location.z = -6.677644
camera.rotation_euler = (4.71076317538,3.14303231159,-4.71770092953)
camera.keyframe_insert(data_path="rotation_euler",frame=723.0)
camera.keyframe_insert(data_path="location", frame=723.0)
camera.location.x = 348.6551
camera.location.y = 0.03707175
camera.location.z = -6.708152
camera.rotation_euler = (4.70976349138,3.14465525959,-4.71770672953)
camera.keyframe_insert(data_path="rotation_euler",frame=726.0)
camera.keyframe_insert(data_path="location", frame=726.0)
camera.location.x = 350.2532
camera.location.y = 0.04156332
camera.location.z = -6.737239
camera.rotation_euler = (4.70933146938,3.14493464059,-4.71770892953)
camera.keyframe_insert(data_path="rotation_euler",frame=729.0)
camera.keyframe_insert(data_path="location", frame=729.0)
camera.location.x = 351.8478
camera.location.y = 0.05261018
camera.location.z = -6.773059
camera.rotation_euler = (4.70911531438,3.14559892359,-4.71771202953)
camera.keyframe_insert(data_path="rotation_euler",frame=732.0)
camera.keyframe_insert(data_path="location", frame=732.0)
camera.location.x = 353.4464
camera.location.y = 0.06277075
camera.location.z = -6.805862
camera.rotation_euler = (4.70909469338,3.14566400159,-4.71771232953)
camera.keyframe_insert(data_path="rotation_euler",frame=735.0)
camera.keyframe_insert(data_path="location", frame=735.0)
camera.location.x = 355.0379
camera.location.y = 0.07506606
camera.location.z = -6.843564
camera.rotation_euler = (4.70912566538,3.14615857759,-4.71771432953)
camera.keyframe_insert(data_path="rotation_euler",frame=738.0)
camera.keyframe_insert(data_path="location", frame=738.0)
camera.location.x = 356.6308
camera.location.y = 0.08570356
camera.location.z = -6.882552
camera.rotation_euler = (4.70909538138,3.14680848259,-4.71771762953)
camera.keyframe_insert(data_path="rotation_euler",frame=741.0)
camera.keyframe_insert(data_path="location", frame=741.0)
camera.location.x = 358.2218
camera.location.y = 0.09729989
camera.location.z = -6.921763
camera.rotation_euler = (4.70897097638,3.14699439059,-4.71771902953)
camera.keyframe_insert(data_path="rotation_euler",frame=744.0)
camera.keyframe_insert(data_path="location", frame=744.0)
camera.location.x = 359.8125
camera.location.y = 0.1091014
camera.location.z = -6.958715
camera.rotation_euler = (4.70904320338,3.14748995759,-4.71772162953)
camera.keyframe_insert(data_path="rotation_euler",frame=747.0)
camera.keyframe_insert(data_path="location", frame=747.0)
camera.location.x = 361.4037
camera.location.y = 0.1223014
camera.location.z = -6.995935
camera.rotation_euler = (4.70911920738,3.14706139759,-4.71771892953)
camera.keyframe_insert(data_path="rotation_euler",frame=750.0)
camera.keyframe_insert(data_path="location", frame=750.0)
camera.location.x = 362.989
camera.location.y = 0.1322206
camera.location.z = -7.034017
camera.rotation_euler = (4.70918958838,3.14858364359,-4.71772812953)
camera.keyframe_insert(data_path="rotation_euler",frame=753.0)
camera.keyframe_insert(data_path="location", frame=753.0)
camera.location.x = 364.5867
camera.location.y = 0.1419952
camera.location.z = -7.072717
camera.rotation_euler = (4.70930480938,3.14993652059,-4.71773822953)
camera.keyframe_insert(data_path="rotation_euler",frame=756.0)
camera.keyframe_insert(data_path="location", frame=756.0)
camera.location.x = 366.1838
camera.location.y = 0.1552999
camera.location.z = -7.112398
camera.rotation_euler = (4.70917329738,3.15159984359,-4.71775382953)
camera.keyframe_insert(data_path="rotation_euler",frame=759.0)
camera.keyframe_insert(data_path="location", frame=759.0)
camera.location.x = 367.7811
camera.location.y = 0.1668615
camera.location.z = -7.146884
camera.rotation_euler = (4.70922587538,3.15215026359,-4.71775932953)
camera.keyframe_insert(data_path="rotation_euler",frame=762.0)
camera.keyframe_insert(data_path="location", frame=762.0)
camera.location.x = 369.3866
camera.location.y = 0.1858911
camera.location.z = -7.18829
camera.rotation_euler = (4.70960290338,3.15103715159,-4.71774712953)
camera.keyframe_insert(data_path="rotation_euler",frame=765.0)
camera.keyframe_insert(data_path="location", frame=765.0)
camera.location.x = 370.9753
camera.location.y = 0.2029185
camera.location.z = -7.225081
camera.rotation_euler = (4.71008151038,3.14902759859,-4.71772892953)
camera.keyframe_insert(data_path="rotation_euler",frame=768.0)
camera.keyframe_insert(data_path="location", frame=768.0)
camera.location.x = 372.6154
camera.location.y = 0.2229981
camera.location.z = -7.26884
camera.rotation_euler = (4.71058345038,3.14769276959,-4.71771882953)
camera.keyframe_insert(data_path="rotation_euler",frame=771.0)
camera.keyframe_insert(data_path="location", frame=771.0)
camera.location.x = 374.2253
camera.location.y = 0.2378134
camera.location.z = -7.306808
camera.rotation_euler = (4.71095365838,3.14729108859,-4.71771592953)
camera.keyframe_insert(data_path="rotation_euler",frame=774.0)
camera.keyframe_insert(data_path="location", frame=774.0)
camera.location.x = 375.7811
camera.location.y = 0.2519893
camera.location.z = -7.344936
camera.rotation_euler = (4.71118901338,3.14747208459,-4.71771662953)
camera.keyframe_insert(data_path="rotation_euler",frame=777.0)
camera.keyframe_insert(data_path="location", frame=777.0)
camera.location.x = 377.3873
camera.location.y = 0.2625878
camera.location.z = -7.379336
camera.rotation_euler = (4.71147111328,3.14731060359,-4.71771542953)
camera.keyframe_insert(data_path="rotation_euler",frame=780.0)
camera.keyframe_insert(data_path="location", frame=780.0)
camera.location.x = 378.9929
camera.location.y = 0.2704012
camera.location.z = -7.414418
camera.rotation_euler = (4.71169605448,3.14692848259,-4.71771312953)
camera.keyframe_insert(data_path="rotation_euler",frame=783.0)
camera.keyframe_insert(data_path="location", frame=783.0)
camera.location.x = 380.6071
camera.location.y = 0.2783585
camera.location.z = -7.448411
camera.rotation_euler = (4.71200762348,3.14577595859,-4.71770742953)
camera.keyframe_insert(data_path="rotation_euler",frame=786.0)
camera.keyframe_insert(data_path="location", frame=786.0)
camera.location.x = 382.2202
camera.location.y = 0.2877925
camera.location.z = -7.485057
camera.rotation_euler = (4.71233212091,3.14448401659,-4.71770282953)
camera.keyframe_insert(data_path="rotation_euler",frame=789.0)
camera.keyframe_insert(data_path="location", frame=789.0)
camera.location.x = 383.8408
camera.location.y = 0.2960866
camera.location.z = -7.522079
camera.rotation_euler = (4.71260043258,3.14333115859,-4.71770012953)
camera.keyframe_insert(data_path="rotation_euler",frame=792.0)
camera.keyframe_insert(data_path="location", frame=792.0)
camera.location.x = 385.4512
camera.location.y = 0.3039652
camera.location.z = -7.558709
camera.rotation_euler = (4.71287027718,3.14246703689,-4.71769912953)
camera.keyframe_insert(data_path="rotation_euler",frame=795.0)
camera.keyframe_insert(data_path="location", frame=795.0)
camera.location.x = 387.0678
camera.location.y = 0.3110174
camera.location.z = -7.596748
camera.rotation_euler = (4.71319635958,3.14172060589,-4.71769892953)
camera.keyframe_insert(data_path="rotation_euler",frame=798.0)
camera.keyframe_insert(data_path="location", frame=798.0)
camera.location.x = 388.6857
camera.location.y = 0.3164538
camera.location.z = -7.631598
camera.rotation_euler = (4.71344989938,3.14047611059,-4.71769982953)
camera.keyframe_insert(data_path="rotation_euler",frame=801.0)
camera.keyframe_insert(data_path="location", frame=801.0)
camera.location.x = 390.3059
camera.location.y = 0.3206582
camera.location.z = -7.664429
camera.rotation_euler = (4.71384137538,3.13935141559,-4.71770222953)
camera.keyframe_insert(data_path="rotation_euler",frame=804.0)
camera.keyframe_insert(data_path="location", frame=804.0)
camera.location.x = 391.9359
camera.location.y = 0.3238003
camera.location.z = -7.696195
camera.rotation_euler = (4.71422853838,3.13868928659,-4.71770452953)
camera.keyframe_insert(data_path="rotation_euler",frame=807.0)
camera.keyframe_insert(data_path="location", frame=807.0)
camera.location.x = 393.5579
camera.location.y = 0.3237896
camera.location.z = -7.731691
camera.rotation_euler = (4.71448072238,3.13866720159,-4.71770512953)
camera.keyframe_insert(data_path="rotation_euler",frame=810.0)
camera.keyframe_insert(data_path="location", frame=810.0)
