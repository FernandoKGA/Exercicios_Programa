import java.io.IOException;
import java.util.Scanner;
//import java.lang.Math
/*
    Problema retirado do site URIOnlineJugde: https://www.urionlinejudge.com.br/judge/pt/problems/view/1002
    "Problem taken from: (see the version for your language)"
*/

public class AreaDoCirculo {
 
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        final double pi = 3.14159;
        double raio = in.nextDouble();
        in.close();
        double area = pi * raio * raio;  //função pow da biblioteca Math também pode ser usada
        System.out.printf("A=%.4f\n",area);     //função printf permite modular a precisão
    }
}