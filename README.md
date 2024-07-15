# Vsco Scraper
A python program that continuously downloads new posts from a list of VSCO profiles.

# Installation
```bash
git clone https://github.com/lockermanwxlf/Vsco-Scraper.git
cd Vsco-Scraper
pip install -r requirements.txt
```

# Usage
VSCO endpoints use siteids rather than usernames. You can get a user's siteid from their username as such:
```python
from vsco_api import get_site_id

site_id = get_site_id(username)
print(site_id)
```

After getting their siteid, place it into [profiles.csv](profiles.csv). Each row has a directory name and a site id. Posts for a site id will be saved to [output folder]/[directory name].

By default, [output folder] is ./output, which will be created on first run, but it can be changed in [filesystems/local.py](filesystems/local.py).

Finally, run the program with `python main.py`.

## FFmpeg (windows only)
VSCO stores higher quality videos as .m3u8 playlists. if you wish to download these as mp4s, download FFmpeg and place ffmpeg.exe in the same folder as main.py.
There's no point to downloading the .m3u8s themselves because they expire.

# Issues
If you are reporting any issues and it has to do with the api wrapper (vsco_api), please report it at https://github.com/lockermanwxlf/Vsco-Api instead.
