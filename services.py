from models import User, Member, Account, Transaction, Budget, Contribution
from datetime import datetime, timedelta

class TransactionService:
    """Service for managing transactions (income and expenses)"""
    
    @staticmethod
    def record_income(account_id, amount, category, description, member_id=None):
        """Record income transaction"""
        transaction = Transaction(
            account_id=account_id,
            amount=amount,
            transaction_type='income',
            category=category,
            description=description,
            member_id=member_id,
            transaction_date=datetime.utcnow()
        )
        return transaction
    
    @staticmethod
    def record_expense(account_id, amount, category, description, member_id=None):
        """Record expense transaction"""
        transaction = Transaction(
            account_id=account_id,
            amount=amount,
            transaction_type='expense',
            category=category,
            description=description,
            member_id=member_id,
            transaction_date=datetime.utcnow()
        )
        return transaction
    
    @staticmethod
    def get_transaction_history(account_id, start_date=None, end_date=None):
        """Get transaction history for an account"""
        if not start_date:
            start_date = datetime.utcnow() - timedelta(days=30)
        if not end_date:
            end_date = datetime.utcnow()
        
        return {
            'account_id': account_id,
            'start_date': start_date,
            'end_date': end_date,
            'transactions': []
        }


class BudgetService:
    """Service for managing budgets and budget tracking"""
    
    @staticmethod
    def create_budget(account_id, category, amount, period, start_date, end_date):
        """Create a new budget"""
        budget = Budget(
            account_id=account_id,
            category=category,
            budget_amount=amount,
            period=period,
            start_date=start_date,
            end_date=end_date
        )
        return budget
    
    @staticmethod
    def check_budget_status(budget_id, spent_amount):
        """Check if budget is within limits"""
        if spent_amount > 0:
            percentage = (spent_amount / budget_id) * 100 if budget_id > 0 else 0
            return {
                'budget_id': budget_id,
                'spent_amount': spent_amount,
                'percentage_used': percentage,
                'status': 'warning' if percentage > 80 else 'ok',
                'exceeded': spent_amount > budget_id
            }
        return {'status': 'ok', 'exceeded': False}


class ContributionService:
    """Service for managing member contributions and cotisations"""
    
    @staticmethod
    def create_contribution(member_id, amount, due_date):
        """Create a new contribution"""
        contribution = Contribution(
            member_id=member_id,
            amount=amount,
            due_date=due_date,
            status='pending'
        )
        return contribution
    
    @staticmethod
    def mark_contribution_paid(contribution_id, payment_date):
        """Mark contribution as paid"""
        return {
            'contribution_id': contribution_id,
            'status': 'paid',
            'payment_date': payment_date
        }
    
    @staticmethod
    def get_overdue_contributions(member_id):
        """Get overdue contributions for a member"""
        current_date = datetime.utcnow()
        return {
            'member_id': member_id,
            'current_date': current_date,
            'overdue_contributions': []
        }


class ReportService:
    """Service for generating financial reports"""
    
    @staticmethod
    def generate_income_report(account_id, start_date, end_date):
        """Generate income report for a period"""
        return {
            'account_id': account_id,
            'period': f'{start_date} to {end_date}',
            'total_income': 0,
            'income_by_category': {}
        }
    
    @staticmethod
    def generate_expense_report(account_id, start_date, end_date):
        """Generate expense report for a period"""
        return {
            'account_id': account_id,
            'period': f'{start_date} to {end_date}',
            'total_expenses': 0,
            'expenses_by_category': {}
        }
    
    @staticmethod
    def generate_financial_summary(account_id):
        """Generate overall financial summary"""
        return {
            'account_id': account_id,
            'total_balance': 0,
            'total_income': 0,
            'total_expenses': 0,
            'net_balance': 0
        }
    
    @staticmethod
    def generate_member_report(member_id):
        """Generate report for a specific member"""
        return {
            'member_id': member_id,
            'total_contributions': 0,
            'paid_contributions': 0,
            'pending_contributions': 0,
            'overdue_contributions': 0
        }


class AccountService:
    """Service for managing accounts"""
    
    @staticmethod
    def get_account_balance(account_id):
        """Get current balance of an account"""
        return {
            'account_id': account_id,
            'balance': 0,
            'last_updated': datetime.utcnow()
        }
    
    @staticmethod
    def update_account_balance(account_id, amount):
        """Update account balance"""
        return {
            'account_id': account_id,
            'new_balance': amount,
            'updated_at': datetime.utcnow()
        }