from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

# Transactions endpoints
@api.route('/transactions', methods=['GET', 'POST'])
def manage_transactions():
    if request.method == 'GET':
        return jsonify({"message": "List of transactions"})
    elif request.method == 'POST':
        return jsonify({"message": "Transaction created"})

# Budgets endpoints
@api.route('/budgets', methods=['GET', 'POST'])
def manage_budgets():
    if request.method == 'GET':
        return jsonify({"message": "List of budgets"})
    elif request.method == 'POST':
        return jsonify({"message": "Budget created"})

# Contributions endpoints
@api.route('/contributions', methods=['GET', 'POST'])
def manage_contributions():
    if request.method == 'GET':
        return jsonify({"message": "List of contributions"})
    elif request.method == 'POST':
        return jsonify({"message": "Contribution created"})

# Reports endpoints
@api.route('/reports', methods=['GET'])
def get_reports():
    return jsonify({"message": "List of reports"})

# Accounts endpoints
@api.route('/accounts', methods=['GET', 'POST'])
def manage_accounts():
    if request.method == 'GET':
        return jsonify({"message": "List of accounts"})
    elif request.method == 'POST':
        return jsonify({"message": "Account created"})

# Members endpoints
@api.route('/members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'GET':
        return jsonify({"message": "List of members"})
    elif request.method == 'POST':
        return jsonify({"message": "Member created"})