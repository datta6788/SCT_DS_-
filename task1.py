import matplotlib.pyplot as plt
import pandas as pd
onepiece=pd.read_csv("OPepisodes.csv")
colors=["red","green","yellow","brown","orange","pink","purple","blue","black"]
plt.bar(onepiece["Arc"],onepiece["Episodes"],color=colors)
plt.title("ONEPIECE (Arcs and episodes)")
for bar in plt.gca().patches:
    heights=bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,heights+1,f'{int(heights)}',ha="center"
    )
plt.xlabel("Arcs")
plt.ylabel("Episodes")
plt.xticks(rotation=90,ha="center",fontsize=10)
plt.show()

