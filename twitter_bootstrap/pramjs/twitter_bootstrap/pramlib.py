from prambanan.compiler import *
from prambanan.compiler.library import PrambananLibrary as BasePrambananLibrary
from os.path import *
from pkg_resources import resource_filename

src_dir = resource_filename("pramjs.twitter_bootstrap", "")
js_dir =  join(src_dir, "js")

class PrambananLibrary(BasePrambananLibrary):

    def __init__(self, *args):
        import datetime
        super(PrambananLibrary, self).__init__(*args)
        modules = [
            PythonModule(join(src_dir, "modal.py"), "pramjs.twitter_bootstrap.modal", self.import_cache, [join(js_dir, "bootstrap-modal.js"), join(src_dir, "bootstrap-modal-gallery.js")]),
            PythonModule(join(src_dir, "datepicker.py"), "pramjs.twitter_bootstrap.datepicker", self.import_cache, [join(src_dir, "bootstrap-datepicker.js")]),
        ]
        self.modules = modules

    def get_modules(self):
        return self.modules[:]
