class Solution(object):
    def topKFrequent(self, nums, k):
        nums.sort()
        
        buckets, bucket, cnt = [], None, 1
        while nums:
            thisBucket = nums.pop(0) 
            if thisBucket != bucket and bucket is not None:
                bisect.insort_left(buckets, [cnt, bucket])
                cnt = 1
            else:
                cnt += 1
            bucket = thisBucket
        bisect.insort_left(buckets, [cnt, bucket])
        
        item, ret = 0, []
        while item < k and buckets: 
            ret.append(buckets.pop()[1])
            item += 1
        return ret

        
