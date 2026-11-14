---
title: "slarrj-f(3)"
name: "slarrj-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slarrj-f/"
description: "slarrj.f –"
---

<p>slarrj.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slarrj</code> (N, D, E2, IFIRST, ILAST, RTOL, OFFSET, W, WERR, WORK, IWORK, PIVMIN, SPDIAM, INFO)<br />
 <i></i><code>SLARRJ</code> performs refinement of the initial estimates of the eigenvalues of the matrix T.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slarrj (integerN, real, dimension( * )D, real, dimension( * )E2, integerIFIRST, integerILAST, realRTOL, integerOFFSET, real, dimension( * )W, real, dimension( * )WERR, real, dimension( * )WORK, integer, dimension( * )IWORK, realPIVMIN, realSPDIAM, integerINFO)</h3>
<p><code>SLARRJ</code> performs refinement of the initial estimates of the eigenvalues of the matrix T. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Given the initial eigenvalue approximations of T, SLARRJ
 does bisection to refine the eigenvalues of T,
 W( IFIRST-OFFSET ) through W( ILAST-OFFSET ), to more accuracy. Initial
 guesses for these eigenvalues are input in W, the corresponding estimate
 of the error in these guesses in WERR. During bisection, intervals
 [left, right] are maintained by storing their mid-points and
 semi-widths in the arrays W and WERR respectively.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 The N diagonal elements of T.</pre>
<p><i>E2</i> </p>
<pre> E2 is REAL array, dimension (N-1)
 The Squares of the (N-1) subdiagonal elements of T.</pre>
<p><i>IFIRST</i> </p>
<pre> IFIRST is INTEGER
 The index of the first eigenvalue to be computed.</pre>
<p><i>ILAST</i> </p>
<pre> ILAST is INTEGER
 The index of the last eigenvalue to be computed.</pre>
<p><i>RTOL</i> </p>
<pre> RTOL is REAL
 Tolerance for the convergence of the bisection intervals.
 An interval [LEFT,RIGHT] has converged if
 RIGHT-LEFT.LT.RTOL*MAX(|LEFT|,|RIGHT|).</pre>
<p><i>OFFSET</i> </p>
<pre> OFFSET is INTEGER
 Offset for the arrays W and WERR, i.e., the IFIRST-OFFSET
 through ILAST-OFFSET elements of these arrays are to be used.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 On input, W( IFIRST-OFFSET ) through W( ILAST-OFFSET ) are
 estimates of the eigenvalues of L D L^T indexed IFIRST through
 ILAST.
 On output, these estimates are refined.</pre>
<p><i>WERR</i> </p>
<pre> WERR is REAL array, dimension (N)
 On input, WERR( IFIRST-OFFSET ) through WERR( ILAST-OFFSET ) are
 the errors in the estimates of the corresponding elements in W.
 On output, these errors are refined.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (2*N)
 Workspace.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (2*N)
 Workspace.</pre>
<p><i>PIVMIN</i> </p>
<pre> PIVMIN is REAL
 The minimum pivot in the Sturm sequence for T.</pre>
<p><i>SPDIAM</i> </p>
<pre> SPDIAM is REAL
 The spectral diameter of T.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 Error flag.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr></dl>
<p> Definition at line 167 of file slarrj.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
