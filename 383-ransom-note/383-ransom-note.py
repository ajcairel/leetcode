class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter not in magazine:
                return False
            magazine = magazine.replace(letter, '', 1)
        return True
    
    
    # For every letter in ransomNote:
    # - if the letter is NOT in magazine, return False
    # If it is in magazine, then manipulate magazine:
    # - replace the letter with a blank
    # Continue this until all of the letters have been checked
    