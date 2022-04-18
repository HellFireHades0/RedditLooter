# RedditLooter
**API-Less** program to download pictures and videos from Reddit **without limit**.

## Redditlooter.get_images 
   
    Subreddit: Required
        - The name of the subreddit to get data 

    Listing 
        - Sort the posts according to 'hot', 'new', 'rising', 'top'
          Default value: top

    media_count
        - Amount of images to download
          Default value: 10
  
    timeframe
        - Sort the posts according to 'day', 'week', 'month', 'year', 'all'
          Default value: month
    path
        - Folder to download images to
          Default value: current working directory
    
    url_only
        - Prints the direct link to the image
          Default value: False
## Redditlooter.get_videos
    Subreddit: Required
        - The name of the subreddit to get data 

    Listing 
        - Sort the posts according to 'hot', 'new', 'rising', 'top'
          Default value: top

    media_count
        - Amount of videos to download
          Default value: 10
  
    timeframe
        - Sort the posts according to 'day', 'week', 'month', 'year', 'all'
          Default value: month
    path
        - Folder to download images to
          Default value: current working directory
    
    url_only
        - Prints the direct link to the video
          Default value: False
## Redditlooter.get_gifs
    Subreddit: Required
        - The name of the subreddit to get data 

    Listing 
        - Sort the posts according to 'hot', 'new', 'rising', 'top'
          Default value: top

    media_count
        - Amount of gif to download
          Default value: 10
  
    timeframe
        - Sort the posts according to 'day', 'week', 'month', 'year', 'all'
          Default value: month
    path
        - Folder to download images to
          Default value: current working directory
    
    url_only
        - Prints the direct link to the gif
          Default value: False
## Redditlooter.get_user_data

    user_data: Required
        - username to get the data from 
```python
from Redditlooter import get_user_data
  
get_user_data('letthedarknesstake')
```
## Redditlooter.get_posts
Subreddit: Required
        - The name of the subreddit to get data 

    Listing 
        - Sort the posts according to 'hot', 'new', 'rising', 'top'
          Default value: top

    media_count
        - Amount of posts to show
          Default value: 10
  
    timeframe
        - Sort the posts according to 'day', 'week', 'month', 'year', 'all'
          Default value: month
 
