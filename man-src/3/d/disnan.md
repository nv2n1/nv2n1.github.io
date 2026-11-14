---
title: "disnan(3)"
name: "disnan"
section: "3"
letter: "d"
url: "/docs/linux/man/3-disnan/"
description: "disnan.f –"
---

<h2 class="name">NAME</h2>
<p> disnan.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> LOGICAL function <code>disnan</code> (DIN)<br />
 <i></i><code>DISNAN</code> tests input for NaN.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>LOGICAL function disnan (double precisionDIN)</h3>
<p> <code>DISNAN</code> tests input for NaN. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DISNAN returns .TRUE. if its argument is NaN, and .FALSE.
 otherwise.  To be replaced by the Fortran 2003 intrinsic in the
 future.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>DIN</i> </p>
<pre>
          DIN is DOUBLE PRECISION
          Input to test for NaN.
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
<p> Definition at line 60 of file disnan.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
