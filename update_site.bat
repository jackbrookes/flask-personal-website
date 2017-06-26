call git push master
call python freezer.py
call cd jbrookes.github.io
call git add .
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
call git commit -m "%mydate%"
git push master
