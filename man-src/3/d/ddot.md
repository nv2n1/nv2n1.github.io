---
title: "ddot(3)"
name: "ddot"
section: "3"
letter: "d"
url: "/docs/linux/man/3-ddot/"
description: "ddot.f –"
---

<h2 class="name">NAME</h2>
<p> ddot.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>ddot</code> (N, DX, INCX, DY, INCY)<br />
 <i></i><code>DDOT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function ddot (integerN, double precision, dimension(*)DX, integerINCX, double precision, dimension(*)DY, integerINCY)</h3>
<p> <code>DDOT</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    DDOT forms the dot product of two vectors.
    uses unrolled loops for increments equal to one.
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
<p> Definition at line 52 of file ddot.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
