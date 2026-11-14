---
title: "dcopy(3)"
name: "dcopy"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dcopy/"
description: "dcopy.f –"
---

<h2 class="name">NAME</h2>
<p> dcopy.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dcopy</code> (N, DX, INCX, DY, INCY)<br />
 <i></i><code>DCOPY</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dcopy (integerN, double precision, dimension(*)DX, integerINCX, double precision, dimension(*)DY, integerINCY)</h3>
<p> <code>DCOPY</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    DCOPY copies a vector, x, to a vector, y.
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
<p> Definition at line 52 of file dcopy.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
