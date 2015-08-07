from json import JSONEncoder
from pycrunchbase.pycrunchbase import CrunchBase
from resource import (
    Acquisition,
    FundingRound,
    Fund,
    IPO,
    Organization,
    Page,
    Person,
    Product,
)

cb = CrunchBase("27c21624cf305e9764e65a21ce1f75a2")

node_data = cb.get_node('organizations', "facebook")

org = Organization(node_data)

page_data = cb.moredata(org.past_team)

print(org.past_team.total_items)

page1 = Page(org.name, page_data)
print(page1.name)

page_data2 = cb.moredata(page1)

file = open(r"d:/1.txt", 'w')
json = JSONEncoder().encode(page_data2)
file.write(json)
file.close()

# print(node_data)
