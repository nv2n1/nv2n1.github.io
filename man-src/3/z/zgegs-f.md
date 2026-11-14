---
title: "zgegs-f(3)"
name: "zgegs-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgegs-f/"
description: "zgegs.f –"
---

<p>zgegs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgegs</code> (JOBVSL, JOBVSR, N, A, LDA, B, LDB, ALPHA, BETA, VSL, LDVSL, VSR, LDVSR, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code> ZGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgegs (characterJOBVSL, characterJOBVSR, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( * )ALPHA, complex*16, dimension( * )BETA, complex*16, dimension( ldvsl, * )VSL, integerLDVSL, complex*16, dimension( ldvsr, * )VSR, integerLDVSR, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code> ZGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This routine is deprecated and has been replaced by routine ZGGES.
 ZGEGS computes the eigenvalues, Schur form, and, optionally, the
 left and or/right Schur vectors of a complex matrix pair (A,B).
 Given two square matrices A and B, the generalized Schur
 factorization has the form
 
 A = Q*S*Z**H, B = Q*T*Z**H
 
 where Q and Z are unitary matrices and S and T are upper triangular.
 The columns of Q are the left Schur vectors
 and the columns of Z are the right Schur vectors.
 
 If only the eigenvalues of (A,B) are needed, the driver routine
 ZGEGV should be used instead. See ZGEGV for a description of the
 eigenvalues of the generalized nonsymmetric eigenvalue problem
 (GNEP).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBVSL</i> </p>
<pre> JOBVSL is CHARACTER*1
 = 'N': do not compute the left Schur vectors;
 = 'V': compute the left Schur vectors (returned in VSL).</pre>
<p><i>JOBVSR</i> </p>
<pre> JOBVSR is CHARACTER*1
 = 'N': do not compute the right Schur vectors;
 = 'V': compute the right Schur vectors (returned in VSR).</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A, B, VSL, and VSR. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA, N)
 On entry, the matrix A.
 On exit, the upper triangular matrix S from the generalized
 Schur factorization.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB, N)
 On entry, the matrix B.
 On exit, the upper triangular matrix T from the generalized
 Schur factorization.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B. LDB &gt;= max(1,N).</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16 array, dimension (N)
 The complex scalars alpha that define the eigenvalues of
 GNEP. ALPHA(j) = S(j,j), the diagonal element of the Schur
 form of A.</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX*16 array, dimension (N)
 The non-negative real scalars beta that define the
 eigenvalues of GNEP. BETA(j) = T(j,j), the diagonal element
 of the triangular factor T.
 Together, the quantities alpha = ALPHA(j) and beta = BETA(j)
 represent the j-th eigenvalue of the matrix pair (A,B), in
 one of the forms lambda = alpha/beta or mu = beta/alpha.
 Since either lambda or mu may overflow, they should not,
 in general, be computed.</pre>
<p><i>VSL</i> </p>
<pre> VSL is COMPLEX*16 array, dimension (LDVSL,N)
 If JOBVSL = 'V', the matrix of left Schur vectors Q.
 Not referenced if JOBVSL = 'N'.</pre>
<p><i>LDVSL</i> </p>
<pre> LDVSL is INTEGER
 The leading dimension of the matrix VSL. LDVSL &gt;= 1, and
 if JOBVSL = 'V', LDVSL &gt;= N.</pre>
<p><i>VSR</i> </p>
<pre> VSR is COMPLEX*16 array, dimension (LDVSR,N)
 If JOBVSR = 'V', the matrix of right Schur vectors Z.
 Not referenced if JOBVSR = 'N'.</pre>
<p><i>LDVSR</i> </p>
<pre> LDVSR is INTEGER
 The leading dimension of the matrix VSR. LDVSR &gt;= 1, and
 if JOBVSR = 'V', LDVSR &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,2*N).
 For good performance, LWORK must generally be larger.
 To compute the optimal value of LWORK, call ILAENV to get
 blocksizes (for ZGEQRF, ZUNMQR, and CUNGQR.) Then compute:
 NB -- MAX of the blocksizes for ZGEQRF, ZUNMQR, and CUNGQR;
 the optimal LWORK is N*(NB+1).
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (3*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 =1,...,N:
 The QZ iteration failed. (A,B) are not in Schur
 form, but ALPHA(j) and BETA(j) should be correct for
 j=INFO+1,...,N.
 &gt; N: errors that usually indicate LAPACK problems:
 =N+1: error return from ZGGBAL
 =N+2: error return from ZGEQRF
 =N+3: error return from ZUNMQR
 =N+4: error return from ZUNGQR
 =N+5: error return from ZGGHRD
 =N+6: error return from ZHGEQZ (other than failed
 iteration)
 =N+7: error return from ZGGBAK (computing VSL)
 =N+8: error return from ZGGBAK (computing VSR)
 =N+9: error return from ZLASCL (various places)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 224 of file zgegs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
