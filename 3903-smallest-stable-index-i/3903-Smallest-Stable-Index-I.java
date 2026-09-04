class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int st;
        int max;
        int min;
        if(nums.length==1)
        {
            return 0;
        }
        for(int i=0;i<nums.length;i++)
        {
            max = nums[i];
            min = nums[i];
            for(int j=0;j<i;j++)
            {
               max=Math.max(max,nums[j]);
            }
            for(int j=i;j<nums.length;j++)
            {
                min=Math.min(min,nums[j]);
            }
            st=max-min;
            if(st<=k)
            {
                return i;
            }
        }
        return -1;
    }
}