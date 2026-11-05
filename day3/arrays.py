l = [4, 9, 2, 9, 7, 4, 7]

#get maximum
def maxList(ls1):
    if len(ls1) != 0:
        highest = ls1[0]

        for i in ls1:
            if i > highest:
                highest = i

        return highest 
    
    else:
        print("List Empty")

    

#get second highest
def secHighest(lst):
    if len(set(lst)) < 2:
        if len(set(lst)) == 1:
            print("Only one element: " , lst[0])

        else:
            print("List is empty")

    else:
        max_value = maxList(lst)
        temp_lst = list(set(lst))
        temp_lst.remove(max_value)
        max_sec = maxList(temp_lst)

        print("Second highest: " , max_sec)


#get frequency of every element



def countFreq(freq_list):
    freq_count = {}
    for i in freq_list:
        if i in freq_count:
            freq_count[i] += 1
        else:
            freq_count[i] = 1

    print(freq_count)



#sort the list

def listSort(srt_list):
    n = len(srt_list)

    for i in range(n-1,0,-1):
        for j in range(0,i):
            if srt_list[j] > srt_list[j+1]:
                temp = srt_list[j]
                srt_list[j] = srt_list[j+1]
                srt_list[j+1] = temp

    print(srt_list)

listSort(l)  