git init
git config --global user.name "pysomedays"
git config --global user.email "pysomedays@163.com"
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding gbk
pause
git add .
git commit -m "提交文件20171008_txt2html"
git remote add -f origin https://github.com/pysomedays/a_new.git
git push -u origin master
pause