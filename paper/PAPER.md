\documentclass[11pt]{article}

\usepackage{amsmath, amssymb}

\title{Tail-Driven Phase Transition in Softmax Collapse}
\author{}
\date{}

\begin{document}

\maketitle

\begin{abstract}
We investigate collapse phenomena in softmax-like exponential competition systems under heavy-tailed energy distributions.

We show that collapse probability is governed by the tail exponent $\nu$ and follows a logistic phase transition. The critical point shifts with system size $N$ as:
\[
\nu_c(N) \approx 0.252 \log N - 0.175.
\]

We demonstrate that softmax collapse is a finite-size phase transition driven by extreme value statistics, where dominance of a single extreme realization suppresses collective contributions. All results are fully reproducible with publicly available code and data.
\end{abstract}

\section{Introduction}

Softmax-based selection mechanisms arise in statistical physics, machine learning, and probabilistic inference. A common phenomenon in such systems is \emph{collapse}, where a single component dominates exponentially.

This behavior is often treated as numerical instability. We show instead that collapse is a statistically governed phase transition controlled by the tail behavior of the underlying distribution.

\section{Problem Definition}

Let $E_1, \dots, E_N \sim P_\nu$, where $P_\nu$ is a Student-t distribution with tail exponent $\nu$.

Define:
\[
S = \sum_{i=1}^{N} \exp\left( -(E_i - E_{\min}) \right) - 1.
\]

We define collapse as:
\[
S < \epsilon, \quad \epsilon = 10^{-8}.
\]

The collapse probability is:
\[
P(\text{collapse} \mid \nu, N).
\]

\section{Experimental Setup}

We simulate:
\begin{itemize}
\item Student-t distributions with varying $\nu$
\item System sizes $N = 100, 300, 1000$
\item 4000 trials per configuration
\end{itemize}

All experiments are fully reproducible with fixed random seeds and no parameter tuning.

\section{Results}

\subsection{Phase Transition}

We observe that collapse probability follows a logistic form:
\[
P(\text{collapse}) \approx \frac{1}{1 + \exp(a(\nu - \nu_c))}.
\]

\subsection{Critical Scaling}

Empirical estimates give:
\[
\nu_c(N) \approx 0.252 \log N - 0.175.
\]

\subsection{Extreme Value Mechanism}

The behavior is explained by extreme value statistics. For heavy-tailed distributions:
\[
E_{\min} \sim N^{-1/\nu}.
\]

As $\nu$ decreases, extreme values dominate the exponential sum:
\[
\exp(-(E_{\min})) \gg \sum_{i \neq \min} \exp(-E_i),
\]

leading to collapse.

\section{Interpretation}

This corresponds to a crossover between:

\begin{itemize}
\item Gumbel regime (light tails): distributed competition
\item Fr\'echet regime (heavy tails): extreme-dominated behavior
\end{itemize}

The transition between these regimes manifests as a smooth finite-size phase transition.

\section{Reproducibility}

All results are fully reproducible. Code, raw data, and analysis scripts are publicly available:

\begin{itemize}
\item GitHub repository: \texttt{https://github.com/shipworm-o/softmax-collapse-phase-transition}
\item DOI archive: \texttt{https://doi.org/10.5281/zenodo.19425876}
\end{itemize}

\section{Conclusion}

We demonstrate that softmax collapse is governed by a tail-driven phase transition, with a critical point that shifts logarithmically with system size.

This establishes a direct quantitative link between extreme value theory and collapse phenomena in exponential competition systems.

\end{document}
