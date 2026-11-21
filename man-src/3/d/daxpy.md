---

title: "daxpy(3)"
name: "daxpy"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daxpy/"
description: "daxpy.f –"
---

<h3>Functions/Subroutines</h3>
<p> subroutine <code>daxpy</code> (N, DA, DX, INCX, DY, INCY)<br />
 <i></i><code>DAXPY</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine daxpy (integerN, double precisionDA, double precision, dimension(*)DX, integerINCX, double precision, dimension(*)DY, integerINCY)</h3>
<p> <code>DAXPY</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    DAXPY constant times a vector plus a vector.
    uses unrolled loops for increments equal to one.
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
<p> Definition at line 53 of file daxpy.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
