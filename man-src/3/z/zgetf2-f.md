---
title: "zgetf2-f(3)"
name: "zgetf2-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgetf2-f/"
description: "zgetf2.f –"
---

<p>zgetf2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgetf2</code> (M, N, A, LDA, IPIV, INFO)<br />
 <i></i><code>ZGETF2</code> computes the LU factorization of a general m-by-n matrix using partial pivoting with row interchanges (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgetf2 (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, integerINFO)</h3>
<p><code>ZGETF2</code> computes the LU factorization of a general m-by-n matrix using partial pivoting with row interchanges (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGETF2 computes an LU factorization of a general m-by-n matrix A
 using partial pivoting with row interchanges.
 The factorization has the form
 A = P * L * U
 where P is a permutation matrix, L is lower triangular with unit
 diagonal elements (lower trapezoidal if m &gt; n), and U is upper
 triangular (upper trapezoidal if m &lt; n).
 This is the right-looking Level 2 BLAS version of the algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the m by n matrix to be factored.
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
 &lt; 0: if INFO = -k, the k-th argument had an illegal value
 &gt; 0: if INFO = k, U(k,k) is exactly zero. The factorization
 has been completed, but the factor U is exactly
 singular, and division by zero will occur if it is used
 to solve a system of equations.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 109 of file zgetf2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
