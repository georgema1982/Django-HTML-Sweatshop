from django.conf import settings
from appconf.base import AppConf

class HtmlSweatshopConf(AppConf):
    THEME = 'bootstrap3'
    DIGG_PAGINATION_LEADING_PAGE_RANGE_DISPLAYED = DIGG_PAGINATION_TRAILING_PAGE_RANGE_DISPLAYED = 10
    DIGG_PAGINATION_LEADING_PAGE_RANGE = DIGG_PAGINATION_TRAILING_PAGE_RANGE = 8
    DIGG_PAGINATION_NUM_PAGES_OUTSIDE_RANGE = 2 
    DIGG_PAGINATION_ADJACENT_PAGES = 4
    MESSAGE_CENTRE_MESSAGE_DISMISSIBLE = True
