dir /B>name.txt
findstr /v "hello" name.txt>newname.txt

for /f %%i in ("newname.txt") do (
for /f "tokens=1,2 delcim=." %%a in("%%i") do (
ren "%%i" "%%a(hello).%%b")
)