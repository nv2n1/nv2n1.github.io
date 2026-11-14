---
title: "zlassq(3)"
name: "zlassq"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlassq/"
description: "zlassq.f –"
---

<p>zlassq.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlassq</code> (N, X, INCX, SCALE, SUMSQ)<br />
 <i></i><code>ZLASSQ</code> updates a sum of squares represented in scaled form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlassq (integerN, complex*16, dimension( * )X, integerINCX, double precisionSCALE, double precisionSUMSQ)</h3>
<p><code>ZLASSQ</code> updates a sum of squares represented in scaled form. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLASSQ returns the values scl and ssq such that
 ( scl**2 )*ssq = x( 1 )**2 +...+ x( n )**2 + ( scale**2 )*sumsq,
 where x( i ) = abs( X( 1 + ( i - 1 )*INCX ) ). The value of sumsq is
 assumed to be at least unity and the value of ssq will then satisfy
 1.0 .le. ssq .le. ( sumsq + 2*n ).
 scale is assumed to be non-negative and scl returns the value
 scl = max( scale, abs( real( x( i ) ) ), abs( aimag( x( i ) ) ) ),
 i
 scale and sumsq must be supplied in SCALE and SUMSQ respectively.
 SCALE and SUMSQ are overwritten by scl and ssq respectively.
 The routine makes only one pass through the vector X.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of elements to be used from the vector X.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (N)
 The vector x as described above.
 x( i ) = X( 1 + ( i - 1 )*INCX ), 1 &lt;= i &lt;= n.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive values of the vector X.
 INCX &gt; 0.</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE PRECISION
 On entry, the value scale in the equation above.
 On exit, SCALE is overwritten with the value scl .</pre>
<p><i>SUMSQ</i> </p>
<pre> SUMSQ is DOUBLE PRECISION
 On entry, the value sumsq in the equation above.
 On exit, SUMSQ is overwritten with the value ssq .</pre>
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
<p> Definition at line 107 of file zlassq.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
