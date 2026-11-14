---
title: "slar2v-f(3)"
name: "slar2v-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slar2v-f/"
description: "slar2v.f –"
---

<p>slar2v.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slar2v</code> (N, X, Y, Z, INCX, C, S, INCC)<br />
 <i></i><code>SLAR2V</code> applies a vector of plane rotations with real cosines and real sines from both sides to a sequence of 2-by-2 symmetric/Hermitian matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slar2v (integerN, real, dimension( * )X, real, dimension( * )Y, real, dimension( * )Z, integerINCX, real, dimension( * )C, real, dimension( * )S, integerINCC)</h3>
<p><code>SLAR2V</code> applies a vector of plane rotations with real cosines and real sines from both sides to a sequence of 2-by-2 symmetric/Hermitian matrices. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAR2V applies a vector of real plane rotations from both sides to
 a sequence of 2-by-2 real symmetric matrices, defined by the elements
 of the vectors x, y and z. For i = 1,2,...,n
 ( x(i) z(i) ) := ( c(i) s(i) ) ( x(i) z(i) ) ( c(i) -s(i) )
 ( z(i) y(i) ) ( -s(i) c(i) ) ( z(i) y(i) ) ( s(i) c(i) )</pre>
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
<p><i>Y</i> </p>
<pre> Y is REAL array,
 dimension (1+(N-1)*INCX)
 The vector y.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array,
 dimension (1+(N-1)*INCX)
 The vector z.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between elements of X, Y and Z. INCX &gt; 0.</pre>
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
<p> Definition at line 111 of file slar2v.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
