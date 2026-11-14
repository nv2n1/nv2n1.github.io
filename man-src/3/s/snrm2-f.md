---
title: "snrm2-f(3)"
name: "snrm2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snrm2-f/"
description: "snrm2.f –"
---

<p>snrm2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>snrm2</code> (N, X, INCX)<br />
 <i></i><code>SNRM2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function snrm2 (integerN, real, dimension(*)X, integerINCX)</h3>
<p><code>SNRM2</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SNRM2 returns the euclidean norm of a vector via the function
 name, so that
 SNRM2 := sqrt( x'*x ).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> -- This version written on 25-October-1982.
 Modified on 14-October-1993 to inline the call to SLASSQ.
 Sven Hammarling, Nag Ltd.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 55 of file snrm2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
