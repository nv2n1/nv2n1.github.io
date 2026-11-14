---
title: "slasv2-f(3)"
name: "slasv2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasv2-f/"
description: "slasv2.f –"
---

<p>slasv2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasv2</code> (F, G, H, SSMIN, SSMAX, SNR, CSR, SNL, CSL)<br />
 <i></i><code>SLASV2</code> computes the singular value decomposition of a 2-by-2 triangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasv2 (realF, realG, realH, realSSMIN, realSSMAX, realSNR, realCSR, realSNL, realCSL)</h3>
<p><code>SLASV2</code> computes the singular value decomposition of a 2-by-2 triangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASV2 computes the singular value decomposition of a 2-by-2
 triangular matrix
 [ F G ]
 [ 0 H ].
 On return, abs(SSMAX) is the larger singular value, abs(SSMIN) is the
 smaller singular value, and (CSL,SNL) and (CSR,SNR) are the left and
 right singular vectors for abs(SSMAX), giving the decomposition
 [ CSL SNL ] [ F G ] [ CSR -SNR ] = [ SSMAX 0 ]
 [-SNL CSL ] [ 0 H ] [ SNR CSR ] [ 0 SSMIN ].</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>F</i> </p>
<pre> F is REAL
 The (1,1) element of the 2-by-2 matrix.</pre>
<p><i>G</i> </p>
<pre> G is REAL
 The (1,2) element of the 2-by-2 matrix.</pre>
<p><i>H</i> </p>
<pre> H is REAL
 The (2,2) element of the 2-by-2 matrix.</pre>
<p><i>SSMIN</i> </p>
<pre> SSMIN is REAL
 abs(SSMIN) is the smaller singular value.</pre>
<p><i>SSMAX</i> </p>
<pre> SSMAX is REAL
 abs(SSMAX) is the larger singular value.</pre>
<p><i>SNL</i> </p>
<pre> SNL is REAL</pre>
<p><i>CSL</i> </p>
<pre> CSL is REAL
 The vector (CSL, SNL) is a unit left singular vector for the
 singular value abs(SSMAX).</pre>
<p><i>SNR</i> </p>
<pre> SNR is REAL</pre>
<p><i>CSR</i> </p>
<pre> CSR is REAL
 The vector (CSR, SNR) is a unit right singular vector for the
 singular value abs(SSMAX).</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> Any input parameter may be aliased with any output parameter.
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
 the underflow threshold.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 139 of file slasv2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
