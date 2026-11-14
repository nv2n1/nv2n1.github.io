---
title: "slarrd(3)"
name: "slarrd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slarrd/"
description: "slarrd.f –"
---

<h2 class="name">NAME</h2>
<p> slarrd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slarrd</code> (RANGE, ORDER, N, VL, VU, IL, IU, GERS, RELTOL, D, E, E2, PIVMIN, NSPLIT, ISPLIT, M, W, WERR, WL, WU, IBLOCK, INDEXW, WORK, IWORK, INFO)<br />
 <i></i><code>SLARRD</code> computes the eigenvalues of a symmetric tridiagonal matrix to suitable accuracy.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slarrd (characterRANGE, characterORDER, integerN, realVL, realVU, integerIL, integerIU, real, dimension( * )GERS, realRELTOL, real, dimension( * )D, real, dimension( * )E, real, dimension( * )E2, realPIVMIN, integerNSPLIT, integer, dimension( * )ISPLIT, integerM, real, dimension( * )W, real, dimension( * )WERR, realWL, realWU, integer, dimension( * )IBLOCK, integer, dimension( * )INDEXW, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SLARRD</code> computes the eigenvalues of a symmetric tridiagonal matrix to suitable accuracy. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLARRD computes the eigenvalues of a symmetric tridiagonal
 matrix T to suitable accuracy. This is an auxiliary code to be
 called from SSTEMR.
 The user may ask for all eigenvalues, all eigenvalues
 in the half-open interval (VL, VU], or the IL-th through IU-th
 eigenvalues.
 To avoid overflow, the matrix must be scaled so that its
 largest element is no greater than overflow**(1/2) * underflow**(1/4) in absolute value, and for greatest
 accuracy, it should not be much smaller than that.
 See W. Kahan &quot;Accurate Eigenvalues of a Symmetric Tridiagonal
 Matrix&quot;, Report CS41, Computer Science Dept., Stanford
 University, July 21, 1966.
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
<p> <i>ORDER</i> </p>
<pre>
          ORDER is CHARACTER*1
          = 'B': (&quot;By Block&quot;) the eigenvalues will be grouped by
                              split-off block (see IBLOCK, ISPLIT) and
                              ordered from smallest to largest within
                              the block.
          = 'E': (&quot;Entire matrix&quot;)
                              the eigenvalues for the entire matrix
                              will be ordered from smallest to
                              largest.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the tridiagonal matrix T.  N &gt;= 0.
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is REAL
</pre>
<p> <i>VU</i> </p>
<pre>
          VU is REAL
          If RANGE='V', the lower and upper bounds of the interval to
          be searched for eigenvalues.  Eigenvalues less than or equal
          to VL, or greater than VU, will not be returned.  VL &lt; VU.
          Not referenced if RANGE = 'A' or 'I'.
</pre>
<p> <i>IL</i> </p>
<pre>
          IL is INTEGER
</pre>
<p> <i>IU</i> </p>
<pre><code>
IU is INTEGER
    If RANGE = 'I',
       the indices(in ascending order) of the
           smallest and largest eigenvalues to be returned.1 &lt;= IL
           &lt;= IU &lt;= N,
       if N &gt; 0;
IL = 1 and IU = 0 if N = 0. Not referenced if RANGE = 'A' or 'V'.
</code></pre>
<p> <i>GERS</i> </p>
<pre>
          GERS is REAL array, dimension (2*N)
          The N Gerschgorin intervals (the i-th Gerschgorin interval
          is (GERS(2*i-1), GERS(2*i)).
</pre>
<p> <i>RELTOL</i> </p>
<pre>
          RELTOL is REAL
          The minimum relative width of an interval.  When an interval
          is narrower than RELTOL times the larger (in
          magnitude) endpoint, then it is considered to be
          sufficiently small, i.e., converged.  Note: this should
          always be at least radix*machine epsilon.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The n diagonal elements of the tridiagonal matrix T.
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
          The (n-1) off-diagonal elements of the tridiagonal matrix T.
</pre>
<p> <i>E2</i> </p>
<pre>
          E2 is REAL array, dimension (N-1)
          The (n-1) squared off-diagonal elements of the tridiagonal matrix T.
</pre>
<p> <i>PIVMIN</i> </p>
<pre>
          PIVMIN is REAL
          The minimum pivot allowed in the Sturm sequence for T.
</pre>
<p> <i>NSPLIT</i> </p>
<pre>
          NSPLIT is INTEGER
          The number of diagonal blocks in the matrix T.
          1 &lt;= NSPLIT &lt;= N.
</pre>
<p> <i>ISPLIT</i> </p>
<pre>
          ISPLIT is INTEGER array, dimension (N)
          The splitting points, at which T breaks up into submatrices.
          The first submatrix consists of rows/columns 1 to <a href="//www.systutorials.com/docs/linux/man/1-ISPLIT/">ISPLIT</a>(1),
          the second of rows/columns <a href="//www.systutorials.com/docs/linux/man/1-ISPLIT/">ISPLIT</a>(1)+1 through <a href="//www.systutorials.com/docs/linux/man/2-ISPLIT/">ISPLIT</a>(2),
          etc., and the NSPLIT-th consists of rows/columns
          ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.
          (Only the first NSPLIT elements will actually be used, but
          since the user cannot know a priori what value NSPLIT will
          have, N words must be reserved for ISPLIT.)
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The actual number of eigenvalues found. 0 &lt;= M &lt;= N.
          (See also the description of INFO=2,3.)
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          On exit, the first M elements of W will contain the
          eigenvalue approximations. SLARRD computes an interval
          I_j = (a_j, b_j] that includes eigenvalue j. The eigenvalue
          approximation is given as the interval midpoint
          W(j)= ( a_j + b_j)/2. The corresponding error is bounded by
          WERR(j) = abs( a_j - b_j)/2
</pre>
<p> <i>WERR</i> </p>
<pre>
          WERR is REAL array, dimension (N)
          The error bound on the corresponding eigenvalue approximation
          in W.
</pre>
<p> <i>WL</i> </p>
<pre>
          WL is REAL
</pre>
<p> <i>WU</i> </p>
<pre>
          WU is REAL
          The interval (WL, WU] contains all the wanted eigenvalues.
          If RANGE='V', then WL=VL and WU=VU.
          If RANGE='A', then WL and WU are the global Gerschgorin bounds
                        on the spectrum.
          If RANGE='I', then WL and WU are computed by SLAEBZ from the
                        index range specified.
</pre>
<p> <i>IBLOCK</i> </p>
<pre>
          IBLOCK is INTEGER array, dimension (N)
          At each row/column j where E(j) is zero or small, the
          matrix T is considered to split into a block diagonal
          matrix.  On exit, if INFO = 0, IBLOCK(i) specifies to which
          block (from 1 to the number of blocks) the eigenvalue W(i)
          belongs.  (SLARRD may use the remaining N-M elements as
          workspace.)
</pre>
<p> <i>INDEXW</i> </p>
<pre><code>
INDEXW is INTEGER array, dimension(N)
                             The indices of the eigenvalues within each block(submatrix);
          for
          example, INDEXW(i) = j and IBLOCK(i) = k imply that the
                                                 i
                                                 - th eigenvalue W(i) is the j - th eigenvalue in block k.
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (4*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (3*N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  some or all of the eigenvalues failed to converge or
                were not computed:
                =1 or 3: Bisection failed to converge for some
                        eigenvalues; these eigenvalues are flagged by a
                        negative block number.  The effect is that the
                        eigenvalues may not be as accurate as the
                        absolute and relative tolerances.  This is
                        generally caused by unexpectedly inaccurate
                        arithmetic.
                =2 or 3: RANGE='I' only: Not all of the eigenvalues
                        IL:IU were found.
                        Effect: M &lt; IU+1-IL
                        Cause:  non-monotonic arithmetic, causing the
                                Sturm sequence to be non-monotonic.
                        Cure:   recalculate, using RANGE='A', and pick
                                out eigenvalues IL:IU.  In some cases,
                                increasing the PARAMETER &quot;FUDGE&quot; may
                                make things work.
                = 4:    RANGE='I', and the Gershgorin interval
                        initially used was too small.  No eigenvalues
                        were computed.
                        Probable cause: your machine has sloppy
                                        floating-point arithmetic.
                        Cure: Increase the PARAMETER &quot;FUDGE&quot;,
                              recompile, and try again.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre>
  FUDGE   REAL, default = 2
          A &quot;fudge factor&quot; to widen the Gershgorin intervals.  Ideally,
          a value of 1 should work, but on machines with sloppy
          arithmetic, this needs to be larger.  The default for
          publicly released versions should be large enough to handle
          the worst machine around.  Note that this has no effect
          on accuracy of the solution.
</pre>
</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> W. Kahan, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Beresford Parlett, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr> </p>
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
<p> Definition at line 319 of file slarrd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
