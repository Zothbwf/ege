class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        triples = []
        for k in range(1,len(nums)-1):
            i = k+1
            j = len(nums) - 1    
            while i != k and j != k:
                triple = [nums[i],nums[k],nums[j]]
                if nums[i] + nums[j] + nums[k] == 0 and triple not in triples:
                        triples.append(triple)
                        i += 1
                        j -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i +=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j -=1
                else:
                    break
        return triples
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sorted([3,0,-2,-1,1,2]))