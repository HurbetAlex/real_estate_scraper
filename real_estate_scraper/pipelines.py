# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RealEstateScraperPipeline:
    def process_item(self, item, spider):
        country = 'Germany' if 'de' in item['url'] else 'Sweden'
        domain = item['url'].split('/')[2]
        rental_object = item

        directory = f'data/{country}/{domain}'
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, f'{item["title"].replace(" ", "_")}.json')
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(dict(item), f, ensure_ascii=False, indent=4)
        return item
