import os,logging
import util
from json import JSONEncoder

BASE_PATH = r"r:/crunchbase/"
CSV_PATH = r"E:/odm.csv/organizations.csv"
LOG_PATH = r"r:/tmp/test.log"

# log模块初始化
import logger
logger = logger.getlog("mylog",LOG_PATH)


# 检查缓存目录
if(not os.path.exists(BASE_PATH)):
    os.makedirs(BASE_PATH)

# 读取csv文件，获得company name
companyNames = util.getOrganizationList(CSV_PATH)

# 添加 CrunchBase python包
from pycrunchbase import CrunchBase
cb = CrunchBase("")

# 遍历所有提取到的name
for name in companyNames:
    filepath = BASE_PATH + name
    if(os.path.exists(filepath)):
        logger.info(name + ' is exite')
        continue
    file = open(filepath, 'w', encoding="utf8")
    while True:
        try:
            node = cb.get_node('organizations', name)
            break
        except Exception:
            logger.error(name + ' 抓取失败')
    json = JSONEncoder().encode(node)
    file.write(json)
    file.close()
    logger.info(name + ' is ok')
