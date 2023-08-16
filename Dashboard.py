def dash():
    while True:
        print("Welcome",input_username,"!!!")
        inp=int(input('''What  would you like to do?
1.     ....
2.     ......
3.     ......'''))
        if inp==1:
            pass
        elif inp==2:
            pass
        elif inp==3:
            pass
        ch=input("Would you like to continue operations? (Y)")
        if ch.lower()!='y':
            break
        else:
            continue
    
