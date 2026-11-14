---
title: "dswap-f(3)"
name: "dswap-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dswap-f/"
description: "dswap.f –"
---

<p>dswap.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dswap</code> (N, DX, INCX, DY, INCY)<br />
 <i></i><code>DSWAP</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dswap (integerN, double precision, dimension(*)DX, integerINCX, double precision, dimension(*)DY, integerINCY)</h3>
<p><code>DSWAP</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> interchanges two vectors.
 uses unrolled loops for increments equal one.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> jack dongarra, linpack, 3/11/78.
 modified 12/3/93, <a href="//www.systutorials.com/docs/linux/man/1-array/">array</a>(1) declarations changed to array(*)</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 52 of file dswap.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
