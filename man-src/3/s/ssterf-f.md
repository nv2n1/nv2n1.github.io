---
title: "ssterf-f(3)"
name: "ssterf-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssterf-f/"
description: "ssterf.f –"
---

<p>ssterf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssterf</code> (N, D, E, INFO)<br />
 <i></i><code>SSTERF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssterf (integerN, real, dimension( * )D, real, dimension( * )E, integerINFO)</h3>
<p><code>SSTERF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSTERF computes all eigenvalues of a symmetric tridiagonal matrix
 using the Pal-Walker-Kahan variant of the QL or QR algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the n diagonal elements of the tridiagonal matrix.
 On exit, if INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N-1)
 On entry, the (n-1) subdiagonal elements of the tridiagonal
 matrix.
 On exit, E has been destroyed.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: the algorithm failed to find all of the eigenvalues in
 a total of 30*N iterations; if INFO = i, then i
 elements of E have not converged to zero.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 87 of file ssterf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
