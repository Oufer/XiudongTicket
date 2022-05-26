# -*- coding: utf-8 -*-
'''
Created on 2022.05.25 上午 12:48
Author : OuyangPeilong
Software: PyCharm
'''
from driver import load_driver
from app import create_app
from concurrent.futures import ThreadPoolExecutor
from gevent import pywsgi

if __name__ == '__main__':
    driver = load_driver()
    pool = ThreadPoolExecutor(max_workers=10)  # 数量为 10 的线程池
    app = create_app(driver, pool)
    # server = pywsgi.WSGIServer(('127.0.0.1',9997),app)
    # server.serve_forever()
    app.run(host='127.0.0.1', port=9997, debug=False)