---
title: "zla_wwaddw-f(3)"
name: "zla_wwaddw-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zla_wwaddw-f/"
description: "zla_wwaddw.f –"
---

<p>zla_wwaddw.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zla_wwaddw</code> (N, X, Y, W)<br />
 <i></i><code>ZLA_WWADDW</code> adds a vector into a doubled-single vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zla_wwaddw (integerN, complex*16, dimension( * )X, complex*16, dimension( * )Y, complex*16, dimension( * )W)</h3>
<p><code>ZLA_WWADDW</code> adds a vector into a doubled-single vector. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLA_WWADDW adds a vector W into a doubled-single vector (X, Y).
 This works for all extant IBM's hex and binary floating point
 arithmetics, but not for decimal.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The length of vectors X, Y, and W.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (N)
 The first part of the doubled-single accumulation vector.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16 array, dimension (N)
 The second part of the doubled-single accumulation vector.</pre>
<p><i>W</i> </p>
<pre> W is COMPLEX*16 array, dimension (N)
 The vector to be added.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 82 of file zla_wwaddw.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
