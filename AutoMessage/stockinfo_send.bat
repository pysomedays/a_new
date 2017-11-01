cd ..\WebCrawler
rd/s/q stock_info
python stocksnotice.py
cd ..\AutoMessage
python send_email.py
pause