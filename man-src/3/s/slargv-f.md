---
title: "slargv-f(3)"
name: "slargv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slargv-f/"
description: "slargv.f –"
---

<p>slargv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slargv</code> (N, X, INCX, Y, INCY, C, INCC)<br />
 <i></i><code>SLARGV</code> generates a vector of plane rotations with real cosines and real sines.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slargv (integerN, real, dimension( * )X, integerINCX, real, dimension( * )Y, integerINCY, real, dimension( * )C, integerINCC)</h3>
<p><code>SLARGV</code> generates a vector of plane rotations with real cosines and real sines. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLARGV generates a vector of real plane rotations, determined by
 elements of the real vectors x and y. For i = 1,2,...,n
 ( c(i) s(i) ) ( x(i) ) = ( a(i) )
 ( -s(i) c(i) ) ( y(i) ) = ( 0 )</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of plane rotations to be generated.</pre>
<p><i>X</i> </p>
<pre> X is REAL array,
 dimension (1+(N-1)*INCX)
 On entry, the vector x.
 On exit, x(i) is overwritten by a(i), for i = 1,...,n.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between elements of X. INCX &gt; 0.</pre>
<p><i>Y</i> </p>
<pre> Y is REAL array,
 dimension (1+(N-1)*INCY)
 On entry, the vector y.
 On exit, the sines of the plane rotations.</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 The increment between elements of Y. INCY &gt; 0.</pre>
<p><i>C</i> </p>
<pre> C is REAL array, dimension (1+(N-1)*INCC)
 The cosines of the plane rotations.</pre>
<p><i>INCC</i> </p>
<pre> INCC is INTEGER
 The increment between elements of C. INCC &gt; 0.</pre>
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
<p> Definition at line 105 of file slargv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
