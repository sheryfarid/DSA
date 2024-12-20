def relativerank(score):
    indexed_score = [(s, i) for i, s in enumerate(score)]
    
    indexed_score.sort(reverse=True, key=lambda x: x[0])  
    
    result = [None] * len(score)
    
    for rank, (s, i) in enumerate(indexed_score):
        if rank == 0:
            result[i] = "Gold Medal"
        elif rank == 1:
            result[i] = "Silver Medal"
        elif rank == 2:
            result[i] = "Bronze Medal"
        else:
            result[i] = str(rank + 1)  
    
    return result

score = [10, 3, 8, 9, 4]
print(relativerank(score))



def isAnagram(s, t) :
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))  
print(isAnagram("silent", "listen"))          