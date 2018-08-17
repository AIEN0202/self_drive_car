# Importing the libraries
import cv2
import socket
import numpy as np
import gpio_mod as mod


# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
video_capture.set(3, 320) #weight
video_capture.set(4, 240) #height

TCP_IP = ""
print(TCP_IP)
TCP_PORT = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(True)

conn, addr = s.accept()

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

while True:
    _, frame = video_capture.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # socket
    result, imgencode = cv2.imencode('.jpg', frame, encode_param)
    data = np.array(imgencode)
    stringData = data.tostring()

    #print(str(len(stringData)).ljust(16))
    conn.send(str(len(stringData)).ljust(16).encode(encoding='utf_8', errors='strict'))
    conn.send(stringData)

    ret, frame = video_capture.read()
    decimg=cv2.imdecode(data,1)
    #cv2.imshow('SERVER2',decimg)    
    #
    
   # cv2.imshow('Video', decimg)
    
    # receive socket msg
    res = conn.recv(1024)
    if res is None:
        print('Not get')
    elif res == b'60':
        mod.go_60()
        print(res)
    elif res == b'30':
        mod.go_30()
        print(res)
    elif res == b'stop':
        mod.stop()
        print(res)
    elif res == b'1':
        mod.go_30()
        print(res)
    elif res == b'2':
        mod.right1()
        print(res)
    elif res == b'3':
        mod.left1()
        print(res)
    else:
        print(res)
    # receive socket msg
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
