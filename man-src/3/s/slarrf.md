---
title: "slarrf(3)"
name: "slarrf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slarrf/"
description: "slarrf.f –"
---

<h2 class="name">NAME</h2>
<p> slarrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slarrf</code> (N, D, L, LD, CLSTRT, CLEND, W, WGAP, WERR, SPDIAM, CLGAPL, CLGAPR, PIVMIN, SIGMA, DPLUS, LPLUS, WORK, INFO)<br />
 <i></i><code>SLARRF</code> finds a new relatively robust representation such that at least one of the eigenvalues is relatively isolated.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slarrf (integerN, real, dimension( * )D, real, dimension( * )L, real, dimension( * )LD, integerCLSTRT, integerCLEND, real, dimension( * )W, real, dimension( * )WGAP, real, dimension( * )WERR, realSPDIAM, realCLGAPL, realCLGAPR, realPIVMIN, realSIGMA, real, dimension( * )DPLUS, real, dimension( * )LPLUS, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SLARRF</code> finds a new relatively robust representation such that at least one of the eigenvalues is relatively isolated. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 Given the initial representation L D L^T and its cluster of close
 eigenvalues (in a relative measure), W( CLSTRT ), W( CLSTRT+1 ), ...
 W( CLEND ), SLARRF finds a new relatively robust representation
 L D L^T - SIGMA I = L(+) D(+) L(+)^T such that at least one of the
 eigenvalues of L(+) D(+) L(+)^T is relatively isolated.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix (subblock, if the matrix splitted).
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The N diagonal elements of the diagonal matrix D.
</pre>
<p> <i>L</i> </p>
<pre>
          L is REAL array, dimension (N-1)
          The (N-1) subdiagonal elements of the unit bidiagonal
          matrix L.
</pre>
<p> <i>LD</i> </p>
<pre>
          LD is REAL array, dimension (N-1)
          The (N-1) elements L(i)*D(i).
</pre>
<p> <i>CLSTRT</i> </p>
<pre>
          CLSTRT is INTEGER
          The index of the first eigenvalue in the cluster.
</pre>
<p> <i>CLEND</i> </p>
<pre>
          CLEND is INTEGER
          The index of the last eigenvalue in the cluster.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension
          dimension is &gt;=  (CLEND-CLSTRT+1)
          The eigenvalue APPROXIMATIONS of L D L^T in ascending order.
          W( CLSTRT ) through W( CLEND ) form the cluster of relatively
          close eigenalues.
</pre>
<p> <i>WGAP</i> </p>
<pre>
          WGAP is REAL array, dimension
          dimension is &gt;=  (CLEND-CLSTRT+1)
          The separation from the right neighbor eigenvalue in W.
</pre>
<p> <i>WERR</i> </p>
<pre>
          WERR is REAL array, dimension
          dimension is &gt;=  (CLEND-CLSTRT+1)
          WERR contain the semiwidth of the uncertainty
          interval of the corresponding eigenvalue APPROXIMATION in W
</pre>
<p> <i>SPDIAM</i> </p>
<pre>
          SPDIAM is REAL
          estimate of the spectral diameter obtained from the
          Gerschgorin intervals
</pre>
<p> <i>CLGAPL</i> </p>
<pre>
          CLGAPL is REAL
</pre>
<p> <i>CLGAPR</i> </p>
<pre>
          CLGAPR is REAL
          absolute gap on each end of the cluster.
          Set by the calling routine to protect against shifts too close
          to eigenvalues outside the cluster.
</pre>
<p> <i>PIVMIN</i> </p>
<pre>
          PIVMIN is REAL
          The minimum pivot allowed in the Sturm sequence.
</pre>
<p> <i>SIGMA</i> </p>
<pre>
          SIGMA is REAL
          The shift used to form L(+) D(+) L(+)^T.
</pre>
<p> <i>DPLUS</i> </p>
<pre>
          DPLUS is REAL array, dimension (N)
          The N diagonal elements of the diagonal matrix D(+).
</pre>
<p> <i>LPLUS</i> </p>
<pre>
          LPLUS is REAL array, dimension (N-1)
          The first (N-1) elements of LPLUS contain the subdiagonal
          elements of the unit bidiagonal matrix L(+).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (2*N)
          Workspace.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          Signals processing OK (=0) or failure (=1)
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
<p> Definition at line 191 of file slarrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
