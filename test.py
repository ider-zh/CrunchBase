# import requests
# requests.get('http://github.com', timeout=0.001)
import logging
import logger
log = logger.getlog("cc")


import util
CSV_PATH = r"E:/odm.csv/organizations.csv"
list = util.getOrganizationList(CSV_PATH)

log.info(list)