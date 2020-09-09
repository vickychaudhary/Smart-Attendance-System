import face_recognition
import pickle
import numpy as np 
from PIL import Image, ImageDraw
import xlsxwriter
import datetime

def fun2(file_name):
    with open('dataset_faces.dat','rb') as f:
        all_face_encodings = pickle.load(f)

    read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()


    known_face_roll = list(all_face_encodings.keys())
    known_face_encodings = np.array(list(all_face_encodings.values()))

    detected = []
    # print(all_face_encodings.keys())

    unknown_image = face_recognition.load_image_file(file_name)

    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image,face_locations)

    pil_image = Image.fromarray(unknown_image)
    # draw = ImageDraw.Draw(pil_image)

    for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        roll = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            roll = known_face_roll[best_match_index]
            detected.append(roll)
        
    #     draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        
    #     text_width, text_height = draw.textsize()
    #     draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    #     draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


    # del draw
    # pil_image.show()  
    



    detected.sort()
    # excel sheet generator
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('class_db.xlsx')
    
    # The workbook object is then used to add new worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet('')

    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 30)


    # Use the worksheet object to write data via the write() method.
    worksheet.write('A1', 'Names')
    worksheet.write('B1', 'Roll Number')
    worksheet.write('C1', 'Enrollment Number')


    # Start from the first cell.
    # Rows and columns are one indexed.
    row = 1
    column = 0





    for i in detected:
        if i == "Unknown":
            worksheet.write(row, column, "Unknown")
            worksheet.write(row, column + 1,"Unknown")
            worksheet.write(row,column+2,"Unknown")

        if i in read_dictionary.keys():
            worksheet.write(row, column, read_dictionary[i][0])
            worksheet.write(row, column + 1,read_dictionary[i][1])
            worksheet.write(row,column+2,read_dictionary[i][2])
        row+=1

    workbook.close()
    print("Your Excel Sheet is Generated!")