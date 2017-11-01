git init
git config --global user.name "pysomedays"
git config --global user.email "pysomedays@163.com"
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding gbk

git add AutoMessage
git commit -m "change AutoMessage folder: adding some files"
git remote add -f origin https://github.com/pysomedays/a_new.git
git push -u origin master
pause