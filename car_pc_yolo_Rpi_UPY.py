import socket
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np
import os
import sys
import time
import cv2
from darkflow.net.build import TFNet
# Importing the libraries
import tensorflow as tf

options = {
    'model': 'cfg/yolov2-voc.cfg',
    'load': 14000,
    'threshold': 0.5,
    'gpu':0.7
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

def yukigo(decimg):
#go FRL                      
    origin_h, origin_w, _ = decimg.shape
    cut_img = decimg[int(origin_h/2)-50::,:origin_w]
    #cut_img = cv2.cvtColor(cut_img, cv2.COLOR_BGR2GRAY)
    imageu = cut_img
    # get shape preprocessing
    np_img_list = np.array([imageu])
    np_img_list = np.reshape(np_img_list, (1, 170, 320, 3))
    print(origin_h, origin_w)
    print(np_img_list.shape)
    np_img_list = np_img_list.astype('float32')
    np_img_list = np_img_list/255
    test_pred = model.predict(np_img_list)
    actu = np.argmax(test_pred[0])
    return actu

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf
actu = 0
#load yuki model
model = load_model('my_model.h5')
model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='categorical_crossentropy', #compare with categorical_crossentropy
              metrics=['accuracy'])
#load yuki model
# def yolo_pd()
    
TCP_IP = "172.20.10.8"
TCP_PORT = 3333

sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))
############################load model yolo ################

act = 0
while True:
    length = recvall(sock,16)
    stringData = recvall(sock, int(length))
    data = np.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    origin_h, origin_w, _ = decimg.shape
    image = decimg
    # get shape preprocessing
    np_img_list = np.array([image])
    np_img_list = np.reshape(np_img_list, (1, 240, 320, 3))

    # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    frame = image
    #
    stime = time.time()
    results = tfnet.return_predict(frame)
    #print(len(results))
    if len(results) > 0 :
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            print(text)
        #cv2.imshow('frame', frame)
        # All the results have been drawn on the frame, so it's time to display it.
            if label == 'Speed 60':
                print('speed 60 {}'.format(confidence))
                act=60
            elif label == 'Speed 30':
                print('speed 30 {}'.format(confidence))
                act=30
            elif label == 'Stop':
                print('stop  {}'.format(confidence))
                act='stop'
    else:
        act = yukigo(decimg)

    #print('FPS {:.1f}'.format(1 / (time.time() - stime)))

    # send back to server
    #################
    if decimg is None:
        start_str = 'start'
        sock.send('{}'.format(start_str).encode(encoding='utf_8', errors='strict'))
    else:
        sock.send('{}'.format(act).encode(encoding='utf_8', errors='strict'))
    ###############
    

    cv2.imshow('server_model_car',decimg)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
cv2.destroyAllWindows()