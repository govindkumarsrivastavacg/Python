flag=False
while(flag==False):
    i=0
    flag_up=False
    flag_lw=False
    flag_len=False
    flag_dig=False
    flag_sp=False
    Flag_spac=True

    password=input("Enter the password: ")
    while(i<len(password)):
        if(password[i]>='A' and password[i]<='Z'):
            flag_up=True
        elif(password[i]>='a' and password[i]<='z'):
                flag_lw=True
        elif(password[i]>='0' and password[i]<='9'):
                    flag_dig=True
        elif(password[i]==" "):
            Flag_spac=False
        else:
            flag_sp=True
        i+=1
    if(len(password)>=8):
        flag_len=True
    flag=flag_len and flag_sp and flag_up and flag_lw and flag_dig and Flag_spac
    if(flag):
        print("Valid Password")
    else:
            print("Invalid Password")
            print("Reason(s):")
            if(flag_up==False):
                print("No Uppercase characters were present")
            if(flag_lw==False):
                print("No lowercase characters were present")
            if(flag_dig==False):
                print("No digit characters were present")
            if(flag_sp==False):
                print("No speical characters were present")
            if(flag_len==False):
                print("Length was less than 8")
            if(Flag_spac==False):
                print("Space was present")
