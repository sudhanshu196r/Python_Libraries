'''
    @Author: Sudhanshu Kumar
    @Date: 10-10-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 10-10-2024
    @Title : Logger file containing logger function

'''

import logging

def logger_init(name):
    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler('all.log')

    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger