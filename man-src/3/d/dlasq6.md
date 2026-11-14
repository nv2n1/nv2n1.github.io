---
title: "dlasq6(3)"
name: "dlasq6"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq6/"
description: "dlasq6.f –"
---

<h2 class="name">NAME</h2>
<p> dlasq6.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasq6</code> (I0, N0, Z, PP, DMIN, DMIN1, DMIN2, DN, DNM1, DNM2)<br />
 <i></i><code>DLASQ6</code> computes one dqd transform in ping-pong form. Used by sbdsqr and sstegr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasq6 (integerI0, integerN0, double precision, dimension( * )Z, integerPP, double precisionDMIN, double precisionDMIN1, double precisionDMIN2, double precisionDN, double precisionDNM1, double precisionDNM2)</h3>
<p> <code>DLASQ6</code> computes one dqd transform in ping-pong form. Used by sbdsqr and sstegr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLASQ6 computes one dqd (shift equal to zero) transform in
 ping-pong form, with protection against underflow and overflow.
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
<p> Definition at line 119 of file dlasq6.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
