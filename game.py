import random

li = ["ACCELERATING","Aircraft","Consequences","ABBREVIATION","Airforce","Grandparents","Civilization","Kaleidoscope","Intelligence","Alphabet","Organization","Relationship","Bodybuilding","Backpack"]
# r = random.choice(li).lower()
r = "booooooooo"
rl = {}
n = len(r)
s=list(r)
ran_l = []
print(s)
for i in range(3):
    c=random.randrange(0,n)
    if c not in ran_l:
        ran_l.append(c)
        print(c)
        rl[c] = s[c]
        x = s.pop(c)
        s.insert(c,"_")
        "".join(s)
        print(s)
print(rl)
a=''
for er in range(len(ran_l)):
    user_inp = input()
    if user_inp==r:
        print("correct: ", user_inp)
        break
    for ke,va in rl.items():
        if va==user_inp:
            s.pop(ke)
            s.insert(ke,va)
            for i in s:
                a+=i
            print(a)
            if s == list(r):
                print(r,"hi you found it!!!")
                exit()

if s == list(r) or user_inp == r:
    print("Wow!!! You found it ")
else:
    print("Out of chances ")
# print("correct",r)
# t=s
# n = len(s)
# rl=[]
# # a=''
# rty=[]
# for i in range(3):
#     c=random.randrange(0,n)
#     print(c)
#     rl.append(c)
#     for p in range(n):
#         if p == c:
#             rty.append(s[p])
#             a = s.replace(s[p],"_",1)
#             s = a
#             print(a)
# print(rty)
    # rl.append(c)
    # for o in range(n):
    #     for h in rl:
    #         if o==h:
    #             a+="_"
    #             print(h)
    #         else:
    #             a+=s[o]
    #         print(a)
# for i  in t(
# v=input()

