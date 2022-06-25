from xml.dom import minidom
import pandas as pd

p1 = minidom.parse("annotations.xml")
print(p1)
df = pd.DataFrame(data)
tagname= p1.getElementsByTagName('image')
for x in tagname:
    tagname= p1.getElementsByTagName('image')
    #print(x.attributes['name'].value)
    a=x.attributes['name'].value
    for y in tagname1:
        tagname1= p1.getElementsByTagName('points')
        #print(y.attributes['label'].value)
        b=y.attributes['label'].value
        #print(y.attributes['points'].value)
        c=y.attributes['points'].value
        print(a, '  ' ,b,'  ',c)
        data = {'images': [ a ],
        'label Name': [b],
        'label point': [c]
        }
        df = df.append(data, ignore_index = True)



print(df)
