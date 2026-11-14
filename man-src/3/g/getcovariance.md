---
title: "getcovariance(3)"
name: "getcovariance"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getcovariance/"
description: "ql/math/matrixutilities/getcovariance.hpp – Covariance matrix calculation."
---

<h2 class="name">NAME</h2>
<p> ql/math/matrixutilities/getcovariance.hpp &#8211; Covariance matrix calculation. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/matrix.hpp&gt;<br />
 #include &lt;ql/utilities/dataformatters.hpp&gt;<br />
 #include &lt;ql/math/matrixutilities/pseudosqrt.hpp&gt; </p>
<h3>Classes</h3>
<p> class <code>CovarianceDecomposition</code><br />
 <i>Covariance decomposition into correlation and variances. </i></p>
<h3>Functions</h3>
<p> template&lt;class DataIterator &gt; Disposable&lt; Matrix &gt; <code>getCovariance</code> (DataIterator stdDevBegin, DataIterator stdDevEnd, const Matrix &amp;corr, Real tolerance=1.0e-12)<br />
 <i>Calculation of covariance from correlation and standard deviations. </i></p>
<h2>Detailed Description</h2>
<p> Covariance matrix calculation. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
