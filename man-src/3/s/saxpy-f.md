---
title: "saxpy-f(3)"
name: "saxpy-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-saxpy-f/"
description: "saxpy.f –"
---

<p>saxpy.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>saxpy</code> (N, SA, SX, INCX, SY, INCY)<br />
 <i></i><code>SAXPY</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine saxpy (integerN, realSA, real, dimension(*)SX, integerINCX, real, dimension(*)SY, integerINCY)</h3>
<p><code>SAXPY</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SAXPY constant times a vector plus a vector.
 uses unrolled loops for increments equal to one.</pre>
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
<pre> jack dongarra, linpack, 3/11/78.
 modified 12/3/93, <a href="//www.systutorials.com/docs/linux/man/1-array/">array</a>(1) declarations changed to array(*)</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 53 of file saxpy.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
