---
title: "eigenvalues(3)"
name: "eigenvalues"
section: "3"
letter: "e"
url: "/docs/linux/man/3-eigenvalues/"
description: "QuantLib::SymmetricSchurDecomposition – symmetric threshold Jacobi algorithm."
---

<h2 class="name">NAME</h2>
<p> QuantLib::SymmetricSchurDecomposition &#8211; symmetric threshold Jacobi algorithm. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/matrixutilities/symmetricschurdecomposition.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p> <code>SymmetricSchurDecomposition</code> (const <code>Matrix</code> &amp;s) </p>
<p> const <code>Array</code> &amp; <code>eigenvalues</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>eigenvectors</code> () const </p>
<h2>Detailed Description</h2>
<p> symmetric threshold Jacobi algorithm. </p>
<p> Given a real symmetric matrix S, the Schur decomposition finds the eigenvalues and eigenvectors of S. If D is the diagonal matrix formed by the eigenvalues and U the unitarian matrix of the eigenvectors we can write the Schur decomposition as [ S = U dot D dot U^T , ,] where $ dot $ is the standard matrix product and $ ^T $ is the transpose operator. This class implements the Schur decomposition using the symmetric threshold Jacobi algorithm. For details on the different Jacobi transfomations see &#8216;Matrix computation,&#8217; second edition, by Golub and Van Loan, The Johns Hopkins University Press</p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> the correctness of the returned values is tested by checking their properties.</dl>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>SymmetricSchurDecomposition</code> (const <code>Matrix</code> &amp; s)</h3>
<p> <code>Precondition:</code></p>
<dl>
<dt>
<dd> s must be symmetric</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
