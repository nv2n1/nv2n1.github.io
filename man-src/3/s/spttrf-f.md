---
title: "spttrf-f(3)"
name: "spttrf-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spttrf-f/"
description: "spttrf.f –"
---

<p>spttrf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>spttrf</code> (N, D, E, INFO)<br />
 <i></i><code>SPTTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spttrf (integerN, real, dimension( * )D, real, dimension( * )E, integerINFO)</h3>
<p><code>SPTTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPTTRF computes the L*D*L**T factorization of a real symmetric
 positive definite tridiagonal matrix A. The factorization may also
 be regarded as having the form A = U**T*D*U.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the n diagonal elements of the tridiagonal matrix
 A. On exit, the n diagonal elements of the diagonal matrix
 D from the L*D*L**T factorization of A.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N-1)
 On entry, the (n-1) subdiagonal elements of the tridiagonal
 matrix A. On exit, the (n-1) subdiagonal elements of the
 unit bidiagonal factor L from the L*D*L**T factorization of A.
 E can also be regarded as the superdiagonal of the unit
 bidiagonal factor U from the U**T*D*U factorization of A.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -k, the k-th argument had an illegal value
 &gt; 0: if INFO = k, the leading minor of order k is not
 positive definite; if k &lt; N, the factorization could not
 be completed, while if k = N, the factorization was
 completed, but D(N) &lt;= 0.</pre>
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
<p> Definition at line 92 of file spttrf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
