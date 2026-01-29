-- SQL schema for Treasury Management System

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(255) NOT NULL,
    account_balance DECIMAL(15, 2) NOT NULL
);

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_date DATETIME NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type ENUM('credit', 'debit') NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

CREATE TABLE Budgets (
    budget_id INT PRIMARY KEY,
    account_id INT,
    budget_amount DECIMAL(15, 2) NOT NULL,
    budget_period VARCHAR(50) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') NOT NULL
);