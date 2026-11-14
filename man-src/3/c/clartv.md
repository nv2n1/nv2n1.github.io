---
title: "clartv(3)"
name: "clartv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clartv/"
description: "clartv.f –"
---

<h2 class="name">NAME</h2>
<p> clartv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clartv</code> (N, X, INCX, Y, INCY, C, S, INCC)<br />
 <i></i><code>CLARTV</code> applies a vector of plane rotations with real cosines and complex sines to the elements of a pair of vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clartv (integerN, complex, dimension( * )X, integerINCX, complex, dimension( * )Y, integerINCY, real, dimension( * )C, complex, dimension( * )S, integerINCC)</h3>
<p> <code>CLARTV</code> applies a vector of plane rotations with real cosines and complex sines to the elements of a pair of vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLARTV applies a vector of complex plane rotations with real cosines
 to elements of the complex vectors x and y. For i = 1,2,...,n
    ( x(i) ) := (        c(i)   s(i) ) ( x(i) )
    ( y(i) )    ( -conjg(s(i))  c(i) ) ( y(i) )
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of plane rotations to be applied.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (1+(N-1)*INCX)
          The vector x.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between elements of X. INCX &gt; 0.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array, dimension (1+(N-1)*INCY)
          The vector y.
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
          The increment between elements of Y. INCY &gt; 0.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (1+(N-1)*INCC)
          The cosines of the plane rotations.
</pre>
<p> <i>S</i> </p>
<pre>
          S is COMPLEX array, dimension (1+(N-1)*INCC)
          The sines of the plane rotations.
</pre>
<p> <i>INCC</i> </p>
<pre>
          INCC is INTEGER
          The increment between elements of C and S. INCC &gt; 0.
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
<p> Definition at line 108 of file clartv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
