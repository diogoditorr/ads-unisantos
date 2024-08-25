package unidade2;

import unidade2.Enums.AccountType;

public class BankAccount {
    public double balance;
    public int accountNumber;
    public AccountType accountType;
    private static int lastAssignedNumber = 1000;
    public static final double OVERDRAFT_FEE = 5;

    public BankAccount(double balance, int accountNumber, AccountType accountType)
    {
        lastAssignedNumber++;

        accountNumber = lastAssignedNumber;
        this.balance = balance;
        this.accountNumber = accountNumber;
        this.accountType = accountType;
    }
}
