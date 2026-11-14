---
title: "dlasq4-f(3)"
name: "dlasq4-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq4-f/"
description: "dlasq4.f –"
---

<p>dlasq4.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasq4</code> (I0, N0, Z, PP, N0IN, DMIN, DMIN1, DMIN2, DN, DN1, DN2, TAU, TTYPE, G)<br />
 <i></i><code>DLASQ4</code> computes an approximation to the smallest eigenvalue using values of d from the previous transform. Used by sbdsqr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasq4 (integerI0, integerN0, double precision, dimension( * )Z, integerPP, integerN0IN, double precisionDMIN, double precisionDMIN1, double precisionDMIN2, double precisionDN, double precisionDN1, double precisionDN2, double precisionTAU, integerTTYPE, double precisionG)</h3>
<p> <code>DLASQ4</code> computes an approximation to the smallest eigenvalue using values of d from the previous transform. Used by sbdsqr. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 DLASQ4 computes an approximation TAU to the smallest eigenvalue
 using values of d from the previous transform.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>I0</i> </p>
<pre>
          I0 is INTEGER
        First index.
</pre>
<p> <i>N0</i> </p>
<pre>
          N0 is INTEGER
        Last index.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension ( 4*N )
        Z holds the qd array.
</pre>
<p> <i>PP</i> </p>
<pre>
          PP is INTEGER
        PP=0 for ping, PP=1 for pong.
</pre>
<p> <i>N0IN</i> </p>
<pre>
          N0IN is INTEGER
        The value of N0 at start of EIGTEST.
</pre>
<p> <i>DMIN</i> </p>
<pre>
          DMIN is DOUBLE PRECISION
        Minimum value of d.
</pre>
<p> <i>DMIN1</i> </p>
<pre>
          DMIN1 is DOUBLE PRECISION
        Minimum value of d, excluding D( N0 ).
</pre>
<p> <i>DMIN2</i> </p>
<pre>
          DMIN2 is DOUBLE PRECISION
        Minimum value of d, excluding D( N0 ) and D( N0-1 ).
</pre>
<p> <i>DN</i> </p>
<pre>
          DN is DOUBLE PRECISION
        d(N)
</pre>
<p> <i>DN1</i> </p>
<pre>
          DN1 is DOUBLE PRECISION
        d(N-1)
</pre>
<p> <i>DN2</i> </p>
<pre>
          DN2 is DOUBLE PRECISION
        d(N-2)
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION
        This is the shift.
</pre>
<p> <i>TTYPE</i> </p>
<pre>
          TTYPE is INTEGER
        Shift type.
</pre>
<p> <i>G</i> </p>
<pre>
          G is REAL
        G is passed as an argument in order to save its value between
        calls to DLASQ4.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> September 2012</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
  CNST1 = 9/16
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 151 of file dlasq4.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
