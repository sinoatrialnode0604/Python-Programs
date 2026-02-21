def FindStr(word,str):
    if word in str:
        return True
    else:
        return False

result = FindStr("ar","Adarsh")
if result == True:
    print("Present.")
else:
    print("Absent.")