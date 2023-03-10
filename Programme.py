### 1. Write a function which return the len of string (Without using inbuilt len function)

def str_len(s):
    s = str(s)
    length = 0
    
    for i in s:
        length += 1
        
    return "length of {}: {}".format(s, length)

str_len("QWERTY")

str_len(12341)

------------
### 2. Write a function which returns index of all primitive elements

def print_index(data):
    itr = 0
    for i in data:
        if (type(i) == int or type(i) == float or type(i) == str or type(i) == bool):
            print("Index: {} and Element: {}".format(itr, i))
        itr += 1

print_index([2,3, 5+7j, 'asd'])

print_index(['data', 2+3j, [2,3,4], 23.13, (66,7,8)])

print_index('Data')

------------
### 3. Function which take dict as input and return all the values as list (for nested dict also)

value_list = []
def values(d):
    for i in d:
        if type(d[i]) == dict:   ## Checking if the value is dict
            values(d[i])         ## Calling function itself if  value is dict
        else:
            value_list.append(d[i])
            
    return value_list


d = {'k1': 1, 'k2': 'data k2', 'k3':{'k3a': (1,2,3), 'k3b':{'k3b1': 3+5j, 'k3b2': [6,7,8]}}}
values(d)

------------
### 4. Function that takes another function as input and return the output

def func_A(numA):
    return numA*10

def func_B(numB):
    return numB*(-11)


ans = func_B(func_A(2))
ans

------------
### 5. Function that take multiple list as argument and return concatination of all elements

def concat_elements(*args):
    out_list = []
    for i in args:
        out_list.append(i)
        
    return out_list

concat_elements([1,2,3], [-2,4, -9.34], [3+5j, True, 'Data'])

---------------------
### 6. Function that take list as argument and return index of all elements

def task6_index(l):
    itr = 0
    for i in l:
        print("Index: {} and Element: {}".format(itr, i))
        itr += 1

task6_index([2,3,1, [7,6,5]])

---------------------
### 7. Function that will return list of all the file name from directory

import os

def task7_ls(path):
    os.chdir(path)
    print("current working directory: ", os.getcwd())
    
    return os.listdir()

path = 'G:\eclipse-workspace\Java Programming'
task7_ls(path)

---------------------
### 8. Function that will display system configuration

pip install platform

import platform
import psutil

def task8_sysconfig():
    sys_info = platform.uname()
    
    print('Node: ', sys_info.node)
    print('Processor: ', sys_info.processor)
    print('OS: ', sys_info.system)
    print('GPU: ', sys_info.machine)  
    print('CPU Count: ', psutil.cpu_count())
    print('Virtual Memory: ', psutil.virtual_memory())
    

task8_sysconfig()

---------------------
### 9. Function that will display date and time

from datetime import datetime

def task9_datetime():
    dt = datetime.now()
    dt = str(dt)   ## Type converstion into str
    
    dt = dt.split(' ')
    print('Date: ', dt[0])
    print('Time: ', dt[1])

task9_datetime()

---------------------
### 10. Function that will read and display the image

!pip install opencv-python

import cv2

def task10_img(img_path):
    
    img = cv2.imread(img_path)
    cv2.imshow('Image :', img)
    cv2.waitKey(0) # waits until a key is pressed
    cv2.destroyAllWindows()

img_path = 'image.png'

task10_img(img_path)

## Showing image in other tab

---------------------
### 11. Function that will read and display the video

import cv2

def task11_video(video_path):
    video = cv2.VideoCapture(video_path)
    
    while(video.isOpened()):
      # Capturing the video frame-by-frame
        ret, frame = video.read()
        if ret == True:
            cv2.imshow('Frame',frame) #Showing the display of current frame
            if cv2.waitKey(25) & 0xFF == ord('x'):  ## Press x for exit the video
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()

task11_video('video.mp4')

---------------------
### 12. Function that will move a file from one directory to another

import shutil

def task12_move(source, target):
    shutil.move(source, target)
    print("File moved\nFrom {} to {}".format(source, target))

source = r'C:\Users\Chandan Kumar\Documents\Ineuron Data Science\Live Class\Python\task12.txt'
target = r'G:\Data Science'

task12_move(source, target)

---------------------
### 13. Function to shutdown the system

import os

def task13_shutdown():
    os.system('shutdown /s')

---------------------
### 14. Function to access the mail

!pip install easyimap

import easyimap as e

def task14_emailAccess(user, passwd, mailNo=0):
    '''
    mailNo[optional]: mail id, 0 for latest, 1 for second latest and so on. By default 0
    In order to establish the connection we need to allow the less secure access:
    https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MxmEFG95x8NccLO3ixua11TmiXtZy-CofzTsE0BqPrLaBPgZYilKEmH_daV8K1JuA9_E8AapH2pFU56PLMyTZkoMOa7w
    '''
    server = e.connect('imap.gmail.com', user, passwd)  ## Establish the connection between gmail and python
    mail = server.mail(server.listids()[mailNo])  ## Fetching the id of latest mail

    print('Sender:\n', mail.from_addr)
    print('\nTitle:\n', mail.title)
    print('\nBody:\n', mail.body)

user = 'Mike2473565@gmail.com'
passwd = ''

task14_emailAccess(user, passwd)

task14_emailAccess(user, passwd, mailNo=3)

---------------------
### 15. Function to write a mail

import smtplib

def task15_writeMail(user, passwd):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  ## creating a connection between gmail and python using tls(transport layer security)
    server.login(user,passwd)  ## Login into the gmail account
    rx_mail = input("Enter receiver mail id: ")
    msg = input('Enter the mail(body): ')
    server.sendmail(user, rx_mail, msg)
    server.close()
    print('Mail Sent')

user = 'Mike2473565@gmail.com'
passwd = ''

task15_writeMail(user, passwd)

![image.png](attachment:image.png)

---------------------
### 16. Function to read the pdf file

!pip install PyPDF2

import PyPDF2

def task16_readPDF(pdf_path):
    pdfFileObj = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("Number of pages: ", pdfReader.numPages)
    
    for i in range(0,pdfReader.numPages):
        print("\nPageNo. ", i)
        pageObj = pdfReader.getPage(i)
        print(pageObj.extractText())
        
    pdfFileObj.close()


task16_readPDF("MYSQL.pdf")

---------------------
### 17. Function to read the word file

!pip install python-docx

import docx

def readtxt(filename):
    doc = docx.Document(filename)
    word_text = []
    for para in doc.paragraphs:
        word_text.append(para.text)
    return '\n'.join(word_text)


print(readtxt('Assignment1.docx'))

---------------------
### 18. Function to extract word file from a directory

def task18_listDocx(dict_path = os.getcwd()):
    os.chdir(dict_path)
    
    files = os.listdir()  ## Contains all the file name 

    for i in files:
        file_details = os.path.splitext(i)   ## Spliting the file from the extension
        if file_details[1] == '.docx':
            print(file_details[0], file_details[1])

task18_listDocx()

dict_path = r'C:\Users\Chandan Kumar\Downloads'
task18_listDocx(dict_path)

---------------------
### 19. Function to display the ip address

# Python Program to Get IP Address
import socket

def task19_displayIP():
    host = socket.gethostname()
    IPAddr = socket.gethostbyname(host)
    
    return "HostName: {} | IP Address: {}".format(host, IPAddr)

task19_displayIP()

---------------------
### 20. Function to merge 2 pdf files

import PyPDF2 

def task20_mergePDF(file1, file2):
    mergeFile = PyPDF2.PdfFileMerger()
    mergeFile.append(PyPDF2.PdfFileReader(file1, 'rb'))
    mergeFile.append(PyPDF2.PdfFileReader(file2, 'rb'))
    mergeFile.write("NewPDF.pdf")
    print('Merge done.')

file1 = 'MYSQL.pdf'
file2 = 'pdf2.pdf'
task20_mergePDF(file1, file2)

