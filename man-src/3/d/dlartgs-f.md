---
title: "dlartgs-f(3)"
name: "dlartgs-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlartgs-f/"
description: "dlartgs.f –"
---

<p>dlartgs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlartgs</code> (X, Y, SIGMA, CS, SN)<br />
 <i></i><code>DLARTGS</code> generates a plane rotation designed to introduce a bulge in implicit QR iteration for the bidiagonal SVD problem.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlartgs (double precisionX, double precisionY, double precisionSIGMA, double precisionCS, double precisionSN)</h3>
<p><code>DLARTGS</code> generates a plane rotation designed to introduce a bulge in implicit QR iteration for the bidiagonal SVD problem. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLARTGS generates a plane rotation designed to introduce a bulge in
 Golub-Reinsch-style implicit QR iteration for the bidiagonal SVD
 problem. X and Y are the top-row entries, and SIGMA is the shift.
 The computed CS and SN define a plane rotation satisfying
 [ CS SN ] . [ X^2 - SIGMA ] = [ R ],
 [ -SN CS ] [ X * Y ] [ 0 ]
 with R nonnegative. If X^2 - SIGMA and X * Y are 0, then the
 rotation is by PI/2.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>X</i> </p>
<pre> X is DOUBLE PRECISION
 The (1,1) entry of an upper bidiagonal matrix.</pre>
<p><i>Y</i> </p>
<pre> Y is DOUBLE PRECISION
 The (1,2) entry of an upper bidiagonal matrix.</pre>
<p><i>SIGMA</i> </p>
<pre> SIGMA is DOUBLE PRECISION
 The shift.</pre>
<p><i>CS</i> </p>
<pre> CS is DOUBLE PRECISION
 The cosine of the rotation.</pre>
<p><i>SN</i> </p>
<pre> SN is DOUBLE PRECISION
 The sine of the rotation.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 91 of file dlartgs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
