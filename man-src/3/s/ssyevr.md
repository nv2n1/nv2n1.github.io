---
title: "ssyevr(3)"
name: "ssyevr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssyevr/"
description: "ssyevr.f –"
---

<h2 class="name">NAME</h2>
<p> ssyevr.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssyevr</code> (JOBZ, RANGE, UPLO, N, A, LDA, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, ISUPPZ, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code> SSYEVR computes the eigenvalues and, optionally, the left and/or right eigenvectors for SY matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssyevr (characterJOBZ, characterRANGE, characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, realVL, realVU, integerIL, integerIU, realABSTOL, integerM, real, dimension( * )W, real, dimension( ldz, * )Z, integerLDZ, integer, dimension( * )ISUPPZ, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code> SSYEVR computes the eigenvalues and, optionally, the left and/or right eigenvectors for SY matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 SSYEVR computes selected eigenvalues and, optionally, eigenvectors
 of a real symmetric matrix A.  Eigenvalues and eigenvectors can be
 selected by specifying either a range of values or a range of
 indices for the desired eigenvalues.
 SSYEVR first reduces the matrix A to tridiagonal form T with a call
 to SSYTRD.  Then, whenever possible, SSYEVR calls SSTEMR to compute
 the eigenspectrum using Relatively Robust Representations.  SSTEMR
 computes eigenvalues by the dqds algorithm, while orthogonal
 eigenvectors are computed from various "good" L D L^T representations
 (also known as Relatively Robust Representations). Gram-Schmidt
 orthogonalization is avoided as far as possible. More specifically,
 the various steps of the algorithm are as follows.
 For each unreduced block (submatrix)
 of T,
     (a)Compute T - sigma I = L D L ^ T, so that L and D define all the wanted eigenvalues to high relative accuracy.This means that small relative changes in the entries of D and L cause only small relative changes in the eigenvalues and eigenvectors.The standard(unfactored) representation of the
        tridiagonal matrix T does not have this property in general.
    (b) Compute the eigenvalues to suitable accuracy.
        If the eigenvectors are desired, the algorithm attains full
        accuracy of the computed eigenvalues only right before
        the corresponding vectors have to be computed, see steps c) and d).
    (c) For each cluster of close eigenvalues, select a new
        shift close to the cluster, find a new factorization, and refine
        the shifted eigenvalues to suitable accuracy.
    (d) For each eigenvalue with a large enough relative separation compute
        the corresponding eigenvector by forming a rank revealing twisted
        factorization. Go back to (c) for any clusters that remain.
 The desired accuracy of the output can be specified by the input
 parameter ABSTOL.
 For more details, see SSTEMR's documentation and:
 - Inderjit S. Dhillon and Beresford N. Parlett: "Multiple representations
   to compute orthogonal eigenvectors of symmetric tridiagonal matrices,"
   Linear Algebra and its Applications, 387(1), pp. 1-28, August 2004.
 - Inderjit Dhillon and Beresford Parlett: "Orthogonal Eigenvectors and
   Relative Gaps," SIAM Journal on Matrix Analysis and Applications, Vol. 25,
   2004.  Also LAPACK Working Note 154.
 - Inderjit Dhillon: "A new O(n^2) algorithm for the symmetric
   tridiagonal eigenvalue/eigenvector problem",
   Computer Science Division Technical Report No. UCB/CSD-97-971,
   UC Berkeley, May 1997.
 Note 1 : SSYEVR calls SSTEMR when the full spectrum is requested
 on machines which conform to the ieee-754 floating point standard.
 SSYEVR calls SSTEBZ and SSTEIN on non-ieee machines and
 when partial spectrum requests are made.
 Normal execution of SSTEMR may create NaNs and infinities and
 hence may abort due to a floating point exception in environments
 which do not handle NaNs and infinities in the ieee standard default
 manner.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBZ</i> </p>
<pre>
          JOBZ is CHARACTER*1
          = 'N':  Compute eigenvalues only;
          = 'V':  Compute eigenvalues and eigenvectors.
</pre>
<p> <i>RANGE</i> </p>
<pre>
          RANGE is CHARACTER*1
          = 'A': all eigenvalues will be found.
          = 'V': all eigenvalues in the half-open interval (VL,VU]
                 will be found.
          = 'I': the IL-th through IU-th eigenvalues will be found.
          For RANGE = 'V' or 'I' and IU - IL &lt; N - 1, SSTEBZ and
          SSTEIN are called
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA, N)
          On entry, the symmetric matrix A.  If UPLO = 'U', the
          leading N-by-N upper triangular part of A contains the
          upper triangular part of the matrix A.  If UPLO = 'L',
          the leading N-by-N lower triangular part of A contains
          the lower triangular part of the matrix A.
          On exit, the lower triangle (if UPLO='L') or the upper
          triangle (if UPLO='U') of A, including the diagonal, is
          destroyed.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is REAL
</pre>
<p> <i>VU</i> </p>
<pre>
          VU is REAL
          If RANGE='V', the lower and upper bounds of the interval to
          be searched for eigenvalues. VL &lt; VU.
          Not referenced if RANGE = 'A' or 'I'.
</pre>
<p> <i>IL</i> </p>
<pre>
          IL is INTEGER
</pre>
<p> <i>IU</i> </p>
<p>IU is INTEGER<br />
    If RANGE = &#8216;I&#8217;,<br />
       the indices(in ascending order) of the<br />
           smallest and largest eigenvalues to be returned.1 &lt;= IL<br />
           &lt;= IU &lt;= N,<br />
       if N &gt; 0;<br />
IL = 1 and IU = 0 if N = 0. Not referenced if RANGE = &#8216;A&#8217; or &#8216;V&#8217;.</p>
<p> <i>ABSTOL</i> </p>
<pre>
          ABSTOL is REAL
          The absolute error tolerance for the eigenvalues.
          An approximate eigenvalue is accepted as converged
          when it is determined to lie in an interval [a,b]
          of width less than or equal to
                  ABSTOL + EPS *   max( |a|,|b| ) ,
          where EPS is the machine precision.  If ABSTOL is less than
          or equal to zero, then  EPS*|T|  will be used in its place,
          where |T| is the 1-norm of the tridiagonal matrix obtained
          by reducing A to tridiagonal form.
          See &quot;Computing Small Singular Values of Bidiagonal Matrices
          with Guaranteed High Relative Accuracy,&quot; by Demmel and
          Kahan, LAPACK Working Note #3.
          If high relative accuracy is important, set ABSTOL to
          SLAMCH( 'Safe minimum' ).  Doing so will guarantee that
          eigenvalues are computed to high relative accuracy when
          possible in future releases.  The current code does not
          make any guarantees about high relative accuracy, but
          future releases will. See J. Barlow and J. Demmel,
          &quot;Computing Accurate Eigensystems of Scaled Diagonally
          Dominant Matrices&quot;, LAPACK Working Note #7, for a discussion
          of which matrices define their eigenvalues to high relative
          accuracy.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The total number of eigenvalues found.  0 &lt;= M &lt;= N.
          If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          The first M elements contain the selected eigenvalues in
          ascending order.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension (LDZ, max(1,M))
          If JOBZ = 'V', then if INFO = 0, the first M columns of Z
          contain the orthonormal eigenvectors of the matrix A
          corresponding to the selected eigenvalues, with the i-th
          column of Z holding the eigenvector associated with W(i).
          If JOBZ = 'N', then Z is not referenced.
          Note: the user must ensure that at least max(1,M) columns are
          supplied in the array Z; if RANGE = 'V', the exact value of M
          is not known in advance and an upper bound must be used.
          Supplying N columns is always safe.
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= max(1,N).
</pre>
<p> <i>ISUPPZ</i> </p>
<pre>
          ISUPPZ is INTEGER array, dimension ( 2*max(1,M) )
          The support of the eigenvectors in Z, i.e., the indices
          indicating the nonzero elements in Z. The i-th eigenvector
          is nonzero only in elements ISUPPZ( 2*i-1 ) through
          ISUPPZ( 2*i ).
          Implemented only for RANGE = 'A' or 'I' and IU - IL = N - 1
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,26*N).
          For optimal efficiency, LWORK &gt;= (NB+6)*N,
          where NB is the max of the blocksize for SSYTRD and SORMTR
          returned by ILAENV.
          If LWORK = -1, then a workspace query is assumed;
          the routine
              only calculates the optimal sizes of the WORK and IWORK
                  arrays,
              returns these values as the first entries of the WORK
                  and IWORK arrays,
              and no error message related to LWORK or
                  LIWORK is issued by XERBLA.
</code></pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LWORK.
</pre>
<p> <i>LIWORK</i> </p>
<pre>
          LIWORK is INTEGER
          The dimension of the array IWORK.  LIWORK &gt;= max(1,10*N).
          If LIWORK = -1, then a workspace query is assumed; the
          routine only calculates the optimal sizes of the WORK and
          IWORK arrays, returns these values as the first entries of
          the WORK and IWORK arrays, and no error message related to
          LWORK or LIWORK is issued by XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  Internal error
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
<dd> Inderjit Dhillon, IBM Almaden, USA </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Ken Stanley, Computer Science Division, University of California at Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Jason Riedy, Computer Science Division, University of California at Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 326 of file ssyevr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
