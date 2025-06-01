import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r"C:\Users\User\Documents\spidertimes.xlsx"  #edited for privacy.
df = pd.read_excel(file_path)

filtered_df = df.dropna(subset=["Visual", "Audio", "Both"], how='all')

long_df = pd.melt(filtered_df, id_vars=["ID"], value_vars=["Visual", "Audio", "Both"],
                  var_name="Condition", value_name="Time")

pivot_df = long_df.pivot_table(index="ID", columns="Condition", values="Time", aggfunc="first")

sns.set_theme(style="whitegrid")
colours = sns.color_palette("Set2")
pivot_df.plot(kind='bar', stacked=False, figsize=(20, 14), color=colours)

plt.title("Spider Completion Time by Condition")
plt.xlabel("Spider ID")
plt.ylabel("Completion Time (seconds)")
plt.legend(title="Condition")
plt.tight_layout()

plt.show()
