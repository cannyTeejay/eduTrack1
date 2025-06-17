import face_recognition
import os
from PIL import Image


def newIdentity(identities,image):
    for iden in identities:
        create_identities(iden,image)

def create_identities(identity,image):
    img_list = [image]
    count = len(img_list)
    for i in range(count):
        # Make dir for identity
        if i == 0:
            os.mkdir(f"./main/known/{identity['dir']}")

        # Find faces in image
        image = face_recognition.load_image_file(img_list[0])

        # Crop out faces 
        face_locations = face_recognition.face_locations(image)
        for face in face_locations:
            top, right, bottom, left = face
        face_image = image[top:bottom, left:right]

        # Create identity
        pil_image = Image.fromarray(face_image)
        pil_image.save(f"./main/known/{identity['dir']}/{img_list[i]}")

