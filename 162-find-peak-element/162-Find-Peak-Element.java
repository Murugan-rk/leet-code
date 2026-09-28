int findPeakElement(int* nums, int numsSize) {
    int i;
    int max=nums[0];
    for(i=1;i<numsSize;i++)
    {
        if(nums[i]>max)
        {
            max=nums[i];
        }
    }
    for(i=0;i<numsSize;i++)
    {
        if(nums[i]==max)
        {
            return i;
        }
    }
    return 0;
}