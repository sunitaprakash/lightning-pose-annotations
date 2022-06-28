import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse('annotations.xml')
root = tree.getroot()

dict_attrib = {'image':[], 'tail':[], 'Nose':[], 'Left Front paw':[] }

#working copy
for i in root.iter('image'):
    name = i.attrib['name']
    dict_attrib['image'].append(name)
    for child in tree.findall(f"./image[@name='{name}']/"):
            labelx = child.attrib['label']
            if (labelx in dict_attrib):
                points = child.attrib['points']
                dict_attrib[labelx].append(points.split(','))
pd.DataFrame.from_dict(dict_attrib)
