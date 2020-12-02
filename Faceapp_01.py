import streamlit as st
import cv2 as cv
from PIL import Image
import numpy as np
import os

# Loading pre-trained parameters for the cascade classifier
try:
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    #smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')
except Exception:
    st.write('Error Loading cascade classifiers')


def detect(image):
    ''''
    Fuction
    to
    detect
    the
    faces, eye and smiling
    mouth
    part
    '''

    image = np.array(image.convert('RGB'))

    faces = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=5)



    for (x, y, w, h) in faces:
        cv.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
        roi = image[y:y + h, x:x + w]

        #eye = eye_cascade.detectMultiScale(roi)

        #smile = smile_cascade.detectMultiScale(roi)


        #for (ex, ey, ew, eh) in eye:
            #cv.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

        #for (sx, sy, sw, sh) in smile:
            #cv.rectangle(roi, (sx, sy), (sx + sw, sy + sh), (255, 0, 255), 2)

    return image, faces


def about():
    st.write(
        '''
        This is awesome movement in my course seeking the efffiecient, right and sound knowledge,
        about Artificial Intelligence. This is just a show as sustainble project have queued for execution.
        ALHAMDULILAH. 

        Inbox me on whatsapp = +2349052751059 for any updates on your updates for me.
        '''
    )


def main():
    st.title('Detecting Human for Security Check :sunglasses: ')
    st.write('Using Computer Vision and advanced artificial Intelligence(OPENCV)')

    activities = ['Home', 'Read Me']
    choice = st.sidebar.selectbox('Explore as You want', activities)

    if choice == 'Home':
        st.write('Make Sure you visit the Read Me as well, to do something AMAZE')

        image_file = st.file_uploader('Upload Image', type=['jpeg', 'png', 'jpg', 'webp'])

        if image_file is not None:
            image = Image.open(image_file)
            if st.button('Detect'):
                result_img, result_faces = detect(image=image)
                st.image(result_img, use_column_width=True)
                st.success('Found {} faces\n'.format(len(result_faces)))




    elif choice == 'Read Me':
        about()


if __name__ == '__main__':
    main()




