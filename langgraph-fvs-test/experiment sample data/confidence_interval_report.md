# Confidence Interval Validation Report

This report verifies the statistical correctness of the confidence intervals reported in the experimental results.

## 📐 Statistical Formulas

The standard formula for computing a $95\%$ confidence interval using the Student $t$-distribution is:

\[CI_{95\%} = \bar{x} \pm t_{\text{crit}} \times \frac{s}{\sqrt{n}}\]

Where:
- $\bar{x}$ is the sample mean.
- $s$ is the sample standard deviation (with $df = n-1$).
- $n$ is the sample size (number of runs, $200$).
- $t_{\text{crit}}$ is the critical value from the Student $t$-distribution with $n-1$ degrees of freedom. For $n=200$, $df=199$ and $t_{\text{crit}, 0.025} \approx 1.972$.

Previously, the summary table reported confidence intervals based on the standard normal approximation:

\[CI_{\text{normal}} = \bar{x} \pm 1.96 \times \frac{s}{\sqrt{n}}\]

---

## 🔬 Validation Log

We compared the recomputed Student $t$ confidence intervals against the currently reported intervals in `overall_comparison.csv`. The validation results are detailed below:

### 🛡️ No Containment — Containment Ratio
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ No Containment — Containment Gain
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ No Containment — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[12.108, 13.582]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[12.113, 13.577]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ No Containment — Message Count After
- **Reported CI**: `[21.034, 23.386]`
- **Recomputed Student $t$ CI**: `[21.026, 23.394]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[21.034, 23.386]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.007553`)

### 🛡️ No Containment — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[6.078, 6.722]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[6.080, 6.720]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ No Containment — FVS Size
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ No Containment — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000128`)

### 🛡️ Random Revocation — Containment Ratio
- **Reported CI**: `[0.653, 0.685]`
- **Recomputed Student $t$ CI**: `[0.653, 0.685]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.653, 0.685]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000320`)

### 🛡️ Random Revocation — Containment Gain
- **Reported CI**: `[8.366, 9.679]`
- **Recomputed Student $t$ CI**: `[8.362, 9.683]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[8.366, 9.679]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.003650`)

### 🛡️ Random Revocation — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[3.663, 3.982]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.664, 3.981]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Random Revocation — Message Count After
- **Reported CI**: `[5.751, 6.264]`
- **Recomputed Student $t$ CI**: `[5.749, 6.266]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[5.751, 6.264]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001954`)

### 🛡️ Random Revocation — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[2.468, 2.623]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[2.469, 2.622]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Random Revocation — FVS Size
- **Reported CI**: `[3.420, 3.730]`
- **Recomputed Student $t$ CI**: `[3.419, 3.731]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.420, 3.730]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000936`)

### 🛡️ Random Revocation — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000066`)

### 🛡️ Degree Centrality — Containment Ratio
- **Reported CI**: `[0.908, 0.935]`
- **Recomputed Student $t$ CI**: `[0.908, 0.935]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.908, 0.935]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000388`)

### 🛡️ Degree Centrality — Containment Gain
- **Reported CI**: `[11.184, 12.646]`
- **Recomputed Student $t$ CI**: `[11.180, 12.650]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[11.184, 12.646]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004422`)

### 🛡️ Degree Centrality — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.778, 1.082]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.779, 1.081]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Degree Centrality — Message Count After
- **Reported CI**: `[0.949, 1.341]`
- **Recomputed Student $t$ CI**: `[0.948, 1.342]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.949, 1.341]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001393`)

### 🛡️ Degree Centrality — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.772, 1.068]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.773, 1.067]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Degree Centrality — FVS Size
- **Reported CI**: `[3.420, 3.730]`
- **Recomputed Student $t$ CI**: `[3.419, 3.731]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.420, 3.730]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000936`)

### 🛡️ Degree Centrality — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000100`)

### 🛡️ Betweenness Centrality — Containment Ratio
- **Reported CI**: `[0.896, 0.944]`
- **Recomputed Student $t$ CI**: `[0.896, 0.944]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.896, 0.944]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000460`)

### 🛡️ Betweenness Centrality — Containment Gain
- **Reported CI**: `[11.277, 12.763]`
- **Recomputed Student $t$ CI**: `[11.272, 12.768]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[11.277, 12.763]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004960`)

### 🛡️ Betweenness Centrality — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.634, 1.016]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.635, 1.015]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Betweenness Centrality — Message Count After
- **Reported CI**: `[1.017, 1.643]`
- **Recomputed Student $t$ CI**: `[1.016, 1.644]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[1.017, 1.643]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001480`)

### 🛡️ Betweenness Centrality — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.604, 0.956]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.605, 0.955]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Betweenness Centrality — FVS Size
- **Reported CI**: `[3.420, 3.730]`
- **Recomputed Student $t$ CI**: `[3.419, 3.731]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.420, 3.730]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000936`)

### 🛡️ Betweenness Centrality — Runtime Execution Time
- **Reported CI**: `[0.000, 0.001]`
- **Recomputed Student $t$ CI**: `[0.000, 0.001]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.001]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000473`)

### 🛡️ PageRank — Containment Ratio
- **Reported CI**: `[0.953, 0.982]`
- **Recomputed Student $t$ CI**: `[0.953, 0.982]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.953, 0.982]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000115`)

### 🛡️ PageRank — Containment Gain
- **Reported CI**: `[11.756, 13.254]`
- **Recomputed Student $t$ CI**: `[11.751, 13.259]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[11.756, 13.254]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004561`)

### 🛡️ PageRank — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.195, 0.485]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.196, 0.484]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ PageRank — Message Count After
- **Reported CI**: `[0.324, 0.786]`
- **Recomputed Student $t$ CI**: `[0.323, 0.787]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.324, 0.786]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001106`)

### 🛡️ PageRank — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.197, 0.463]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.198, 0.462]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ PageRank — FVS Size
- **Reported CI**: `[3.420, 3.730]`
- **Recomputed Student $t$ CI**: `[3.419, 3.731]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.420, 3.730]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000936`)

### 🛡️ PageRank — Runtime Execution Time
- **Reported CI**: `[-0.001, 0.013]`
- **Recomputed Student $t$ CI**: `[-0.002, 0.014]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[-0.001, 0.013]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000530`)

### 🛡️ Supervisor Only — Containment Ratio
- **Reported CI**: `[0.874, 0.905]`
- **Recomputed Student $t$ CI**: `[0.873, 0.905]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.874, 0.905]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000545`)

### 🛡️ Supervisor Only — Containment Gain
- **Reported CI**: `[10.703, 11.987]`
- **Recomputed Student $t$ CI**: `[10.699, 11.991]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[10.703, 11.987]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.003694`)

### 🛡️ Supervisor Only — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[1.288, 1.712]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[1.290, 1.710]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Supervisor Only — Message Count After
- **Reported CI**: `[1.639, 2.181]`
- **Recomputed Student $t$ CI**: `[1.637, 2.183]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[1.639, 2.181]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001566`)

### 🛡️ Supervisor Only — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[1.185, 1.555]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[1.186, 1.554]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Supervisor Only — FVS Size
- **Reported CI**: `[3.194, 3.456]`
- **Recomputed Student $t$ CI**: `[3.193, 3.457]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.194, 3.456]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000830`)

### 🛡️ Supervisor Only — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000091`)

### 🛡️ Department Isolation — Containment Ratio
- **Reported CI**: `[0.621, 0.674]`
- **Recomputed Student $t$ CI**: `[0.621, 0.674]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.621, 0.674]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000142`)

### 🛡️ Department Isolation — Containment Gain
- **Reported CI**: `[8.323, 9.757]`
- **Recomputed Student $t$ CI**: `[8.319, 9.761]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[8.323, 9.757]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004210`)

### 🛡️ Department Isolation — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[3.648, 3.962]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.649, 3.961]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Department Isolation — Message Count After
- **Reported CI**: `[6.543, 7.047]`
- **Recomputed Student $t$ CI**: `[6.541, 7.049]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[6.543, 7.047]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001668`)

### 🛡️ Department Isolation — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[2.689, 2.951]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[2.690, 2.950]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Department Isolation — FVS Size
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Department Isolation — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000098`)

### 🛡️ Static FVS — Containment Ratio
- **Reported CI**: `[0.930, 0.964]`
- **Recomputed Student $t$ CI**: `[0.930, 0.964]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.930, 0.964]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000342`)

### 🛡️ Static FVS — Containment Gain
- **Reported CI**: `[11.530, 13.010]`
- **Recomputed Student $t$ CI**: `[11.526, 13.014]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[11.530, 13.010]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004129`)

### 🛡️ Static FVS — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.412, 0.738]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.413, 0.737]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Static FVS — Message Count After
- **Reported CI**: `[0.673, 1.207]`
- **Recomputed Student $t$ CI**: `[0.672, 1.208]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.673, 1.207]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001394`)

### 🛡️ Static FVS — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.351, 0.629]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.352, 0.628]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Static FVS — FVS Size
- **Reported CI**: `[4.000, 4.340]`
- **Recomputed Student $t$ CI**: `[3.999, 4.341]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[4.000, 4.340]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.001268`)

### 🛡️ Static FVS — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000089`)

### 🛡️ Oracle Compromised Node — Containment Ratio
- **Reported CI**: `[1.000, 1.000]`
- **Recomputed Student $t$ CI**: `[1.000, 1.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[1.000, 1.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Oracle Compromised Node — Containment Gain
- **Reported CI**: `[12.113, 13.577]`
- **Recomputed Student $t$ CI**: `[12.108, 13.582]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[12.113, 13.577]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004526`)

### 🛡️ Oracle Compromised Node — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Oracle Compromised Node — Message Count After
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Oracle Compromised Node — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Oracle Compromised Node — FVS Size
- **Reported CI**: `[1.000, 1.000]`
- **Recomputed Student $t$ CI**: `[1.000, 1.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[1.000, 1.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Oracle Compromised Node — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000217`)

### 🛡️ Runtime FVS — Containment Ratio
- **Reported CI**: `[0.968, 0.980]`
- **Recomputed Student $t$ CI**: `[0.968, 0.980]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.968, 0.980]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000342`)

### 🛡️ Runtime FVS — Containment Gain
- **Reported CI**: `[11.810, 13.270]`
- **Recomputed Student $t$ CI**: `[11.806, 13.274]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[11.810, 13.270]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.004366`)

### 🛡️ Runtime FVS — K After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.235, 0.375]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.235, 0.375]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Runtime FVS — Message Count After
- **Reported CI**: `[0.235, 0.375]`
- **Recomputed Student $t$ CI**: `[0.235, 0.375]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.235, 0.375]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000170`)

### 🛡️ Runtime FVS — Propagation Depth After
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[0.235, 0.375]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.235, 0.375]`
- **Status**: **Not Reported in Summary** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Runtime FVS — FVS Size
- **Reported CI**: `[3.420, 3.730]`
- **Recomputed Student $t$ CI**: `[3.419, 3.731]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[3.420, 3.730]`
- **Status**: **Precision discrepancy (using Normal approximation instead of Student t)** (Absolute difference vs. Student $t$: `0.000936`)

### 🛡️ Runtime FVS — Runtime Execution Time
- **Reported CI**: `[0.000, 0.000]`
- **Recomputed Student $t$ CI**: `[0.000, 0.000]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[0.000, 0.000]`
- **Status**: **Pass** (Absolute difference vs. Student $t$: `0.000084`)

### 🛡️ Runtime FVS (Before) — K Before
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[12.108, 13.582]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[12.113, 13.577]`
- **Status**: **Verified (Not reported in baseline comparisons summary)** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Runtime FVS (Before) — Message Count Before
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[21.026, 23.394]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[21.034, 23.386]`
- **Status**: **Verified (Not reported in baseline comparisons summary)** (Absolute difference vs. Student $t$: `0.000000`)

### 🛡️ Runtime FVS (Before) — Propagation Depth Before
- **Reported CI**: `N/A`
- **Recomputed Student $t$ CI**: `[6.078, 6.722]` (using $t_{\text{crit}} = 1.9720$)
- **Recomputed Normal CI**: `[6.080, 6.720]`
- **Status**: **Verified (Not reported in baseline comparisons summary)** (Absolute difference vs. Student $t$: `0.000000`)

---

## 📈 Recommendation
The reported intervals in the summary comparison table match the recomputed Normal approximation confidence intervals with $100\%$ precision. However, to maintain the highest statistical rigor, we recommend updating all publication summaries to use the recomputed Student $t$-distribution intervals since the sample size $n=200$ is finite and the Student $t$-distribution provides the mathematically exact interval.
