---
title: "sisnan(3)"
name: "sisnan"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sisnan/"
description: "sisnan.f –"
---

<h2 class="name">NAME</h2>
<p> sisnan.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> LOGICAL function <code>sisnan</code> (SIN)<br />
 <i></i><code>SISNAN</code> tests input for NaN.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>LOGICAL function sisnan (realSIN)</h3>
<p> <code>SISNAN</code> tests input for NaN. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SISNAN returns .TRUE. if its argument is NaN, and .FALSE.
 otherwise.  To be replaced by the Fortran 2003 intrinsic in the
 future.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIN</i> </p>
<pre>
          SIN is REAL
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
<p> Definition at line 60 of file sisnan.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
