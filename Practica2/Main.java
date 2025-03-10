import java.awt.*;
import javax.swing.*;

class Punto {
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
}

class Linea {
    private Punto p1;
    private Punto p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    @Override
    public String toString() {
        return "Linea[p1=" + p1 + ", p2=" + p2 + "]";
    }

    public void dibujaLinea(Graphics g) {
        g.drawLine((int) p1.coord_cartesianas()[0], (int) p1.coord_cartesianas()[1],
                   (int) p2.coord_cartesianas()[0], (int) p2.coord_cartesianas()[1]);
    }
}

class Circulo {
    private Punto centro;
    private double radio;

    public Circulo(Punto centro, double radio) {
        this.centro = centro;
        this.radio = radio;
    }

    @Override
    public String toString() {
        return "Circulo[centro=" + centro + ", radio=" + radio + "]";
    }

    public void dibujaCirculo(Graphics g) {
        int x = (int) (centro.coord_cartesianas()[0] - radio);
        int y = (int) (centro.coord_cartesianas()[1] - radio);
        int diametro = (int) (2 * radio);
        g.drawOval(x, y, diametro, diametro);
    }
}

public class Main extends JPanel {
	private static final long serialVersionUID = 1L;
	private Circulo circulo;
    private Linea linea;

    public Main() {
        Punto p1 = new Punto(100, 100);
        Punto p2 = new Punto(200, 200);
        linea = new Linea(p1, p2);
        Punto centro = new Punto(150, 150);
        circulo = new Circulo(centro, 50);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        circulo.dibujaCirculo(g);
        linea.dibujaLinea(g);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame();
        Main panel = new Main();
        frame.add(panel);
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
