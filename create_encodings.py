import face_recognition
import pickle
import numpy as np

img = "2173228.jpg"
all_face_encodings = {}

full_name = input("Enter the Fullname of Student: ")
roll = input("Enter the Roll no of Student: ")
prn = input("Enter Enrollment no of the Student: ")

temp_list = img.split(".")
img = face_recognition.load_image_file(img)
all_face_encodings[temp_list[0]] = face_recognition.face_encodings(img)[0]

with open('dataset_faces.dat','wb') as f:
    pickle.dump(all_face_encodings,f)

dictionary = {roll:[full_name,roll,prn]}
np.save('my_file.npy', dictionary)