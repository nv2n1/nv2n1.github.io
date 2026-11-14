---
title: "dlar2v-f(3)"
name: "dlar2v-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlar2v-f/"
description: "dlar2v.f –"
---

<p>dlar2v.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlar2v</code> (N, X, Y, Z, INCX, C, S, INCC)<br />
 <i></i><code>DLAR2V</code> applies a vector of plane rotations with real cosines and real sines from both sides to a sequence of 2-by-2 symmetric/Hermitian matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlar2v (integerN, double precision, dimension( * )X, double precision, dimension( * )Y, double precision, dimension( * )Z, integerINCX, double precision, dimension( * )C, double precision, dimension( * )S, integerINCC)</h3>
<p><code>DLAR2V</code> applies a vector of plane rotations with real cosines and real sines from both sides to a sequence of 2-by-2 symmetric/Hermitian matrices. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAR2V applies a vector of real plane rotations from both sides to
 a sequence of 2-by-2 real symmetric matrices, defined by the elements
 of the vectors x, y and z. For i = 1,2,...,n
 ( x(i) z(i) ) := ( c(i) s(i) ) ( x(i) z(i) ) ( c(i) -s(i) )
 ( z(i) y(i) ) ( -s(i) c(i) ) ( z(i) y(i) ) ( s(i) c(i) )</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of plane rotations to be applied.</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array,
 dimension (1+(N-1)*INCX)
 The vector x.</pre>
<p><i>Y</i> </p>
<pre> Y is DOUBLE PRECISION array,
 dimension (1+(N-1)*INCX)
 The vector y.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array,
 dimension (1+(N-1)*INCX)
 The vector z.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between elements of X, Y and Z. INCX &gt; 0.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (1+(N-1)*INCC)
 The cosines of the plane rotations.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (1+(N-1)*INCC)
 The sines of the plane rotations.</pre>
<p><i>INCC</i> </p>
<pre> INCC is INTEGER
 The increment between elements of C and S. INCC &gt; 0.</pre>
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
<p> Definition at line 111 of file dlar2v.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
