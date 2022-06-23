/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = (prices) => {
    
    let left = 0;
    let right = 1;
    let maxProfit = 0;
    while (right < prices.length) {
        let currentProfit = prices[right] - prices[left]
        if (prices[left] < prices[right]) {
            maxProfit = Math.max(maxProfit, currentProfit)
        }
        else {
            left = right;
        }
        right += 1
    }
    return maxProfit;
    
};

    
