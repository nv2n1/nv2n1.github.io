---

title: "dscal(3)"
name: "dscal"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dscal/"
description: "dscal.f –"
---

<p> dscal.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dscal</code> (N, DA, DX, INCX)<br />
 <i></i><code>DSCAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dscal (integerN, double precisionDA, double precision, dimension(*)DX, integerINCX)</h3>
<p> <code>DSCAL</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    DSCAL scales a vector by a constant.
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
<p> Definition at line 54 of file dscal.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
