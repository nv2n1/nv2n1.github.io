---
title: "sasum(3)"
name: "sasum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasum/"
description: "sasum.f –"
---

<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>sasum</code> (N, SX, INCX)<br />
 <i></i><code>SASUM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function sasum (integerN, real, dimension(*)SX, integerINCX)</h3>
<p> <code>SASUM</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    SASUM takes the sum of the absolute values.
    uses unrolled loops for increment equal to one.
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
     jack dongarra, linpack, 3/11/78.
     modified 3/93 to return if incx .le. 0.
     modified 12/3/93, array(1) declarations changed to array(*)
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> Definition at line 53 of file sasum.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
