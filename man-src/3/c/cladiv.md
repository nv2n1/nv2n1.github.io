---
title: "cladiv(3)"
name: "cladiv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cladiv/"
description: "cladiv.f –"
---

<h2 class="name">NAME</h2>
<p> cladiv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> COMPLEX function <code>cladiv</code> (X, Y)<br />
 <i></i><code>CLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>COMPLEX function cladiv (complexX, complexY)</h3>
<p> <code>CLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLADIV := X / Y, where X and Y are complex.  The computation of X / Y
 will not overflow on an intermediary step unless the results
 overflows.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>X</i> </p>
<pre>
          X is COMPLEX
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX
          The complex scalars X and Y.
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
<p> Definition at line 65 of file cladiv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
