import os
path = 'C:\\Users\\Vilaksh\\Desktop\\images\\midConfig'
files = os.listdir(path)
i=40
for file in files:
    
    i = i + 1
    os.rename(os.path.join(path, file), os.path.join(path, str(i) + '.jpg'))


