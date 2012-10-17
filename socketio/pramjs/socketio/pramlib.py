from prambanan.compiler import *
from prambanan.compiler.library import PrambananLibrary as BasePrambananLibrary
from os.path import *
from pkg_resources import resource_filename

src_dir = resource_filename("pramjs.socketio", "")

class PrambananLibrary(BasePrambananLibrary):

    def __init__(self, *args):
        super(PrambananLibrary, self).__init__(*args)
        modules = [
            JavascriptModule([join(src_dir, "socket.io.js"), join(src_dir, "pramjs.socketio.js")], "pramjs.socketio"),
        ]
        self.modules = modules

    def get_modules(self):
        return self.modules[:]
