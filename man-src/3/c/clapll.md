---
title: "clapll(3)"
name: "clapll"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clapll/"
description: "clapll.f –"
---

<h2 class="name">NAME</h2>
<p> clapll.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clapll</code> (N, X, INCX, Y, INCY, SSMIN)<br />
 <i></i><code>CLAPLL</code> measures the linear dependence of two vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clapll (integerN, complex, dimension( * )X, integerINCX, complex, dimension( * )Y, integerINCY, realSSMIN)</h3>
<p> <code>CLAPLL</code> measures the linear dependence of two vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 Given two column vectors X and Y, let
                      A = ( X Y ).
 The subroutine first computes the QR factorization of A = Q*R,
 and then computes the SVD of the 2-by-2 upper triangular matrix R.
 The smaller singular value of R is returned in SSMIN, which is used
 as the measurement of the linear dependency of the vectors X and Y.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The length of the vectors X and Y.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (1+(N-1)*INCX)
          On entry, X contains the N-vector X.
          On exit, X is overwritten.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between successive elements of X. INCX &gt; 0.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array, dimension (1+(N-1)*INCY)
          On entry, Y contains the N-vector Y.
          On exit, Y is overwritten.
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
          The increment between successive elements of Y. INCY &gt; 0.
</pre>
<p> <i>SSMIN</i> </p>
<pre>
          SSMIN is REAL
          The smallest singular value of the N-by-2 matrix A = ( X Y ).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> Definition at line 101 of file clapll.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
