---
title: "zdscal(3)"
name: "zdscal"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdscal/"
description: "zdscal.f –"
---

<p>zdscal.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zdscal</code> (N, DA, ZX, INCX)<br />
 <i></i><code>ZDSCAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zdscal (integerN, double precisionDA, complex*16, dimension(*)ZX, integerINCX)</h3>
<p><code>ZDSCAL</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZDSCAL scales a vector by a constant.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> jack dongarra, 3/11/78.
 modified 3/93 to return if incx .le. 0.
 modified 12/3/93, <a href="//www.systutorials.com/docs/linux/man/1-array/">array</a>(1) declarations changed to array(*)</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 53 of file zdscal.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
