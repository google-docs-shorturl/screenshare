# file for person sharing their screen

import socket
from threading import Thread
from zlib import compress
from mss import mss

import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)

import pygame

ip = 'PUT IP DISPLAYED WHEN RUNNING client.py HERE'

WIDTH = screensize[0]
HEIGHT = screensize[1]

def retreive_screenshot(conn):
    with mss() as sct:
        # The region to capture
        rect = {'top': 0, 'left': 0, 'width': WIDTH, 'height': HEIGHT}

        while True:
            # Capture the screen
            img = sct.grab(rect)
            # Tweak the compression level here (0-9)
            pixels = compress(img.rgb, 6)

            # Send the size of the pixels length
            size = len(pixels)
            size_len = (size.bit_length() + 7) // 8
            conn.send(bytes([size_len]))

            # Send the actual pixels length
            size_bytes = size.to_bytes(size_len, 'big')
            conn.send(size_bytes)

            # Send pixels
            conn.sendall(pixels)
x = socket.socket()
def main(host=ip, port=6969):
    sock = socket.socket()
    sock.connect((host, port))
    screen_data = '{0}x{1}'.format(screensize[0], screensize[1])
    sock.send(screen_data.encode('utf-8'))
    try:
        while True:
            thread = Thread(target=retreive_screenshot, args=(sock,))
            thread.start()
            thread.join()
    except Exception as e:
        print("ERR: ", e)
        sock.close()
x.close()
if __name__ == '__main__':
    main()
