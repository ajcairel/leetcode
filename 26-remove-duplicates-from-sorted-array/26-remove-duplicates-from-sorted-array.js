/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
//     let i = 0;
    
//     for (let j = 0; j < nums.length; j++) {
//         if (nums[j] != nums[i]) {
//             nums[++i] = nums[j]
//         }
//     }
    
//     return ++i;
    
    let x = 1;
    
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] != nums[i+1]){
            nums[x] = nums[i+1];
            x++;
        }
    }
    
    return x;
    
};