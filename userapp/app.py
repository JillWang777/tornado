# -*- coding: utf-8 -*-
# Author：ala
# @Date   : 2020/4/19 10:33
# @Project : userapp
# @File    : app.py
from tornado import ioloop
from tornado import web,httpserver
from handles import user as user_handles

HANDLERS = [
    (r'/api/users',user_handles.UserListHandler),
    (r'/api/users/(\d+)',user_handles.UserHandler)

]

def run():
    app = web.Application(
        HANDLERS,
        debug=True,
    )
    http_server = httpserver.HTTPServer(app)
    port = 8888
    http_server.listen(port)
    print('server start on port:{}'.format(port))
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
