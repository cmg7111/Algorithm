str=input()
bomb=input()

flag=True
"""
while flag:
    if bomb not in str:
        flag=False
        break
    else:
        str=str.replace(bomb,"")
        print(str)
"""
while flag:
    new=""
    if bomb not in str:
        flag=False
        break
    else:
        lst=[]
        cnt=0
        for idx,data in enumerate(str):
            if data==bomb[cnt]:
                lst.append(data)
                cnt+=1
                print(lst)
                if cnt==len(bomb):
                    for loop in range(cnt):
                        lst.pop()
                    cnt=0
            else:
                new+=data
        print(new)

if str=="":
    print("FRULA")
else:
    print(str)