---
title: "clargv(3)"
name: "clargv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clargv/"
description: "clargv.f –"
---

<h2 class="name">NAME</h2>
<p> clargv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clargv</code> (N, X, INCX, Y, INCY, C, INCC)<br />
 <i></i><code>CLARGV</code> generates a vector of plane rotations with real cosines and complex sines.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clargv (integerN, complex, dimension( * )X, integerINCX, complex, dimension( * )Y, integerINCY, real, dimension( * )C, integerINCC)</h3>
<p> <code>CLARGV</code> generates a vector of plane rotations with real cosines and complex sines. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLARGV generates a vector of complex plane rotations with real
 cosines, determined by elements of the complex vectors x and y.
 For i = 1,2,...,n
    (        c(i)   s(i) ) ( x(i) ) = ( r(i) )
    ( -conjg(s(i))  c(i) ) ( y(i) ) = (   0  )
    where c(i)**2 + ABS(s(i))**2 = 1
 The following conventions are used (these are the same as in CLARTG,
 but differ from the BLAS1 routine CROTG):
    If y(i)=0, then c(i)=1 and s(i)=0.
    If x(i)=0, then c(i)=0 and s(i) is chosen so that r(i) is real.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of plane rotations to be generated.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (1+(N-1)*INCX)
          On entry, the vector x.
          On exit, x(i) is overwritten by r(i), for i = 1,...,n.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between elements of X. INCX &gt; 0.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array, dimension (1+(N-1)*INCY)
          On entry, the vector y.
          On exit, the sines of the plane rotations.
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
<p> <i>INCC</i> </p>
<pre>
          INCC is INTEGER
          The increment between elements of C. INCC &gt; 0.
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  6-6-96 - Modified with a new algorithm by W. Kahan and J. Demmel
  This version has a few statements commented out for thread safety
  (machine parameters are computed on each entry). 10 feb 03, SJH.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 123 of file clargv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
