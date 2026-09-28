int findMin(int* nums, int numsSize) {
    int min=nums[0];
    int i;
    for(i=1;i<numsSize;i++)
    {
        if(min>nums[i])
        {
            min=nums[i];
        }
    }
    return min;
}