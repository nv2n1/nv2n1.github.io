---

title: "scasum(3)"
name: "scasum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scasum/"
description: "scasum.f –"
---

<p> scasum.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>scasum</code> (N, CX, INCX)<br/>
 <i></i><code>SCASUM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function scasum (integerN, complex, dimension(*)CX, integerINCX)</h3>
<p> <code>SCASUM</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    SCASUM takes the sum of the absolute values of a complex vector and
    returns a single precision result.
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
<p> Definition at line 53 of file scasum.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
