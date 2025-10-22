def fourSum(list,target):
    list.sort()
    collection=[]

    for i in range(len(list)-3):
        if i > 0 and list[i] == list[i - 1]:
            continue
        for j in range(i+1,len(list) - 2):
            if j>i+1 and list[j]==list[j-1]:
                continue
            left,right=j+1,len(list)-1

            while left< right:
                result=list[i] +list[j] + list[left] + list[right]

                if result==target:
                    collection.append([list[i],list[j],list[left],list[right]])

                    left+=1
                    right-=1

                    while left < right and list[left]==list[left-1]:
                        left+=1
                    while left < right and list[right]==list[right+1]:
                        right-=1

                elif result > target:
                    right-=1
                else:
                    left+=1
    return collection




nums = [1,0,-1,0,-2,2]
aa=fourSum(nums,0)
print(aa)