// 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
// IMPORTANTE:
// Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

import java.util.Scanner;

public class Teste02 {

    public static void main(String[] args) {

        Integer a = 0;
        Integer b = 1;
        Integer anterior = 1;

        Integer Fibonacci = a + b;

        System.out.println("Teste 02");
        System.out.println("Digite um valor:");
        Scanner scanner = new Scanner(System.in); // Cria um scanner para ler a entrada do usuário

        Integer valor = Integer.parseInt(scanner.nextLine()); // Recebe o valor digitado
        scanner.close(); // Fecha o scanner

        // System.out.println("Valor digitado: " + valor);

        while (Fibonacci <= valor) {
            if (valor.equals(Fibonacci)) {
                System.out.println("O número " + valor + " é um número de Fibonacci.");
                return;
            } else {
                Integer temp = Fibonacci;
                Fibonacci = Fibonacci + anterior;
                anterior = temp;
            }
            if (!valor.equals(Fibonacci) && Fibonacci > valor) {
                System.out.println("O número " + valor + " não é um número de Fibonacci.");
                break;
            }
        }
    }
}