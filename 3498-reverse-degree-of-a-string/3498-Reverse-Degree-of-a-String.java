class Solution {
    public int reverseDegree(String s) {
        int sum=0;
        for(int i=0;i<s.length();i++)
        {
            char o=s.charAt(i);
            int v=rev(o);
            sum=sum+(v*(i+1));
        }
        return sum;
    }
    public int rev(char a)
    {
        return 'z'-a+1;
    }
}