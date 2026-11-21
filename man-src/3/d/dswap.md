---

title: "dswap(3)"
name: "dswap"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dswap/"
description: "dswap.f –"
---

<p> dswap.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dswap</code> (N, DX, INCX, DY, INCY)<br />
 <i></i><code>DSWAP</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dswap (integerN, double precision, dimension(*)DX, integerINCX, double precision, dimension(*)DY, integerINCY)</h3>
<p> <code>DSWAP</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    interchanges two vectors.
    uses unrolled loops for increments equal one.
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
     modified 12/3/93, array(1) declarations changed to array(*)
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> Definition at line 52 of file dswap.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
