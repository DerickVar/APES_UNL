package lcg;

/** Coordina el generador; --secuencia permite comparar por stdout con Python. */
public final class Main {
    private static final long SEMILLA_INICIAL = 12345L;
    private static final int CANTIDAD = 10_000;

    private Main() {
    }

    private static long leerSemilla(String[] args) {
        if (args.length == 0) {
            return SEMILLA_INICIAL;
        }
        if ((args.length != 2 && args.length != 3) || !"--semilla".equals(args[0])
                || (args.length == 3 && !"--secuencia".equals(args[2]))) {
            throw new IllegalArgumentException(
                "Uso: java -jar lcg-java-1.0.0.jar [--semilla ENTERO [--secuencia]]");
        }
        long semilla = Long.parseLong(args[1]);
        if (semilla < 0 || semilla >= GeneradorLCG.MODULO) {
            throw new IllegalArgumentException("La semilla debe estar entre 0 y 4294967295.");
        }
        return semilla;
    }

    private static void ejecutar(long semilla, boolean secuenciaCompleta) {
        GeneradorLCG generador = new GeneradorLCG(semilla);
        if (!secuenciaCompleta) {
            System.out.println("n X_n U_n (primeras 20 observaciones)");
        }
        for (int n = 1; n <= CANTIDAD; n++) {
            long x = generador.siguiente();
            double u = GeneradorLCG.normalizar(x);
            if (secuenciaCompleta || n <= 20) {
                System.out.println(n + " " + x + " " + Double.toString(u));
            }
        }
        if (!secuenciaCompleta) {
            System.out.printf("Java: %d observaciones generadas con semilla %d.%n", CANTIDAD, semilla);
        }
    }

    public static void main(String[] args) {
        try {
            long semilla = leerSemilla(args);
            ejecutar(semilla, args.length == 3);
        } catch (IllegalArgumentException ex) {
            System.err.println(ex.getMessage());
            System.exit(1);
        }
    }
}
