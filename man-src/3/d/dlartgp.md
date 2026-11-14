---
title: "dlartgp(3)"
name: "dlartgp"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlartgp/"
description: "dlartgp.f –"
---

<h2 class="name">NAME</h2>
<p> dlartgp.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlartgp</code> (F, G, CS, SN, R)<br />
 <i></i><code>DLARTGP</code> generates a plane rotation so that the diagonal is nonnegative.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlartgp (double precisionF, double precisionG, double precisionCS, double precisionSN, double precisionR)</h3>
<p> <code>DLARTGP</code> generates a plane rotation so that the diagonal is nonnegative. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
DLARTGP generates a plane rotation so that
    [CS SN]
        .[F] = [R] where CS ** 2 + SN ** 2 = 1.
                   [-SN CS][G][0] This is a slower,
     more accurate version of the Level 1 BLAS routine DROTG,
     with the following other differences : F and G are unchanged on return.If G = 0, then CS = (+ / -)1 and SN = 0. If F = 0 and (G.ne.0), then CS = 0 and SN = (+ / -)1. The sign is chosen so that R &gt;= 0.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>F</i> </p>
<pre>
          F is DOUBLE PRECISION
          The first component of vector to be rotated.
</pre>
<p> <i>G</i> </p>
<pre>
          G is DOUBLE PRECISION
          The second component of vector to be rotated.
</pre>
<p> <i>CS</i> </p>
<pre>
          CS is DOUBLE PRECISION
          The cosine of the rotation.
</pre>
<p> <i>SN</i> </p>
<pre>
          SN is DOUBLE PRECISION
          The sine of the rotation.
</pre>
<p> <i>R</i> </p>
<pre>
          R is DOUBLE PRECISION
          The nonzero component of the rotated vector.
  This version has a few statements commented out for thread safety
  (machine parameters are computed on each entry). 10 feb 03, SJH.
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
<p> Definition at line 96 of file dlartgp.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
