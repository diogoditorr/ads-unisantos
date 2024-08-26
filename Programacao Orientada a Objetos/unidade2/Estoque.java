package unidade2;

public class Estoque {
    private String produto;
    private double valor;
    static int disponibilidadeEstoque = 10;

    public Estoque(int qtde) {
        int ret = verificaDisponibilidade(qtde);

        if (ret == 1) {
            removerProdutos(qtde);
        } else {
            System.out.println("Sem estoque suficiente");
        }
    }

    private void removerProdutos(int qtde) {
        disponibilidadeEstoque -= qtde;
        System.out.println(disponibilidadeEstoque);
    }

    private int verificaDisponibilidade(int qtde) {
        if (disponibilidadeEstoque >= qtde) {
            return 1;
        } else {
            return 0;
        }
    }
}
