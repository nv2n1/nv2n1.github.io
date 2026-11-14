---
title: "clascl2(3)"
name: "clascl2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clascl2/"
description: "clascl2.f –"
---

<h2 class="name">NAME</h2>
<p> clascl2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clascl2</code> (M, N, D, X, LDX)<br />
 <i></i><code>CLASCL2</code> performs diagonal scaling on a vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clascl2 (integerM, integerN, real, dimension( * )D, complex, dimension( ldx, * )X, integerLDX)</h3>
<p> <code>CLASCL2</code> performs diagonal scaling on a vector. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLASCL2 performs a diagonal scaling on a vector:
   x &lt;-- D * x
 where the diagonal REAL matrix D is stored as a vector.
 Eventually to be replaced by BLAS_cge_diag_scale in the new BLAS
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
          X is COMPLEX array, dimension (LDX,N)
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
<p> Definition at line 92 of file clascl2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
