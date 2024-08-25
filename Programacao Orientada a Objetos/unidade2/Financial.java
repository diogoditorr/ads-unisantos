package unidade2;

import unidade2.Enums.AccountType;

public class Financial {
    public static void main(String[] args) {
        Financial.percentOf(0, 0);
        System.out.println(percentOf(12, 20));

        var bankAccount = new BankAccount(100.0, 12, AccountType.PessoaFisica);
        
        System.out.println("Balanço da conta: " + bankAccount.balance);
        System.out.println("Tipo da conta: " + bankAccount.accountType);
    }

    public static double percentOf(double percent, double value)
    {
        return (percent / 100) * value;
    }    
}
