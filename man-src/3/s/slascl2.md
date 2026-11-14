---
title: "slascl2(3)"
name: "slascl2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slascl2/"
description: "slascl2.f –"
---

<h2 class="name">NAME</h2>
<p> slascl2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slascl2</code> (M, N, D, X, LDX)<br />
 <i></i><code>SLASCL2</code> performs diagonal scaling on a vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slascl2 (integerM, integerN, real, dimension( * )D, real, dimension( ldx, * )X, integerLDX)</h3>
<p> <code>SLASCL2</code> performs diagonal scaling on a vector. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLASCL2 performs a diagonal scaling on a vector:
   x &lt;-- D * x
 where the diagonal matrix D is stored as a vector.
 Eventually to be replaced by BLAS_sge_diag_scale in the new BLAS
 standard.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
     The number of rows of D and X. M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
     The number of columns of D and X. N &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, length M
     Diagonal matrix D, stored as a vector of length M.
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension (LDX,N)
     On entry, the vector X to be scaled by D.
     On exit, the scaled vector.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
     The leading dimension of the vector X. LDX &gt;= 0.
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
<p> Definition at line 91 of file slascl2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
