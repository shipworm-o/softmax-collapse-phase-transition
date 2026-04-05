# Tail-Driven Phase Transition in Softmax Collapse

---

## Abstract

We investigate collapse phenomena in softmax-like exponential competition systems under heavy-tailed energy distributions.

We show that collapse probability is governed by the tail exponent $\nu$ and follows a logistic phase transition. The critical point shifts with system size $N$ as:

$$
\nu_c(N) \approx 0.252 \log N - 0.175
$$

We demonstrate that softmax collapse is a finite-size phase transition driven by extreme value statistics, where dominance of a single extreme realization suppresses collective contributions. All results are fully reproducible with publicly available code and data.

---

## 1. Introduction

Softmax-based selection mechanisms arise in statistical physics, machine learning, and probabilistic inference. A common phenomenon in such systems is *collapse*, where a single component dominates exponentially.

This behavior is often treated as numerical instability. We show instead that collapse is a statistically governed phase transition controlled by the tail behavior of the underlying distribution.

This has direct implications for stability in softmax-based systems, including machine learning models and probabilistic inference methods.

---

## 2. Problem Definition

Let $E_1, \dots, E_N \sim P_\nu$, where $P_\nu$ is a Student-t distribution with tail exponent $\nu$.

Define:

$$
S = \sum_{i=1}^{N} \exp\left(-(E_i - E_{\min})\right) - 1
$$

We define collapse as:

$$
S < \epsilon, \quad \epsilon = 10^{-8}
$$

The collapse probability is:

$$
P(\text{collapse} \mid \nu, N)
$$

---

## 3. Experimental Setup

- Distributions: Student-t with varying $\nu$  
- System sizes: $N = 100, 300, 1000$  
- Trials per configuration: 4000  
- Fixed random seed (fully reproducible)  

No tuning or normalization is applied.

---

## 4. Results

### 4.1 Collapse Phase Transition

We observe that collapse probability follows a logistic form:

$$
P(\text{collapse}) \approx \frac{1}{1 + \exp(a(\nu - \nu_c))}
$$

- Small $\nu$: high collapse probability  
- Large $\nu$: near-zero collapse  
- Smooth transition between regimes  

The logistic form suggests an underlying competition between bulk contributions and extreme-value dominance.

---

### 4.2 Critical Point Extraction

Empirical estimates:

| N | $\nu_c$ |
|---|--------|
| 100 | 1.0048 |
| 300 | 1.2272 |
| 1000 | 1.5836 |

---

### 4.3 Finite-Size Scaling

The critical point follows:

$$
\nu_c(N) \approx 0.252 \log N - 0.175
$$

indicating logarithmic drift with system size.

---

### 4.4 Extreme Value Scaling

For heavy-tailed distributions:

$$
\max_i |E_i| \sim N^{1/\nu}
$$

Extreme values grow polynomially with system size, leading to dominance in the exponential sum.

---

## 5. Interpretation

The observed behavior is consistent with a transition between:

- **Gumbel regime (light tails):** distributed competition  
- **Fréchet regime (heavy tails):** extreme-dominated dynamics  

As $\nu$ decreases, the contribution of the minimum energy dominates:

$$
\exp(-E_{\min}) \gg \sum_{i \ne \min} \exp(-E_i)
$$

leading to collapse.

---

## 6. Discussion

Our results suggest:

1. Collapse is intrinsic to exponential competition systems  
2. Tail behavior acts as a control parameter  
3. System size shifts the effective critical point  

We emphasize that this is a **finite-size effect**, not a thermodynamic phase transition.

---

## 7. Reproducibility

All results are fully reproducible. Code, raw data, and analysis scripts are publicly available:

- Repository: https://github.com/shipworm-o/softmax-collapse-phase-transition  
- DOI archive: https://doi.org/10.5281/zenodo.19425876  

---

## 8. Conclusion

We demonstrate that softmax collapse is governed by a tail-driven phase transition, with a critical point that shifts logarithmically with system size.

This establishes a direct quantitative link between extreme value theory and collapse phenomena in exponential competition systems.
