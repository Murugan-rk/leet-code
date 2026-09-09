class Solution {
    public long countCommas(long n) {
       int a=0;
       int limit=1000;
       while(n>=limit)
       {
        a+=(n-limit+1);
        if (limit>Long.MAX_VALUE/1000) {
                break;
            }
            limit*= 1000;
       }
       return a;
    }
}