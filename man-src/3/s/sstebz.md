---
title: "sstebz(3)"
name: "sstebz"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sstebz/"
description: "sstebz.f –"
---

<h2 class="name">NAME</h2>
<p> sstebz.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sstebz</code> (RANGE, ORDER, N, VL, VU, IL, IU, ABSTOL, D, E, M, NSPLIT, W, IBLOCK, ISPLIT, WORK, IWORK, INFO)<br />
 <i></i><code>SSTEBZ</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sstebz (characterRANGE, characterORDER, integerN, realVL, realVU, integerIL, integerIU, realABSTOL, real, dimension( * )D, real, dimension( * )E, integerM, integerNSPLIT, real, dimension( * )W, integer, dimension( * )IBLOCK, integer, dimension( * )ISPLIT, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SSTEBZ</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSTEBZ computes the eigenvalues of a symmetric tridiagonal
 matrix T.  The user may ask for all eigenvalues, all eigenvalues
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
<p> <i>ABSTOL</i> </p>
<pre>
          ABSTOL is REAL
          The absolute tolerance for the eigenvalues.  An eigenvalue
          (or cluster) is considered to be located if it has been
          determined to lie in an interval whose width is ABSTOL or
          less.  If ABSTOL is less than or equal to zero, then ULP*|T|
          will be used, where |T| means the 1-norm of T.
          Eigenvalues will be computed most accurately when ABSTOL is
          set to twice the underflow threshold 2*SLAMCH('S'), not zero.
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
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The actual number of eigenvalues found. 0 &lt;= M &lt;= N.
          (See also the description of INFO=2,3.)
</pre>
<p> <i>NSPLIT</i> </p>
<pre>
          NSPLIT is INTEGER
          The number of diagonal blocks in the matrix T.
          1 &lt;= NSPLIT &lt;= N.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          On exit, the first M elements of W will contain the
          eigenvalues.  (SSTEBZ may use the remaining N-M elements as
          workspace.)
</pre>
<p> <i>IBLOCK</i> </p>
<pre>
          IBLOCK is INTEGER array, dimension (N)
          At each row/column j where E(j) is zero or small, the
          matrix T is considered to split into a block diagonal
          matrix.  On exit, if INFO = 0, IBLOCK(i) specifies to which
          block (from 1 to the number of blocks) the eigenvalue W(i)
          belongs.  (SSTEBZ may use the remaining N-M elements as
          workspace.)
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
  RELFAC  REAL, default = 2.0e0
          The relative tolerance.  An interval (a,b] lies within
          &quot;relative tolerance&quot; if  b-a &lt; RELFAC*ulp*max(|a|,|b|),
          where &quot;ulp&quot; is the machine precision (distance from 1 to
          the next larger floating point number.)
  FUDGE   REAL, default = 2
          A &quot;fudge factor&quot; to widen the Gershgorin intervals.  Ideally,
          a value of 1 should work, but on machines with sloppy
          arithmetic, this needs to be larger.  The default for
          publicly released versions should be large enough to handle
          the worst machine around.  Note that this has no effect
          on accuracy of the solution.
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
<dd> November 2011</dl>
<p> Definition at line 262 of file sstebz.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
