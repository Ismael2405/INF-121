import java.util.Scanner;

public class Areas {

    // Método para el área del círculo
    public static double calcularArea(double radio) {
        return Math.PI * Math.pow(radio, 2);
    }

    // Método para el área del rectángulo
    public static double calcularArea(double base, double altura) {
        return base * altura;
    }

    // Método para el área del triángulo
    public static double calcularArea(double base, double altura, boolean esTriangulo) {
        return (base * altura) / 2;
    }

    // Método para el área del trapecio
    public static double calcularArea(double baseMayor, double baseMenor, double altura, boolean esTrapecio) {
        return ((baseMayor + baseMenor) * altura) / 2;
    }

    // Método para el área del pentágono
    public static double calcularArea(double lado, double apotema, int lados) {
        return (5 * lado * apotema) / 2;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Seleccione la figura geométrica:");
        System.out.println("1. Círculo");
        System.out.println("2. Rectángulo");
        System.out.println("3. Triángulo rectángulo");
        System.out.println("4. Trapecio");
        System.out.println("5. Pentágono");

        int opcion = scanner.nextInt();

        switch (opcion) {
            case 1: // Círculo
                System.out.print("Ingrese el radio del círculo: ");
                double radio = scanner.nextDouble();
                System.out.printf("El área del círculo es: %.2f%n", calcularArea(radio));
                break;

            case 2: // Rectángulo
                System.out.print("Ingrese la base del rectángulo: ");
                double baseRect = scanner.nextDouble();
                System.out.print("Ingrese la altura del rectángulo: ");
                double alturaRect = scanner.nextDouble();
                System.out.printf("El área del rectángulo es: %.2f%n", calcularArea(baseRect, alturaRect));
                break;

            case 3: // Triángulo
                System.out.print("Ingrese la base del triángulo: ");
                double baseTri = scanner.nextDouble();
                System.out.print("Ingrese la altura del triángulo: ");
                double alturaTri = scanner.nextDouble();
                System.out.printf("El área del triángulo es: %.2f%n", calcularArea(baseTri, alturaTri, true));
                break;

            case 4: // Trapecio
                System.out.print("Ingrese la base mayor del trapecio: ");
                double baseMayor = scanner.nextDouble();
                System.out.print("Ingrese la base menor del trapecio: ");
                double baseMenor = scanner.nextDouble();
                System.out.print("Ingrese la altura del trapecio: ");
                double alturaTra = scanner.nextDouble();
                System.out.printf("El área del trapecio es: %.2f%n", calcularArea(baseMayor, baseMenor, alturaTra, true));
                break;

            case 5: // Pentágono
                System.out.print("Ingrese el lado del pentágono: ");
                double lado = scanner.nextDouble();
                System.out.print("Ingrese la apotema del pentágono: ");
                double apotema = scanner.nextDouble();
                System.out.printf("El área del pentágono es: %.2f%n", calcularArea(lado, apotema, 5));
                break;

            default:
                System.out.println("Opción no válida. Seleccione un número entre 1 y 5.");
                break;
        }

        scanner.close();
    }
}
