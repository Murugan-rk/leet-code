int hammingDistance(int x, int y) {
    int r=x^y;
    int i,count=0;
    char buffer[33];
    for (int i = 31; i >= 0; i--) {
        int bit = (r>> i) & 1;
        buffer[i]=bit+'0';
        }
        buffer[32]='\0';
       for(i=0;i<strlen(buffer);i++)
       {
        if(buffer[i]=='1')
        {
            count++;
        }
       }
       return count;
}