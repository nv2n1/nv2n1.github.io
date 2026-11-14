---
title: "zgesc2(3)"
name: "zgesc2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgesc2/"
description: "zgesc2.f –"
---

<p>zgesc2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgesc2</code> (N, A, LDA, RHS, IPIV, JPIV, SCALE)<br />
 <i></i><code>ZGESC2</code> solves a system of linear equations using the LU factorization with complete pivoting computed by sgetc2.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgesc2 (integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )RHS, integer, dimension( * )IPIV, integer, dimension( * )JPIV, double precisionSCALE)</h3>
<p><code>ZGESC2</code> solves a system of linear equations using the LU factorization with complete pivoting computed by sgetc2. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGESC2 solves a system of linear equations
 A * X = scale* RHS
 with a general N-by-N matrix A using the LU factorization with
 complete pivoting computed by ZGETC2.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA, N)
 On entry, the LU part of the factorization of the n-by-n
 matrix A computed by ZGETC2: A = P * L * U * Q</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1, N).</pre>
<p><i>RHS</i> </p>
<pre> RHS is COMPLEX*16 array, dimension N.
 On entry, the right hand side vector b.
 On exit, the solution vector X.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N).
 The pivot indices; for 1 &lt;= i &lt;= N, row i of the
 matrix has been interchanged with row IPIV(i).</pre>
<p><i>JPIV</i> </p>
<pre> JPIV is INTEGER array, dimension (N).
 The pivot indices; for 1 &lt;= j &lt;= N, column j of the
 matrix has been interchanged with column JPIV(j).</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE PRECISION
 On exit, SCALE contains the scale factor. SCALE is chosen
 0 &lt;= SCALE &lt;= 1 to prevent owerflow in the solution.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> Definition at line 116 of file zgesc2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
