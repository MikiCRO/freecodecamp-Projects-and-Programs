from itertools import zip_longest

class Category:
 
 def __init__(self,name):
   self.name = name
   #print(self.name)
   self.ledger = list()

 def deposit(self,amount,description = ""):
  self.ledger.append({"amount": amount, "description": description})
    
 def withdraw(self,amount,description = ""):
  if self.check_funds(amount) is False:
    return False
   
  else:
    self.ledger.append({"amount": -amount, "description": description})
    return True
    
 def get_balance(self)-> float:
  myBalance = 0
  for item in self.ledger:
    myBalance += item["amount"]
  print(myBalance)
  return myBalance
  
 def transfer(self,amount,budget):
   if self.check_funds(amount) is False:
    
    return False
   else:
    print(budget.name) 
    self.withdraw(amount,f"Transfer to {budget.name}")
    budget.deposit(amount,f"Transfer from {self.name}")
    print(budget.name) 
    return True 

 def check_funds(self,amount):
  if amount > self.get_balance():
    return False
  else:
    return True

 def __str__(self):
  title = f"{self.name:*^30}\n"
  items = ""
  total = 0
  for item in self.ledger:
    items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n' #Fixed point to two decimals
    total += item['amount']
    
  output = title + items + "Total: " + str(total)
  return output 
   
def create_spend_chart(categories):
 #Create heading for chart
  chart = "Percentage spent by category\n"
  arrCategories = list()
  deductions = list()
  #percentages = [60,20,10]#random percentages to test graph
  
  for cat in categories:
    arrCategories.append(cat.name)
    #currentLedger = cat.ledger
    addAmount = 0
    for ledger in cat.ledger:
     myWithdrawel = ledger['amount']
     if myWithdrawel < 0:
      addAmount += myWithdrawel
    deductions.append(addAmount)
  myTotal = int(round(sum(deductions)))
  percentages = list()
  #https://www.wikihow.com/Calculate-Percentages How to calculate percentages of the biger whole
  for x in deductions:
    per = x * 100/myTotal
    per = round(per//10)*10
    percentages.append(per)
    #myObject = cat.ledger
    #for myLedger in myObject:
      #print(myLedger['amount'])
      
  #space = " "
  
  #Loop numbers in range of 100 to 0. In decrements by 10.
  for num in range(100,-1,-10):
    chart += f"{num:3d}|"#f"{str(num) + '|':>4}"#f"{num:3d}|"
    for percent in percentages:
      if percent >= num:
        chart += " o "
      else:
        chart += "   "#f"{space:>3}"
        
    chart += ' \n'
   
  chart += f"{'-'*10:>14}" + '\n'
  
  for name in zip_longest(*arrCategories, fillvalue=" "):
    chart +="     " + ("  ".join(name)) + '  \n'
  
  return chart.rstrip('\n')
    
        
    
cat = Category( "Food")
cat.transfer(4,50)
cat.deposit(40, "Car")
print(cat)
