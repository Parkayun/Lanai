# -*- coding:utf-8 -*-
from gevent.server import StreamServer


class LanaiServer(StreamServer):

    def __init__(self, app):
        print app
        super(LanaiServer, self).__init__(
            listener=(app.config['host'], app.config['port']),
            handle=app.connection_handler_class
        )
        self.app = app

    def do_handle(self, *args):
        args = args + (self.app.protocol_dict,)
        super(LanaiServer, self).do_handle(*args)