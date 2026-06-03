int factorial (int n){

    if (n==0){
        return 1 ;
    }
    return n * factorial (n-1);
}

int main (){
    int resultado = factorial(6);
    printf(resultado);
    return 0;
}
