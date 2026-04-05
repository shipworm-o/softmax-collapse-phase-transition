import numpy as np
import pandas as pd
import os

# 설정
Ns = [100, 300, 1000]
dfs = np.linspace(0.5, 5.0, 15)  # 더 세밀한 분석을 위해 구간 세분화
TRIALS = 4000
THRESH = 1e-8
SEED = 42

np.random.seed(SEED)

def check_collapse(df, N):
    # Student-t 분포 샘플링
    E = np.random.standard_t(df, size=N)
    E_min = np.min(E)
    # 수치적 안정성을 위해 E_min을 뺀 후 exp 계산
    S = np.sum(np.exp(-(E - E_min))) - 1
    return 1 if S < THRESH else 0

def run():
    os.makedirs("../data", exist_ok=True)
    results = []

    for N in Ns:
        print(f"Running Experiment for N={N}...")
        for df_val in dfs:
            collapses = [check_collapse(df_val, N) for _ in range(TRIALS)]
            rate = np.mean(collapses)
            results.append({"N": N, "df": df_val, "collapse_rate": rate})
            print(f"  df: {df_val:.2f} | Rate: {rate:.4f}")

    df_res = pd.DataFrame(results)
    df_res.to_csv("../data/collapse_summary.csv", index=False)
    print("\n✅ 실험 완료: ../data/collapse_summary.csv 저장됨")

if __name__ == "__main__":
    run()