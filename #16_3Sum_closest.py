def the_three_closest(lists,target):
    lists.sort()
    the_closest_sum=float('inf')

    for i in range(len(lists)-2):
        left, right= i+1, len(lists)-1

        while left<right:
            the_current_sum=lists[i] + lists[left] +lists[right]

            if abs(target-the_current_sum) < abs(target - the_closest_sum):
                the_closest_sum=the_current_sum

            if the_current_sum<target:
                left+=1
            elif the_current_sum> target:
                right-=1
            else:
                return the_current_sum
    return the_closest_sum

print(the_three_closest([-1, 2, 1,-4], 1))

