---
title: "dlasq5(3)"
name: "dlasq5"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq5/"
description: "dlasq5.f –"
---

<h2 class="name">NAME</h2>
<p> dlasq5.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasq5</code> (I0, N0, Z, PP, TAU, SIGMA, DMIN, DMIN1, DMIN2, DN, DNM1, DNM2, IEEE, EPS)<br />
 <i></i><code>DLASQ5</code> computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasq5 (integerI0, integerN0, double precision, dimension( * )Z, integerPP, double precisionTAU, double precisionSIGMA, double precisionDMIN, double precisionDMIN1, double precisionDMIN2, double precisionDN, double precisionDNM1, double precisionDNM2, logicalIEEE, double precisionEPS)</h3>
<p> <code>DLASQ5</code> computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLASQ5 computes one dqds transform in ping-pong form, one
 version for IEEE machines another for non IEEE machines.
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
          Z is DOUBLE PRECISION array, dimension ( 4*N )
        Z holds the qd array. EMIN is stored in Z(4*N0) to avoid
        an extra argument.
</pre>
<p> <i>PP</i> </p>
<pre>
          PP is INTEGER
        PP=0 for ping, PP=1 for pong.
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION
        This is the shift.
</pre>
<p> <i>SIGMA</i> </p>
<pre>
          SIGMA is DOUBLE PRECISION
        This is the accumulated shift up to this step.
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
        d(N0), the last value of d.
</pre>
<p> <i>DNM1</i> </p>
<pre>
          DNM1 is DOUBLE PRECISION
        d(N0-1).
</pre>
<p> <i>DNM2</i> </p>
<pre>
          DNM2 is DOUBLE PRECISION
        d(N0-2).
</pre>
<p> <i>IEEE</i> </p>
<pre>
          IEEE is LOGICAL
        Flag for IEEE or non IEEE arithmetic.
</pre>
<p>&nbsp;<wbr><br />
 <i>EPS</i> </p>
<pre>
          EPS is DOUBLE PRECISION
        This is the value of epsilon used.
</pre>
</dl>
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
<p> Definition at line 144 of file dlasq5.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
