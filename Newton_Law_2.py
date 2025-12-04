import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# ==========================================================
#               PARAMETER FISIKA (HUKUM NEWTON 2)
# ==========================================================

m = 2.0  # massa benda (kg)

forces = {
    "F1": np.array([10, 4]),
    "F2": np.array([-6, 4]),
    "F3": np.array([5, -3]),
    "F4": np.array([-8, 6]),
}

# Hitung resultan gaya ΣF dan percepatan a = ΣF / m
sumF = np.sum(list(forces.values()), axis=0)
acc = sumF / m

print("=== HUKUM NEWTON 2 ===")
print("Massa:", m, "kg")
print("ΣF =", sumF)
print("a = ΣF / m =", acc, "m/s²")

# ==========================================================
#             FUNGSI PENGGAMBARAN PANAH (ANIMASI)
# ==========================================================

def draw_arrow(ax, vec, label, scale, color, origin=(0,0)):
    ox, oy = origin
    Fx, Fy = vec * scale
    ax.arrow(ox, oy, Fx, Fy,
             head_width=0.4,
             head_length=0.6,
             length_includes_head=True,
             linewidth=2.5,
             color=color)
    
    ax.text(ox + Fx * 1.05,
            oy + Fy * 1.05,
            label,
            fontsize=13, color=color, weight="bold")

# ==========================================================
#               SETUP KANVAS / FIGURE BESAR
# ==========================================================

fig, ax = plt.subplots(figsize=(10, 10))

# Range kanvas mengikuti nilai gaya terbesar
max_range = np.max(np.abs(np.array(list(forces.values())))) * 3
colors = ["red", "blue", "green", "orange", "purple"]

# ==========================================================
#                    FUNGSI ANIMASI
# ==========================================================

def animate(frame):
    ax.clear()
    
    # Tampilan dasar grafis
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    
    ax.set_title(
        "Hukum Newton 2 – Free Body Diagram (Animasi)\nΣF = m·a",
        fontsize=18,
        weight="bold"
    )
    
    # Tahapan animasi
    steps = 40
    i = 0
    
    # Animasi gaya-gaya F1–F4
    for (name, F), col in zip(forces.items(), colors):
        start = i * steps
        end = start + steps
        
        if start <= frame <= end:
            scale = (frame - start) / steps  # animasi membesar
            draw_arrow(ax, F, name, scale, col)
        elif frame > end:
            draw_arrow(ax, F, name, 1, col)
        
        i += 1
    
    # Animasi resultan ΣF
    if frame > len(forces) * steps:
        scale = min((frame - len(forces)*steps) / steps, 1)
        draw_arrow(ax, sumF, "Resultan (ΣF)", scale, "purple")
    
    # Animasi percepatan a = ΣF / m
    if frame > (len(forces) + 1) * steps:
        scale = min((frame - (len(forces)+1)*steps) / steps, 1)
        draw_arrow(ax, acc, "Percepatan (a)", scale, "brown")

# ==========================================================
#                    PROSES ANIMASI
# ==========================================================

anim = FuncAnimation(fig, animate, frames=250, interval=30)

# Hindari muncul grafik duplikat
plt.close(fig)

HTML(anim.to_jshtml())
