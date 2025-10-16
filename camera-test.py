
import os
import sys
import cv2
import climage

#for qt enviroment
os.environ["QT_QPA_PLATFORM"] = "xcb"

def capture_and_display():
    cam = cv2.VideoCapture(0, cv2.CAP_V4L2)
    filename = 'captured_image.png'
    print("Streaming camera in terminal. Press ENTER to stop and save the current image.")
    
    while True:
        
        ret, frame = cam.read()
        cv2.imwrite(filename, frame)
        
        output = climage.convert(filename, is_unicode=True, width=50)
        
        os.system('clear')
        print(output)
        
        sleep_time = 0.001
        
        import select
        if select.select([sys.stdin], [], [], sleep_time)[0]: #reads the terminal for input (sys.stdin) and waits 0.001 seconds to check if there was input
            _ = sys.stdin.readline()
            break
        
    cam.release()
    print(f"\nStreaming stopped, saved as {filename}")

if __name__ == "__main__":
    capture_and_display()
