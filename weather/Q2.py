import xml.etree.ElementTree as ET
import json


def convert(root):
    dic = dict()
    if len(root.attrib) != 0:
        dic.update(root.attrib)
    if (root.text != None) and (len(root.text.strip()) != 0):
        return {root.tag: root.text}
    for child in root:
        dic.update(convert(child))
    return {root.tag: dic}


x = input("input the XML file's name : ")
tree = ET.parse(x)
root = tree.getroot()
ans = convert(root)
jsonn = json.dumps(ans[root.tag])
filee = open("out.json", "w")
filee.write(jsonn)
filee.close()
