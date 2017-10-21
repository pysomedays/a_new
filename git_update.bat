git init
git remote add -f origin https://github.com/pysomedays/a_new.git
git config core.sparsecheckout true
echo Server >> .git/info/sparse-checkout
git pull origin master
pause