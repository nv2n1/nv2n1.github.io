---
title: "quantlib_onefactorstudentcopula(3)"
name: "quantlib_onefactorstudentcopula"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_onefactorstudentcopula/"
description: "QuantLib::OneFactorStudentCopula – One-factor Double Student t-Copula."
---

<p>QuantLib::OneFactorStudentCopula &#8211; One-factor Double Student t-Copula. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/onefactorstudentcopula.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorCopula</code>. </p>
<h3>Public Member Functions</h3>
<p><code>OneFactorStudentCopula</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;correlation, int nz, int nm, Real maximum=10, Size integrationSteps=200) </p>
<p> Real <code>density</code> (Real m) const<br />
 <i>Density function of M. </i><br />
 Real <code>cumulativeZ</code> (Real z) const<br />
 <i>Cumulative distribution of Z. </i></p>
<h2>Detailed Description</h2>
<p>One-factor Double Student t-Copula. </p>
<p> The copula model [ Y_i = a_i,M+qrt{1-a_i^2}:Z_i ] </p>
<p> is specified here by setting the probability density functions for $ Z_i $ ($ D_Z $) and $ M $ ($ D_M $) to Student t-distributions with $ N_z $ and $ N_m $ degrees of freedom, respectively. </p>
<p> The variance of the Student t-distribution with $ $ degrees of freedom is $ / ( &#8211; 2) $. Since the copula approach requires zero mean and unit variance distributions, variables $ Z $ and $ M $ are scaled by $ qrt{(N_z &#8211; 2) / N_z} $ and $ qrt{(N_m &#8211; 2) / N_m}, $ respectively. </p>
<p> <code>Possible enhancements</code></p>
<dl COMPACT>
<dd>Improve performance/accuracy of the calculation of inverse cumulative Y. Tabulate and store it for selected correlations?</dl>
<h2>Member Function Documentation</h2>
<h3>Real density (Real m) const [virtual]</h3>
<p>Density function of M. </p>
<p> Derived classes must override this method and ensure zero mean and unit variance. </p>
<p> Implements <code>OneFactorCopula</code>.</p>
<h3>Real cumulativeZ (Real z) const [virtual]</h3>
<p>Cumulative distribution of Z. </p>
<p> Derived classes must override this method and ensure zero mean and unit variance. </p>
<p> Implements <code>OneFactorCopula</code>. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
