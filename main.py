# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
# import ffmpegcv

'''
apiPreference    preferred Capture API backends to use. 
Can be used to enforce a specific reader implementation 
if multiple are available: 
e.g. cv2.CAP_MSMF or cv2.CAP_DSHOW.
'''
# from pymf import get_MF_devices
# device_list = get_MF_devices()
# for i, device_name in enumerate(device_list):
#     print(f"opencv_index: {i}, device_name: {device_name}")

def run_camera():
    # open video0
    cap = cv2.VideoCapture(2, 2+cv2.CAP_DSHOW )
    # set width and height
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    # set fps
    cap.set(cv2.CAP_PROP_FPS, 1)
    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        try:
            if ret and type(frame)!=type(None) and frame.sum().sum()>0:
            # Display the resulting frame
                cv2.imshow('frame', frame)
            else:
                print('n',frame)
                # cap.release()
                # #reopen
                # cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)

        except Exception as e:
            print('skipped',e)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def run_camera_ff():
    cap = ffmpegcv.VideoCaptureCAM(0)

    for frame in cap:
        cv2.imshow('image', frame)
# Press the green button in the gutter to run the script.

def find_cameras():
    for i in range(-10,10):
        try:

            cap = cv2.VideoCapture(i)

            cap_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            cap_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            if cap_width==0 or cap_height==0:
                continue
            print(f"Found a camera {i} with resolution {int(cap_width)}x{int(cap_height)}")

        except:
            pass
if __name__ == '__main__':
    # run_camera()
    find_cameras()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
