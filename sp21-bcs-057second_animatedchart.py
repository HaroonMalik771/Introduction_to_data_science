# Bar Chart
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation

# dataset
data_url = (
    "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
)

df = pd.read_csv(data_url, usecols=["Country Name", "Year", "Value"])

df_pivot = df.pivot(index="Country Name", columns="Year", values="Value")

fig, ax = plt.subplots(figsize=(10, 6))
years = df_pivot.columns  # year Column


def update(year):
    top_10bars = df_pivot[year].sort_values(ascending=False).head(10)

    ax.clear()

    ax.invert_yaxis()

    colors = ["green", "orange", "yellow"]

    upper_limit_xaxis = top_10bars.max() + 100_000_000
    ax.set_xlim(0, upper_limit_xaxis)
    ax.set_xlabel("Population (millions)")

    if upper_limit_xaxis > 1_000_000:
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(lambda v, pos: f"{v/1000000:.0f}M")
        )
    else:
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(lambda v, pos: f"{v/1000:.1f}K")
        )

    ax.barh(top_10bars.index[:3], top_10bars[:3], color=colors, height=0.7)
    ax.barh(top_10bars.index[3:], top_10bars[3:], color="blue", height=0.7)

    ax.set_title(f"Top 10 countries by  population in {year}")


anim = FuncAnimation(fig=fig, func=update, frames=years, repeat=True, interval=100)
fig.subplots_adjust(left=0.25)
plt.show()
