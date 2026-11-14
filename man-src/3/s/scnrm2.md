---
title: "scnrm2(3)"
name: "scnrm2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scnrm2/"
description: "scnrm2.f –"
---

<h2 class="name">NAME</h2>
<p> scnrm2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>scnrm2</code> (N, X, INCX)<br />
 <i></i><code>SCNRM2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function scnrm2 (integerN, complex, dimension(*)X, integerINCX)</h3>
<p> <code>SCNRM2</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SCNRM2 returns the euclidean norm of a vector via the function
 name, so that
    SCNRM2 := sqrt( x**H*x )
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
  -- This version written on 25-October-1982.
     Modified on 14-October-1993 to inline the call to CLASSQ.
     Sven Hammarling, Nag Ltd.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 55 of file scnrm2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
