package lcg;

/** Fórmula del Generador Congruencial Lineal especificada en la APE 05. */
final class GeneradorLCG {
    static final long MODULO = 1L << 32; // 2^32.
    private static final long MULTIPLICADOR = 1664525L;
    private static final long INCREMENTO = 1013904223L;

    private long estado;

    GeneradorLCG(long semilla) {
        estado = semilla; // X_0.
    }

    long siguiente() {
        // Se utiliza long para evitar el desbordamiento de los int de Java.
        estado = (MULTIPLICADOR * estado + INCREMENTO) % MODULO;
        return estado;
    }

    static double normalizar(long valor) {
        return (double) valor / MODULO;
    }
}
