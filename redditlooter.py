import os
import pprint
import datetime

import requests
import tqdm
import fake_useragent
import youtube_dl


count = 0
track = []


def get_images(subreddit,
               listing='top',
               media_count=10,
               timeframe='',
               path=os.getcwd(),
               url_only=False):
    global count, track
    track.append(media_count)
    listing = listing.lower()
    if path != os.getcwd() and not os.path.isdir(path):
        os.makedirs(path)
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={media_count}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={media_count}'
    r = requests.get(url, headers={'User-Agent': fake_useragent.UserAgent().random}).json()
    for i in r['data']['children']:
        if str(i['data']['url']).startswith('https://i.redd.it') and \
                str(i['data']['url']).endswith('jpg') or \
                str(i['data']['url']).endswith('png'):
            if not os.path.isfile(rf"{path}\{str(i['data']['url']).split('/')[-1]}"):
                if not url_only:
                    download_images(i['data']['url'], rf"{path}\{str(i['data']['url']).split('/')[-1]}")
            if url_only:
                print(f"{i['data']['author']} {i['data']['url']}")
    if count < int(track[0]):
        get_images(subreddit, listing, media_count+1, timeframe, path, url_only)


def get_gifs(subreddit,
             listing='top',
             limit_results=10,
             timeframe='month',
             path=os.getcwd(),
             url_only=False):
    listing = listing.lower()
    if path != os.getcwd() and not os.path.isdir(path):
        os.makedirs(path)
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}'
    r = requests.get(url, headers={'User-Agent': fake_useragent.UserAgent().random}).json()
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
               timeframe='month',
               path=os.getcwd(),
               url_only=False):
    listing = listing.lower()
    if path != os.getcwd() and not os.path.isdir(path):
        os.makedirs(path)
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}'
    r = requests.get(url, headers={'User-Agent': fake_useragent.UserAgent().random}).json()
    for i in r['data']['children']:
        if str(i['data']['url']).startswith('https://v.redd.it'):
            if not os.path.isfile(rf"{path}{str(i['data']['url']).split('/')[-1]}") and not url_only:
                download_videos(i['data']['url'], rf"{path}\{str(i['data']['url']).split('/')[-1]}.mp4")
            if url_only:
                print(i['data']['url'])


def download_images(url, path_to_file=''):
    global count
    r = requests.get(url, stream=True)
    count += 1
    progress = tqdm.tqdm(r.iter_content(1024), f"[{count}] Downloading {path_to_file}",
                         total=int(r.headers.get("Content-Length", 0)), unit="B", unit_scale=True, unit_divisor=1024)
    with open(fr"{path_to_file}", "wb+") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


def download_videos(url, path_to_file=''):
    opts = {'outtmpl': path_to_file}
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])


def get_user_data(user_name):
    user_data = requests.get(f'https://www.reddit.com/user/{user_name}/about.json',
                             headers={'User-Agent': fake_useragent.UserAgent().random}).json()
    user_data['data']['created_date'] = datetime.datetime.fromtimestamp(user_data['data']['created']) \
        .strftime("%A, %B %d, %Y %I:%M:%S")
    pprint.pprint(user_data)


def get_subreddit_data(subreddit):
    sub_data = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers={'User-Agent': fake_useragent.UserAgent().random}).json()
    pprint.pprint(sub_data)


def get_posts(subreddit,
              listing='top',
              limit_results=10,
              timeframe='month'):
    if listing == 'top':
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}&t={timeframe}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit_results}'
    post = requests.get(url, headers={'User-Agent': fake_useragent.UserAgent().random}).json()
    for i in post['data']['children']:
        print(i)




