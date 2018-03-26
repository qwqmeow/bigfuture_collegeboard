#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
from bs4 import BeautifulSoup
import requests
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')


major_url = 'https://bigfuture.collegeboard.org/collegePlan/majors-careers-service-action'
career_data = '7|0|4|https://bigfuture.collegeboard.org/collegePlan/|DDA706080150A342A73213A45F261164|org.collegeboard.pacollegeplan.shared.service.MajorsCareersSelectorUiService|getCareersHierarchy|1|2|3|4|0|='
major_data = """7|0|4|https://bigfuture.collegeboard.org/collegePlan/|DDA706080150A342A73213A45F261164|org.collegeboard.pacollegeplan.shared.service.MajorsCareersSelectorUiService|getMajorsHierarchy|1|2|3|4|0|="""
headers = {
        'User-Agent	' : 'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0', 
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'https://bigfuture.collegeboard.org/majors-careers',
        'X-GWT-Module-Base':'https://bigfuture.collegeboard.org/collegePlan/',
        'X-GWT-Permutation':'681318D4C1A7B123366AB0CE6EB86F48',
        'Accept-Encoding':'gzip, deflate, br'}
def loadCookie():

    cwd = os.getcwd()
    filename='cookie.txt'
    cookiefile = os.path.join(cwd,filename)

    # with open(cookiefile,'r') as f:
    #     cookies={}
    #     for line in f.read().split(';'):
    #         name,value = line.strip().split('=',1)
    #         cookies[name]=value

    cookies = {}
    with open(cookiefile,'r') as f:
        cookie_text = f.read()
    for cookie_unit_text in cookie_text.split('; '):
        cookie_unit = cookie_unit_text.split('=')
        if len(cookie_unit) >= 2:
            cookies[cookie_unit[0]] = cookie_unit[1]
    return cookies

    print "[*] cookie load success!"
    return cookies


def get_majors():
    s = requests.Session()
    
    cookies = loadCookie()
    req = s.post(major_url, headers=headers,data=major_data,cookies=cookies)
    print req.content


def get_careers():  
    s = requests.Session()
  
    cookies = loadCookie()
    req = s.post(major_url, headers=headers,data=career_data,cookies=cookies)

    print req.content


def get_major_categories(html):
    
    major_url_list = []
    main_url = 'https://bigfuture.collegeboard.org'
    soup = BeautifulSoup(html, "html.parser")
    major_categories = soup.select('ul[class="treeview major-categories-treeview tree-root"]')
    majors = major_categories[0].select('a[class="gwt-Anchor"]')

    for x in majors:
        major_url_list.append(main_url+x.get('href'))

    return major_url_list

    
def parse_major(html):
    helpful_courses_list=[]
    related_majors_list=[]
    soup = BeautifulSoup(html, "html.parser")
    title = soup.select('h1[id="majorCareerProfile_titleHeading"]')[0].text
    intro = soup.select('div[class="grid_9 alpha margin60 marginBottomOnly"]')[0].text
    helpful_courses_li = soup.select('div[id="majorCareerProfile_highSchoolCourseList"]')[0].select('li')

    for x in helpful_courses_li:
        helpful_courses_list.append(x.text)

    helpful_courses = ','.join([x for x in helpful_courses_list])

    related_majors_li = soup.select('div[id="majorCareerProfile_relatedMajors"]')[0].select('li')

    for x in related_majors_li:
        related_majors_list.append(x.text)

    related_majors =','.join([x for x in related_majors_list])


    return title,intro,helpful_courses,related_majors