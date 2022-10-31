class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.money = 0

    def deposit(self,amount,description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.money += amount

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.money -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.money

    def transfer(self,amount,another_category):
        if self.check_funds(amount):
            self.withdraw(amount,'Transfer to '+another_category.name)
            another_category.deposit(amount,'Transfer from '+self.name)
            return True
        else:
            return False

    def check_funds(self,amount):
        return not amount>self.money

    def __str__(self):
        max_length = max([min(len(i['description']),23)+min(len('%.2f'%i['amount']),7)+1 for i in self.ledger])
        output = '*'*int((30-len(self.name))/2)+self.name+'*'*int((30-len(self.name))/2)+'\n'
        for i in self.ledger:
            description = i['description'] if len(i['description'])<23 else i['description'][:23]
            amount = '%.2f'%i['amount'] if len('%.2f'%i['amount'])<7 else ('%.2f'%i['amount'])[:7]
            output += description+' '*(max_length-len(description)-len(amount))+amount+'\n'
        output += 'Total: %.2f'%self.money
        return output
        
def create_spend_chart(categories):
    output = 'Percentage spent by category\n'
    empty_chart = [list('%3d'%(10*(10-i))+'| '+'   '*len(categories)+'\n') for i in range(11)]
    sum_spend = sum([-j['amount'] for i in categories for j in i.ledger if j['amount']<0])
    for i,j in enumerate(categories):
        spend = sum([-k['amount'] for k in j.ledger if k['amount']<0])
        percent = int(spend/sum_spend*10)
        for k in range(percent+1):
            empty_chart[10-k][5+i*3] = 'o'
    output += ''.join([''.join(i) for i in empty_chart])+'    '+'-'*(1+len(categories)*3)+'\n'
    max_name_length = max([len(i.name) for i in categories])
    empty_name = [list(' '*(5+len(categories)*3)).copy() for i in range(max_name_length)]
    for i in range(max_name_length):
        for j,k in enumerate(categories):
            if i<len(k.name):
                empty_name[i][5+j*3] = k.name[i]
    output += '\n'.join([''.join(i) for i in empty_name])
    return output