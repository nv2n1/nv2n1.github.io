---
title: "dlarfgp-f(3)"
name: "dlarfgp-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarfgp-f/"
description: "dlarfgp.f –"
---

<p>dlarfgp.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlarfgp</code> (N, ALPHA, X, INCX, TAU)<br />
 <i></i><code>DLARFGP</code> generates an elementary reflector (Householder matrix) with non-negatibe beta.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarfgp (integerN, double precisionALPHA, double precision, dimension( * )X, integerINCX, double precisionTAU)</h3>
<p><code>DLARFGP</code> generates an elementary reflector (Householder matrix) with non-negatibe beta. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLARFGP generates a real elementary reflector H of order n, such
 that
 H * ( alpha ) = ( beta ), H**T * H = I.
 ( x ) ( 0 )
 where alpha and beta are scalars, beta is non-negative, and x is
 an (n-1)-element real vector. H is represented in the form
 H = I - tau * ( 1 ) * ( 1 v**T ) ,
 ( v )
 where tau is a real scalar and v is a real (n-1)-element
 vector.
 If the elements of x are all zero, then tau = 0 and H is taken to be
 the unit matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the elementary reflector.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is DOUBLE PRECISION
 On entry, the value alpha.
 On exit, it is overwritten with the value beta.</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array, dimension
 (1+(N-2)*abs(INCX))
 On entry, the vector x.
 On exit, it is overwritten with the vector v.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 The increment between elements of X. INCX &gt; 0.</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION
 The value tau.</pre>
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
<p> Definition at line 105 of file dlarfgp.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
