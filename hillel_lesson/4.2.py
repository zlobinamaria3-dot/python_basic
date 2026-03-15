lst=[]
if len(lst)>0:
    new_lst=sum(lst[::2])*lst[-1]
    print(new_lst)
if len(lst)==0:
    new_lst=lst
    print([0])


