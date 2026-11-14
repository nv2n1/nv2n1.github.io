---
title: "dznrm2-f(3)"
name: "dznrm2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dznrm2-f/"
description: "dznrm2.f –"
---

<p>dznrm2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>dznrm2</code> (N, X, INCX)<br />
 <i></i><code>DZNRM2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dznrm2 (integerN, complex*16, dimension(*)X, integerINCX)</h3>
<p><code>DZNRM2</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DZNRM2 returns the euclidean norm of a vector via the function
 name, so that
 DZNRM2 := sqrt( x**H*x )</pre>
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
<pre> -- This version written on 25-October-1982.
 Modified on 14-October-1993 to inline the call to ZLASSQ.
 Sven Hammarling, Nag Ltd.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 55 of file dznrm2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
