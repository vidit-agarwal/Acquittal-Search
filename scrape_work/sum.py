
def tag_count(list) :
    global count
    count=0
    for i in list :
        if i[0] =='<' and i[-1] =='>' :
            count +=1

    return count

list=['<greetings>', 'hello' , '</br>']
print(tag_count(list))


a = [  ['a'] , ['b'] , ['c'] , ['d'] , ['b'] ]
b= set()
for i in a :
    for j in i :
        b.add(j)

print(b)
