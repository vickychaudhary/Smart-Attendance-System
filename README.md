# Smart-Attendance-System
A face recognition software to identify and recognize faces captured in image.

This is a Face Recognition based attendance system which uses face_recognition module to detect and recognize faces.

Steps to follow:
1) Run final.py for a gui based operation.
2) For the first time click on create_encodings and pass the image(of individual user) which you want the model to recognise and store the encodings in database.
3) Then after the first user's entry add another users with append_encodings.
4) For generating the list click on recognise faces and it will create a list of recognised students and you have to pass image of whole class such that all faces 
  are distinctively recognisable and donot overlaps.
5) Also the faces found in group class should already be feeded to model otherwise it will create a blank entry.
6) Explore the codes individual for each buttons !!!!
