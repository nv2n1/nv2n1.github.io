---
title: "dnrm2(3)"
name: "dnrm2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dnrm2/"
description: "dnrm2.f –"
---

<h2 class="name">NAME</h2>
<p> dnrm2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dnrm2</code> (N, X, INCX)<br />
 <i></i><code>DNRM2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dnrm2 (integerN, double precision, dimension(*)X, integerINCX)</h3>
<p> <code>DNRM2</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DNRM2 returns the euclidean norm of a vector via the function
 name, so that
    DNRM2 := sqrt( x'*x )
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
     Modified on 14-October-1993 to inline the call to DLASSQ.
     Sven Hammarling, Nag Ltd.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 55 of file dnrm2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
