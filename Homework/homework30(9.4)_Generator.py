def all_variants(word):
    for i in range(1, len(word)+1):
        for j in range(len(word)-i+1):
            yield word[j:j+i]


a = all_variants("abc")
for i in a:
    print(i)
