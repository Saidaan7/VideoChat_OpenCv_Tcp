import cv2
import socket
import base64
import os
import threading
import time


# Function for receiving video
def videoreciver():
    s= socket.socket()
    #Server IP 
    #public ip of server host
    ip="65.0.29.91"
    # Port on which User connect and recv data
    recv_port=4444

    # Connect to server
    s.connect((ip,recv_port))
    
    i=0
    while True:
        time.sleep(0.2)
        try:
            # Receive and decode image data
            data =s.recv(100000000)
            imgdata = base64.b64decode(data)

            # Create a file and write the image data in that(binary format)
            filename="{}.jpg".format(i)
            with open(filename, 'wb') as f:
                f.write(imgdata)

            # Read the image file
            image=cv2.imread(filename)

            # Flip the image
            image = cv2.flip(image, 1)

            print(image)
            cv2.imshow('B is calling...',image)

            # Remove the i.jpg file
            os.remove("{}.jpg".format(i))
            i=i+1
            if cv2.waitKey(10) == 13:
                cap.release()
                break
        except:
            pass
    cv2.destroyAllWindows()


def videosender():
    s = socket.socket()
    #Server IP & Port
    ip="65.0.29.91"

    # Port on whcih user connect and send data 
    send_port =3333

    # Connect to server
    s.connect((ip,send_port))
    
    # Capture video video
    cap=cv2.VideoCapture(0)
    
    while True:
        time.sleep(0.2)
        # Read frames
        ret,frame=cap.read()
        
        # Write the Frames in the .jpg file
        cv2.imwrite("frames.jpg",frame)
        
        #Read and encode the data in the file
        with open("frames.jpg", 'rb') as f:
            image_encoded=base64.b64encode(f.read())
        
        # send the encoded data to the server
        s.send(image_encoded)
    


# Run send and receive funtions in two different threads
t_send=threading.Thread(target=videosender)
t_recv=threading.Thread(target=videoreciver)

t_send.start()
t_recv.start()
