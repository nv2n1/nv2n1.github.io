---
title: "slartv-f(3)"
name: "slartv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slartv-f/"
description: "slartv.f –"
---

<p>slartv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slartv</code> (N, X, INCX, Y, INCY, C, S, INCC)<br />
 <i></i><code>SLARTV</code> applies a vector of plane rotations with real cosines and real sines to the elements of a pair of vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slartv (integerN, real, dimension( * )X, integerINCX, real, dimension( * )Y, integerINCY, real, dimension( * )C, real, dimension( * )S, integerINCC)</h3>
<p><code>SLARTV</code> applies a vector of plane rotations with real cosines and real sines to the elements of a pair of vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLARTV applies a vector of real plane rotations to elements of the
 real vectors x and y. For i = 1,2,...,n
 ( x(i) ) := ( c(i) s(i) ) ( x(i) )
 ( y(i) ) ( -s(i) c(i) ) ( y(i) )</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of plane rotations to be applied.</pre>
<p><i>X</i> </p>
<pre> X is REAL array,
 dimension (1+(N-1)*INCX)
 The vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between elements of X. INCX &gt; 0.</pre>
<p><i>Y</i> </p>
<pre> Y is REAL array,
 dimension (1+(N-1)*INCY)
 The vector y.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 The increment between elements of Y. INCY &gt; 0.</pre>
<p><i>C</i> </p>
<pre> C is REAL array, dimension (1+(N-1)*INCC)
 The cosines of the plane rotations.</pre>
<p><i>S</i> </p>
<pre> S is REAL array, dimension (1+(N-1)*INCC)
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
<p> Definition at line 109 of file slartv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
