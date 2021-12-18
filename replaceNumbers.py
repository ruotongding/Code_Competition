
# You have an array of integers (initially empty).
#
# You have to perform 𝑞 queries. Each query is of one of two types:
#
# "1 𝑥" — add the element 𝑥 to the end of the array;
# "2 𝑥 𝑦" — replace all occurrences of 𝑥 in the array with 𝑦.
# Find the resulting array after performing all the queries



cases_num = int(input("the number of queries: "))
out_array = []
for i in range(0,cases_num):
    query = str(input("query "+str(i)+": "))
    if int(query[0])==1:
        inte = int(query[2:])
        out_array.append(inte)
    elif int(query[0])==2:
        firstspace = -1
        secondspace = -1
        for i in range(0, len(query)):
            if query[i]==" ":
                if firstspace ==-1:
                    firstspace = i
                elif firstspace!=-1:
                    secondspace=i
        firstnum = int(query[firstspace+1:secondspace])
        secondnum = int(query[secondspace+1:])

        for i in range(0, len(out_array)):
            if out_array[i]==firstnum:
                out_array[i]=secondnum

print(out_array)
