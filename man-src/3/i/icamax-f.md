---
title: "icamax-f(3)"
name: "icamax-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-icamax-f/"
description: "icamax.f –"
---

<p>icamax.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>icamax</code> (N, CX, INCX)<br/>
 <i></i><code>ICAMAX</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function icamax (integerN, complex, dimension(*)CX, integerINCX)</h3>
<p><code>ICAMAX</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> ICAMAX finds the index of element having max. absolute value.</pre>
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
<p> Definition at line 52 of file icamax.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
</p>