/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let checker = {}
    
    for (let i = 0; i < nums.length; i++) {
        const match = target - nums[i]
        // console.log('match: ', match)
        
        if (match in checker) {
            return [checker[match], i]
        }
        
        checker[nums[i]] = i
        // console.log(checker)
    }
    
    
};