/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package arquitetura.de.sistemas;

public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());

        Celular celular = new Celular("oi");
        System.out.println(celular.nome);
    }
}