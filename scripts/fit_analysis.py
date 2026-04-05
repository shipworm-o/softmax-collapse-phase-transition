import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import os

def logistic(x, a, b):
    # a: 경사도, b: nu_c (임계점)
    return 1 / (1 + np.exp(a * (x - b)))

def run():
    df_data = pd.read_csv("../data/collapse_summary.csv")
    results = []

    for N in df_data["N"].unique():
        sub = df_data[df_data["N"] == N]
        x = sub["df"].values
        y = sub["collapse_rate"].values

        try:
            # p0=[경사도 초기값, 임계점 초기값]
            popt, _ = curve_fit(logistic, x, y, p0=[2, 1.5])
            results.append({"N": N, "nu_c": popt[1], "slope": popt[0]})
        except Exception as e:
            print(f"N={N} 피팅 실패: {e}")

    df_crit = pd.DataFrame(results)
    df_crit.to_csv("../data/critical_points.csv", index=False)
    print(df_crit)
    print("\n✅ 분석 완료: ../data/critical_points.csv 저장됨")

if __name__ == "__main__":
    run()