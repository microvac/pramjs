from prambanan import JS
from pramjs.elquery import ElQuery

def modal(el, options):
    ElQuery(el).modal(options)

def modal_gallery(el, options):
    JS("modal_gallery_show(el, options)")

