import shutil
import os

# shutil.copy("D:\Data Science Course\Python\shutil\main.py", "D:\Data Science Course\Python\shutil\main2.py")
# shutil.copytree(".tutorial", "mytutorial")
# shutil.move(".tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial")
# os.remove("file.file")

for i in range(1,11):
    print(i)
    shutil.copytree("Day", f"Day {i}")
    # shutil.rmtree(f"Day {i}")
    # os.remove(f"d:/Data Science Course/Python/shutil/Day {i}/day.py")