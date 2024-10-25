/*
My solution to the 1233 LeetCode's problem in Javascript.

Runtime: 37 ms
Allocated memory: 65.7 MB
Complexity: O(n log n)

https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
*/

/**
 * @param {string[]} folder
 * @return {string[]}
 */
var removeSubfolders = function(folder) {
    folder.sort();
    var folders = [folder[0]];
    var last = 0;
    for (f of folder) {
        if (f == folders[last] || f.startsWith(`${folders[last]}/`))
            continue;
        folders.push(f);
        last++;
    }
    return folders;
};