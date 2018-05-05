prefix=str(input("What is the prefix? (without numbers) "))
domain= str(input("What is the domain? @"))
password=str(input("What is the password? "))
accountnumbers=int(input("How many accounts do you want to create? "))
accountnumbers=accountnumbers+1
if accountnumbers<=100:
    for index in range(accountnumbers):
        if len(str(index))==1:
            print(str(prefix) + "00" + str(index) + "@" + str(domain) + ":" + str(password))
        elif len(str(index))==2:
            print(str(prefix) + "0" + str(index) + "@" + str(domain) + ":" + str(password))
        else:
            print(str(prefix) + str(index) + "@" + str(domain) + ":" + str(password))
elif accountnumbers<=1000:
    for index in range(accountnumbers):
        if len(str(index))==1:
            print(str(prefix) + "000" + str(index) + "@" + str(domain) + ":" + str(password))
        elif len(str(index))==2:
            print(str(prefix) + "00" + str(index) + "@" + str(domain) + ":" + str(password))
        elif len(str(index))==3:
            print(str(prefix) + "0" + str(index) + "@" + str(domain) + ":" + str(password))
        else:
            print(str(prefix) + str(index) + "@" + str(domain) + ":" + str(password))
elif accountnumbers<=10000:
    for index in range(accountnumbers):
        if len(str(index))==1:
            print(str(prefix) + "0000" + str(index) + "@" + str(domain) + ":" + str(password))
        elif len(str(index))==2:
            print(str(prefix) + "000" + str(index) + "@" + str(domain) + ":" + str(password))
        elif len(str(index))==3:
            print(str(prefix) + "00" + str(index) + "@" + str(domain) + ":" + str(password))
        elif len(str(index))==4:
            print(str(prefix) + "0" + str(index) + "@" + str(domain) + ":" + str(password))
        else:
            print(str(prefix) + str(index) + "@" + str(domain) + ":" + str(password))
