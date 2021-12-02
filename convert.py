import sys
import os
import time
 
 
def video_to_mp3(file_name):
    """ Transforms video file into a MP3 file """
    try:
        file, extension = os.path.splitext(file_name)
        # Convert video into .wav file
        os.system('ffmpeg -i {file}{ext} {file}.wav'.format(file=file, ext=extension))
        print('"{}" successfully converted into Wav!'.format(file_name))
    except OSError as err:
        print(err.reason)
        exit(1)
 
 
def main():
    # Confirm the script is called with the required params
    if len(sys.argv) != 2:
        print('Usage: python video_to_mp3.py FILE_NAME')
        exit(1)
 
    file_path = sys.argv[1]
    try:
        if not os.path.exists(file_path):
            print('file "{}" not found!'.format(file_path))
            exit(1)
 
    except OSError as err:
        print(err.reason)
        exit(1)
 
    video_to_mp3(file_path)
    time.sleep(1)
 
 
if __name__ == '__main__':
    main()