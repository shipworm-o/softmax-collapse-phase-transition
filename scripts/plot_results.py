import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def run():
    os.makedirs("../results", exist_ok=True)
    df = pd.read_csv("../data/collapse_summary.csv")
    crit = pd.read_csv("../data/critical_points.csv")

    plt.style.use('seaborn-v0_8-whitegrid') # 깔끔한 논문 스타일

    # 1. Collapse Phase Transition
    plt.figure(figsize=(8, 5))
    for N in df["N"].unique():
        sub = df[df["N"] == N]
        plt.plot(sub["df"], sub["collapse_rate"], 'o-', label=f"N={N}", markersize=4)
    plt.axhline(0.5, color='gray', linestyle='--', alpha=0.5)
    plt.xlabel(r"Tail Exponent ($\nu$)")
    plt.ylabel("Collapse Probability")
    plt.title("Softmax Collapse Phase Transition")
    plt.legend()
    plt.savefig("../results/fig_collapse_vs_df.png", dpi=300)

    # 2. Critical Point Scaling (Log-Linear)
    plt.figure(figsize=(8, 5))
    plt.semilogx(crit["N"], crit["nu_c"], 'rs--', label="Empirical $\\nu_c$")
    
    # 선형 회귀 결과 시각화 (제시하신 수식 검증용)
    N_range = np.logspace(np.log10(100), np.log10(1000), 100)
    nu_c_pred = 0.252 * np.log(N_range) - 0.175
    plt.plot(N_range, nu_c_pred, 'k:', label="Theory: $0.252 \log N - 0.175$")
    
    plt.xlabel("System Size (N)")
    plt.ylabel(r"Critical Point ($\nu_c$)")
    plt.title("Scaling of Critical Point")
    plt.legend()
    plt.savefig("../results/fig_nu_c_scaling.png", dpi=300)

    print("\n✅ 시각화 완료: ../results/ 폴더 확인")

if __name__ == "__main__":
    run()