import os
import yaml
import eyed3
import time

# read mp3 files from the audio folder

def read_mp3_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            try:
                audio_path = os.path.join('audio', file)
                audio_file = eyed3.load(audio_path)
                duration = time.strftime('%H:%M:%S', time.gmtime(audio_file.info.time_secs))
                size = os.path.getsize(audio_path)
                size_str = '{:,}'.format(size)
                comments = ''
                for comment in audio_file.tag.comments:
                    comments += comment.text
                audio_files.append({
                    'title': audio_file.tag.title,
                    'description': comments,
                    'file': '/audio/' + file,
                    'duration': duration,
                    'length': size_str,
                })
            except Exception as e:
                print(f'Error processing {audio_path}: {e}')
    return audio_files

def convert_to_yaml():
    data = read_mp3_files()
    yaml_data = yaml.dump(read_mp3_files(), sort_keys=False)
    with open('episodes.yaml', 'w') as file:
        file.write(yaml_data)

convert_to_yaml()
