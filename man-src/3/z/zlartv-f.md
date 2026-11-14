---
title: "zlartv-f(3)"
name: "zlartv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlartv-f/"
description: "zlartv.f –"
---

<p>zlartv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlartv</code> (N, X, INCX, Y, INCY, C, S, INCC)<br />
 <i></i><code>ZLARTV</code> applies a vector of plane rotations with real cosines and complex sines to the elements of a pair of vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlartv (integerN, complex*16, dimension( * )X, integerINCX, complex*16, dimension( * )Y, integerINCY, double precision, dimension( * )C, complex*16, dimension( * )S, integerINCC)</h3>
<p><code>ZLARTV</code> applies a vector of plane rotations with real cosines and complex sines to the elements of a pair of vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLARTV applies a vector of complex plane rotations with real cosines
 to elements of the complex vectors x and y. For i = 1,2,...,n
 ( x(i) ) := ( c(i) s(i) ) ( x(i) )
 ( y(i) ) ( -conjg(s(i)) c(i) ) ( y(i) )</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of plane rotations to be applied.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (1+(N-1)*INCX)
 The vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between elements of X. INCX &gt; 0.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16 array, dimension (1+(N-1)*INCY)
 The vector y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 The increment between elements of Y. INCY &gt; 0.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (1+(N-1)*INCC)
 The cosines of the plane rotations.</pre>
<p><i>S</i> </p>
<pre> S is COMPLEX*16 array, dimension (1+(N-1)*INCC)
 The sines of the plane rotations.</pre>
<p><i>INCC</i> </p>
<pre> INCC is INTEGER
 The increment between elements of C and S. INCC &gt; 0.</pre>
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
<p> Definition at line 108 of file zlartv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
