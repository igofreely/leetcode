class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        all=0
        sum=0
        ans=0
        for i in range(len(satisfaction)-1,-1,-1):
            all+=sum+satisfaction[i]
            ans=max(all,ans)
            sum+=satisfaction[i]
        return ans
