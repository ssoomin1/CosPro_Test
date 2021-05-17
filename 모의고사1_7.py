#신수민
def solution(file_info):
    success=0
    fail=0
    for f in file_info:
        splited=f.split(",")
        print(splited)
        if splited[0]=="jpeg" and int(splited[2])<1000:
            success+=1
        else:
            fail+=1
    return success,fail

files_info=["jpeg,all.jpg,500","mpeg,all.mp3,500"]
success,fail=solution(files_info)
print("success=",success)
print("fail=",fail)

# string="this is string constant"
# splited=string.split(" ")
# print(splited)