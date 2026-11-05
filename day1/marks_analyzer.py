std_count = int(input("How many student? "))

ls_name = []
ls_marks = []

i= 0
while i < std_count:

    std_name = input("Enter student name: ")
    ls_name.append(std_name)
    std_marks = int(input("Enter marks: "))
    ls_marks.append(std_marks)

    i += 1 

def highMarks(lst):
    highest = lst[0]
    for i in range(len(lst)):
        if highest < lst[i]:
            highest = lst[i]

    return highest

def lowMarks(lst):
    lowest = lst[0]
    for i in range(len(lst)):
        if lowest > lst[i]:
            lowest = lst[i]

    return lowest

def std_hghMarks(lstm,lstn):
    highest = highMarks(lstm)
    std_with_hgh_mks = []

    for i in range(len(lstm)):
        if lstm[i] == highest:
            std_with_hgh_mks.append(lstn[i])

    for j in std_with_hgh_mks:
        print(j, end=" ")
    print("\n")

def avgMarks(lst):
    sum = 0
    for  i in lst:
        sum += i

    return sum / len(lst)


print("Highest Marks: ", highMarks(ls_marks))
std_hghMarks(ls_marks,ls_name)
print("Lowest Marks: ", lowMarks(ls_marks))
print("Avg Marks: ", avgMarks(ls_marks))