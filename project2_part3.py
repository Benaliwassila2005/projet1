#import cv2 the OpenCV library (open computer vision)
#step1: load libraries
import cv2
import os
#step2: get the video path 
#path is just a variable storing the name of the video file,you can give the full path of video here

path = "video.mp4"
#---------------------------------------------------------------
#---------------------------------------------------------------
#step3:load The Video
# cv2.VideoCapture : creates A video Obejct from the file 
p  = cv2.VideoCapture(path)
#the p is now your video Object

#------------------------------------------------------------
#------------------------------------------------------------
#step4:Extract The MetaData
# Converts the value to an integer (because width and height are whole numbers
width = int(p.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(p.get(cv2.CAP_PROP_FRAME_HEIGHT))
#Frames Per Second(FPS)
fps = p.get(cv2.CAP_PROP_FPS)
#This tells how many images (frames) are shown per second in the video.

#Total Frames:
total_Frame = int(p.get(cv2.CAP_PROP_FRAME_COUNT))
#extract The Duration of the video
# Formula: total frames ÷ frames per second

duration = total_Frame /fps
#extract the File Format
file_extension = os.path.splitext(path)[1] 
#---------------------------------------------------------------
#--------------------------------------------------------------
#Step 5: Print The extracted Data
print(f"Video Metadata for: {path}")
print(f"Resolution: {width}x{height}")
print(f"FPS: {fps}")
print(f"Total Frames: {total_Frame}")
print(f"Duration (seconds): {duration:.2f}")
print(f"File format: {file_extension}")


