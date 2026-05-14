import pandas as pd
import io

data = """
PRODUCT,QUANTITY,PRICE
A,2,100
B,1,200
A,3,100
C,5,50
"""
df = pd.DataFrame
df = pd.read_csv(io.StringIO(data))
# Adding the total column in dataframe
df["TOTAL"] = df["QUANTITY"] * df["PRICE"]

# Sales per product
sales_per_product = df.groupby("PRODUCT")["TOTAL"].sum()
print(f"SALE PER PRODUCT :\n{sales_per_product}")

# Total revenue
total_revenue = df["TOTAL"].sum()
print(f"TOTAL REVENUE : {total_revenue}")

# Top selling product
top = sales_per_product.idxmax()
print("TOP SELLING PRODUCT :",top)

# Sorting values in decreasing order
summary_df = df.groupby('PRODUCT', as_index=False)['TOTAL'].sum()  # as_index =False used to reset the index
sorted_values = summary_df.sort_values(by=["TOTAL"],ascending= False)
print(f"SORTED BY REVENUE:\n   {sorted_values}")
