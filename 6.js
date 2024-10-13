/*
My solution to the 6 LeetCode's problem in Javascript.

Runtime: 81 ms
Allocated memory: 54.73 MB
Complexity: O(n)

https://leetcode.com/problems/zigzag-conversion/description/
*/

/*
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = (s, numRows) => {
    var zigzagStrings = Array(numRows).fill('');
    var row = -1;
    var up = false;
    for (let c of s) {
        if (numRows == 1){
            row = 0;
        } else {
            row += up ? -1 : 1;
        }
        
        zigzagStrings[row] = `${zigzagStrings[row]}${c}`;
        if (!up && row >= numRows-1){
            up = true;
        } else if (up && row <= 0) {
            up = false;
        }
    }

    return zigzagStrings.join('');
};