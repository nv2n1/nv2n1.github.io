---
title: "quantlib_svd(3)"
name: "quantlib_svd"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_svd/"
description: "QuantLib::SVD – Singular value decomposition."
---

<p>QuantLib::SVD &#8211; Singular value decomposition. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/matrixutilities/svd.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>SVD</code> (const <code>Matrix</code> &amp;) </p>
<p> const <code>Matrix</code> &amp; <code>U</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>V</code> () const </p>
<p> const <code>Array</code> &amp; <code>singularValues</code> () const </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>S</code> () const </p>
<p> <code>Real</code> <code>norm2</code> () </p>
<p> <code>Real</code> <code>cond</code> () </p>
<p> <code>Integer</code> <code>rank</code> () </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>solveFor</code> (const <code>Array</code> &amp;) const </p>
<h2>Detailed Description</h2>
<p>Singular value decomposition. </p>
<p> Refer to Golub and Van Loan: <code>Matrix</code> computation, The Johns Hopkins University Press </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>the correctness of the returned values is tested by checking their properties.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
