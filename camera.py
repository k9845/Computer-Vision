#!/usr/lib/python2.7
import numpy
from pygame import mixer
import time
import cv2
from Tkinter import *
import tkMessageBox
root=Tk()
root.geometry('600x670')
frame = Frame(root, relief=RIDGE, borderwidth=4)
frame.pack(fill=BOTH,expand=1)
root.title('User Cam')
frame.config(background='light blue')
label = Label(frame, text="User Cam",font=('Times 35 bold'),padx=10,pady=10)
label.pack(side=TOP)


def hel():
   help(cv2)

def Contri():
   tkMessageBox.showinfo("Contributors","\nRishi Khatri \n")


def anotherWin():
   tkMessageBox.showinfo("About",'User Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="User Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample3.avi',fourcc,9.0,(640,480))
   
   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.putText(frame,'Eye',(ex+ew,ey+eh),font,1,(250,250,250),2,cv2.LINE_AA)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
   op.release()
   capture.release()
   cv2.destroyAllWindows()

def movement():
  cap = cv2.VideoCapture(0)
  frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

  frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

  fourcc=cv2.VideoWriter_fourcc(*'XVID') 
  out=cv2.VideoWriter('Sample3.avi',fourcc,9.0,(640,480))
   
  ret, frame1 = cap.read()
  ret, frame2 = cap.read()
  while cap.isOpened():
      diff = cv2.absdiff(frame1, frame2)
      gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
      blur = cv2.GaussianBlur(gray, (5,5), 0)
      _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
      dilated = cv2.dilate(thresh, None, iterations=3)
      contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

      for contour in contours:
          (x, y, w, h) = cv2.boundingRect(contour)

          if cv2.contourArea(contour) < 900:
              continue
          cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
          cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                      1, (0, 0, 255), 3)
      #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

      image = cv2.resize(frame1, (1280,720))
      out.write(image)
      cv2.imshow("feed", frame1)
      frame1 = frame2
      ret, frame2 = cap.read()

      if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
  

   
but1=Button(frame,padx=10,pady=10,width=39,bg='#03A9F4',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=100,y=119)

but2=Button(frame,padx=5,pady=5,width=39,bg='#03A9F4',fg='black',relief=GROOVE,command=webrec,text='Open Cam & Record',font=('helvetica 15 bold'))
but2.place(x=100,y=191)

but3=Button(frame,padx=5,pady=5,width=39,bg='#03A9F4',fg='black',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but3.place(x=100,y=265)

but4=Button(frame,padx=5,pady=5,width=39,bg='#03A9F4',fg='black',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
but4.place(x=100,y=337)

but5=Button(frame,padx=5,pady=5,width=39,bg='#03A9F4',fg='black',relief=GROOVE,command=blink,text='Detect Eye Blink & Record With Sound',font=('helvetica 15 bold'))
but5.place(x=100,y=415)

but5=Button(frame,padx=5,pady=5,width=39,bg='#03A9F4',fg='black',relief=GROOVE,command=movement,text='Movement Track',font=('helvetica 15 bold'))
but5.place(x=100,y=485)

but6=Button(frame,padx=5,pady=5,width=5,bg='#03A9F4',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but6.place(x=275,y=550)


root.mainloop()
