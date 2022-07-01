/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t){
    let arr1 = [];
    let arr2 = [];
    
    for (let i = 0; i < s.length; i++){
        arr1.push(s.indexOf(s[i]));
        arr2.push(t.indexOf(t[i]));
    }
    
    return arr1.toString() === arr2.toString();
}