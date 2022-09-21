function twoSum(nums: number[], target: number): number[] {
    
    
    let dic = {}
    
    for (let i = 0; i < nums.length; i++){
        const match = target - nums[i]
        
        if (match in dic){
            return [dic[match], i]
        } else {
            dic[nums[i]] = i
        }
    }

};