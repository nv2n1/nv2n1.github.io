---
title: "dlasv2(3)"
name: "dlasv2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasv2/"
description: "dlasv2.f –"
---

<h2 class="name">NAME</h2>
<p> dlasv2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasv2</code> (F, G, H, SSMIN, SSMAX, SNR, CSR, SNL, CSL)<br />
 <i></i><code>DLASV2</code> computes the singular value decomposition of a 2-by-2 triangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasv2 (double precisionF, double precisionG, double precisionH, double precisionSSMIN, double precisionSSMAX, double precisionSNR, double precisionCSR, double precisionSNL, double precisionCSL)</h3>
<p> <code>DLASV2</code> computes the singular value decomposition of a 2-by-2 triangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DLASV2 computes the singular value decomposition of a 2-by-2
 triangular matrix
    [  F   G  ]
    [  0   H  ].
 On return, abs(SSMAX) is the larger singular value, abs(SSMIN) is the
 smaller singular value, and (CSL,SNL) and (CSR,SNR) are the left and
 right singular vectors for abs(SSMAX), giving the decomposition
    [ CSL  SNL ] [  F   G  ] [ CSR -SNR ]  =  [ SSMAX   0   ]
    [-SNL  CSL ] [  0   H  ] [ SNR  CSR ]     [  0    SSMIN ].
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
          abs(SSMIN) is the smaller singular value.
</pre>
<p> <i>SSMAX</i> </p>
<pre>
          SSMAX is DOUBLE PRECISION
          abs(SSMAX) is the larger singular value.
</pre>
<p> <i>SNL</i> </p>
<pre>
          SNL is DOUBLE PRECISION
</pre>
<p> <i>CSL</i> </p>
<pre>
          CSL is DOUBLE PRECISION
          The vector (CSL, SNL) is a unit left singular vector for the
          singular value abs(SSMAX).
</pre>
<p> <i>SNR</i> </p>
<pre>
          SNR is DOUBLE PRECISION
</pre>
<p> <i>CSR</i> </p>
<pre>
          CSR is DOUBLE PRECISION
          The vector (CSR, SNR) is a unit right singular vector for the
          singular value abs(SSMAX).
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
  Any input parameter may be aliased with any output parameter.
  Barring over/underflow and assuming a guard digit in subtraction, all
  output quantities are correct to within a few units in the last
  place (ulps).
  In IEEE arithmetic, the code works correctly if one matrix element is
  infinite.
  Overflow will not occur unless the largest singular value itself
  overflows or is within a few ulps of overflow. (On machines with
  partial overflow, like the Cray, overflow may occur if the largest
  singular value is within a factor of 2 of overflow.)
  Underflow is harmless if underflow is gradual. Otherwise, results
  may correspond to a matrix modified by perturbations of size near
  the underflow threshold.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 139 of file dlasv2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
