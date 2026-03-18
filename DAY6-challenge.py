# input transactions
trans = []
n = int(input("Enter total transactions: "))

for i in range(n):
    amount = int(input(f"Transaction {i + 1}: "))
    trans.append(amount)

# categories
categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

total = 0
valid_count = 0

# processing
for amt in trans:
    if amt <= 0:
        categories["invalid"].append(amt)
    else:
        total += amt
        valid_count += 1

        if amt <= 500:
            categories["normal"].append(amt)
        elif amt <= 2000:
            categories["large"].append(amt)
        else:
            categories["high_risk"].append(amt)

# list comprehension
valid_trans = [x for x in trans if x > 0]
txn_count = len(trans)

# patterns
is_frequent = txn_count > 5
is_high_spending = total > 5000
is_suspicious = len(categories["high_risk"]) >= 3

#checking sm amt multiple times
repeat_count=0
for val in valid_trans:
    if valid_trans.count(val) >= 3:
        repeat_count = repeat_count+ 1

# extra logic
all_same = all(trans[i] == trans[0] for i in range(len(trans))) if trans else False

# risk decision
if is_suspicious:
    risk = "High Risk"
elif is_frequent or is_high_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

# tuple
summary = (total, txn_count, risk)

# output
for key, value in categories.items():
    print(f"{key}: {value}")

print("Total Amount:", total)
print("Transaction Count:", txn_count)
print("Valid Transactions:", valid_count)

print("Frequent:", is_frequent)
print("High Spending:", is_high_spending)
print("Suspicious:", is_suspicious)

print("Repeated values:", repeat_count)
if repeat_count >= 3:
 print("WARING: The same amount is transacted multiple times ,becareful")
print("High Risk:", risk)

print("All Same Values:", all_same)

print("Final Risk:", risk)
print("Summary:", summary)