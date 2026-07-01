# Baseline Significance and Effect Size Report

This report statistically validates the performance of **Runtime FVS** containment against alternative baselines. We evaluate paired observations across 200 simulation runs. Shapiro-Wilk test determines the normality of paired differences, paired t-tests or Wilcoxon signed-rank tests assess statistical significance, and Benjamini-Hochberg FDR adjustments correct for multiple hypothesis testing.

---

## 🔬 Per-Baseline Comparison Summaries

### 🛡️ Runtime FVS vs. No Containment

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 12.845 (No Containment) [Diff: -12.540]
  - Relative Improvement: **97.6%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.000 (No Containment) [Diff: 0.974]
  - Relative Improvement: **100.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 0.000 (No Containment) [Diff: 12.540]
  - Relative Improvement: **100.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 22.210 (No Containment) [Diff: -21.905]
  - Relative Improvement: **98.6%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 6.400 (No Containment) [Diff: -6.095]
  - Relative Improvement: **95.2%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

**Conclusion**: Runtime FVS significantly outperformed No Containment in containment effectiveness.

---

### 🛡️ Runtime FVS vs. Random Revocation

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 3.822 (Random Revocation) [Diff: -3.517]
  - Relative Improvement: **92.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.669 (Random Revocation) [Diff: 0.305]
  - Relative Improvement: **45.6%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 9.023 (Random Revocation) [Diff: 3.517]
  - Relative Improvement: **39.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 6.007 (Random Revocation) [Diff: -5.702]
  - Relative Improvement: **94.9%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 2.546 (Random Revocation) [Diff: -2.240]
  - Relative Improvement: **88.0%**
  - Test: Paired t-test (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Cohen's d): -3.343 (Large Effect)

**Conclusion**: Runtime FVS significantly outperformed Random Revocation in containment effectiveness.

---

### 🛡️ Runtime FVS vs. Degree Centrality

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.930 (Degree Centrality) [Diff: -0.625]
  - Relative Improvement: **67.2%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.801 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.922 (Degree Centrality) [Diff: 0.053]
  - Relative Improvement: **5.7%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 0.883 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 11.915 (Degree Centrality) [Diff: 0.625]
  - Relative Improvement: **5.2%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 0.801 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 1.145 (Degree Centrality) [Diff: -0.840]
  - Relative Improvement: **73.4%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.836 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.920 (Degree Centrality) [Diff: -0.615]
  - Relative Improvement: **66.8%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.799 (Large Effect)

**Conclusion**: Runtime FVS significantly outperformed Degree Centrality in containment effectiveness.

---

### 🛡️ Runtime FVS vs. Betweenness Centrality

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.825 (Betweenness Centrality) [Diff: -0.520]
  - Relative Improvement: **63.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.700 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.920 (Betweenness Centrality) [Diff: 0.054]
  - Relative Improvement: **5.9%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 0.651 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 12.020 (Betweenness Centrality) [Diff: 0.520]
  - Relative Improvement: **4.3%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 0.700 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 1.330 (Betweenness Centrality) [Diff: -1.025]
  - Relative Improvement: **77.1%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.758 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.780 (Betweenness Centrality) [Diff: -0.475]
  - Relative Improvement: **60.9%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.699 (Large Effect)

**Conclusion**: Runtime FVS significantly outperformed Betweenness Centrality in containment effectiveness.

---

### 🛡️ Runtime FVS vs. PageRank

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.340 (PageRank) [Diff: -0.035]
  - Relative Improvement: **10.3%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.8137, Significant: **No**)
  - Effect Size (Rank-biserial): -0.034 (Negligible Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.968 (PageRank) [Diff: 0.007]
  - Relative Improvement: **0.7%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.8352, Significant: **No**)
  - Effect Size (Rank-biserial): -0.029 (Negligible Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 12.505 (PageRank) [Diff: 0.035]
  - Relative Improvement: **0.3%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.8137, Significant: **No**)
  - Effect Size (Rank-biserial): 0.034 (Negligible Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.555 (PageRank) [Diff: -0.250]
  - Relative Improvement: **45.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.2897, Significant: **No**)
  - Effect Size (Rank-biserial): -0.148 (Small Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.330 (PageRank) [Diff: -0.025]
  - Relative Improvement: **7.6%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.8137, Significant: **No**)
  - Effect Size (Rank-biserial): -0.034 (Negligible Effect)

**Conclusion**: No statistically significant difference in containment effectiveness was observed between Runtime FVS and PageRank.

---

### 🛡️ Runtime FVS vs. Supervisor Only

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 1.500 (Supervisor Only) [Diff: -1.195]
  - Relative Improvement: **79.7%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.889 (Supervisor Only) [Diff: 0.085]
  - Relative Improvement: **9.5%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 11.345 (Supervisor Only) [Diff: 1.195]
  - Relative Improvement: **10.5%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 1.910 (Supervisor Only) [Diff: -1.605]
  - Relative Improvement: **84.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 1.370 (Supervisor Only) [Diff: -1.065]
  - Relative Improvement: **77.7%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

**Conclusion**: Runtime FVS significantly outperformed Supervisor Only in containment effectiveness.

---

### 🛡️ Runtime FVS vs. Department Isolation

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 3.805 (Department Isolation) [Diff: -3.500]
  - Relative Improvement: **92.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.647 (Department Isolation) [Diff: 0.327]
  - Relative Improvement: **50.5%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 9.040 (Department Isolation) [Diff: 3.500]
  - Relative Improvement: **38.7%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 6.795 (Department Isolation) [Diff: -6.490]
  - Relative Improvement: **95.5%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 2.820 (Department Isolation) [Diff: -2.515]
  - Relative Improvement: **89.2%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

**Conclusion**: Runtime FVS significantly outperformed Department Isolation in containment effectiveness.

---

### 🛡️ Runtime FVS vs. Static FVS

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.575 (Static FVS) [Diff: -0.270]
  - Relative Improvement: **47.0%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.432 (Medium Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 0.947 (Static FVS) [Diff: 0.027]
  - Relative Improvement: **2.9%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.0142, Significant: **Yes**)
  - Effect Size (Rank-biserial): 0.323 (Medium Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 12.270 (Static FVS) [Diff: 0.270]
  - Relative Improvement: **2.2%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 0.432 (Medium Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.940 (Static FVS) [Diff: -0.635]
  - Relative Improvement: **67.6%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.506 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.490 (Static FVS) [Diff: -0.185]
  - Relative Improvement: **37.8%**
  - Test: Wilcoxon signed-rank (adjusted $p$ = 0.0047, Significant: **Yes**)
  - Effect Size (Rank-biserial): -0.371 (Medium Effect)

**Conclusion**: Runtime FVS significantly outperformed Static FVS in containment effectiveness.

---

### 🛡️ Runtime FVS vs. Oracle Compromised Node

- **K After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.000 (Oracle Compromised Node) [Diff: 0.305]
  - Relative Improvement: **-inf%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Containment Ratio**:
  - Mean: 0.974 (Runtime FVS) vs. 1.000 (Oracle Compromised Node) [Diff: -0.026]
  - Relative Improvement: **-2.6%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Containment Gain**:
  - Mean: 12.540 (Runtime FVS) vs. 12.845 (Oracle Compromised Node) [Diff: -0.305]
  - Relative Improvement: **-2.4%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): -1.000 (Large Effect)

- **Message Count After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.000 (Oracle Compromised Node) [Diff: 0.305]
  - Relative Improvement: **-inf%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

- **Propagation Depth After**:
  - Mean: 0.305 (Runtime FVS) vs. 0.000 (Oracle Compromised Node) [Diff: 0.305]
  - Relative Improvement: **-inf%**
  - Test: Wilcoxon signed-rank (adjusted $p$ < 0.001, Significant: **Yes**)
  - Effect Size (Rank-biserial): 1.000 (Large Effect)

**Conclusion**: Oracle Compromised Node achieved significantly different containment levels (e.g. oracle compromised node isolation).

---

## 📊 LaTeX Publication Tables

### LaTeX Table: Statistical Significance and Effect Sizes
```latex
\begin{table}[ht]
\centering
\caption{Paired Statistical Significance Comparisons of Runtime FVS against Baselines}
\begin{tabular}{llrrrrrc}
\hline
Baseline & Metric & FVS Mean & Base Mean & Mean Diff & adj. $p$-val & Effect Size & Sig. \\
\hline
No Containment & K After & 0.305 & 12.845 & -12.540 & $< 0.001$ & -1.000 (large) & Yes \\
No Containment & Containment Ratio & 0.974 & 0.000 & 0.974 & $< 0.001$ & 1.000 (large) & Yes \\
No Containment & Containment Gain & 12.540 & 0.000 & 12.540 & $< 0.001$ & 1.000 (large) & Yes \\
No Containment & Message Count After & 0.305 & 22.210 & -21.905 & $< 0.001$ & -1.000 (large) & Yes \\
No Containment & Propagation Depth After & 0.305 & 6.400 & -6.095 & $< 0.001$ & -1.000 (large) & Yes \\
Random Revocation & K After & 0.305 & 3.822 & -3.517 & $< 0.001$ & -1.000 (large) & Yes \\
Random Revocation & Containment Ratio & 0.974 & 0.669 & 0.305 & $< 0.001$ & 1.000 (large) & Yes \\
Random Revocation & Containment Gain & 12.540 & 9.023 & 3.517 & $< 0.001$ & 1.000 (large) & Yes \\
Random Revocation & Message Count After & 0.305 & 6.007 & -5.702 & $< 0.001$ & -1.000 (large) & Yes \\
Random Revocation & Propagation Depth After & 0.305 & 2.546 & -2.240 & $< 0.001$ & -3.343 (large) & Yes \\
Degree Centrality & K After & 0.305 & 0.930 & -0.625 & $< 0.001$ & -0.801 (large) & Yes \\
Degree Centrality & Containment Ratio & 0.974 & 0.922 & 0.053 & $< 0.001$ & 0.883 (large) & Yes \\
Degree Centrality & Containment Gain & 12.540 & 11.915 & 0.625 & $< 0.001$ & 0.801 (large) & Yes \\
Degree Centrality & Message Count After & 0.305 & 1.145 & -0.840 & $< 0.001$ & -0.836 (large) & Yes \\
Degree Centrality & Propagation Depth After & 0.305 & 0.920 & -0.615 & $< 0.001$ & -0.799 (large) & Yes \\
Betweenness Centrality & K After & 0.305 & 0.825 & -0.520 & $< 0.001$ & -0.700 (large) & Yes \\
Betweenness Centrality & Containment Ratio & 0.974 & 0.920 & 0.054 & $< 0.001$ & 0.651 (large) & Yes \\
Betweenness Centrality & Containment Gain & 12.540 & 12.020 & 0.520 & $< 0.001$ & 0.700 (large) & Yes \\
Betweenness Centrality & Message Count After & 0.305 & 1.330 & -1.025 & $< 0.001$ & -0.758 (large) & Yes \\
Betweenness Centrality & Propagation Depth After & 0.305 & 0.780 & -0.475 & $< 0.001$ & -0.699 (large) & Yes \\
PageRank & K After & 0.305 & 0.340 & -0.035 & 0.8137 & -0.034 (negligible) & No \\
PageRank & Containment Ratio & 0.974 & 0.968 & 0.007 & 0.8352 & -0.029 (negligible) & No \\
PageRank & Containment Gain & 12.540 & 12.505 & 0.035 & 0.8137 & 0.034 (negligible) & No \\
PageRank & Message Count After & 0.305 & 0.555 & -0.250 & 0.2897 & -0.148 (small) & No \\
PageRank & Propagation Depth After & 0.305 & 0.330 & -0.025 & 0.8137 & -0.034 (negligible) & No \\
Supervisor Only & K After & 0.305 & 1.500 & -1.195 & $< 0.001$ & -1.000 (large) & Yes \\
Supervisor Only & Containment Ratio & 0.974 & 0.889 & 0.085 & $< 0.001$ & 1.000 (large) & Yes \\
Supervisor Only & Containment Gain & 12.540 & 11.345 & 1.195 & $< 0.001$ & 1.000 (large) & Yes \\
Supervisor Only & Message Count After & 0.305 & 1.910 & -1.605 & $< 0.001$ & -1.000 (large) & Yes \\
Supervisor Only & Propagation Depth After & 0.305 & 1.370 & -1.065 & $< 0.001$ & -1.000 (large) & Yes \\
Department Isolation & K After & 0.305 & 3.805 & -3.500 & $< 0.001$ & -1.000 (large) & Yes \\
Department Isolation & Containment Ratio & 0.974 & 0.647 & 0.327 & $< 0.001$ & 1.000 (large) & Yes \\
Department Isolation & Containment Gain & 12.540 & 9.040 & 3.500 & $< 0.001$ & 1.000 (large) & Yes \\
Department Isolation & Message Count After & 0.305 & 6.795 & -6.490 & $< 0.001$ & -1.000 (large) & Yes \\
Department Isolation & Propagation Depth After & 0.305 & 2.820 & -2.515 & $< 0.001$ & -1.000 (large) & Yes \\
Static FVS & K After & 0.305 & 0.575 & -0.270 & $< 0.001$ & -0.432 (medium) & Yes \\
Static FVS & Containment Ratio & 0.974 & 0.947 & 0.027 & 0.0142 & 0.323 (medium) & Yes \\
Static FVS & Containment Gain & 12.540 & 12.270 & 0.270 & $< 0.001$ & 0.432 (medium) & Yes \\
Static FVS & Message Count After & 0.305 & 0.940 & -0.635 & $< 0.001$ & -0.506 (large) & Yes \\
Static FVS & Propagation Depth After & 0.305 & 0.490 & -0.185 & 0.0047 & -0.371 (medium) & Yes \\
Oracle Compromised Node & K After & 0.305 & 0.000 & 0.305 & $< 0.001$ & 1.000 (large) & Yes \\
Oracle Compromised Node & Containment Ratio & 0.974 & 1.000 & -0.026 & $< 0.001$ & -1.000 (large) & Yes \\
Oracle Compromised Node & Containment Gain & 12.540 & 12.845 & -0.305 & $< 0.001$ & -1.000 (large) & Yes \\
Oracle Compromised Node & Message Count After & 0.305 & 0.000 & 0.305 & $< 0.001$ & 1.000 (large) & Yes \\
Oracle Compromised Node & Propagation Depth After & 0.305 & 0.000 & 0.305 & $< 0.001$ & 1.000 (large) & Yes \\
\hline
\end{tabular}
\label{tab:statistical_significance}
\end{table}
```
