def count_vowels(s):
    count=0
    for ch in s:
        if ch in 'aeiouAEIOU':
            count+=1
    print("Count of vowels=",count)
count_vowels("Hello World")