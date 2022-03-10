import bpy
import json

width, height = 80, 60
title = 'He_Man'
rate = 5
totalFrame = 7000

with open(r'C:\\Users\\User\\Programming\\Data-Verse\\Video-to-3dPixels\\Video_to_Array\\Arrays.Json', 'r', encoding='utf-8') as file:
    jsonFile = json.loads(file.read())
    arr = jsonFile[title]


def generateArray():
    for x in range(width):
        for y in range(height):
            bpy.ops.mesh.primitive_cube_add(
                size=1, enter_editmode=False, location=(0, x, y)
            )


def makeMotion(arr):
    fx = 30/rate + 1
#    end = len(arr) * fx
    end = 100
    print(end)
    cubes = bpy.data.collections['Cubes'].objects
    frame = 0
    while(frame < end / fx ):
        for i in range(width*height):
            j = width*height-1-i
            cubes[j].scale = [arr[frame][i]*2, 1, 1]
            cubes[j].keyframe_insert(data_path="scale", frame=frame*fx)
        frame += 1


#generateArray()
makeMotion(arr)
 