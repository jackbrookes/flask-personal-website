call git push
call python freezer.py
call cd jackbrookes.github.io
call git add .
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%a-%%b)
call git commit -m "%mydate%"
call git push
