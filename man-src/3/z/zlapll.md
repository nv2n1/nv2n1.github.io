---
title: "zlapll(3)"
name: "zlapll"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlapll/"
description: "zlapll.f –"
---

<p>zlapll.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlapll</code> (N, X, INCX, Y, INCY, SSMIN)<br />
 <i></i><code>ZLAPLL</code> measures the linear dependence of two vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlapll (integerN, complex*16, dimension( * )X, integerINCX, complex*16, dimension( * )Y, integerINCY, double precisionSSMIN)</h3>
<p><code>ZLAPLL</code> measures the linear dependence of two vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Given two column vectors X and Y, let
 A = ( X Y ).
 The subroutine first computes the QR factorization of A = Q*R,
 and then computes the SVD of the 2-by-2 upper triangular matrix R.
 The smaller singular value of R is returned in SSMIN, which is used
 as the measurement of the linear dependency of the vectors X and Y.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The length of the vectors X and Y.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (1+(N-1)*INCX)
 On entry, X contains the N-vector X.
 On exit, X is overwritten.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive elements of X. INCX &gt; 0.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16 array, dimension (1+(N-1)*INCY)
 On entry, Y contains the N-vector Y.
 On exit, Y is overwritten.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 The increment between successive elements of Y. INCY &gt; 0.</pre>
<p><i>SSMIN</i> </p>
<pre> SSMIN is DOUBLE PRECISION
 The smallest singular value of the N-by-2 matrix A = ( X Y ).</pre>
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
<p> Definition at line 101 of file zlapll.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
