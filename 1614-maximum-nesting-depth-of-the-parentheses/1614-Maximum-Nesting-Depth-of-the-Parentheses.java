class Solution {
    public int maxDepth(String s) {
        int o=0;
        int dep=0;
        for(char c : s.toCharArray())
        {
            if(c=='(')
            {
                dep++;
                o=Math.max(o,dep);
            }
            else if(c==')')
            {
                dep--;
            }
        }
        return o;
    }
}