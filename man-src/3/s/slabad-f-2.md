---
title: "slabad-f-2(3)"
name: "slabad-f-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slabad-f-2/"
description: "slabad.f –"
---

<p>slabad.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slabad</code> (SMALL, LARGE)<br />
 <i></i><code>SLABAD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slabad (realSMALL, realLARGE)</h3>
<p><code>SLABAD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLABAD takes as input the values computed by SLAMCH for underflow and
 overflow, and returns the square root of each of these values if the
 log of LARGE is sufficiently large. This subroutine is intended to
 identify machines with a large exponent range, such as the Crays, and
 redefine the underflow and overflow limits to be the square roots of
 the values computed by SLAMCH. This subroutine is needed because
 SLAMCH does not compensate for poor arithmetic in the upper half of
 the exponent range, as is found on a Cray.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SMALL</i> </p>
<pre> SMALL is REAL
 On entry, the underflow threshold as computed by SLAMCH.
 On exit, if LOG10(LARGE) is sufficiently large, the square
 root of SMALL, otherwise unchanged.</pre>
<p><i>LARGE</i> </p>
<pre> LARGE is REAL
 On entry, the overflow threshold as computed by SLAMCH.
 On exit, if LOG10(LARGE) is sufficiently large, the square
 root of LARGE, otherwise unchanged.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 75 of file slabad.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
