---
title: "dlarre(3)"
name: "dlarre"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarre/"
description: "dlarre.f –"
---

<h2 class="name">NAME</h2>
<p> dlarre.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlarre</code> (RANGE, N, VL, VU, IL, IU, D, E, E2, RTOL1, RTOL2, SPLTOL, NSPLIT, ISPLIT, M, W, WERR, WGAP, IBLOCK, INDEXW, GERS, PIVMIN, WORK, IWORK, INFO)<br />
 <i></i><code>DLARRE</code> given the tridiagonal matrix T, sets small off-diagonal elements to zero and for each unreduced block Ti, finds base representations and eigenvalues.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarre (characterRANGE, integerN, double precisionVL, double precisionVU, integerIL, integerIU, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( * )E2, double precisionRTOL1, double precisionRTOL2, double precisionSPLTOL, integerNSPLIT, integer, dimension( * )ISPLIT, integerM, double precision, dimension( * )W, double precision, dimension( * )WERR, double precision, dimension( * )WGAP, integer, dimension( * )IBLOCK, integer, dimension( * )INDEXW, double precision, dimension( * )GERS, double precisionPIVMIN, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DLARRE</code> given the tridiagonal matrix T, sets small off-diagonal elements to zero and for each unreduced block Ti, finds base representations and eigenvalues. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 To find the desired eigenvalues of a given real symmetric
 tridiagonal matrix T, DLARRE sets any &quot;small&quot; off-diagonal
 elements to zero, and for each unreduced block T_i, it finds
 (a) a suitable shift at one end of the block's spectrum,
 (b) the base representation, T_i - sigma_i I = L_i D_i L_i^T, and
 (c) eigenvalues of each L_i D_i L_i^T.
 The representations and eigenvalues found are then used by
 DSTEMR to compute the eigenvectors of T.
 The accuracy varies depending on whether bisection is used to
 find a few eigenvalues or the dqds algorithm (subroutine DLASQ2) to
 conpute all and then discard any unwanted one.
 As an added benefit, DLARRE also outputs the n
 Gerschgorin intervals for the matrices L_i D_i L_i^T.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>RANGE</i> </p>
<pre>
          RANGE is CHARACTER*1
          = 'A': (&quot;All&quot;)   all eigenvalues will be found.
          = 'V': (&quot;Value&quot;) all eigenvalues in the half-open interval
                           (VL, VU] will be found.
          = 'I': (&quot;Index&quot;) the IL-th through IU-th eigenvalues (of the
                           entire matrix) will be found.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix. N &gt; 0.
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is DOUBLE PRECISION
</pre>
<p> <i>VU</i> </p>
<pre>
          VU is DOUBLE PRECISION
          If RANGE='V', the lower and upper bounds for the eigenvalues.
          Eigenvalues less than or equal to VL, or greater than VU,
          will not be returned.  VL &lt; VU.
          If RANGE='I' or ='A', DLARRE computes bounds on the desired
          part of the spectrum.
</pre>
<p> <i>IL</i> </p>
<pre>
          IL is INTEGER
</pre>
<p> <i>IU</i> </p>
<pre>
          IU is INTEGER
          If RANGE='I', the indices (in ascending order) of the
          smallest and largest eigenvalues to be returned.
          1 &lt;= IL &lt;= IU &lt;= N.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          On entry, the N diagonal elements of the tridiagonal
          matrix T.
          On exit, the N diagonal elements of the diagonal
          matrices D_i.
</pre>
<p> <i>E</i> </p>
<pre>
          E is DOUBLE PRECISION array, dimension (N)
          On entry, the first (N-1) entries contain the subdiagonal
          elements of the tridiagonal matrix T; E(N) need not be set.
          On exit, E contains the subdiagonal elements of the unit
          bidiagonal matrices L_i. The entries E( ISPLIT( I ) ),
          1 &lt;= I &lt;= NSPLIT, contain the base points sigma_i on output.
</pre>
<p> <i>E2</i> </p>
<pre>
          E2 is DOUBLE PRECISION array, dimension (N)
          On entry, the first (N-1) entries contain the SQUARES of the
          subdiagonal elements of the tridiagonal matrix T;
          E2(N) need not be set.
          On exit, the entries E2( ISPLIT( I ) ),
          1 &lt;= I &lt;= NSPLIT, have been set to zero
</pre>
<p> <i>RTOL1</i> </p>
<pre>
          RTOL1 is DOUBLE PRECISION
</pre>
<p> <i>RTOL2</i> </p>
<pre><code>
          RTOL2 is DOUBLE PRECISION
           Parameters for bisection.
           An interval [LEFT,RIGHT] has converged if
           RIGHT-LEFT.LT.MAX( RTOL1*GAP, RTOL2*MAX(|LEFT|,|RIGHT|) )
</code></pre>
<p> <i>SPLTOL</i> </p>
<pre>
          SPLTOL is DOUBLE PRECISION
          The threshold for splitting.
</pre>
<p> <i>NSPLIT</i> </p>
<pre>
          NSPLIT is INTEGER
          The number of blocks T splits into. 1 &lt;= NSPLIT &lt;= N.
</pre>
<p> <i>ISPLIT</i> </p>
<pre>
          ISPLIT is INTEGER array, dimension (N)
          The splitting points, at which T breaks up into blocks.
          The first block consists of rows/columns 1 to <a href="//www.systutorials.com/docs/linux/man/1-ISPLIT/">ISPLIT</a>(1),
          the second of rows/columns <a href="//www.systutorials.com/docs/linux/man/1-ISPLIT/">ISPLIT</a>(1)+1 through <a href="//www.systutorials.com/docs/linux/man/2-ISPLIT/">ISPLIT</a>(2),
          etc., and the NSPLIT-th consists of rows/columns
          ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The total number of eigenvalues (of all L_i D_i L_i^T)
          found.
</pre>
<p> <i>W</i> </p>
<pre>
          W is DOUBLE PRECISION array, dimension (N)
          The first M elements contain the eigenvalues. The
          eigenvalues of each of the blocks, L_i D_i L_i^T, are
          sorted in ascending order ( DLARRE may use the
          remaining N-M elements as workspace).
</pre>
<p> <i>WERR</i> </p>
<pre>
          WERR is DOUBLE PRECISION array, dimension (N)
          The error bound on the corresponding eigenvalue in W.
</pre>
<p> <i>WGAP</i> </p>
<pre>
          WGAP is DOUBLE PRECISION array, dimension (N)
          The separation from the right neighbor eigenvalue in W.
          The gap is only with respect to the eigenvalues of the same block
          as each block has its own representation tree.
          Exception: at the right end of a block we store the left gap
</pre>
<p> <i>IBLOCK</i> </p>
<pre>
          IBLOCK is INTEGER array, dimension (N)
          The indices of the blocks (submatrices) associated with the
          corresponding eigenvalues in W; IBLOCK(i)=1 if eigenvalue
          W(i) belongs to the first block from the top, =2 if W(i)
          belongs to the second block, etc.
</pre>
<p> <i>INDEXW</i> </p>
<pre><code>
INDEXW is INTEGER array, dimension(N)
                             The indices of the eigenvalues within each block(submatrix);
          for
          example, INDEXW(i) = 10 and IBLOCK(i) = 2 imply that the
                                                  i
                                                  - th eigenvalue W(i) is the 10 - th eigenvalue in block 2
</code></pre>
<p> <i>GERS</i> </p>
<pre>
          GERS is DOUBLE PRECISION array, dimension (2*N)
          The N Gerschgorin intervals (the i-th Gerschgorin interval
          is (GERS(2*i-1), GERS(2*i)).
</pre>
<p> <i>PIVMIN</i> </p>
<pre>
          PIVMIN is DOUBLE PRECISION
          The minimum pivot in the Sturm sequence for T.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (6*N)
          Workspace.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (5*N)
          Workspace.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &gt; 0:  A problem occured in DLARRE.
          &lt; 0:  One of the called subroutines signaled an internal problem.
                Needs inspection of the corresponding parameter IINFO
                for further information.
          =-1:  Problem in DLARRD.
          = 2:  No base representation could be found in MAXTRY iterations.
                Increasing MAXTRY and recompilation might be a remedy.
          =-3:  Problem in DLARRB when computing the refined root
                representation for DLASQ2.
          =-4:  Problem in DLARRB when preforming bisection on the
                desired part of the spectrum.
          =-5:  Problem in DLASQ2.
          =-6:  Problem in DLASQ2.
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
  The base representations are required to suffer very little
  element growth and consequently define all their eigenvalues to
  high relative accuracy.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 295 of file dlarre.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
