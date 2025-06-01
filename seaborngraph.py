import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = r"C:\Users\Documents\spidertimes.xlsx"  #edited for privacy
df = pd.read_excel(file_path)


filtered_df = df.dropna(subset=["Visual", "Audio", "Both"], how="all")


long_df = (
    filtered_df
    .melt(id_vars="ID",
          value_vars=["Visual", "Audio", "Both"],
          var_name="Condition",
          value_name="Time")
    .dropna(subset=["Time"])            
)


sns.set_theme(style="whitegrid", palette="Set2")
plt.figure(figsize=(20, 14))

ax = sns.barplot(
    data=long_df,
    x="ID",              
    y="Time",            
    hue="Condition",     
    dodge=True           
)

# Title, labels, legend
ax.set_title("Spider Completion Time by Condition", fontsize=9)
ax.set_xlabel("Spider ID", fontsize=26)
ax.set_ylabel("Completion Time (seconds)", fontsize=34)
ax.tick_params(axis='x', labelsize=20)
ax.tick_params(axis='y', labelsize=34)
ax.legend(title="Condition", fontsize=24, title_fontsize=26)

ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

plt.tight_layout()
plt.show()
