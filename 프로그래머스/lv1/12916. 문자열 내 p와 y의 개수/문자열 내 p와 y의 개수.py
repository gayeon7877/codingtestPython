def solution(s):
    num_p,num_y=0,0
    
    for i in s:
        if i=='p' or i=='P':
            num_p+=1
        elif i=='y' or i=='Y':
            num_y+=1
        else:
            continue
    if  num_p==num_y:
        return True
    else:
        return False
   