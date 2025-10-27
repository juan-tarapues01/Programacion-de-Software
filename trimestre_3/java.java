class Producto {
    String nombre;
    double precio;
    String tipoProducto;

    Producto(String nombre, double precio, String tipoProducto) {
        this.nombre = nombre;
        this.precio = precio;
        this.tipoProducto = tipoProducto;
    }

    String mostrarInfo() {
        return nombre + " - $" + precio + " (Tipo: " + tipoProducto + ")";
    }
}

class Cliente {
    String nombre, correo;

    Cliente(String nombre, String correo) {
        this.nombre = nombre;
        this.correo = correo;
    }

    void verProductos(Producto[] productos) {
        System.out.println("Productos disponibles:");
        for (Producto p : productos) {
            System.out.println(p.mostrarInfo());
        }
    }
}

class Pedido extends Cliente {
    Producto[] lista;
    Pedido(String nombre, String correo, Producto[] lista) {
        super(nombre, correo);
        this.lista = lista;
    }

    double calcularTotal() {
        double total = 0;
        for (Producto p : lista) total += p.precio;
        return total;
    }

    void mostrarPedido() {
        System.out.println("\nPedido de " + nombre + ":");
        for (Producto p : lista)
            System.out.println("- " + p.nombre);
        System.out.println("Total a pagar: $" + calcularTotal());
    }
}

public class TiendaOnline {
    public static void main(String[] args) {
        Producto p1 = new Producto("Celular", 900, "Tecnología");
        Producto p2 = new Producto("Audífonos", 100, "Accesorios");
        Producto[] lista = {p1, p2};

        Pedido pedido = new Pedido("Juan", "juan@mail.com", lista);
        pedido.verProductos(lista);
        pedido.mostrarPedido();
    }
}