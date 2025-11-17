import os
import time

print('Valid path:', os.path.exists('D:\\Screenshots\\Books\\Books1.png'))
print('Invalid path:', os.path.exists('D:\\Screenshots\\Bookings\\Books1.png'))

print('Is file:', os.path.isfile('D:\\Screenshots\\Books\\Books1.png'))
print('Is directory 1:', os.path.isdir('D:\\Screenshots\\Books\\Books1.png'))
print('Is directory 2:', os.path.isdir('D:\\Screenshots\\Books'))

print('Split:', os.path.split('D:\\Screenshots\\Books\\Books1.png'))
print('Join:', os.path.join('D:\\Screenshots\\Books\\Books1.png'))

print('Base name:', os.path.basename('D:\\Screenshots\\Books\\Books1.png'))
print('Directory name:', os.path.dirname('D:\\Screenshots\\Books\\Books1.png'))

# As of 1st January, 1970
print('Last modified time 1:', os.path.getmtime('C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Math.py'))
print('Last modified time 2:', time.ctime(os.path.getmtime('C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Math.py')))

print('Last access time 1:', os.path.getatime('C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Math.py'))
print('Last access time 2:', time.ctime(os.path.getatime('C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Math.py')))

print('Creation time 1:', os.path.getctime('C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Math.py'))
print('Creation time 2:', time.ctime(os.path.getctime('C:\\Users\\HP\\OneDrive\\Desktop\\Python\\Math.py')))

os.chdir('D:\\Screenshots\\Books') # Change current working directory
print('Current working directory:', os.getcwd())

print('Relative path:', os.path.relpath('D:\Screenshots\Quotes\\quote1.png'))
print('Absolute path:', os.path.abspath('..\\Quotes\\quote1.png'))