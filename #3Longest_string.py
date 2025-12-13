def LongestString(s):
    container=[]
    max_string=0

    for i in s:

        while i in container:
            container.pop(0)

        container+=i
        max_string=max(max_string,len(container))
    return max_string

s = "abcabcbb"
print(LongestString(s))
