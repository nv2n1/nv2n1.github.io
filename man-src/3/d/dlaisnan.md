---
title: "dlaisnan(3)"
name: "dlaisnan"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaisnan/"
description: "dlaisnan.f –"
---

<h2 class="name">NAME</h2>
<p> dlaisnan.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> LOGICAL function <code>dlaisnan</code> (DIN1, DIN2)<br />
 <i></i><code>DLAISNAN</code> tests input for NaN by comparing two arguments for inequality.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>LOGICAL function dlaisnan (double precisionDIN1, double precisionDIN2)</h3>
<p> <code>DLAISNAN</code> tests input for NaN by comparing two arguments for inequality. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 This routine is not for general use.  It exists solely to avoid
 over-optimization in DISNAN.
 DLAISNAN checks for NaNs by comparing its two arguments for
 inequality.  NaN is the only floating-point value where NaN != NaN
 returns .TRUE.  To check for NaNs, pass the same variable as both
 arguments.
 A compiler must assume that the two arguments are
 not the same variable, and the test will not be optimized away.
 Interprocedural or whole-program optimization may delete this
 test.  The ISNAN functions will be replaced by the correct
 Fortran 03 intrinsic once the intrinsic is widely available.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>DIN1</i> </p>
<pre>
          DIN1 is DOUBLE PRECISION
</pre>
<p> <i>DIN2</i> </p>
<pre>
          DIN2 is DOUBLE PRECISION
          Two numbers to compare for inequality.
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
<p> Definition at line 75 of file dlaisnan.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
