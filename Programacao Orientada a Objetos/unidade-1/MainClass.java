import javax.swing.JOptionPane;

public class MainClass {
    static class Hospital {
        public String nome;
        public int capacidade;
        public boolean possuiUTI;

        public Hospital(String nome, int capacidade, boolean possuiUTI) {
            this.nome = nome;
            this.capacidade = capacidade;
            this.possuiUTI = possuiUTI;
        }

        public void realizarAtendimento(String paciente) {
            System.out.println("O paciente " + paciente + " está sendo atendido no hospital " + nome);
        }

        public void adicionarLeito() {
            capacidade++;
            System.out.println("Foi adicionado mais um leito ao hospital " + nome);
        }

        public void verificarDisponibilidadeUTI() {
            if (possuiUTI) {
                System.out.println("O hospital " + nome + " possui UTI");
            } else {
                System.out.println("O hospital " + nome + " não possui UTI");
            }
        }
    }

    public static void main(String[] args) {
        Hospital hospital = new Hospital("Hospital ABC", 100, true);
        System.out.println(String.format("Nome do hospital: %s", hospital.nome));
        System.out.println(String.format("Capacidade do hospital: %s", hospital.capacidade));

        hospital.realizarAtendimento("João");
        hospital.adicionarLeito();
        hospital.verificarDisponibilidadeUTI();

        hospital.nome = "Hospital Santo Antônio";
        hospital.capacidade = 152;
        hospital.possuiUTI = false;

        System.out.println(String.format("Novo nome do hospital: %s", hospital.nome));
        System.out.println(String.format("Nova capacidade do hospital: %s", hospital.capacidade));
        hospital.verificarDisponibilidadeUTI();
        JOptionPane.showMessageDialog(null, "Teste mensagem", "Titutlo", 1);

    }
}
