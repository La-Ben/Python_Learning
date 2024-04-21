# 4.2.1scrapy项目创建
# 创建一个名为"myproject"的scrapy项目
# scrapy startproject scrapy_magic_spider(项目名)

# 4.2.2定义item（数据）-----------------------------------------------
# items.py文件中定义爬虫的数据结构类型

# 4.2.3创建和编写spider文件-------------------------------------------

# 4.2.3.1创建spider
# 在scrapy_magic_spider/spiders目录下创建一个名为"magic_spider.py"的文件


# 4.2.3.2编写spider
# 编写爬虫的逻辑代码，参照/spiders/magic_spider.py文件

# 4.2.4修改settings.py文件-------------------------------------------
# 4.2.4.1 关闭 robots爬虫规则
# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

# 4.2.4.2 设置 HEADERS
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en",
#
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/58.0.3029.110 Safari/537.3'
#
# }

# 4.2.4.3 启用 pipelines设置
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "scrapy_magic_spider.pipelines.ScrapyMagicSpiderPipeline": 300,
# }


# 4.2.6编写pipelines------------------------------------------------------
# pipelines.py文件中编写数据处理逻辑 参照pipelines.py文件

# 4.2.5运行爬虫-------------------------------------------------------------
# 在scrapy_magic_spider目录下创建start.py文件
# 文件内容为：
# from scrapy import cmdline
# cmdline.execute('scrapy crawl magic_spider'.split(" "))

