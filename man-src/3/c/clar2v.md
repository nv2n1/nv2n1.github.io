---
title: "clar2v(3)"
name: "clar2v"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clar2v/"
description: "clar2v.f –"
---

<h2 class="name">NAME</h2>
<p> clar2v.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clar2v</code> (N, X, Y, Z, INCX, C, S, INCC)<br />
 <i></i><code>CLAR2V</code> applies a vector of plane rotations with real cosines and complex sines from both sides to a sequence of 2-by-2 symmetric/Hermitian matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clar2v (integerN, complex, dimension( * )X, complex, dimension( * )Y, complex, dimension( * )Z, integerINCX, real, dimension( * )C, complex, dimension( * )S, integerINCC)</h3>
<p> <code>CLAR2V</code> applies a vector of plane rotations with real cosines and complex sines from both sides to a sequence of 2-by-2 symmetric/Hermitian matrices. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLAR2V applies a vector of complex plane rotations with real cosines
 from both sides to a sequence of 2-by-2 complex Hermitian matrices,
 defined by the elements of the vectors x, y and z. For i = 1,2,...,n
    (       x(i)  z(i) ) :=
    ( conjg(z(i)) y(i) )
      (  c(i) conjg(s(i)) ) (       x(i)  z(i) ) ( c(i) -conjg(s(i)) )
      ( -s(i)       c(i)  ) ( conjg(z(i)) y(i) ) ( s(i)        c(i)  )
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
          The vector x; the elements of x are assumed to be real.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array, dimension (1+(N-1)*INCX)
          The vector y; the elements of y are assumed to be real.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is COMPLEX array, dimension (1+(N-1)*INCX)
          The vector z.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between elements of X, Y and Z. INCX &gt; 0.
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
<p> Definition at line 112 of file clar2v.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
