---
title: "chegvx(3)"
name: "chegvx"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chegvx/"
description: "chegvx.f –"
---

<h2 class="name">NAME</h2>
<p> chegvx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chegvx</code> (ITYPE, JOBZ, RANGE, UPLO, N, A, LDA, B, LDB, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, LWORK, RWORK, IWORK, IFAIL, INFO)<br />
 <i></i><code>CHEGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chegvx (integerITYPE, characterJOBZ, characterRANGE, characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, realVL, realVU, integerIL, integerIU, realABSTOL, integerM, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p> <code>CHEGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHEGVX computes selected eigenvalues, and optionally, eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.  Here A and
 B are assumed to be Hermitian and B is also positive definite.
 Eigenvalues and eigenvectors can be selected by specifying either a
 range of values or a range of indices for the desired eigenvalues.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ITYPE</i> </p>
<pre>
          ITYPE is INTEGER
          Specifies the problem type to be solved:
          = 1:  A*x = (lambda)*B*x
          = 2:  A*B*x = (lambda)*x
          = 3:  B*A*x = (lambda)*x
</pre>
<p> <i>JOBZ</i> </p>
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
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangles of A and B are stored;
          = 'L':  Lower triangles of A and B are stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA, N)
          On entry, the Hermitian matrix A.  If UPLO = 'U', the
          leading N-by-N upper triangular part of A contains the
          upper triangular part of the matrix A.  If UPLO = 'L',
          the leading N-by-N lower triangular part of A contains
          the lower triangular part of the matrix A.
          On exit,  the lower triangle (if UPLO='L') or the upper
          triangle (if UPLO='U') of A, including the diagonal, is
          destroyed.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB, N)
          On entry, the Hermitian matrix B.  If UPLO = 'U', the
          leading N-by-N upper triangular part of B contains the
          upper triangular part of the matrix B.  If UPLO = 'L',
          the leading N-by-N lower triangular part of B contains
          the lower triangular part of the matrix B.
          On exit, if INFO &lt;= N, the part of B containing the matrix is
          overwritten by the triangular factor U or L from the Cholesky
          factorization B = U**H*U or B = L*L**H.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
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
          The absolute error tolerance for the eigenvalues.
          An approximate eigenvalue is accepted as converged
          when it is determined to lie in an interval [a,b]
          of width less than or equal to
                  ABSTOL + EPS *   max( |a|,|b| ) ,
          where EPS is the machine precision.  If ABSTOL is less than
          or equal to zero, then  EPS*|T|  will be used in its place,
          where |T| is the 1-norm of the tridiagonal matrix obtained
          by reducing C to tridiagonal form, where C is the symmetric
          matrix of the standard symmetric problem to which the
          generalized problem is transformed.
          Eigenvalues will be computed most accurately when ABSTOL is
          set to twice the underflow threshold 2*SLAMCH('S'), not zero.
          If this routine returns with INFO&gt;0, indicating that some
          eigenvectors did not converge, try setting ABSTOL to
          2*SLAMCH('S').
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
          The first M elements contain the selected
          eigenvalues in ascending order.
</pre>
<p> <i>Z</i> </p>
<p>Z is COMPLEX array, dimension(LDZ, max(1, M)) If JOBZ = &#8216;N&#8217;, then Z is not referenced.If JOBZ = &#8216;V&#8217;, then if INFO = 0, the first M columns of Z contain the orthonormal eigenvectors of the matrix A corresponding to the selected eigenvalues, with the i &#8211; th column of Z holding the eigenvector associated with W(i).The eigenvectors are normalized as follows : if ITYPE = 1 or 2, Z **T *B *Z = I;<br />
if ITYPE<br />
    = 3, Z **T *inv(B) *Z = I.If an eigenvector fails to converge, then that column of Z contains the latest approximation to the eigenvector, and the index of the eigenvector is returned in IFAIL.Note : the user must ensure that at least max(1, M) columns are supplied in the array Z;<br />
if RANGE<br />
= &#8216;V&#8217;, the exact value of M<br />
               is not known in advance and<br />
           an upper bound must be used.</p>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= max(1,N).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>          LWORK is INTEGER<br />
          The length of the array WORK.  LWORK &gt;= max(1,2*N).<br />
          For optimal efficiency, LWORK &gt;= (NB+1)*N,<br />
          where NB is the blocksize for CHETRD returned by ILAENV.<br />
          If LWORK = -1, then a workspace query is assumed;<br />
          the routine<br />
              only calculates the optimal size of the WORK array,<br />
              returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.</p>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (7*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (5*N)
</pre>
<p> <i>IFAIL</i> </p>
<pre>
          IFAIL is INTEGER array, dimension (N)
          If JOBZ = 'V', then if INFO = 0, the first M elements of
          IFAIL are zero.  If INFO &gt; 0, then IFAIL contains the
          indices of the eigenvectors that failed to converge.
          If JOBZ = 'N', then IFAIL is not referenced.
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : CPOTRF or CHEEVX returned an error code : &lt;= N : if INFO = i, CHEEVX failed to converge;
                    i eigenvectors failed to converge.  Their indices
                    are stored in array IFAIL.
             &gt; N:   if INFO = N + i, for 1 &lt;= i &lt;= N, then the leading
                    minor of order i of B is not positive definite.
                    The factorization of B could not be completed and
                    no eigenvalues or eigenvectors were computed.
</code></pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Mark Fahey, Department of Mathematics, Univ. of Kentucky, USA</dl>
<p> Definition at line 297 of file chegvx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
