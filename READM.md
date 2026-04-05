# Tail-driven Phase Transition in Softmax Collapse

*(Reproducible Research Package)*

---

## 📌 Overview

This repository demonstrates that **softmax collapse** is governed by a **tail-driven phase transition**.

* Collapse probability follows a **logistic transition** in the tail exponent ( \nu )
* The critical point scales with system size:

[
\nu_c(N) \approx 0.252 \log N - 0.175
]

All results are fully reproducible using the provided data and scripts.

---

## ⚙️ Problem Setup

Given energy samples:

```
E_i ~ Student-t(ν)
```

Define:

```
S = sum exp(-(E_i - E_min)) - 1
```

Collapse condition:

```
S < 1e-8
```

---

## 🔬 Key Findings

* Logistic phase transition in collapse probability
* Critical point scales as ( \nu_c(N) \propto \log N )
* Heavy-tailed regime → collapse-dominated
* Light-tailed regime → competitive dynamics

---

## ▶️ Run

Install dependencies:

```
pip install -r requirements.txt
```

Run full pipeline:

```
python scripts/run_experiment.py
python scripts/fit_analysis.py
python scripts/plot_results.py
```

---

## 📁 Project Structure

```
project/
├── README.md
├── requirements.txt
├── data/
├── paper/
│   └── PAPER.md
├── scripts/
└── results/
```

---

## 📊 Data

### collapse_raw.csv

```
N,df,trial,collapse
```

### collapse_summary.csv

```
N,df,collapse_rate
```

### critical_points.csv

```
N,nu_c,slope
```

---

## 📄 Paper

Full write-up available at:

```
paper/PAPER.md
```

---

## 🧠 Summary

Softmax collapse is not a numerical artifact, but a **finite-size phase transition** driven by extreme values in heavy-tailed distributions.

---
