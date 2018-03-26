#!/usr/bin/env python
#-*-coding:utf-8-*-

import controler
import downloader
import pageparser
import time
import sqlite3
import string
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


main_url = 'https://bigfuture.collegeboard.org'




def main(entrance):
    
    print "entrance:{}".format(entrance)

    entrance_html = downloader.get_html_from_phantomjs(entrance)
    major_url_list = pageparser.get_specialty(entrance_html)
    i=0

    for major_url in major_url_list:#1182
        print 'spider to page {}/1182'.format(i)
        major_html = downloader.get_html_from_phantomjs(major_url)
        title,intro,helpful_courses,related_majors = pageparser.parse_major(major_html)



       # controler.write_data(title,intro,helpful_courses,related_majors)
        print 'title:{},code:{},helpful_courses:{},related_majors:{}'.format(title,intro,helpful_courses,related_majors)
        i=i+1


if __name__ == '__main__':
    main('https://bigfuture.collegeboard.org/majors-careers')
