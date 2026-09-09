hr,minu,sec=map(int,input("Enter the time: ").split())
if((hr>=0 and hr<24)and(minu>=0 and minu<60)and(sec>=0 and sec<60)):
    print("Valid time")
else:
    print("Invalid time")