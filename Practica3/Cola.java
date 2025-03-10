public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int numeroElementos;

    public Cola(int n) {
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;
        this.n = n;
        this.numeroElementos = 0;
    }

    public void insert(long e) {
        if (isFull()) {
            System.out.println("La cola está llena");
        } else {
            fin = (fin + 1) % n;
            arreglo[fin] = e;
            numeroElementos++;
        }
    }

    public long remove() {
        if (isEmpty()) {
            System.out.println("La cola está vacía");
            return -1; // Valor de retorno indicativo de error
        } else {
            long e = arreglo[inicio];
            inicio = (inicio + 1) % n;
            numeroElementos--;
            return e;
        }
    }

    public long peek() {
        if (isEmpty()) {
            System.out.println("La cola está vacía");
            return -1; // Valor de retorno indicativo de error
        } else {
            return arreglo[inicio];
        }
    }

    public boolean isEmpty() {
        return numeroElementos == 0;
    }

    public boolean isFull() {
        return numeroElementos == n;
    }

    public int size() {
        return numeroElementos;
    }

    // Ejemplo de uso
    public static void main(String[] args) {
        Cola cola = new Cola(5);
        cola.insert(10);
        cola.insert(20);
        System.out.println("Elemento en la parte delantera: " + cola.peek());
        System.out.println("Eliminar elemento: " + cola.remove());
        System.out.println("Elemento en la parte delantera: " + cola.peek());
    }
}
