from time import sleep
from exit import ExitType, ExitUnit
import pygame
import random
import pyttsx3
import cv2
from ffpyplayer.player import MediaPlayer
from menu import main_menu
from constants import MenuButton
from level import select_level

VERSION = "0.0.5"

# Initialize pygame
pygame.init()

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

# Set up display
width, height = 1600, 1200
win = pygame.display.set_mode((width, height))
pygame.display.set_caption(f"Alphabet and Number Game v{VERSION}")

# Set up font
font = pygame.font.SysFont(None, 1000)

# Function to display a character
def display_char(char):
    win.fill((255, 255, 255))
    text = font.render(char, True, (0, 0, 0))
    win.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
    pygame.display.update()

# Function to read out a character using TTS
def read_char(char):
    tts_engine.say(char)
    tts_engine.runAndWait()

# Function to play a video
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        audio_frame, val = player.get_frame()
        if not ret:
            break

        # Convert the frame from BGR to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert the frame to a Pygame surface
        frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        
        # Display the frame on the Pygame window
        win.blit(frame, (-150, 0))
        pygame.display.update()

        # if val != 'eof' and audio_frame is not None:
        #     # Get the audio frame as a NumPy array
        #     img, t = audio_frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                cap.release()
                return


while True:
    rtn_item = main_menu(win, width, height)

    if rtn_item.exit_type == ExitType.QUIT or rtn_item.rtn_msg.type == MenuButton.QUIT:
        break
    elif rtn_item.rtn_msg.type == MenuButton.START:
        select_rtn = select_level(win, width, height)
        if select_rtn.exit_type == ExitType.QUIT:
            continue
        else:
            level_setting = select_rtn.rtn_msg

        running = True
        REWARD_THRESHOLD = 10
        reward_counter = 0

        # Create a list of characters A-Z and 0-9
        characters = level_setting.dictionary
        char = random.choice(characters)  # Get the first random character
        display_char(char)  # Display the first character
        read_char(char)  # Read out the first character

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.upper() == char:
                        reward_counter+=1
                        if reward_counter == REWARD_THRESHOLD:
                            play_video('wheels_on_the_bus_0.mp4')
                            reward_counter = 0
                        char = random.choice(characters)  # Get a new random character
                        display_char(char)  # Display the new character
                        read_char(char)  # Read out the first character
                    else:
                        read_char(char)  # Read out the first character
pygame.quit()
