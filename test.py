from zipfile import ZipFile
import pandas as pd

lst = []
c = 0
with ZipFile('testtask.zip') as zip_file:
    my_lst = zip_file.infolist()
for i in my_lst:
    if not i.is_dir():
        lst.append([c, i.filename[:i.filename.rfind("/")], i.filename[i.filename.rfind("/")+1:], i.filename[i.filename.find("."):]])
        c += 1
for i in lst:
    print(i)


df = pd.DataFrame(lst)
df.to_excel('result.xlsx')