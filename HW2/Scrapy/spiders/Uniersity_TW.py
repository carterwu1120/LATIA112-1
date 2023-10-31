# type to terminal:scrapy crawl Uniersity_TW
import scrapy
import bs4
import pandas as pd
class UniersityTwSpider(scrapy.Spider):
    name = "Uniersity_TW"
    allowed_domains = ["university-tw.ldkrsi.men"]
    start_urls = ["https://university-tw.ldkrsi.men/register/"]
    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        data = soup.select('table')[0]  # 抓到第一個表格
        df = pd.read_html(data.prettify())  #read html and transfer it to pandas frame
        df[0].to_csv("2022學年公立一般大學新生註冊率.csv")
        print(df[0])
        pass
