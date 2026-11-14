---
title: "onefactorgaussianstudentcopula(3)"
name: "onefactorgaussianstudentcopula"
section: "3"
letter: "o"
url: "/docs/linux/man/3-onefactorgaussianstudentcopula/"
description: "QuantLib::OneFactorGaussianStudentCopula – One-factor Gaussian-Student t-Copula."
---

<p>QuantLib::OneFactorGaussianStudentCopula &#8211; One-factor Gaussian-Student t-Copula. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/onefactorstudentcopula.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorCopula</code>. </p>
<h3>Public Member Functions</h3>
<p><code>OneFactorGaussianStudentCopula</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;correlation, int nz, Real maximum=10, Size integrationSteps=200) </p>
<p> Real <code>density</code> (Real m) const<br />
 <i>Density function of M. </i><br />
 Real <code>cumulativeZ</code> (Real z) const<br />
 <i>Cumulative distribution of Z. </i></p>
<h2>Detailed Description</h2>
<p>One-factor Gaussian-Student t-Copula. </p>
<p> The copula model [ Y_i = a_i,M+qrt{1-a_i^2}:Z_i ] </p>
<p> is specified here by setting the probability density functions for $ Z_i $ ($ D_Z $) to a Student t-distributions with $ N_z $ degrees of freedom, and for $ M $ ($ D_M $) to a Gaussian. </p>
<p> The variance of the Student t-distribution with $ $ degrees of freedom is $ / ( &#8211; 2) $. Since the copula approach requires zero mean and unit variance distributions, $ Z $ is scaled by $ qrt{(N_z &#8211; 2) / N_z}.$ </p>
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
