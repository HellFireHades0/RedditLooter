import os
import pprint
from datetime import datetime
from requests import get
from tqdm import tqdm
from fake_useragent import UserAgent
from youtube_dl import YoutubeDL


def get_images(subreddit,
               listing='top',
               limit_results=10,
               timeframe='',
               path=os.getcwd(),
               url_only=False):
    listing = listing.lower()
    if path != os.getcwd() and not os.path.isdir(path):
        os.makedirs(path)
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}'
    r = get(url, headers={'User-Agent': UserAgent().random}).json()
    for i in r['data']['children']:
        if str(i['data']['url']).startswith('https://i.redd.it') and \
                str(i['data']['url']).endswith('jpg') or \
                str(i['data']['url']).endswith('png'):
            if not os.path.isfile(rf"{path}{str(i['data']['url']).split('/')[-1]}") and not url_only:
                download_images(i['data']['url'], rf"{path}\{str(i['data']['url']).split('/')[-1]}")
            if url_only:
                print(i['data']['url'])


def get_gifs(subreddit,
             listing='top',
             limit_results=10,
             timeframe='',
             path=os.getcwd(),
             url_only=False):
    listing = listing.lower()
    if path != os.getcwd() and not os.path.isdir(path):
        os.makedirs(path)
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}'
    r = get(url, headers={'User-Agent': UserAgent().random}).json()
    for i in r['data']['children']:
        if str(i['data']['url']).startswith('https://i.redd.it') and \
                str(i['data']['url']).endswith('gif'):
            if not os.path.isfile(rf"{path}{str(i['data']['url']).split('/')[-1]}") and not url_only:
                download_images(i['data']['url'], rf"{path}\{str(i['data']['url']).split('/')[-1]}")
            if url_only:
                print(i['data']['url'])


def get_videos(subreddit,
               listing='top',
               limit_results=10,
               timeframe='',
               path=os.getcwd(),
               url_only=False):
    listing = listing.lower()
    if path != os.getcwd() and not os.path.isdir(path):
        os.makedirs(path)
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}'
    r = get(url, headers={'User-Agent': UserAgent().random}).json()
    for i in r['data']['children']:
        if str(i['data']['url']).startswith('https://v.redd.it'):
            if not os.path.isfile(rf"{path}{str(i['data']['url']).split('/')[-1]}") and not url_only:
                download_videos(i['data']['url'], rf"{path}\{str(i['data']['url']).split('/')[-1]}.mp4")
            if url_only:
                print(i['data']['url'])


def download_images(url, path_to_file=''):
    r = get(url, stream=True)
    progress = tqdm(r.iter_content(1024), f"Downloading {path_to_file}", total=int(r.headers.get("Content-Length", 0)),
                    unit="B", unit_scale=True, unit_divisor=1024)
    with open(fr"{path_to_file}{str(url).split('/')[-1]}", "wb+") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def download_videos(url, path_to_file=''):
    opts = {'outtmpl': path_to_file}
    with YoutubeDL(opts) as ydl:
        ydl.download([url])


def get_user_data(user_name):
    user_data = get(f'https://www.reddit.com/user/{user_name}/about.json',
                    headers={'User-Agent': UserAgent().random}).json()
    user_data['data']['created_date'] = datetime.fromtimestamp(user_data['data']['created'])\
                                                .strftime("%A, %B %d, %Y %I:%M:%S")
    pprint.pprint(user_data)


