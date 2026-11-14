---
title: "clarfgp(3)"
name: "clarfgp"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clarfgp/"
description: "clarfgp.f –"
---

<h2 class="name">NAME</h2>
<p> clarfgp.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clarfgp</code> (N, ALPHA, X, INCX, TAU)<br />
 <i></i><code>CLARFGP</code> generates an elementary reflector (Householder matrix) with non-negatibe beta.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clarfgp (integerN, complexALPHA, complex, dimension( * )X, integerINCX, complexTAU)</h3>
<p> <code>CLARFGP</code> generates an elementary reflector (Householder matrix) with non-negatibe beta. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLARFGP generates a complex elementary reflector H of order n, such
 that
       H**H * ( alpha ) = ( beta ),   H**H * H = I.
              (   x   )   (   0  )
 where alpha and beta are scalars, beta is real and non-negative, and
 x is an (n-1)-element complex vector.  H is represented in the form
       H = I - tau * ( 1 ) * ( 1 v**H ) ,
                     ( v )
 where tau is a complex scalar and v is a complex (n-1)-element
 vector. Note that H is not hermitian.
 If the elements of x are all zero and alpha is real, then tau = 0
 and H is taken to be the unit matrix.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the elementary reflector.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is COMPLEX
          On entry, the value alpha.
          On exit, it is overwritten with the value beta.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension
                         (1+(N-2)*abs(INCX))
          On entry, the vector x.
          On exit, it is overwritten with the vector v.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between elements of X. INCX &gt; 0.
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX
          The value tau.
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
<p> Definition at line 105 of file clarfgp.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
