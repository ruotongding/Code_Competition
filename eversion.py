
num_cases = int(input("enter the numver of array: "))
case_len = [""]*num_cases
global eversion
for i in range(num_cases):
    case_len[i] = int(input("No."+str(i+1)+" array len: "))
    array = [""]*case_len[i]
    eversion = 0
    for j in range(case_len[i]):
        array[j] = int(input(str(j+1)+"array element: "))
    print(array)

    left = []
    right = []
    newarray = []

    while True:
        left = []
        right = []
        newarray = []
        for k in range(len(array)):
            if array[k]<= array[len(array)-1]:
                left.append(array[k])
            else:
                right.append(array[k])
        newarray = left+right

        if newarray == array:
            break
        else:
            array = newarray
            print(array)
            eversion+=1
    print(eversion)

def eversion(array):
    left = []
    right = []
    newarray = []
    for k in range(len(array)):
        if array[k]<= array[len(array)-1]:
            left.append(array[k])
        else:
            right.append(array[k])
        newarray = left+right

        if newarray == array:
            pass
        else:
            eversion+=1

    return newarray
