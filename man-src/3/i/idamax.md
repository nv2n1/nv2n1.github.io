---
title: "idamax(3)"
name: "idamax"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idamax/"
description: "idamax.f –"
---

<h2 class="name">NAME</h2>
<p> idamax.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>idamax</code> (N, DX, INCX)<br />
 <i></i><code>IDAMAX</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function idamax (integerN, double precision, dimension(*)DX, integerINCX)</h3>
<p> <code>IDAMAX</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    IDAMAX finds the index of element having max. absolute value.
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
<p> Definition at line 52 of file idamax.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
