import face_recognition
import os
from PIL import Image


def new_identity(identities):
    for iden in identities:
        create_identities(iden)

def create_identities(identity):
    print()
    img_list = os.listdir(identity["dir"])
    count = len(img_list)
    for i in range(count):
        # Make dir for identity
        if i == 0:
            os.mkdir(f"./known/{identity['dir']}")

        # Find faces in image
        image = face_recognition.load_image_file(f"{identity['dir']}/{img_list[i]}")

        # Crop out faces 
        face_locations = face_recognition.face_locations(image)
        for face in face_locations:
            top, right, bottom, left = face
        face_image = image[top:bottom, left:right]

        # Create identity
        pil_image = Image.fromarray(face_image)
        pil_image.save(f"./known/{identity['dir']}/{img_list[i]}")

identities = [
    {
        "dir":"keanu",
        "name": "keanu"
    },
    {
        "dir":"chadwick",
        "name": "chadwick"
    },
    {
        "dir":"londa",
        "name": "londa"
    }
]

new_identity(identities)
