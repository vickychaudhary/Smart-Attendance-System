import face_recognition
import pickle
import numpy as np

def fun1(file_name):
    all_face_encodings = {}  # this is going to store all face encodings as key,value pairs with key as roll_no and value as face encoding

    full_name = input("Enter the Fullname of Student: ")
    roll = input("Enter the Roll no of Student: ")
    prn = input("Enter Enrollment no of the Student: ")

    with open('dataset_faces.dat','rb') as f:
        all_face_encodings = pickle.load(f)



    img = face_recognition.load_image_file(file_name)
    all_face_encodings[roll] = face_recognition.face_encodings(img)[0]

    with open('dataset_faces.dat','wb') as f:
        pickle.dump(all_face_encodings,f)


    read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item() #this my_file.npy will hold the all preloaded data
                                                                        # for further data fetching

    read_dictionary[roll] =[full_name,roll,prn]
    np.save('my_file.npy', read_dictionary)
    print("Done")
