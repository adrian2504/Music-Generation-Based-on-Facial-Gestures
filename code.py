import numpy as np
import cv2
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def Band():
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
    cap=cv2.VideoCapture(0)
    while True:
        _,img=cap.read()
        img=cv2.flip(img,1)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow("image",img)
        faces=face_cascade.detectMultiScale(img,1.1,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            roi_gray=gray[y:y+h,x:x+h]
            roi_color=img[y:y+h,x:x+h]
            eyes=eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)
        
        
        if len(faces)==1:
            x,y,w,h=faces[0]
            width  =cap.get(3) 
            height =cap.get(4)
            
            if len(eyes)==1:
                song = AudioSegment.from_wav("./Cymbal.wav")
                print('playing Cymbal sound')
                play(song)
            if len(eyes)==0:
                song = AudioSegment.from_wav("./Bass Drum.wav")
                print('playing Bass Drum sound')
                play(song)
            if x<width/4:
                song = AudioSegment.from_wav("./DRUM_ROL.wav")
                print('playing DRUM_ROL sound')
                play(song)
            if x>3*width/4:
                song = AudioSegment.from_wav("./Triangle.wav")
                print('playing Triangle sound')
                play(song)
            if y<height/4:
                song = AudioSegment.from_wav("./Cymbal.wav")
                print('playing Cymbal sound')
                play(song)
        
        cv2.imshow("image",img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyWindow("image")
