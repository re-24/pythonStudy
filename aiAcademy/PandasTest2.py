import pandas as pd
df = pd.DataFrame([[10, 20], [25, 50]], index=["1行", "2行"], columns=["1列", "2列"])

print(df)
df.iloc[::1]
print(df.iloc[::-1])