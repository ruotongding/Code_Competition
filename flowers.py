
test_cases = int(input("Please enter the number of test case:"))

case_len = [""]*test_cases

for i in range(test_cases):
    case_len[i] = int(input("No."+str(i+1)+" case len: "))
    flowers = [""]*case_len[i]
    height = 1
    for j in range(case_len[i]):
        flowers[j] = int(input("water(0 or 1): "))
    for k in range(0,len(flowers)):
        if(k!=1 and k != len(flowers)-1):
            if flowers[k]==0 and (flowers[k+1]==0 or flowers[k-1]==0):
                height = -1
                break
        if(k==0):
            if flowers[k]==1:
                height+=1
        elif(k==len(flowers)-1):
            if flowers[k]==1 and flowers[k-1]==0:
                height+=1
            elif flowers[k]==1 and flowers[k-1]==1:
                height+=5
        else:
            if flowers[k]==1:
                if flowers[k-1]==0:
                    height+=1
                elif flowers[k-1]==1:
                    height+=5
            elif flowers[k]==0:
                height+=0
    print("output: "+str(height))
