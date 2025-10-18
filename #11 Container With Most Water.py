

def max_area(heights):
    max_area_of_water=0
    left=0
    right=len(heights)-1

    while left < right:
        width=right-left
        height=min(heights[left],heights[right])
        new_area=width*height

        if new_area > max_area_of_water:
            max_area_of_water=new_area

        if heights[left] <heights[right]:
            left+=1
        else:
            right-=1
    return max_area_of_water

print(max_area([1,1]))