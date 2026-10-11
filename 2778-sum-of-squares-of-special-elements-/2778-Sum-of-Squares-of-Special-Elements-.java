class Solution {
    public int sumOfSquares(int[] nums) {
        int n=nums.length;
        System.out.println(n);
        int sum=0;
        int j=1;
        for(int i=0;i<n;i++)
        {
            if(n%j==0)
            {
             sum+=Math.pow(nums[i],2);
             j++;
            }
            else
            {
            j++;
            }
        }
        return sum;
    }
}