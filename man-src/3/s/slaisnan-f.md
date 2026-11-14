---
title: "slaisnan-f(3)"
name: "slaisnan-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaisnan-f/"
description: "slaisnan.f –"
---

<p>slaisnan.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>LOGICAL function <code>slaisnan</code> (SIN1, SIN2)<br />
 <i></i><code>SLAISNAN</code> tests input for NaN by comparing two arguments for inequality.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>LOGICAL function slaisnan (realSIN1, realSIN2)</h3>
<p><code>SLAISNAN</code> tests input for NaN by comparing two arguments for inequality. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This routine is not for general use. It exists solely to avoid
 over-optimization in SISNAN.
 SLAISNAN checks for NaNs by comparing its two arguments for
 inequality. NaN is the only floating-point value where NaN != NaN
 returns .TRUE. To check for NaNs, pass the same variable as both
 arguments.
 A compiler must assume that the two arguments are
 not the same variable, and the test will not be optimized away.
 Interprocedural or whole-program optimization may delete this
 test. The ISNAN functions will be replaced by the correct
 Fortran 03 intrinsic once the intrinsic is widely available.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIN1</i> </p>
<pre> SIN1 is REAL</pre>
<p><i>SIN2</i> </p>
<pre> SIN2 is REAL
 Two numbers to compare for inequality.</pre>
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
<p> Definition at line 75 of file slaisnan.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
