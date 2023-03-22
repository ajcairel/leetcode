class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return Counter(s) == Counter(t) 
        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        
        chars = {}
        
        for c in s:
            chars[c] = chars.get(c, 0) + 1
            
        for c in t:
            if c not in chars:
                return False
            else:
                chars[c] -= 1
                
        for val in chars.values():
            if val != 0:
                return False
        
        return True

      
        

    
    #1 if they aren't the same length, can't be anagrams
    
    #2 count up occurances of each letter in one of the words, put in 'counter'
    
    #3 compare letters of second word with counter, if it's in there subtract from the letter count, if it's not return False because not an anagram at that point
    
    #4 if there are any letters with the count of 1, not a valid anagram. A valid anagram would have meant that all counts were subtracted to 0 
    


            
            
        
                 

      