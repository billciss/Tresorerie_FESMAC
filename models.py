from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime)

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    joined_at = Column(DateTime)
    user = relationship('User', back_populates='members')

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    balance = Column(Float, default=0.0)
    member = relationship('Member', back_populates='accounts')

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Float)
    transaction_date = Column(DateTime)
    account = relationship('Account', back_populates='transactions')

class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    amount = Column(Float)
    due_date = Column(DateTime)
    member = relationship('Member', back_populates='budgets')

class Contribution(Base):
    __tablename__ = 'contributions'
    id = Column(Integer, primary_key=True)
    budget_id = Column(Integer, ForeignKey('budgets.id'))
    amount = Column(Float)
    contribution_date = Column(DateTime)
    budget = relationship('Budget', back_populates='contributions')

User.members = relationship('Member', order_by=Member.id, back_populates='user')
Member.accounts = relationship('Account', order_by=Account.id, back_populates='member')
Account.transactions = relationship('Transaction', order_by=Transaction.id, back_populates='account')
Member.budgets = relationship('Budget', order_by=Budget.id, back_populates='member')
Budget.contributions = relationship('Contribution', order_by=Contribution.id, back_populates='budget')