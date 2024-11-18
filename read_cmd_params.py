import sys
import os

for i, p in enumerate(sys.argv):
    print (f'{i}-->{p}')

oneDrive=os.getenv('OneDrive')
print(oneDrive)