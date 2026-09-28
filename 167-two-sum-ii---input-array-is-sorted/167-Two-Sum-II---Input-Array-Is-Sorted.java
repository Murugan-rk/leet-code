/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    if (result == NULL) {
        return NULL;
    }
    int i;
    int l=0,r=numbersSize-1;
    while(l<r)
    {
        int sum=numbers[r]+numbers[l];
        if(sum==target)
        {
            result[0]=l+1;
            result[1]=r+1;
            *returnSize = 2;
            return result;
        }
        else if(sum<target)
        {
            l++;
        }
        else
        {
            r--;
        }
    }
    *returnSize = 0;
    return NULL;
}