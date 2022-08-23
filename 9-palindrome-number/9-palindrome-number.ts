function isPalindrome(x: number): boolean {
    
    const newX = x.toString();
    
    let start = 0;
    let end = newX.length - 1;
    
    while (start < end) {
        if (newX[start] != newX[end]) {
            return false;
        } else {
            start++;
            end--;
        }
    }
    
    return true;

};