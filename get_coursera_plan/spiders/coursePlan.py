# -*- coding: utf-8 -*-

#import sys
#sys.path.append('C:\\Users\\Helen YU Yu\\iCloudDrive\\Desktop\\Code\\python_crawl\\getCourseraPlan')

#from selenium import webdriver


import scrapy
from get_coursera_plan.items import GetCourseraPlanItem
from scrapy import Request
from bs4 import BeautifulSoup

class CourseplanSpider(scrapy.Spider):
    name = 'coursePlan'
    #fallowed_domains = ['coursera.org']
    start_urls = ['https://www.coursera.org/?authMode=login']
    #options=webdriver.ChromeOptions()
    #driver=webdriver.Chrome(options=options,executable_path='C:\\Users\\Helen YU Yu\\Downloads\\chromedriver_win32\\chromedriver.exe')
    #driver.get("https://www.coursera.org")
    def parse(self, response):
        soup = BeautifulSoup(response.body)
        deadline = []
        for div in soup.findAll('div',attrs={'class':'transitionContainer_xmmnjl'}):
            deadline_text=div.find('div',attrs={'class':'rc-AssignmentDueDate'}).find('a').get_text()
            deadline.append(deadline_text)
        i = 0
        for a in soup.findAll('a',attrs={'class':'rc-NavigationDrawerLink headline-1-text horizontal-box rc-WeekNavigationItem'}):
            url = "https://www.coursera.org" + a.get('href')
            week_info = a.find('div').find('span').get_text()
            request = Request(url, callback=self.parse_lesson,dont_filter=True)
            request.meta['new_handler'] = True
            request.meta['week_info'] = week_info
            request.meta['deadline'] = deadline[i]
            yield request
            i = i+1
        
        
    def parse_lesson(self, response):
        item = GetCourseraPlanItem()
        week = response.meta['week_info']
        deadline = response.meta['deadline']
        soup = BeautifulSoup(response.body)
        print(response.meta['week_info'])
        for lesson in soup.findAll('div',attrs={'class':'rc-NamedItemList'}):
            lesson_name = lesson.find('h4',attrs={'class':'flex-1 align-self-center headline-2-text'}).get_text()
            for lesson_tip in lesson.findAll('div',attrs={'class':'horizontal-box headline-1-text od-item align-items-vertical-center'}):
                tip_name = lesson_tip.find('div',attrs={'class':'item-text-container'}).find('h5').find('span').get_text()
                try:
                    tip_duration = lesson_tip.find('div',attrs={'class':'item-text-container'}).find('span',attrs={'class':'inline-child rc-EffortText caption-text text-hint'}).get_text()
                except:
                    tip_duration=""
                    
                item['week']=week
                item['deadline'] = deadline
                item['lesson_name'] = lesson_name
                item['tip_name'] = tip_name
                item['tip_duration'] = tip_duration
                yield item