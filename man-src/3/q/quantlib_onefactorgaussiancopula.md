---
title: "quantlib_onefactorgaussiancopula(3)"
name: "quantlib_onefactorgaussiancopula"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_onefactorgaussiancopula/"
description: "QuantLib::OneFactorGaussianCopula – One-factor Gaussian Copula."
---

<p>QuantLib::OneFactorGaussianCopula &#8211; One-factor Gaussian Copula. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/experimental/credit/onefactorgaussiancopula.hpp&gt; </p>
<p> Inherits <code>QuantLib::OneFactorCopula</code>. </p>
<h3>Public Member Functions</h3>
<p><code>OneFactorGaussianCopula</code> (const <code>Handle</code>&lt; <code>Quote</code> &gt; &amp;correlation, Real maximum=5, Size integrationSteps=50) </p>
<p> Real <code>density</code> (Real m) const<br />
 <i>Density function of M. </i><br />
 Real <code>cumulativeZ</code> (Real z) const<br />
 <i>Cumulative distribution of Z. </i><br />
 Real <code>cumulativeY</code> (Real y) const </p>
<p> Real <code>testCumulativeY</code> (Real y) const </p>
<p> Real <code>inverseCumulativeY</code> (Real p) const </p>
<h2>Detailed Description</h2>
<p>One-factor Gaussian Copula. </p>
<p> The copula model [ Y_i = a_i,M+qrt{1-a_i^2}:Z_i ] is specified here by setting the desnity function for all variables, $ M, Z,$ and also $ Y $ to the standard normal distribution $<br />
 hi(x) = \xp(-x^2/2) / qrt{2<br />
 i}. $  </p>
<h2>Member Function Documentation</h2>
<h3>Real density (Real m) const [virtual]</h3>
<p> Density function of M. </p>
<p> Derived classes must override this method and ensure zero mean and unit variance. </p>
<p> Implements <code>OneFactorCopula</code>.  </p>
<h3>Real cumulativeZ (Real z) const [virtual]</h3>
<p> Cumulative distribution of Z. </p>
<p> Derived classes must override this method and ensure zero mean and unit variance. </p>
<p> Implements <code>OneFactorCopula</code>.  </p>
<h3>Real cumulativeY (Real y) const [virtual]</h3>
<p> overrides the base class implementation based on table data </p>
<p> Reimplemented from <code>OneFactorCopula</code>.  </p>
<h3>Real inverseCumulativeY (Real p) const [virtual]</h3>
<p> overrides the base class implementation based on table data </p>
<p> Reimplemented from <code>OneFactorCopula</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
