from djitellopy.tello import Tello
import cv2
import pygame
import numpy as np
import time

pygame.init()
pygame.display.set_caption("Tello camera")
screen = pygame.display.set_mode([960, 720])
tello = Tello()
pygame.time.set_timer(pygame.USEREVENT + 1, 50)
tello.connect()
#tello.takeoff()
tello.streamoff()
tello.streamon()
frame_read = tello.get_frame_read()
should_stop = False
while not should_stop:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1:
            print("event 1")
        elif event.type == pygame.QUIT:
            print("event elif 1")
            should_stop = True    
        
    if frame_read.stopped:
        frame_read.stop()
        break
    screen.fill([0, 0, 0])
    frame = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = np.flipud(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0, 0))
    pygame.display.update()
    time.sleep(1 / 25)
#tello.land()    
tello.end()  