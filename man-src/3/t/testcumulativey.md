---
title: "testcumulativey(3)"
name: "testcumulativey"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testcumulativey/"
description: "QuantLib::OneFactorGaussianCopula – One-factor Gaussian Copula."
---

<p>QuantLib::OneFactorGaussianCopula &#8211; One-factor Gaussian Copula. </p>
<h2>Synopsis</h2>
<pre><code>OneFactorGaussianCopula (const Handle&lt; Quote &gt; &amp;correlation, Real maximum=5, Size integrationSteps=50)



Real density (Real m) const


Density function of M.


Real cumulativeZ (Real z) const


Cumulative distribution of Z.


Real cumulativeY (Real y) const



Real testCumulativeY (Real y) const



Real inverseCumulativeY (Real p) const</code></pre>
<p> Inherits <code>QuantLib::OneFactorCopula</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>OneFactorGaussianCopula (const Handle&lt; Quote &gt; &amp;correlation, Real maximum=5, Size integrationSteps=50)



Real density (Real m) const


Density function of M.


Real cumulativeZ (Real z) const


Cumulative distribution of Z.


Real cumulativeY (Real y) const



Real testCumulativeY (Real y) const



Real inverseCumulativeY (Real p) const</code></pre>
<h2>Detailed Description</h2>
<p>One-factor Gaussian Copula. </p>
<p> The copula model [ Y_i = a_i,M+qrt{1-a_i^2}:Z_i ] is specified here by setting the desnity function for all variables, $ M, Z,$ and also $ Y $ to the standard normal distribution $<br />
 hi(x) = 
