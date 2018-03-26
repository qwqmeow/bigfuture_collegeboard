#!/usr/bin/env python
#-*-coding:utf-8-*-

import pymysql

def _decode_utf8(str):
    return str.encode('utf-8','ignore').decode('utf-8')



def write_data(title,intro,helpful_courses,related_majors):

    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='pass',db='edu',charset='utf8')
    cursor = conn.cursor()
    #对数据解码为unicode
    # title,intro,helpful_courses,related_majors = map(_decode_utf8, (title, code,subject, class_, name, intro))

    #插入数据
    try:

        cursor.execute('INSERT INTO edu_spider_en (title,intro,helpful,related)VALUES("{}","{}","{}","{}")'.format(title,intro,helpful_courses,related_majors))
    except Exception as e:
        print e
        pass
    cursor.close()
    conn.commit()
    conn.close()

