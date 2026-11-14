---
title: "clanht-f(3)"
name: "clanht-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clanht-f/"
description: "clanht.f –"
---

<p>clanht.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>clanht</code> (NORM, N, D, E)<br />
 <i></i><code>CLANHT</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a complex Hermitian tridiagonal matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function clanht (characterNORM, integerN, real, dimension( * )D, complex, dimension( * )E)</h3>
<p><code>CLANHT</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a complex Hermitian tridiagonal matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLANHT returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 complex Hermitian tridiagonal matrix A.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>CLANHT </p>
<pre> CLANHT = ( max(abs(A(i,j))), NORM = 'M' or 'm'
 (
 ( norm1(A), NORM = '1', 'O' or 'o'
 (
 ( normI(A), NORM = 'I' or 'i'
 (
 ( normF(A), NORM = 'F', 'f', 'E' or 'e'
 where norm1 denotes the one norm of a matrix (maximum column sum),
 normI denotes the infinity norm of a matrix (maximum row sum) and
 normF denotes the Frobenius norm of a matrix (square root of sum of
 squares). Note that max(abs(A(i,j))) is not a consistent matrix norm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>NORM</i> </p>
<pre> NORM is CHARACTER*1
 Specifies the value to be returned in CLANHT as described
 above.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0. When N = 0, CLANHT is
 set to zero.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 The diagonal elements of A.</pre>
<p><i>E</i> </p>
<pre> E is COMPLEX array, dimension (N-1)
 The (n-1) sub-diagonal or super-diagonal elements of A.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 102 of file clanht.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
