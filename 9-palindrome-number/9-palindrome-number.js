/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    let newX = x.toString();
    
    console.log(newX);
    
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