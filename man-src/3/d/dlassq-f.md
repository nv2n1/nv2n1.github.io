---
title: "dlassq-f(3)"
name: "dlassq-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlassq-f/"
description: "dlassq.f –"
---

<p>dlassq.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlassq</code> (N, X, INCX, SCALE, SUMSQ)<br />
 <i></i><code>DLASSQ</code> updates a sum of squares represented in scaled form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlassq (integerN, double precision, dimension( * )X, integerINCX, double precisionSCALE, double precisionSUMSQ)</h3>
<p><code>DLASSQ</code> updates a sum of squares represented in scaled form. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLASSQ returns the values scl and smsq such that
 ( scl**2 )*smsq = x( 1 )**2 +...+ x( n )**2 + ( scale**2 )*sumsq,
 where x( i ) = X( 1 + ( i - 1 )*INCX ). The value of sumsq is
 assumed to be non-negative and scl returns the value
 scl = max( scale, abs( x( i ) ) ).
 scale and sumsq must be supplied in SCALE and SUMSQ and
 scl and smsq are overwritten on SCALE and SUMSQ respectively.
 The routine makes only one pass through the vector x.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of elements to be used from the vector X.</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array, dimension (N)
 The vector for which a scaled sum of squares is computed.
 x( i ) = X( 1 + ( i - 1 )*INCX ), 1 &lt;= i &lt;= n.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between successive values of the vector X.
 INCX &gt; 0.</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE PRECISION
 On entry, the value scale in the equation above.
 On exit, SCALE is overwritten with scl , the scaling factor
 for the sum of squares.</pre>
<p><i>SUMSQ</i> </p>
<pre> SUMSQ is DOUBLE PRECISION
 On entry, the value sumsq in the equation above.
 On exit, SUMSQ is overwritten with smsq , the basic sum of
 squares from which scl has been factored out.</pre>
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
<p> Definition at line 104 of file dlassq.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
