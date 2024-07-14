import os
import requests
from vsco_api import VscoMedia, VscoMediaType
import fake_useragent
import subprocess

OUTPUT_FOLDER = 'output'

fake_ua = fake_useragent.FakeUserAgent()

class LocalFilesystem:
    
    def get_filepath(self, directory_name: str, post: VscoMedia):
        global OUTPUT_FOLDER
        extension = '.png' if post.type == VscoMediaType.IMAGE else '.mp4'
        filename = f'{directory_name} {post.timestamp}{extension}'
        os.makedirs(os.path.join(OUTPUT_FOLDER, directory_name), exist_ok=True)
        return os.path.join(OUTPUT_FOLDER, directory_name, filename)

    def process_post(self, directory_name: str, post: VscoMedia):
        global fake_ua
        filepath = self.get_filepath(directory_name, post)
        if os.path.exists(filepath): 
            return False
        print('Downloading', directory_name, post.timestamp)
        match post.type:
            case VscoMediaType.IMAGE:
                response = requests.get(
                    url=post.download_url,
                    headers={
                        'User-Agent': fake_ua.random
                    })
                response.raise_for_status()
                with open(filepath, 'wb+') as file:
                    file.write(response.content)
            case VscoMediaType.VIDEO_MP4:
                response = requests.get(
                    url=post.download_url,
                    headers={
                        'User-Agent': fake_ua.random
                    })
                response.raise_for_status()
                with open(filepath, 'wb+') as file:
                    file.write(response.content)
            case VscoMediaType.VIDEO_M3U8:
                print("DOWNLOADING PLAYLIST WITH FFMPEG")
                subprocess.run([r'ffmpeg.exe', 
                            '-protocol_whitelist', 'file,http,https,tcp,tls,crypto', 
                            '-i', post.download_url,
                            '-c', 'copy',
                            '-bsf:a', 'aac_adtstoasc',
                            filepath])
        return True
