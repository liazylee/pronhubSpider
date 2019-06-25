# -*- coding: utf-8 -*-

# Scrapy settings for pronhubSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pronhubSpider'

SPIDER_MODULES = ['pronhubSpider.spiders']
NEWSPIDER_MODULE = 'pronhubSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'pronhubSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
REDIRECT_ENABLED = False
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'pronhubSpider.middlewares.PronhubspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'pronhubSpider.middlewares.PronhubspiderDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    # 'pronhubSpider.middlewares.ProxyMiddlewares': 400, #国内服务器请打开这个配置
    'pronhubSpider.middlewares.UserAgentMiddlewares': 401,
    'pronhubSpider.middlewares.CookiesMiddlewares': 402
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'pronhubSpider.pipelines.PronhubspiderPipeline': 300,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
    'scrapy.pipelines.files.FilesPipeline': 1,
    'pronhubSpider.pipelines.OwnFilePipeline': 2

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PHTYPE = ['video?c=1',
          # 'recommended',
          # 'video?o=ht',  # hot
          # 'video?o=mv',  # Most Viewed
          # 'video?o=tr',  # Top Rate

          # Examples of certain categories
          # 'video?c=1',  # Category = Asian
          # 'video?c=111',  # Category = Japanese
          ]
SPLASH_URL = 'http://127.0.0.1:8050/'  # 境外服务器
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

PROXY = 'http://127.0.0.1:8118' #此配置需tor, privoxy,ssr,详情  https://blog.csdn.net/liazylee/article/details/93078175
FILES_STORE = './video'
FILES_URLS_FIELD = 'field_name_for_your_files_urls'
FILES_EXPIRES = 90
DOWNLOAD_MAXSIZE = 1073741824
DOWNLOAD_WARNSIZE = 1073741824
DOWNLOAD_FAIL_ON_DATALOSS = False
DOWNLOAD_TIMEOUT = 1800
