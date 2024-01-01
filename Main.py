from math import hypot

import cv2
import mediapipe as mp
import numpy as np
from discord_webhook import DiscordWebhook
# Used to convert protobuf message to a dictionary.
from google.protobuf.json_format import MessageToDict


def Logo():
    print(" _______         _   _             _____           _       _ ")  
    print("|__   __|       | | | |           / ____|         (_)     | |")
    print("   | |_   _ _ __| |_| | ___ _____| (___   ___ _ __ _ _ __ | |_ ")
    print("   | | | | | '__| __| |/ _ \______\___ \ / __| '__| | '_ \| __|")
    print("   | | |_| | |  | |_| |  __/      ____) | (__| |  | | |_) | |_ ")
    print("   |_|\__,_|_|   \__|_|\___|     |_____/ \___|_|  |_| .__/ \__|")
    print("")
    print("Made by turtle-zhu for non nefarious reasons")
    print("Use the command [help] for useful commands!!!")
    print("--------------------------------------------------------------------")

#print("Use the help command to find usefull commands to ue the system!")
    
commands = [
             "discord(embeded optional)",
             "end"
             
             ]


def main():
    Logo()  
    while True:
        userInput = str(input(""))
        if userInput.isdigit():
            print("you entered in a digit. Thats no bueno fr")
            break
        match userInput: #list of commands
            case "help":
                print("")
                print("")
                for i in range(len(commands)):
                    print(commands[i])
            case "end":
                print("Ending terminal")
                break
            case "discord":
                discordparams = str(input("enter in params:")) #message
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1191069822658818141/n0wWuyRcUfFvNmUijktEJ_z6N6W6bJKkk4iIoNcVChN7-E-cQfmtNLM3xYbUveC987iD", content=discordparams)
                #embed = DiscordEmbed(title="Your Title", description="Lorem ipsum dolor sit", color="03b2f8")
                # add embed object to webhook
                #webhook.add_embed(embed)
                response = webhook.execute()
            case "hands":
                # Initializing the Model 
                mpHands = mp.solutions.hands 
                hands = mpHands.Hands(
                static_image_mode=False,
                 model_complexity=1, 
                min_detection_confidence=0.75, 
                min_tracking_confidence=0.75, 
                max_num_hands=2) 
        
                 # Start capturing video from webcam 
                cap = cv2.VideoCapture(0) 
        
                while True: 
                    # Read video frame by frame 
                    success, img = cap.read() 
                
                    # Flip the image(frame) 
                    img = cv2.flip(img, 1) 
                
                    # Convert BGR image to RGB image 
                    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
                
                    # Process the RGB image 
                    results = hands.process(imgRGB) 
                
                    # If hands are present in image(frame) 
                    if results.multi_hand_landmarks: 
                
                        # Both Hands are present in image(frame) 
                        if len(results.multi_handedness) == 2: 
                                # Display 'Both Hands' on the image 
                            cv2.putText(img, 'Both Hands', (250, 50), 
                                        cv2.FONT_HERSHEY_COMPLEX, 
                                        0.9, (0, 255, 0), 2) 
                
                        # If any hand present 
                        else: 
                            for i in results.multi_handedness: 
                                
                                # Return whether it is Right or Left Hand 
                                label = MessageToDict(i) 
                               # ['classification'][0]['label']
                
                                if label == 'Left': 
                                    
                                    # Display 'Left Hand' on 
                                    # left side of window 
                                    cv2.putText(img, label+' Hand', 
                                                (20, 50), 
                                                cv2.FONT_HERSHEY_COMPLEX,  
                                                0.9, (0, 255, 0), 2) 
                
                                if label == 'Right': 
                                    
                                    # Display 'Left Hand' 
                                    # on left side of window 
                                    cv2.putText(img, label+' Hand', (460, 50), 
                                                cv2.FONT_HERSHEY_COMPLEX, 
                                                0.9, (0, 255, 0), 2) 
                
                    # Display Video and when 'q' 
                    # is entered, destroy the window 
                    cv2.imshow('Image', img) 
                    if cv2.waitKey(1) & 0xff == ord('q'): 
                        break
            #new command here
            case "light":
                #Initializing the Model
                mpHands = mp.solutions.hands
                hands = mpHands.Hands(
                static_image_mode=False,
                model_complexity=1,
                min_detection_confidence=0.75,
                min_tracking_confidence=0.75,
                max_num_hands=2)

                Draw = mp.solutions.drawing_utils

                # Start capturing video from webcam
                cap = cv2.VideoCapture(0)

                while True:
                    # Read video frame by frame
                    _, frame = cap.read()

                    # Flip image
                    frame = cv2.flip(frame, 1)

                    # Convert BGR image to RGB image
                    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # Process the RGB image
                    Process = hands.process(frameRGB)

                    landmarkList = []
                    # if hands are present in image(frame)
                    if Process.multi_hand_landmarks:
                        # detect handmarks
                        for handlm in Process.multi_hand_landmarks:
                            for _id, landmarks in enumerate(handlm.landmark):
                                # store height and width of image
                                height, width, color_channels = frame.shape

                                # calculate and append x, y coordinates
                                # of handmarks from image(frame) to lmList
                                x, y = int(landmarks.x * width), int(landmarks.y * height)
                                landmarkList.append([_id, x, y])

                                # draw Landmarks
                            Draw.draw_landmarks(frame, handlm,
                                                mpHands.HAND_CONNECTIONS)

                            # If landmarks list is not empty
                    if landmarkList != []:
                        # store x,y coordinates of (tip of) thumb
                        x_1, y_1 = landmarkList[4][1], landmarkList[4][2]

                        # store x,y coordinates of (tip of) index finger
                        x_2, y_2 = landmarkList[8][1], landmarkList[8][2]

                        #store x,y coordinates of (tip of) middle finger
                        x_3, y_3 = landmarkList[12][1], landmarkList[12][2]

                        # store x,y coordinates of (tip of) ring finger
                        x_4, y_4 = landmarkList[16][1], landmarkList[16][2]

                        # store x,y coordinates of (tip of) pinkie finger
                        x_5, y_5 = landmarkList[20][1], landmarkList[20][2]


                        # draw circle on thumb and index finger tip
                        cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED)
                        cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)

                        # draw line from tip of thumb to tip of index finger
                        cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 3)

                        cv2.line(frame, (x_2, y_2), (x_3, y_3), (255, 255, 0), 3)

                        cv2.line(frame, (x_2, y_2), (x_4, y_4), (0, 255, 255), 3)

                        cv2.line(frame, (x_2, y_2), (x_5, y_5), (255, 0, 0), 3)


                        # calculate square root of the sum of
                        # squares of the specified arguments.
                        L = hypot(x_2 - x_1, y_2 - y_1)

                        # 1-D linear interpolant to a function
                        # with given discrete data points
                        # (Hand range 15 - 220, Brightness
                        # range 0 - 100), evaluated at length.
                        b_level = np.interp(L, [15, 220], [0, 100])

                        # set brightness
                        #sbc.set_brightness(int(b_level))
                        print(str(b_level))
                        # Display Video and when 'q' is entered, destroy
                    # the window
                    cv2.imshow('Image', frame)
                    if cv2.waitKey(1) & 0xff == ord('q'):
                        break

main()



