public class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.arreglo = new long[n];
        this.top = -1;
        this.n = n;
    }

    public void push(long e) {
        if (isFull()) {
            System.out.println("La pila está llena");
        } else {
            top++;
            arreglo[top] = e;
        }
    }

    public long pop() {
        if (isEmpty()) {
            System.out.println("La pila está vacía");
            return -1; // Valor de retorno indicativo de error
        } else {
            long e = arreglo[top];
            top--;
            return e;
        }
    }

    public long peek() {
        if (isEmpty()) {
            System.out.println("La pila está vacía");
            return -1; // Valor de retorno indicativo de error
        } else {
            return arreglo[top];
        }
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    // Ejemplo de uso
    public static void main(String[] args) {
        Pila pila = new Pila(5);
        pila.push(10);
        pila.push(20);
        System.out.println("Elemento en la cima: " + pila.peek());
        System.out.println("Eliminar elemento: " + pila.pop());
        System.out.println("Elemento en la cima: " + pila.peek());
    }
}
