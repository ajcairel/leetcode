/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {

   const check = new Set(nums);
    
    if (check.size === nums.length) {
        return false;
    }
    
    return true;
   
    
};