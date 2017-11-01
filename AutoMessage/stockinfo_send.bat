cd ..\WebCrawler
rd/s/q stock_info
python stocksnotice.py
cd ..\AutoMessage
python sendemail.py
pause