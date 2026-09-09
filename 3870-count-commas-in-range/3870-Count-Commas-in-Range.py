class Solution {
    public int countCommas(int n) {
        int a=0;
        for(int i=0;i<=n;++i)
        {
            if(i>999)
           {
               a+=1;
           }
        }
        return a;
    }
}