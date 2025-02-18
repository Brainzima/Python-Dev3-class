import os
# os.remove('about.txt')

if os.path.exists('aboutdfgdfg.html'):
    os.remove('aboutdfgdfg.html')
    print('Deleted Successfully')
else:
    print('File Not Found')