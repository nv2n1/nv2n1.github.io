---
title: "slasq4(3)"
name: "slasq4"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasq4/"
description: "slasq4.f –"
---

<h2 class="name">NAME</h2>
<p> slasq4.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slasq4</code> (I0, N0, Z, PP, N0IN, DMIN, DMIN1, DMIN2, DN, DN1, DN2, TAU, TTYPE, G)<br />
 <i></i><code>SLASQ4</code> computes an approximation to the smallest eigenvalue using values of d from the previous transform. Used by sbdsqr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasq4 (integerI0, integerN0, real, dimension( * )Z, integerPP, integerN0IN, realDMIN, realDMIN1, realDMIN2, realDN, realDN1, realDN2, realTAU, integerTTYPE, realG)</h3>
<p> <code>SLASQ4</code> computes an approximation to the smallest eigenvalue using values of d from the previous transform. Used by sbdsqr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLASQ4 computes an approximation TAU to the smallest eigenvalue
 using values of d from the previous transform.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
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
          Z is REAL array, dimension ( 4*N )
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
          DMIN is REAL
        Minimum value of d.
</pre>
<p> <i>DMIN1</i> </p>
<pre>
          DMIN1 is REAL
        Minimum value of d, excluding D( N0 ).
</pre>
<p> <i>DMIN2</i> </p>
<pre>
          DMIN2 is REAL
        Minimum value of d, excluding D( N0 ) and D( N0-1 ).
</pre>
<p> <i>DN</i> </p>
<pre>
          DN is REAL
        d(N)
</pre>
<p> <i>DN1</i> </p>
<pre>
          DN1 is REAL
        d(N-1)
</pre>
<p> <i>DN2</i> </p>
<pre>
          DN2 is REAL
        d(N-2)
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is REAL
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
        calls to SLASQ4.
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
  CNST1 = 9/16
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 151 of file slasq4.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
