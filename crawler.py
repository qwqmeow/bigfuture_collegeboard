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
import time
reload(sys)
sys.setdefaultencoding('utf-8')


main_url = 'https://bigfuture.collegeboard.org'




def main(entrance):
    start_time = time.time()
    
    print "entrance:{}".format(entrance)

    entrance_html = downloader.get_html_from_phantomjs(entrance)
    major_url_list = pageparser.get_major_categories(entrance_html)
    
    for id in xrange(144,len(major_url_list)):
        major_url = major_url_list[id]
        print 'spider to page {}/{}\nurl:{}'.format(str(id),str(len(major_url_list)),major_url)
        
        major_html = downloader.get_html_from_phantomjs(major_url)
        try:
            title,intro,helpful_courses,related_majors = pageparser.parse_major(major_html)
        except Exception as e:
            with open('fail_url.txt', 'a') as fd:
                fd.write('{}\n{}'.format(e,major_url))
            continue


        controler.write_data(title,intro,helpful_courses,related_majors)
        print 'running time:{}s'.format(str(time.time()-start_time))
        # print 'title:{},code:{},helpful_courses:{},related_majors:{}'.format(title,intro,helpful_courses,related_majors)


if __name__ == '__main__':
    main('https://bigfuture.collegeboard.org/majors-careers')
