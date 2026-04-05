import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs("figs", exist_ok=True)

np.random.seed(42)
# -------------------------
# CONFIG
# -------------------------
N_list = [100, 300, 1000, 3000]
nu_list = np.linspace(1.2, 3.5, 25)
eps = 1e-3
runs = 2000

# -------------------------
# Sampling (heavy lower tail)
# -------------------------
def sample_energy(N, nu):
    # symmetric heavy tail (Student-t like)
    return -np.abs(np.random.standard_t(df=nu, size=N))

def compute_gap(E):
    E_sorted = np.sort(E)
    return E_sorted[1] - E_sorted[0]

# -------------------------
# Run experiments
# -------------------------
results = {}

for N in N_list:
    probs = []
    gaps = []
    
    for nu in nu_list:
        collapse_count = 0
        gap_samples = []
        
        for _ in range(runs):
            E = sample_energy(N, nu)
            gap = compute_gap(E)
            threshold = np.log(1/eps)
            gap_samples.append(gap)
            
            if gap > threshold:
                collapse_count += 1
        
        probs.append(collapse_count / runs)
        print(f"[RUN] N={N}, nu={nu:.2f}, P={collapse_count / runs:.3f}")
        gaps.append(np.mean(gap_samples))
    
    results[N] = {
        "probs": np.array(probs),
        "gaps": np.array(gaps)
    }

# -------------------------
# FIG 1: Collapse probability
# -------------------------
plt.figure()
for N in N_list:
    plt.plot(nu_list, results[N]["probs"], label=f"N={N}")
plt.xlabel("nu")
plt.ylabel("P(collapse)")
plt.legend()
plt.title("Collapse Transition")
plt.savefig("figs/fig1.png", dpi=300)
plt.close()

# -------------------------
# FIG 2: Scaling collapse
# -------------------------
plt.figure()

for N in N_list:
    nu_c = np.log(N) / np.log(1/eps)
    x = (nu_list - nu_c) * np.log(N)
    plt.plot(x, results[N]["probs"], label=f"N={N}")

plt.xlabel("(nu - nu_c) log N")
plt.ylabel("P(collapse)")
plt.legend()
plt.title("Scaling Collapse")
plt.savefig("figs/fig2.png", dpi=300)
plt.close()

# -------------------------
# FIG 3: Gap scaling
# -------------------------
plt.figure()

for N in N_list:
    plt.plot(nu_list, results[N]["gaps"], label=f"N={N}")

plt.xlabel("nu")
plt.ylabel("Mean gap")
plt.legend()
plt.title("Gap scaling")
plt.savefig("figs/fig3.png", dpi=300)
plt.close()