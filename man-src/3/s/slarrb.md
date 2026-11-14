---
title: "slarrb(3)"
name: "slarrb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slarrb/"
description: "slarrb.f –"
---

<h2 class="name">NAME</h2>
<p> slarrb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slarrb</code> (N, D, LLD, IFIRST, ILAST, RTOL1, RTOL2, OFFSET, W, WGAP, WERR, WORK, IWORK, PIVMIN, SPDIAM, TWIST, INFO)<br />
 <i></i><code>SLARRB</code> provides limited bisection to locate eigenvalues for more accuracy.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slarrb (integerN, real, dimension( * )D, real, dimension( * )LLD, integerIFIRST, integerILAST, realRTOL1, realRTOL2, integerOFFSET, real, dimension( * )W, real, dimension( * )WGAP, real, dimension( * )WERR, real, dimension( * )WORK, integer, dimension( * )IWORK, realPIVMIN, realSPDIAM, integerTWIST, integerINFO)</h3>
<p> <code>SLARRB</code> provides limited bisection to locate eigenvalues for more accuracy. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 Given the relatively robust representation(RRR) L D L^T, SLARRB
 does &quot;limited&quot; bisection to refine the eigenvalues of L D L^T,
 W( IFIRST-OFFSET ) through W( ILAST-OFFSET ), to more accuracy. Initial
 guesses for these eigenvalues are input in W, the corresponding estimate
 of the error in these guesses and their gaps are input in WERR
 and WGAP, respectively. During bisection, intervals
 [left, right] are maintained by storing their mid-points and
 semi-widths in the arrays W and WERR respectively.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The N diagonal elements of the diagonal matrix D.
</pre>
<p> <i>LLD</i> </p>
<pre>
          LLD is REAL array, dimension (N-1)
          The (N-1) elements L(i)*L(i)*D(i).
</pre>
<p> <i>IFIRST</i> </p>
<pre>
          IFIRST is INTEGER
          The index of the first eigenvalue to be computed.
</pre>
<p> <i>ILAST</i> </p>
<pre>
          ILAST is INTEGER
          The index of the last eigenvalue to be computed.
</pre>
<p> <i>RTOL1</i> </p>
<pre>
          RTOL1 is REAL
</pre>
<p> <i>RTOL2</i> </p>
<pre><code>
          RTOL2 is REAL
          Tolerance for the convergence of the bisection intervals.
          An interval [LEFT,RIGHT] has converged if
          RIGHT-LEFT.LT.MAX( RTOL1*GAP, RTOL2*MAX(|LEFT|,|RIGHT|) )
          where GAP is the (estimated)
          distance to the nearest
              eigenvalue.
</code></pre>
<p> <i>OFFSET</i> </p>
<pre>
          OFFSET is INTEGER
          Offset for the arrays W, WGAP and WERR, i.e., the IFIRST-OFFSET
          through ILAST-OFFSET elements of these arrays are to be used.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          On input, W( IFIRST-OFFSET ) through W( ILAST-OFFSET ) are
          estimates of the eigenvalues of L D L^T indexed IFIRST throug
          ILAST.
          On output, these estimates are refined.
</pre>
<p> <i>WGAP</i> </p>
<pre>
          WGAP is REAL array, dimension (N-1)
          On input, the (estimated) gaps between consecutive
          eigenvalues of L D L^T, i.e., WGAP(I-OFFSET) is the gap between
          eigenvalues I and I+1. Note that if IFIRST.EQ.ILAST
          then WGAP(IFIRST-OFFSET) must be set to ZERO.
          On output, these gaps are refined.
</pre>
<p> <i>WERR</i> </p>
<pre>
          WERR is REAL array, dimension (N)
          On input, WERR( IFIRST-OFFSET ) through WERR( ILAST-OFFSET ) are
          the errors in the estimates of the corresponding elements in W.
          On output, these errors are refined.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (2*N)
          Workspace.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (2*N)
          Workspace.
</pre>
<p> <i>PIVMIN</i> </p>
<pre>
          PIVMIN is REAL
          The minimum pivot in the Sturm sequence.
</pre>
<p> <i>SPDIAM</i> </p>
<pre>
          SPDIAM is REAL
          The spectral diameter of the matrix.
</pre>
<p> <i>TWIST</i> </p>
<pre>
          TWIST is INTEGER
          The twist index for the twisted factorization that is used
          for the negcount.
          TWIST = N: Compute negcount from L D L^T - LAMBDA I = L+ D+ L+^T
          TWIST = 1: Compute negcount from L D L^T - LAMBDA I = U- D- U-^T
          TWIST = R: Compute negcount from L D L^T - LAMBDA I = N(r) D(r) N(r)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          Error flag.
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr></dl>
<p> Definition at line 195 of file slarrb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
