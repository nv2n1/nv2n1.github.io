---
title: "dlas2(3)"
name: "dlas2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlas2/"
description: "dlas2.f –"
---

<h2 class="name">NAME</h2>
<p> dlas2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlas2</code> (F, G, H, SSMIN, SSMAX)<br />
 <i></i><code>DLAS2</code> computes singular values of a 2-by-2 triangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlas2 (double precisionF, double precisionG, double precisionH, double precisionSSMIN, double precisionSSMAX)</h3>
<p> <code>DLAS2</code> computes singular values of a 2-by-2 triangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
DLAS2 computes the singular values of the 2 - by - 2 matrix[F G][0 H].On return, SSMIN is the smaller singular value and SSMAX is the
                                                                                     larger singular value.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>F</i> </p>
<pre>
          F is DOUBLE PRECISION
          The (1,1) element of the 2-by-2 matrix.
</pre>
<p> <i>G</i> </p>
<pre>
          G is DOUBLE PRECISION
          The (1,2) element of the 2-by-2 matrix.
</pre>
<p> <i>H</i> </p>
<pre>
          H is DOUBLE PRECISION
          The (2,2) element of the 2-by-2 matrix.
</pre>
<p> <i>SSMIN</i> </p>
<pre>
          SSMIN is DOUBLE PRECISION
          The smaller singular value.
</pre>
<p> <i>SSMAX</i> </p>
<pre>
          SSMAX is DOUBLE PRECISION
          The larger singular value.
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Barring over/underflow, all output quantities are correct to within
  a few units in the last place (ulps), even in the absence of a guard
  digit in addition/subtraction.
  In IEEE arithmetic, the code works correctly if one matrix element is
  infinite.
  Overflow will not occur unless the largest singular value itself
  overflows, or is within a few ulps of overflow. (On machines with
  partial overflow, like the Cray, overflow may occur if the largest
  singular value is within a factor of 2 of overflow.)
  Underflow is harmless if underflow is gradual. Otherwise, results
  may correspond to a matrix modified by perturbations of size near
  the underflow threshold.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 108 of file dlas2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
