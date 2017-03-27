# -*- coding: utf-8 -*-


class OlxPipeline(object):

    def process_item(self, item, spider):
        spider.log('------ ITEM CAPTURADO -------')
        return item
