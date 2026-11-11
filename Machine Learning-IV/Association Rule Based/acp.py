
# STEP 1: Download Dataset from Google Drive


import gdown

file_id = '1-hfNTgH-1hTGpQPDuvLsSvMTFCJPVZy9'
url = f'https://drive.google.com/uc?id={file_id}'

gdown.download(url, 'grocery.csv', quiet=False)


# STEP 2: Import Necessary Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from itertools import combinations
from collections import Counter

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

import warnings
warnings.filterwarnings('ignore')


# STEP 3: Load Dataset

df = pd.read_csv('GroceryStoreDataSet.csv')

print("First 5 Records:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())


# STEP 4: Prepare Tidy Data for Association Rules

# Remove unnecessary spaces from column names
df.columns = df.columns.str.strip()

# Identify item column
item_col = next(
    (col for col in df.columns
     if col.lower() in ['itemdescription', 'item', 'product']),
    None
)

if item_col is None:
    raise ValueError("Item column not found. Check dataset columns.")

# Remove rows with missing item names
df = df.dropna(subset=[item_col])

# Remove extra spaces and convert items to lowercase
df[item_col] = df[item_col].astype(str).str.strip().str.lower()

# Identify transaction columns
member_col = next(
    (col for col in df.columns
     if col.lower() in ['member_number', 'membernumber', 'customer_id']),
    None
)

date_col = next(
    (col for col in df.columns
     if col.lower() in ['date', 'transaction_date']),
    None
)

transaction_col = next(
    (col for col in df.columns
     if col.lower() in ['transaction_id', 'transactionid', 'basket_id']),
    None
)

# Group items belonging to the same transaction
if member_col and date_col:
    transactions = df.groupby(
        [member_col, date_col]
    )[item_col].apply(list).tolist()

elif transaction_col:
    transactions = df.groupby(
        transaction_col
    )[item_col].apply(list).tolist()

elif member_col:
    transactions = df.groupby(
        member_col
    )[item_col].apply(list).tolist()

else:
    raise ValueError(
        "Transaction ID or customer and date columns are required."
    )

# Remove duplicate items within each transaction
transactions = [
    list(set(items)) for items in transactions
]

print("\nTotal Transactions:", len(transactions))

print("\nFirst 5 Transactions:")
for transaction in transactions[:5]:
    print(transaction)


# STEP 5: Find Support for Single Grocery Items

# Count occurrences of each item
item_counts = Counter(
    item
    for transaction in transactions
    for item in transaction
)

total_transactions = len(transactions)

# Calculate support for individual items
single_support = pd.DataFrame([
    {
        'Item': item,
        'Count': count,
        'Support': count / total_transactions
    }
    for item, count in item_counts.items()
])

single_support = single_support.sort_values(
    by='Support',
    ascending=False
)

print("\nSupport for Single Grocery Items:")
print(single_support.to_string(index=False))


# STEP 6: Find Support for Pairs of Grocery Items

pair_counts = Counter()

for transaction in transactions:
    for pair in combinations(sorted(transaction), 2):
        pair_counts[pair] += 1

# Calculate pair support
pair_support = pd.DataFrame([
    {
        'Items': pair,
        'Count': count,
        'Support': count / total_transactions
    }
    for pair, count in pair_counts.items()
])

pair_support = pair_support.sort_values(
    by='Support',
    ascending=False
)

print("\nSupport for Pairs of Grocery Items:")
print(pair_support.head(20).to_string(index=False))

print("\nTotal Unique Pairs:", len(pair_support))


# STEP 7: Convert Transactions into Tidy Data

te = TransactionEncoder()

te_array = te.fit(transactions).transform(transactions)

basket = pd.DataFrame(
    te_array,
    columns=te.columns_
)

print("\nTidy Transaction Data:")
print(basket.head())


# STEP 8: Apply Apriori Algorithm

frequent_itemsets = apriori(
    basket,
    min_support=0.01,
    use_colnames=True
)

print("\nFrequent Itemsets:")
print(frequent_itemsets.sort_values(
    by='support',
    ascending=False
).to_string(index=False))


# STEP 9: Create a Function for Association Rules

def create_association_rules(frequent_itemsets, min_confidence=0.2):

    rules = []

    # Create a dictionary of itemset supports
    support_dict = {
        frozenset(row['itemsets']): row['support']
        for _, row in frequent_itemsets.iterrows()
    }

    # Generate rules from frequent itemsets
    for itemset in support_dict:

        if len(itemset) < 2:
            continue

        # Generate all possible antecedents
        for i in range(1, len(itemset)):

            for antecedent in combinations(itemset, i):

                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent

                # Calculate support
                support = support_dict[itemset]

                # Calculate antecedent support
                antecedent_support = support_dict[antecedent]

                # Calculate consequent support
                consequent_support = support_dict[consequent]

                # Calculate confidence
                confidence = support / antecedent_support

                # Calculate lift
                lift = confidence / consequent_support

                if confidence >= min_confidence:

                    rules.append({
                        'Antecedents': ', '.join(sorted(antecedent)),
                        'Consequents': ', '.join(sorted(consequent)),
                        'Support': support,
                        'Confidence': confidence,
                        'Lift': lift
                    })

    return pd.DataFrame(rules)


# STEP 10: Generate Association Rules

rules = create_association_rules(
    frequent_itemsets,
    min_confidence=0.2
)

if not rules.empty:

    rules = rules.sort_values(
        by='Lift',
        ascending=False
    )

    print("\nAssociation Rules:")
    print(rules.to_string(index=False))

else:
    print("\nNo association rules found. Try lowering the thresholds.")


# STEP 11: Analyze Relationships Between Grocery Items

if not rules.empty:

    print("\nTop 10 Grocery Item Relationships:")

    print(
        rules.head(10)[
            ['Antecedents', 'Consequents',
             'Support', 'Confidence', 'Lift']
        ].to_string(index=False)
    )

    print("\nInterpretation of Top Rules:")

    for _, row in rules.head(10).iterrows():

        print(
            f"If a customer buys {row['Antecedents']}, "
            f"they may also buy {row['Consequents']}."
        )

        print(
            f"Confidence: {row['Confidence']:.2f}, "
            f"Lift: {row['Lift']:.2f}\n"
        )


# STEP 12: Visualize Association Rules

if not rules.empty:

    plt.figure(figsize=(10, 6))

    plt.scatter(
        rules['Support'],
        rules['Confidence'],
        s=rules['Lift'] * 30,
        alpha=0.6
    )

    plt.xlabel('Support')
    plt.ylabel('Confidence')
    plt.title('Association Rules: Support vs Confidence')

    plt.show()


# STEP 13: Save Results

single_support.to_csv(
    'single_item_support.csv',
    index=False
)

pair_support.to_csv(
    'pair_item_support.csv',
    index=False
)

frequent_itemsets.to_csv(
    'frequent_itemsets.csv',
    index=False
)

rules.to_csv(
    'grocery_association_rules.csv',
    index=False
)

print("\nAll results saved successfully!")
