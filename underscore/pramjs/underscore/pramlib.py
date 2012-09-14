from prambanan.compiler import *
from prambanan.compiler.library import PrambananLibrary as BasePrambananLibrary
from os.path import *
from pkg_resources import resource_filename

src_dir = resource_filename("pramjs.underscore", "")

class PrambananLibrary(BasePrambananLibrary):

    def __init__(self, *args):
        super(PrambananLibrary, self).__init__(*args)
        modules = [
            JavascriptModule([join(src_dir, "pramjs.underscore.js")], "pramjs.underscore"),
        ]
        self.modules = modules

    def get_modules(self):
        return self.modules[:]
