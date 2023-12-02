from xml.etree import ElementTree as et


ans = {}
tree = et.parse("currency.xml")
root = tree.getroot()
for child in root:
    ans[child[3].text] = child[4].text
print(ans)