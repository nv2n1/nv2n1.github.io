---
title: "clartg(3)"
name: "clartg"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clartg/"
description: "clartg.f –"
---

<h2 class="name">NAME</h2>
<p> clartg.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clartg</code> (F, G, CS, SN, R)<br />
 <i></i><code>CLARTG</code> generates a plane rotation with real cosine and complex sine.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clartg (complexF, complexG, realCS, complexSN, complexR)</h3>
<p> <code>CLARTG</code> generates a plane rotation with real cosine and complex sine. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 CLARTG generates a plane rotation so that
    [  CS  SN  ]     [ F ]     [ R ]
    [  __      ]  .  [   ]  =  [   ]   where CS**2 + |SN|**2 = 1.
    [ -SN  CS  ]     [ G ]     [ 0 ]
 This is a faster version of the BLAS1 routine CROTG, except for
 the following differences:
    F and G are unchanged on return.
    If G=0, then CS=1 and SN=0.
    If F=0, then CS=0 and SN is chosen so that R is real.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>F</i> </p>
<pre>
          F is COMPLEX
          The first component of vector to be rotated.
</pre>
<p> <i>G</i> </p>
<pre>
          G is COMPLEX
          The second component of vector to be rotated.
</pre>
<p> <i>CS</i> </p>
<pre>
          CS is REAL
          The cosine of the rotation.
</pre>
<p> <i>SN</i> </p>
<pre>
          SN is COMPLEX
          The sine of the rotation.
</pre>
<p> <i>R</i> </p>
<pre>
          R is COMPLEX
          The nonzero component of the rotated vector.
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
<dd> November 2013</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  3-5-96 - Modified with a new algorithm by W. Kahan and J. Demmel
  This version has a few statements commented out for thread safety
  (machine parameters are computed on each entry). 10 feb 03, SJH.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 104 of file clartg.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
