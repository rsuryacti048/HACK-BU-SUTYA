import sys

path = 'https://www.techiedelight.com/redirect-standard-output-to-file-python/'
sys.stdout = open(path, 'w')
print('Hello, World')
