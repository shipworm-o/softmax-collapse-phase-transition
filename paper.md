# Tail-Driven Finite-Size Transition in Softmax Collapse

## Extreme-Value Scaling and Gap Mechanism

---

# Abstract

We investigate the collapse phenomenon in softmax distributions and show that it can be understood as a finite-size transition driven by extreme-value statistics of the lower tail of logit distributions.

By reducing the problem to the gap between the two smallest energies, we derive a scaling theory that explains both the onset and sharpness of collapse.

We show that:

- The extreme gap follows Fréchet-type scaling
- Collapse emerges via thresholding, producing a Gumbel-like transition
- The critical point depends explicitly on system size

Numerical simulations confirm the predicted finite-size scaling behavior and demonstrate data collapse across different system sizes.

---

# 1. Introduction

The softmax function:

\[
w_i = \frac{e^{-E_i}}{\sum_{j=1}^N e^{-E_j}}
\]

is widely used to normalize energy-like variables into probability distributions.

Under heavy-tailed conditions, softmax can exhibit a **collapse phenomenon**, where a single component dominates the distribution.

We propose that:

- Collapse is governed by extreme-value statistics
- The mechanism reduces to a two-body gap variable
- The transition is intrinsically finite-size dependent

---

# 2. Reduction to an Extreme-Gap Problem

Let:

\[
E_{(1)} \le E_{(2)} \le \dots \le E_{(N)}
\]

Define:

\[
S = \sum_{i \ne (1)} e^{-(E_i - E_{(1)})}
\]

Using a dominant-term approximation:

\[
S \approx e^{-(E_{(2)} - E_{(1)})} = e^{-\Delta}
\]

Thus:

\[
\text{Collapse} \iff \Delta > \log(1/\varepsilon)
\]

where:

\[
\Delta = E_{(2)} - E_{(1)}
\]

---

# 3. Extreme Gap Scaling

Assume a regularly varying lower tail:

\[
P(E < -x) = L(x) x^{-\nu}
\]

Then the minimum satisfies:

\[
E_{(1)} \sim -N^{1/\nu}
\]

Using the Poisson point process limit of extremes, the gap satisfies:

\[
\Delta = N^{1/\nu} Z
\]

where \(Z\) is an \(N\)-independent heavy-tailed random variable:

\[
P(Z > z) \sim z^{-\nu}
\]

This establishes a Fréchet-type scaling for the extreme gap.

---

# 4. Finite-Size Transition

Using the collapse condition:

\[
\Delta > c = \log(1/\varepsilon)
\]

we obtain:

\[
N^{1/\nu} \gtrsim c
\]

which yields a size-dependent critical point:

\[
\nu_c(N) \sim \frac{\log N}{\log(1/\varepsilon)}
\]

Thus, the transition exists only at finite system size.

---

# 5. Scaling Law and Gumbel-like Transition

Using:

\[
\Delta = N^{1/\nu} Z
\]

we obtain:

\[
P_{\text{collapse}} = P\left(Z > \frac{c}{N^{1/\nu}}\right)
\]

Define:

\[
x = (\nu - \nu_c(N)) \log N
\]

Then:

\[
P_{\text{collapse}} = F(x)
\]

where \(F\) is a smooth crossover function.

The transition exhibits a **Gumbel-like double-exponential structure**, not because the underlying variable is Gumbel-distributed, but because of thresholding applied to a heavy-tailed variable.

---

# 6. Role of Tail Asymmetry

Collapse is controlled entirely by the lower tail:

- Heavy lower tail → collapse occurs
- Light or bounded lower tail → collapse suppressed
- One-sided distributions → no collapse

Thus, the existence of extreme negative values is the determining factor.

---

# 7. Numerical Validation

We validate the theoretical predictions via Monte Carlo simulations.

### Figure 1 — Phase Transition

- Collapse probability vs ν
- Sharpening transition with increasing N

![Figure 1](figs/fig1.png)

---

### Figure 2 — Scaling Collapse

- Rescaled variable:

\[
x = (\nu - \nu_c(N)) \log N
\]

- All curves collapse onto a single master curve

![Figure 2](figs/fig2.png)

---

### Figure 3 — Gap Scaling

- Mean gap vs ν
- Strong growth for small ν, consistent with EVT scaling

![Figure 3](figs/fig3.png)

---

# 8. Connection to Particle Filter Degeneracy

Let:

\[
E_i = -\log p(y|x_i)
\]

Then softmax weights become particle weights:

\[
w_i = \frac{p(y|x_i)}{\sum_j p(y|x_j)}
\]

Collapse corresponds to:

- \(w_{\max} \to 1\)
- ESS → 1

Thus, particle filter degeneracy is an instance of the same extreme-gap mechanism.

---

# 9. Conclusion

We have shown that softmax collapse:

- is governed by an extreme-gap mechanism  
- exhibits finite-size scaling  
- arises from thresholding of heavy-tailed variables  
- explains particle filter degeneracy  

---

## Core Result

Softmax collapse is a finite-size transition induced by extreme-value spacing between the two smallest energies.

Code and data available at DOI: https://doi.org/10.5281/zenodo.19425876
