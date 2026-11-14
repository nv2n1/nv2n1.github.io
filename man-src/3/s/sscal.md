---
title: "sscal(3)"
name: "sscal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sscal/"
description: "sscal.f –"
---

<h2 class="name">NAME</h2>
<p> sscal.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sscal</code> (N, SA, SX, INCX)<br />
 <i></i><code>SSCAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sscal (integerN, realSA, real, dimension(*)SX, integerINCX)</h3>
<p> <code>SSCAL</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    scales a vector by a constant.
    uses unrolled loops for increment equal to 1.
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
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
     jack dongarra, linpack, 3/11/78.
     modified 3/93 to return if incx .le. 0.
     modified 12/3/93, <a href="//www.systutorials.com/docs/linux/man/1-array/">array</a>(1) declarations changed to array(*)
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 54 of file sscal.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
