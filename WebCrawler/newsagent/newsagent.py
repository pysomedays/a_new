__author__ = 'sks'
from nntplib import NNTP
from time import strftime, time, localtime
day = 24*60*60
yesterday = localtime(time()-day)
date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

servername = 'data.eastmoney.com'
group = 'comp.lang.python.announce'
server = NNTP(servername)

print(server.group(group)[0])
# to be continued
#ids = server.newnews()