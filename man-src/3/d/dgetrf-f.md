---
title: "dgetrf-f(3)"
name: "dgetrf-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgetrf-f/"
description: "dgetrf.f –"
---

<p>dgetrf.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgetrf</code> (M, N, A, LDA, IPIV, INFO)<br />
 <i></i><code>DGETRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgetrf (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, integerINFO)</h3>
<p><code>DGETRF</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGETRF computes an LU factorization of a general M-by-N matrix A
 using partial pivoting with row interchanges.
 The factorization has the form
 A = P * L * U
 where P is a permutation matrix, L is lower triangular with unit
 diagonal elements (lower trapezoidal if m &gt; n), and U is upper
 triangular (upper trapezoidal if m &lt; n).
 This is the right-looking Level 3 BLAS version of the algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the M-by-N matrix to be factored.
 On exit, the factors L and U from the factorization
 A = P*L*U; the unit diagonal elements of L are not stored.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (min(M,N))
 The pivot indices; for 1 &lt;= i &lt;= min(M,N), row i of the
 matrix was interchanged with row IPIV(i).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, U(i,i) is exactly zero. The factorization
 has been completed, but the factor U is exactly
 singular, and division by zero will occur if it is used
 to solve a system of equations.</pre>
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
<p> Definition at line 109 of file dgetrf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
