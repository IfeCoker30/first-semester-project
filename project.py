import uuid
from datetime import datetime, timezone

#create an Expense class
class Expense:
    def __init__(self, title: str, amount: float):
#Initialize an Expense instance with a unique ID, title, amount, and timestamps.
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc) #store UTC timestamp
        self.updated_at = self.created_at

    def update(self, title =None, amount = None):
        #update on the title and amount parameters will update the timestamp
        if title:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)
        
    def to_dict(self):
        #a dictionary rep of the expense
        dictrep = {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() 
        }
        return dictrep

class ExpenseDB:
    def __init__(self):
        self.expenses = {}
    def add_expense(self, expense: Expense):
        #Adds an expense object
        self.expenses[expense.id] = expense
    def remove_expense(self, expense_id):
        return self.expenses.pop(expense_id, None) is not None
    def get_expense_by_id(self, expense_id):
        return self.expenses.get(expense_id)
    def get_expense_by_title(self, title):
        matching_expenses = []
        for expense in self.expenses.values():
            if expense.title == title:
                matching_expenses.append(expense)
        return matching_expenses
    def to_dict(self):
        all_expenses = []
        for expense in self.expenses.values():
            all_expenses.append(expense.to_dict())
        return all_expenses