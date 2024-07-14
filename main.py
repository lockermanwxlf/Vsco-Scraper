from vsco_api import ProfileIterator
from modules.profiles import Profiles
import time
from filesystems.local import LocalFilesystem

def main():
    profiles = Profiles()
    local = LocalFilesystem()
    while True:
        for directory_name, site_id in profiles:
            print(directory_name)
            for i, page in enumerate(ProfileIterator(site_id)):
                print('Page', i)
                for post in page:
                    downloaded = local.process_post(directory_name, post)
                    if downloaded:
                        time.sleep(6)
                time.sleep(10)
            time.sleep(10)

if __name__ == '__main__':
    main()