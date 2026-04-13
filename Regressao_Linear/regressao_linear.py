import numpy as np
import matplotlib.pyplot as plt
from dataset import HOUSE_AREA, HOUSE_PRICE

# Cálculos base
media_area : float = HOUSE_AREA.mean()
variancia_area : float = HOUSE_AREA.var()
desvio_padrao_area : float = HOUSE_AREA.std()
media_price : float = HOUSE_PRICE.mean()
variancia_price : float = HOUSE_PRICE.var()
desvio_padrao_price : float = HOUSE_PRICE.std()

# ----------------------------------------------------------------------------------

# Cálculo dos coeficientes
def calcula_coef_angular() -> float:
    numerador = ((HOUSE_AREA - media_area) * (HOUSE_PRICE - media_price)).sum()
    denominador = ((HOUSE_AREA - media_area)**2).sum()
    return (numerador / denominador)

def calcula_coef_linear() -> float:
    return (media_price - (coef_angular * media_area))

coef_angular : float = calcula_coef_angular()
coef_linear : float = calcula_coef_linear()

# Cálculo da reta de regressão f(x) = ax + b
y : float = coef_angular * HOUSE_AREA + coef_linear

# ----------------------------------------------------------------------------------

# Visualização
fig, ax = plt.subplots(figsize=(12,8))

scatter = ax.scatter(
    HOUSE_AREA,
    HOUSE_PRICE,
    color='blue',
    marker='o',
    label='Dados',
    picker=5  
)

ax.plot(
    HOUSE_AREA,
    y,
    label=f"y = {coef_angular:.2f}x + {coef_linear:.2f}",
    color='red'
)

ax.set_xticks(np.linspace(min(HOUSE_AREA), max(HOUSE_AREA), 8))
ax.set_yticks(np.linspace(min(HOUSE_PRICE), max(HOUSE_PRICE), 8))
ax.ticklabel_format(style='plain', axis='y')

ax.set_title("Regressão Linear: \nPreço x Área das Casas")
ax.set_ylabel("Preços das Casas (M $)")
ax.set_xlabel("Área das Casas (m²)")

ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="center left", bbox_to_anchor=(1, 0.8))

stats_text = (
    f"Média área = {media_area:.0f}\n"
    f"Variância área = {variancia_area:.0f}\n"
    f"Desvio padrão área = {desvio_padrao_area:.0f}\n\n"
    f"Média preço = {media_price:.0f}\n"
    f"Variância preço = {variancia_price:.0f}\n"
    f"Desvio padrão preço = {desvio_padrao_price:.0f}"
)

fig.text(
    0.81, 0.2,
    stats_text,
    fontsize=8,
    bbox=dict(
        facecolor="white",
        edgecolor="black",
        boxstyle="round,pad=0.5"
    )
)

annot = ax.annotate(
    "",
    xy=(0,0),
    xytext=(10,10),
    textcoords="offset points",
    bbox=dict(boxstyle="round", fc="white"),
    arrowprops=dict(arrowstyle="->")
)
annot.set_visible(False)

def on_pick(event):
    ind = event.ind[0]
    x = HOUSE_AREA[ind]
    y = HOUSE_PRICE[ind]

    annot.xy = (x, y)
    annot.set_text(f"Área: {x:.0f}\nPreço: {y:,.0f}")
    annot.set_visible(True)
    fig.canvas.draw_idle()

fig.canvas.mpl_connect("pick_event", on_pick)

plt.tight_layout()
plt.show()