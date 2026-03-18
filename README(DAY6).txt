# Smart Transaction Risk Detector

## Overview
This Python script serves as a risk assessment tool for digital payment systems. It takes a sequence of transaction amounts from a user, categorizes them into a dictionary (`invalid`, `normal`, `large`, `high_risk`), and analyzes the data for fraudulent patterns. Alongside standard volume and spending checks, this version includes advanced anomaly detection to flag repeated identical transactions.

## Features
* **Data Categorization:** Uses a dictionary to automatically sort transactions into appropriate risk buckets.
* **List Comprehension:** Filters out invalid (≤ 0) transactions to ensure accuracy in volume and pattern calculations.
* **Duplicate Anomaly Detection:** Identifies if the same transaction amount appears multiple times, triggering a custom security warning.
* **Uniformity Check:** Uses the `all()` function to evaluate if every transaction in the sequence is completely identical.
* **Risk Classification:** Evaluates volume, high-risk frequency, and total spending to assign a Low, Moderate, or High risk tier.
* **Summary Tuple:** Packages the total value, transaction count, and final risk tier into a single, immutable data structure.

## How to Run
1. Save the code as `transaction_analyzer.py`.
2. Run the script in your terminal using: `python transaction_analyzer.py`
3. Enter the total number of transactions you wish to process.
4. Input the integer amount for each individual transaction when prompted.

---

## Assignment Documentation (Anti-Copying / Anti-AI Submission)

### 1. Algorithm Explanation
The script reads user input for transaction amounts, storing them in a sequence list. It uses a `for` loop to segregate the amounts into a dictionary based on value thresholds, safely routing ≤ 0 entries to an `invalid` category. A list comprehension extracts only valid transactions to calculate the total valid spend and transaction count. The program then checks for base risk patterns (frequency > 5, spending > 5000, suspicious amounts ≥ 3) alongside custom looping logic to detect repeated identical transactions. Finally, it uses conditional statements to assign a final risk tier, packages the summary into a tuple, and prints a comprehensive console report.

### 2. Custom Test Cases

**Test Case 1: The "Repeated Values" Anomaly**
* **Input:** `Enter total transactions: 4` -> Amounts: `100`, `100`, `100`, `50`
* **Expected Output:** The code will classify this as `Low Risk` (since totals and frequencies don't break standard thresholds), but it will successfully trigger the custom security alert: `WARING: The same amount is transacted multiple times ,becareful`.

**Test Case 2: High Risk + Uniformity Check**
* **Input:** `Enter total transactions: 3` -> Amounts: `2500`, `2500`, `2500`
* **Expected Output:** * Total Amount: 7500
  * Suspicious: True
  * Risk: High Risk (triggered by 3 high-risk transactions).
  * It will trigger the repeated value warning, and the custom `All Same Values:` flag will correctly evaluate to `True`.

### 3. Reflection: "What logic decision did you make?"
For my logic decision, I chose to implement a check for repeated transaction amounts. In real life, fraudsters often test stolen cards by making multiple identical purchases or running automated scripts. By iterating through the valid transactions and using the `.count()` method, I added a custom security warning if the same amount is transacted 3 or more times. I also added an `all_same` boolean flag to quickly identify if every single transaction in the batch is exactly identical. This adds an extra layer of real-world anomaly detection to the final risk report without breaking the core assignment requirements.