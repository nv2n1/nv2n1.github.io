---
title: "slartgs-f(3)"
name: "slartgs-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slartgs-f/"
description: "slartgs.f –"
---

<p>slartgs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slartgs</code> (X, Y, SIGMA, CS, SN)<br />
 <i></i><code>SLARTGS</code> generates a plane rotation designed to introduce a bulge in implicit QR iteration for the bidiagonal SVD problem.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slartgs (realX, realY, realSIGMA, realCS, realSN)</h3>
<p><code>SLARTGS</code> generates a plane rotation designed to introduce a bulge in implicit QR iteration for the bidiagonal SVD problem. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLARTGS generates a plane rotation designed to introduce a bulge in
 Golub-Reinsch-style implicit QR iteration for the bidiagonal SVD
 problem. X and Y are the top-row entries, and SIGMA is the shift.
 The computed CS and SN define a plane rotation satisfying
 [ CS SN ] . [ X^2 - SIGMA ] = [ R ],
 [ -SN CS ] [ X * Y ] [ 0 ]
 with R nonnegative. If X^2 - SIGMA and X * Y are 0, then the
 rotation is by PI/2.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>X</i> </p>
<pre> X is REAL
 The (1,1) entry of an upper bidiagonal matrix.</pre>
<p><i>Y</i> </p>
<pre> Y is REAL
 The (1,2) entry of an upper bidiagonal matrix.</pre>
<p><i>SIGMA</i> </p>
<pre> SIGMA is REAL
 The shift.</pre>
<p><i>CS</i> </p>
<pre> CS is REAL
 The cosine of the rotation.</pre>
<p><i>SN</i> </p>
<pre> SN is REAL
 The sine of the rotation.</pre>
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
<p> Definition at line 91 of file slartgs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
