# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql
from scrapy.conf import settings


class AnimationPipeline(object):

    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mysql', database='dongman', charset='utf8')
        # 创建游标
        self.cs = self.conn.cursor()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        # 关闭游标
        self.cs.close()
        # 关闭数据库连接
        self.conn.close()

    def process_item(self, item, spider):
        name = item['name']
        picture_url = item['picture_url']
        count = item['count']
        spider_name = item['spider_name']

        # 处理sql语句
        create_table_sql = '''create table if not exists {}(id int unsigned primary key auto_increment not null,name varchar(40),picture_url varchar(300) default '',count int unsigned default 1)'''.format(spider_name)

        try:
            if settings.get('FLAG') == False:
                self.cs.execute(create_table_sql)
        except:
            settings.set('FLAG', 'True')

        sql = 'insert into {} values (null,"{}","{}",{});'.format(spider_name, name, picture_url, count)

        self.cs.execute(sql)
        # 获取数据
        # data = self.cs.fetchall()

        self.conn.commit()

        return item