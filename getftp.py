#/usr/bin/env python
#--coding:utf-8--

#ftp.cc.ac.cn


import ftplib
import os
import socket

HOST = 'ftp.cc.ac.cn'
DIRN = 'pub/home/yyx'
FILE = 'newname.doc'

def testftp():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'Error: can not reach %s'%HOST
        return
    print '*** Connect to host "%s"'%HOST

    f.login()
    print 'login as anonymous'
    f.cwd(DIRN)
    f.retrbinary('retr %s'%FILE, open(FILE,'wb').write)
    
    print '***download '

    f.quit()

if __name__ == '__main__':
    testftp()






