class Solution {
    fun search(nums: IntArray, target: Int): Boolean {
        if (nums.size == 0) return false
        val piv = findPiv(nums, 0, nums.size-1)
        
        if (target > nums[piv]) {
            return false
        } else {
            var ret: Int
            if (target >= nums[0]) {
                ret = nums.binarySearch(target, 0, piv+1)
            } else {
                ret = nums.binarySearch(target, piv+1, nums.size)
            }
            return if (ret >= 0) true else false
        }
    }
    
    fun findPiv(nums: IntArray, left: Int, right: Int): Int {
        if (left >= right) {
            return left
        }
        
        var l: Int = left
        var r: Int = right
        var ret: Int = left
        while (l < r) {
            if (l + 1 == r) {
                if (nums[l] > nums[r]) {
                    ret = l
                    break
                } else {
                    ret = r
                    break
                }
            }
            
            var mid: Int = (l + r) / 2
            if (nums[l] < nums[mid]) {
                l = mid
            } else if (nums[l] > nums[mid]){
                r = mid
            } else {
                if (nums[l] != nums[r]) {
                    l = mid
                } else {
                    if (maybeOnLeft(nums, l, mid)) {
                        r = mid  
                    } else {
                        l = mid
                    }
                }
            }
        }
        return ret
    }
    
    fun maybeOnLeft(nums: IntArray, left: Int, right:Int): Boolean {
        for (i in left until right+1) {
            if (nums[i] != nums[left]) return true
        }
        return false
    }
}