import face_recognition
import os
from PIL import Image


def identifyFace(unknown,known):
    # Load the images
    knwn_img = face_recognition.load_image_file(known)
    unknwn_img = face_recognition.load_image_file(unknown)

    # Encode them
    knwn_enc = face_recognition.face_encodings(knwn_img)[0]
    unknwn_enc = face_recognition.face_encodings(unknwn_img)[0]

    # Compare the images
    result = face_recognition.compare_faces([knwn_enc],unknwn_enc)

    if result[0] == True:
        # delete test image
        # Redirect to dashboard
        print("You are who you say you are")
    else:
        # delete test image
        # Redirect to error page
        print("You are not who you said you are")

def checkIdentity(user,image_loc):
    current_dir = os.getcwd() 
    print(current_dir)
    known = os.listdir("./known")

    for id in known:
        if user == id:
            known = os.listdir(f"./known/{id}")
            known = f"./known/{id}/{known[0]}"
            identifyFace(image_loc, known)
    
checkIdentity("londa","./londa/londa1.jpg")
