class Solution {
    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
        var table = hashMapOf<String, List<Int>>()
        nums.sort()
        addOne(nums, 0, emptyArray<Int>(), table)
        
        var ret = mutableListOf<List<Int>>()
        for ((key, value)  in table) {
            ret.add(value)
        }
        return ret
    }
    
    fun addOne(nums: IntArray, pos: Int, comb: Array<Int>, table: HashMap<String, List<Int>>) {
        
        if (pos >= nums.size) {
            if (!table.containsKey(Arrays.toString(comb))) {
                table.put(Arrays.toString(comb), comb.toList())
            }
            return
        }
        
        for (i in pos until nums.size+1) {
            if (i < nums.size) {
                addOne(nums, i+1, comb+arrayOf<Int>(nums[i]), table)
            }
            else {
                addOne(nums, i+1, comb, table)
            }
        }
    }
}