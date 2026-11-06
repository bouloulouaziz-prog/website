import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':13})
plt.rcParams["svg.fonttype"]="path"
plt.rcParams["font.family"]="DejaVu Sans"
INK="#003340"; ACC="#D3104C"; GREY="#9AA6B5"
# grafiek 1
jaren=["2021","2022","2023","2024","2025"]
tot=[41047,39447,38731,38170,37445]
fig,ax=plt.subplots(figsize=(5.2,5.2))
b=ax.bar(jaren,tot,color=[GREY]*4+[ACC],width=0.62)
for r,v in zip(b,tot):
    ax.text(r.get_x()+r.get_width()/2,v+500,f"{v:,}".replace(",","."),ha="center",fontsize=13,color=INK,fontweight="bold")
ax.set_ylim(0,46000); ax.set_ylabel("Aantal studenten")
ax.set_title("Totaal aantal studenten\nHogeschool Rotterdam, 2021-2025",fontsize=15,color=INK,loc="left")
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x,p:f"{int(x):,}".replace(",",".")))
fig.text(0.01,0.01,"Bron: Jaarverslag 2025, Hogeschool Rotterdam",fontsize=11,color="#555")
fig.tight_layout(rect=(0,0.05,1,1)); fig.savefig("w/grafieken/grafiek1_totaal_studenten.svg"); plt.close(fig)
# grafiek 2
typen=["Bachelor","Associate degree","Master"]
v21=[36605,3461,981]; v25=[31841,4358,1246]
import numpy as np
x=np.arange(3); w=0.36
fig,ax=plt.subplots(figsize=(5.2,5.2))
b1=ax.bar(x-w/2,v21,w,color=GREY,label="2021"); b2=ax.bar(x+w/2,v25,w,color=ACC,label="2025")
for bs in (b1,b2):
    for r in bs:
        v=r.get_height(); ax.text(r.get_x()+r.get_width()/2,v+500,f"{v:,}".replace(",","."),ha="center",fontsize=12,color=INK,fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(typen); ax.set_ylim(0,41000)
ax.set_ylabel("Aantal studenten")
ax.set_title("Studenten per onderwijstype,\n2021 en 2025",fontsize=15,color=INK,loc="left")
ax.legend(frameon=False)
for s in ("top","right"): ax.spines[s].set_visible(False)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x,p:f"{int(x):,}".replace(",",".")))
fig.text(0.01,0.01,"Bron: Jaarverslag 2025, Hogeschool Rotterdam",fontsize=11,color="#555")
fig.tight_layout(rect=(0,0.05,1,1)); fig.savefig("w/grafieken/grafiek2_onderwijstype.svg"); plt.close(fig)
print("ok")
