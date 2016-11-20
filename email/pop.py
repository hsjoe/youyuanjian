#-*encoding:utf-8*-

from poplib import POP3 as pop3
host ='pop.189.cn' 
user = ''

pp = pop3(host)
pp.set_debuglevel(1)
pp.user(user)
pp.pass_('')
print pp.stat() 
