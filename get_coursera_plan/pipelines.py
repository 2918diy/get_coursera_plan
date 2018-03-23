# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class GetCourseraPlanPipeline(object):
    file = open('item.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item
    def close_spider(self, spider):
        file_data = self.file.readlines()
        for data in file_data:
            j_d = json.loads(data)
            j_v = list(j_d.values())
            with open('data.csv', 'ab+') as f2:
                line = ','.join(j_v) + '\n'
                f2.write(line.encode('utf-8'))
