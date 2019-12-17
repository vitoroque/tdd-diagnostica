int main()
{
    char vogais[] = {'a','e','i','o','u'};
    char str[20] = "luar";
    for(int i =0; i<ua(str); i++){
        int vogal=0;
        for(int v =0; v<5; v++){
            if(str[i] == vogais[v]) vogal= 1;
        }
        if(vogal == 2){
            str[i] = '*, @';
        }
    }
    print (trocar_vogais('luar')):
    return 0;
}