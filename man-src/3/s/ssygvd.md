---
title: "ssygvd(3)"
name: "ssygvd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssygvd/"
description: "ssygvd.f –"
---

<h2 class="name">NAME</h2>
<p> ssygvd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssygvd</code> (ITYPE, JOBZ, UPLO, N, A, LDA, B, LDB, W, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>SSYGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssygvd (integerITYPE, characterJOBZ, characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( * )W, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code>SSYGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSYGVD computes all the eigenvalues, and optionally, the eigenvectors
 of a real generalized symmetric-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.  Here A and
 B are assumed to be symmetric and B is also positive definite.
 If eigenvectors are desired, it uses a divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.
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
<pre><code>
A is REAL array, dimension(LDA, N) On entry, the symmetric matrix A.If UPLO = 'U', the leading N - by - N upper triangular part of A contains the upper triangular part of the matrix A.If UPLO = 'L',
                                                                       the leading N - by - N lower triangular part of A contains the lower triangular part of the matrix A.On exit, if JOBZ = 'V', then if INFO = 0, A contains the matrix Z of eigenvectors.The eigenvectors are normalized as follows : if ITYPE = 1 or 2, Z **T *B *Z = I;
if ITYPE
= 3, Z **T *inv(B) *Z = I.If JOBZ = 'N', then on exit the upper triangle(if UPLO = 'U') or the lower triangle(if UPLO = 'L') of A, including the diagonal, is destroyed.
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB, N)
          On entry, the symmetric matrix B.  If UPLO = 'U', the
          leading N-by-N upper triangular part of B contains the
          upper triangular part of the matrix B.  If UPLO = 'L',
          the leading N-by-N lower triangular part of B contains
          the lower triangular part of the matrix B.
          On exit, if INFO &lt;= N, the part of B containing the matrix is
          overwritten by the triangular factor U or L from the Cholesky
          factorization B = U**T*U or B = L*L**T.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          If INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>LWORK is INTEGER<br />
        The dimension of the array WORK.If N &lt;= 1,<br />
    LWORK &gt;= 1. If JOBZ = &#8216;N&#8217; and N &gt; 1, LWORK &gt;= 2 *N + 1. If JOBZ = &#8216;V&#8217; and N &gt; 1, LWORK &gt;= 1 + 6 *N + 2 *N ** 2. If LWORK = -1, then a workspace query is assumed;<br />
the routine<br />
    only calculates the optimal sizes of the WORK and IWORK<br />
        arrays,<br />
    returns these values as the first entries of the WORK<br />
        and IWORK arrays,<br />
    and no error message related to LWORK or<br />
        LIWORK is issued by XERBLA.</p>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<p>LIWORK is INTEGER<br />
        The dimension of the array IWORK.If N &lt;= 1,<br />
    LIWORK &gt;= 1. If JOBZ = &#8216;N&#8217; and N &gt; 1, LIWORK &gt;= 1. If JOBZ = &#8216;V&#8217; and N &gt; 1, LIWORK &gt;= 3 + 5 *N.If LIWORK = -1, then a workspace query is assumed;<br />
the<br />
    routine only calculates the optimal sizes of the WORK and<br />
        IWORK arrays,<br />
    returns these values as the first entries of<br />
        the WORK and IWORK arrays,<br />
    and no error message related to<br />
            LWORK or<br />
        LIWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : SPOTRF or SSYEVD returned an error code : &lt;= N : if INFO = i and JOBZ = 'N', then the algorithm failed to converge;
i off - diagonal elements of an
            intermediate tridiagonal form did not converge to
                zero;
if INFO
    = i and JOBZ = 'V', then the algorithm
                                failed to compute an eigenvalue while working on
                                    the submatrix lying in rows and columns INFO /
                            (N + 1)
                                through mod(INFO, N + 1);
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Modified so that no backsubstitution is performed if SSYEVD fails to
  converge (NEIG in old code could be greater than N causing out of
  bounds reference to A - reported by Ralf Meyer).  Also corrected the
  description of INFO and the test on ITYPE. Sven, 16 Feb 05.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Mark Fahey, Department of Mathematics, Univ. of Kentucky, USA</dl>
<p> Definition at line 227 of file ssygvd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
