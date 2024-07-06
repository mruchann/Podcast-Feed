import os
import eyed3

# read mp3 files from the audio folder

def read_mp3_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            try:
                audio_path = os.path.join('audio', file)
                audio = eyed3.load(audio_path)
                audio_files.append({
                    'title': audio.tag.title,
                    'comments': audio.tag.comments[0].text
                })
            except Exception as e:
                print(f'Error processing {audio_path}: {e}')
    return audio_files

print(read_mp3_files())
