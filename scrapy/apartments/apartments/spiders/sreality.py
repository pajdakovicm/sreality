import scrapy
import json


class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 ' \
                 'Safari/537.36 '
    # ...
    allowed_domains = ['www.sreality.cz']
    start_urls = [
        'https://www.sreality.cz/api/cs/v2/estates?building_condition=6&category_main_cb=1&category_sub_cb=6'
        '&category_type_cb=1&leftBottomBounding=8.261292749999996%7C48.89262937047895&locality_country_id=10001'
        '&per_page=20&rightTopBounding=22.851136499999996%7C50.5962342686479&tms=1659985323566&zoom=6']

    def parse(self, response):

        data = json.loads(response.body)
        next_page_number = data['page']
        # loop through all 20 items on one page
        for i in range(20):
            yield {
                'name:': data['_embedded']['estates'][i]['name'],
                'image:': data['_embedded']['estates'][i]['_links']['images'][0]

            }
        # check first 25 pages to get the first 500 items
        if next_page_number < 25:
            next_page_number = data['page'] + 1
            yield scrapy.Request(
                url=f'https://www.sreality.cz/api/cs/v2/estates?building_condition=6&category_main_cb=1'
                    f'&category_sub_cb=6&category_type_cb=1&leftBottomBounding=8.261292749999996%7C48'
                    f'.89262937047895&locality_country_id=10001&page={next_page_number}&per_page=20&rightTopBounding=22'
                    f'.851136499999996%7C50.5962342686479&tms=1659982357826&zoom=6 ',
                callback=self.parse

            )
        print(next_page_number)
