/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let results = [];
    let sum = 0;
    
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        results.push(sum);
    }
    
    return results;
    
};