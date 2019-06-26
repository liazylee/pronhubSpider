# pronhubSpider

pornhubをクロールしているWebHubBotプロジェクトの模倣、効率が遅すぎる、方法を探しています

![][py3x] [![GitHub forks][forks]][network] [![GitHub stars][stars]][stargazers] [![GitHub license][license]][lic_file] ![issues][issues_img]
> Disclaimer: This project is intended to study the Scrapy Spider Framework and the MongoDB database, it cannot be used for commercial or other personal intentions. If used improperly, it will be the individuals bear.

* The project is mainly used for crawling a Website, the largest site for pornhub  in the world. In doing so it retrieves video titles, duration, mp4 file, cover url and direct Website`s url.
* This project crawls PornHub.com slow, but with a simple structure.
* This project can crawl up to 5 millon Website`s videos per day(it is not work), depending on your personal network. Because of my slow bandwith my results are relatively slow.
* The crawler requests 10 threads at a time, and because of this can achieve the speed mentioned above. If your network is more performant you can request more threads and crawl a larger amount of videos per day. For the specific configuration see [pre-boot configuration]


## Environment, Architecture

Language: Python3.6

Environment: ubuntu, 4G RAM

Database: MongoDB

* Mainly uses the scrapy reptile framework.
* Join to the Spider randomly by extracted from the Cookie pool and UA pool and tor ip pool.(if you are not in China,tor is no need)
* Start_requests start five Request based on Website`s classification, and crawl the one categorie.
* Support paging crawl data, and join to the queue.

## Instructions for use

### Pre-boot configuration

* Install MongoDB and start without configuration
* Install Python dependent modules：Scrapy, pymongo, requests ,scrapy-splash,or `pip install -r requirements.txt` 
* Modify the configuration by needed, such as the interval time, the number of threads, etc.
* Install the  [Splash] and use docker to run.

### Start up

* cd WebHub
* python quickstart.py



## Database description

The table in the database that holds the data is PhRes. The following is a field description:

#### PhRes table：
  
    video_title:     The title of the video, and as a unique.
    link_url:        Video jump to Website`s link
    image_url:       Video cover link
    video_duration:  The length of the video, in seconds
    quality_480p:    Video 480p mp4 download path



[py3x]: https://img.shields.io/badge/python-3.x-brightgreen.svg
[issues_img]: https://img.shields.io/github/issues/liazylee/pronhubSpider.svg
[issues]: https://github.com/liazylee/pronhubSpider/issues
[Splash]:https://splash.readthedocs.io/en/stable/install.html
[forks]: https://img.shields.io/github/forks/liazylee/pronhubSpider.svg
[network]: https://github.com/liazylee/pronhubSpider

[stars]: https://img.shields.io/github/stars/liazylee/pronhubSpider.svg
[stargazers]: https://github.com/xiyouMc/liazylee/stargazers

[license]: https://img.shields.io/badge/license-MIT-blue.svg
[lic_file]: https://raw.githubusercontent.com/liazylee/pronhubSpider/master/LICENSE
