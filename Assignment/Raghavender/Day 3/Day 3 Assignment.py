#1.Write a program to see how single condition and multiple condition based statement works. (hint: single condition based if-else)

    rname0 = "Raghu"
    if rname0 == "Ayub":
        print("You name is not correct")
    
    rname1 = "Raghu"
    if rname1 == "Ayub":
        print("You name is not correct")
    else:
        print("You are right")
    
    rname2 = "Raghavender Rao"
    rname3 = input()
    if rname2 == rname3:
    	print("Your name is updated correctly")
    elif rname3 == "Male":
    	print("You have typed gender instaed of name, please check and update it correctly")
    else:
    	print("You name is not updated correctly in first attmept")

#2.Write a program to differentiate between for loop and while loop
    # For loops
    for x in range(0,25):
        print(x)
    
    # While Loop
    x = 10
    while x <= 20:
        print(x)
        x += 1
    print(x)

#3.Write a program to see how break, continue and pass works

    # break in the below code is belongs to number break statment apply because 6 is in the series
    rname5 = 5
    while rname5<=100:
        rname5+=1
        if rname5==26:
            break
        print(rname5)
    
           
    # break will not work, in the below code statment will not work becuase 26 is in not the series
    rname6 = 1
    while rname6<=8:
        if rname6 ==10:
            break
        print(rname6)
        rname6+=1
    
    
    # Continue will skip the condiation what we have given
    r6 = 1
    while r6 <=50:
        r6+=1
        if r6==10:
            continue
        print(r6)
    # continue will not work in below statment because we are given digit more than what we have defined r7
    r7 = 1
    while r7 <=50:
        r7+=1
        if r7==51:
            continue
        print(r7)
    # pass will continue given condition what we have given it will not break or skip condition even if we mentioned a if condiations
    
    r8 = 1
    while r8<=15:
        if r8 ==3:
            pass
        print(r8)
        r8+=1
    # pass will not continue given condition becuase we have digit more than what we have assigned for r9
    r9 = 1
    while r9 <=10:
        if r9 ==11:
            pass
        print(r9)
        r9+=1
    # below code what i am writing is combination of break,continue and pass
    r10 = 0
    while r10<=26:
        r10+=1
        if r10==8:
            break
        elif r10==5:
            continue
        else:
            pass
        print(r10)