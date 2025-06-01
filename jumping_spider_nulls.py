import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\Documents\spidertimes.xlsx"  #edited for privacy  
df = pd.read_excel(file_path)

null_counts = df[["Visual", "Both", "Audio"]].isnull().sum()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x=null_counts.index, y=null_counts.values, palette="Set2")

plt.title("Number of Missing (Null) Values per Condition", fontsize=0)
plt.xlabel("Condition", fontsize= 18
           )
plt.ylabel("Number of Non-Completions", fontsize= 19)

for i, v in enumerate(null_counts.values):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold', fontsize= 9)

plt.tight_layout()
plt.show()
