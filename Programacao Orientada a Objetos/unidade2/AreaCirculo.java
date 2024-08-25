package unidade2;

public class AreaCirculo {
    static private double pi = Math.PI;
    private double raio;
    private double area;

    public void setRaio(double raio) {
        this.raio = raio;
        area = pi * (raio * raio);
    }

    public double getArea() {
        return area;
    }

    public double getPi() {
        return pi;
    }
}
