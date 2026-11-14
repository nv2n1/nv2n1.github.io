---
title: "chegv(3)"
name: "chegv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chegv/"
description: "chegv.f –"
---

<h2 class="name">NAME</h2>
<p> chegv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chegv</code> (ITYPE, JOBZ, UPLO, N, A, LDA, B, LDB, W, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code>CHEGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chegv (integerITYPE, characterJOBZ, characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, real, dimension( * )W, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CHEGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHEGV computes all the eigenvalues, and optionally, the eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.
 Here A and B are assumed to be Hermitian and B is also
 positive definite.
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
A is COMPLEX array, dimension(LDA, N) On entry, the Hermitian matrix A.If UPLO = 'U', the leading N - by - N upper triangular part of A contains the upper triangular part of the matrix A.If UPLO = 'L',
                                                                          the leading N - by - N lower triangular part of A contains the lower triangular part of the matrix A.On exit, if JOBZ = 'V', then if INFO = 0, A contains the matrix Z of eigenvectors.The eigenvectors are normalized as follows : if ITYPE = 1 or 2, Z **H *B *Z = I;
if ITYPE
= 3, Z **H *inv(B) *Z = I.If JOBZ = 'N', then on exit the upper triangle(if UPLO = 'U') or the lower triangle(if UPLO = 'L') of A, including the diagonal, is destroyed.
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB, N)
          On entry, the Hermitian positive definite matrix B.
          If UPLO = 'U', the leading N-by-N upper triangular part of B
          contains the upper triangular part of the matrix B.
          If UPLO = 'L', the leading N-by-N lower triangular part of B
          contains the lower triangular part of the matrix B.
          On exit, if INFO &lt;= N, the part of B containing the matrix is
          overwritten by the triangular factor U or L from the Cholesky
          factorization B = U**H*U or B = L*L**H.
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
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>          LWORK is INTEGER<br />
          The length of the array WORK.  LWORK &gt;= max(1,2*N-1).<br />
          For optimal efficiency, LWORK &gt;= (NB+1)*N,<br />
          where NB is the blocksize for CHETRD returned by ILAENV.<br />
          If LWORK = -1, then a workspace query is assumed;<br />
          the routine<br />
              only calculates the optimal size of the WORK array,<br />
              returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.</p>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (max(1, 3*N-2))
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : CPOTRF or CHEEV returned an error code : &lt;= N : if INFO = i, CHEEV failed to converge;
i off - diagonal elements of an intermediate
            tridiagonal form did not converge to zero;
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
<p> Definition at line 181 of file chegv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
