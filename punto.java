import java.lang.Math;

public class Punto {
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double[] coord_cartesianas() {
        return new double[]{x, y};
    }

    public double[] coord_polares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan2(y, x);
        return new double[]{r, theta};
    }

    @Override
    public String toString() {
        return "Punto(x: " + x + ", y: " + y + ")";
    }

    // Ejemplo de uso
    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println(p);
        double[] cartesianas = p.coord_cartesianas();
        System.out.println("Coordenadas Cartesianas: (" + cartesianas[0] + ", " + cartesianas[1] + ")");
        double[] polares = p.coord_polares();
        System.out.println("Coordenadas Polares: (r: " + polares[0] + ", theta: " + polares[1] + ")");
    }
}
