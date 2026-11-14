---
title: "slasq5-f(3)"
name: "slasq5-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasq5-f/"
description: "slasq5.f –"
---

<p>slasq5.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasq5</code> (I0, N0, Z, PP, TAU, SIGMA, DMIN, DMIN1, DMIN2, DN, DNM1, DNM2, IEEE, EPS)<br />
 <i></i><code>SLASQ5</code> computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasq5 (integerI0, integerN0, real, dimension( * )Z, integerPP, realTAU, realSIGMA, realDMIN, realDMIN1, realDMIN2, realDN, realDNM1, realDNM2, logicalIEEE, realEPS)</h3>
<p><code>SLASQ5</code> computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASQ5 computes one dqds transform in ping-pong form, one
 version for IEEE machines another for non IEEE machines.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>I0</i> </p>
<pre> I0 is INTEGER
 First index.</pre>
<p><i>N0</i> </p>
<pre> N0 is INTEGER
 Last index.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension ( 4*N )
 Z holds the qd array. EMIN is stored in Z(4*N0) to avoid
 an extra argument.</pre>
<p><i>PP</i> </p>
<pre> PP is INTEGER
 PP=0 for ping, PP=1 for pong.</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL
 This is the shift.</pre>
<p><i>DMIN</i> </p>
<pre> DMIN is REAL
 Minimum value of d.</pre>
<p><i>DMIN1</i> </p>
<pre> DMIN1 is REAL
 Minimum value of d, excluding D( N0 ).</pre>
<p><i>DMIN2</i> </p>
<pre> DMIN2 is REAL
 Minimum value of d, excluding D( N0 ) and D( N0-1 ).</pre>
<p><i>DN</i> </p>
<pre> DN is REAL
 d(N0), the last value of d.</pre>
<p><i>DNM1</i> </p>
<pre> DNM1 is REAL
 d(N0-1).</pre>
<p><i>DNM2</i> </p>
<pre> DNM2 is REAL
 d(N0-2).</pre>
<p><i>IEEE</i> </p>
<pre> IEEE is LOGICAL
 Flag for IEEE or non IEEE arithmetic.</pre>
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
<p> Definition at line 132 of file slasq5.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
