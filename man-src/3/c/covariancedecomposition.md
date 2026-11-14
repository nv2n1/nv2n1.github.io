---
title: "covariancedecomposition(3)"
name: "covariancedecomposition"
section: "3"
letter: "c"
url: "/docs/linux/man/3-covariancedecomposition/"
description: "QuantLib::CovarianceDecomposition – Covariance decomposition into correlation and variances."
---

<p>QuantLib::CovarianceDecomposition &#8211; Covariance decomposition into correlation and variances. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/matrixutilities/getcovariance.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>CovarianceDecomposition</code> (const <code>Matrix</code> &amp;covarianceMatrix, <code>Real</code> tolerance=1.0e-12, SalvagingAlgorithm::Type sa=SalvagingAlgorithm::None) </p>
<p> const <code>Array</code> &amp; <code>variances</code> () const </p>
<p> const <code>Array</code> &amp; <code>standardDeviations</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>correlationMatrix</code> () const </p>
<h2>Detailed Description</h2>
<p>Covariance decomposition into correlation and variances. </p>
<p> Extracts the correlation matrix and the vector of variances out of the input covariance matrix. </p>
<p> Note that only the lower symmetric part of the covariance matrix is used. </p>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>The covariance matrix must be symmetric.</dl>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>cross checked with getCovariance</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>CovarianceDecomposition</code> (const <code>Matrix</code> &amp; covarianceMatrix, <code>Real</code> tolerance = 1.0e-12, SalvagingAlgorithm::Type sa = SalvagingAlgorithm::None)</h3>
<p><code>Precondition:</code></p>
<dl COMPACT>
<dd>covarianceMatrix must be symmetric</dl>
<h2>Member Function Documentation</h2>
<h3>const <code>Array</code>&amp; variances () const</h3>
<p>returns the variances <code>Array</code></p>
<h3>const <code>Array</code>&amp; standardDeviations () const</h3>
<p>returns the standard deviations <code>Array</code></p>
<h3>const <code>Matrix</code>&amp; correlationMatrix () const</h3>
<p>returns the correlation matrix </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
