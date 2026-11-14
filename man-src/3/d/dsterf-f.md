---
title: "dsterf-f(3)"
name: "dsterf-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsterf-f/"
description: "dsterf.f –"
---

<p>dsterf.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dsterf</code> (N, D, E, INFO)<br />
 <i></i><code>DSTERF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsterf (integerN, double precision, dimension( * )D, double precision, dimension( * )E, integerINFO)</h3>
<p><code>DSTERF</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSTERF computes all eigenvalues of a symmetric tridiagonal matrix
 using the Pal-Walker-Kahan variant of the QL or QR algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the n diagonal elements of the tridiagonal matrix.
 On exit, if INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
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
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 87 of file dsterf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
