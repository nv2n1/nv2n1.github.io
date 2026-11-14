---
title: "iterations(3)"
name: "iterations"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iterations/"
description: "QuantLib::TqrEigenDecomposition – tridiag. QR eigen decomposition with explicite shift aka Wilkinson"
---

<h2 class="name">NAME</h2>
<p> QuantLib::TqrEigenDecomposition &#8211; tridiag. QR eigen decomposition with explicite shift aka Wilkinson </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/matrixutilities/tqreigendecomposition.hpp&gt; </p>
<h3>Public Types</h3>
<p> enum <code>EigenVectorCalculation</code> { <code>WithEigenVector</code>, <code>WithoutEigenVector</code>, <code>OnlyFirstRowEigenVector</code> } </p>
<p> enum <code>ShiftStrategy</code> { <code>NoShift</code>, <code>Overrelaxation</code>, <code>CloseEigenValue</code> } </p>
<h3>Public Member Functions</h3>
<p> <code>TqrEigenDecomposition</code> (const <code>Array</code> &amp;diag, const <code>Array</code> &amp;sub, EigenVectorCalculation calc=WithEigenVector, ShiftStrategy strategy=CloseEigenValue) </p>
<p> const <code>Array</code> &amp; <code>eigenvalues</code> () const </p>
<p> const <code>Matrix</code> &amp; <code>eigenvectors</code> () const </p>
<p> Size <code>iterations</code> () const </p>
<h2>Detailed Description</h2>
<p> tridiag. QR eigen decomposition with explicite shift aka Wilkinson </p>
<p> References: </p>
<p> Wilkinson, J.H. and Reinsch, C. 1971, <code>Linear</code> Algebra, vol. II of Handbook for Automatic Computation (New York: Springer-Verlag) </p>
<p> <code>Tests</code></p>
<dl>
<dt>
<dd> the correctness of the result is tested by checking it against known good values.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
