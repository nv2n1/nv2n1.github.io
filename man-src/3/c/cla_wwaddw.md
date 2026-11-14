---
title: "cla_wwaddw(3)"
name: "cla_wwaddw"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_wwaddw/"
description: "cla_wwaddw.f –"
---

<h2 class="name">NAME</h2>
<p> cla_wwaddw.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cla_wwaddw</code> (N, X, Y, W)<br />
 <i></i><code>CLA_WWADDW</code> adds a vector into a doubled-single vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cla_wwaddw (integerN, complex, dimension( * )X, complex, dimension( * )Y, complex, dimension( * )W)</h3>
<p> <code>CLA_WWADDW</code> adds a vector into a doubled-single vector. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    CLA_WWADDW adds a vector W into a doubled-single vector (X, Y).
    This works for all extant IBM's hex and binary floating point
    arithmetics, but not for decimal.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
            The length of vectors X, Y, and W.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (N)
            The first part of the doubled-single accumulation vector.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array, dimension (N)
            The second part of the doubled-single accumulation vector.
</pre>
<p> <i>W</i> </p>
<pre>
          W is COMPLEX array, dimension (N)
            The vector to be added.
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
<dd> September 2012</dl>
<p> Definition at line 82 of file cla_wwaddw.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
