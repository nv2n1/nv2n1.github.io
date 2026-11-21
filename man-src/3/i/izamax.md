---
title: "izamax(3)"
name: "izamax"
section: "3"
letter: "i"
url: "/docs/linux/man/3-izamax/"
description: "izamax.f –"
---

<h2 class="name">NAME</h2>
<p> izamax.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>izamax</code> (N, ZX, INCX)<br />
 <i></i><code>IZAMAX</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function izamax (integerN, complex*16, dimension(*)ZX, integerINCX)</h3>
<p> <code>IZAMAX</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    IZAMAX finds the index of element having max. absolute value.
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
</dt><dd> Univ. of Tennessee </dd>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
</dt><dd> November 2011</dd></dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
     jack dongarra, 1/15/85.
     modified 3/93 to return if incx .le. 0.
     modified 12/3/93, array(1) declarations changed to array(*)
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> Definition at line 52 of file izamax.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
