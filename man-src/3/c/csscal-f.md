---
title: "csscal-f(3)"
name: "csscal-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csscal-f/"
description: "csscal.f –"
---

<p>csscal.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>csscal</code> (N, SA, CX, INCX)<br />
 <i></i><code>CSSCAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csscal (integerN, realSA, complex, dimension(*)CX, integerINCX)</h3>
<p><code>CSSCAL</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CSSCAL scales a complex vector by a real constant.</pre>
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
 modified 3/93 to return if incx .le. 0.
 modified 12/3/93, <a href="//www.systutorials.com/docs/linux/man/1-array/">array</a>(1) declarations changed to array(*)</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 53 of file csscal.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
