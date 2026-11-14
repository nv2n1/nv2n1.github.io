---
title: "sswap(3)"
name: "sswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sswap/"
description: "sswap.f –"
---

<h2 class="name">NAME</h2>
<p> sswap.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sswap</code> (N, SX, INCX, SY, INCY)<br />
 <i></i><code>SSWAP</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sswap (integerN, real, dimension(*)SX, integerINCX, real, dimension(*)SY, integerINCY)</h3>
<p> <code>SSWAP</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    interchanges two vectors.
    uses unrolled loops for increments equal to 1.
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
     modified 12/3/93, <a href="//www.systutorials.com/docs/linux/man/1-array/">array</a>(1) declarations changed to array(*)
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 52 of file sswap.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
