# util.py
def getOrganizationList(CSV_PATH, IgnoreLine=1, readLine=10):
    """
    by ider
    the csv must be organizations.csv
    CSV_PATH:the csv path
    """
    import csv
    import re
    reader = csv.reader(open(CSV_PATH, encoding="utf8"))
    companyNames = []
    for line in reader:
        # 忽略第一行
        if reader.line_num == IgnoreLine:
            continue

        # 正则表达式提取name
        match = re.search(r"organization/(.*)\?", line[4])
        if match:
            companyNames.append(match.group(1))
        else:
            logger.error(line[4] + " csv read failed")
            exit()

        # 读取多少行
        if readLine != 0 and reader.line_num == readLine:
            break
    return companyNames
