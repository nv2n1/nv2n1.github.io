---
title: "cscal-f(3)"
name: "cscal-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cscal-f/"
description: "cscal.f –"
---

<p>cscal.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cscal</code> (N, CA, CX, INCX)<br />
 <i></i><code>CSCAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cscal (integerN, complexCA, complex, dimension(*)CX, integerINCX)</h3>
<p><code>CSCAL</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CSCAL scales a vector by a constant.</pre>
<p>&nbsp;<wbr></dd></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </dd>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dd></dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> jack dongarra, linpack, 3/11/78.
 modified 3/93 to return if incx .le. 0.
 modified 12/3/93, array(1) declarations changed to array(*)</pre>
<p>&nbsp;<wbr></dd></dl>
<p> Definition at line 53 of file cscal.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
</p>