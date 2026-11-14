---
title: "sgegs-f(3)"
name: "sgegs-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgegs-f/"
description: "sgegs.f –"
---

<p>sgegs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sgegs</code> (JOBVSL, JOBVSR, N, A, LDA, B, LDB, ALPHAR, ALPHAI, BETA, VSL, LDVSL, VSR, LDVSR, WORK, LWORK, INFO)<br />
 <i></i><code> SGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgegs (characterJOBVSL, characterJOBVSR, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( * )ALPHAR, real, dimension( * )ALPHAI, real, dimension( * )BETA, real, dimension( ldvsl, * )VSL, integerLDVSL, real, dimension( ldvsr, * )VSR, integerLDVSR, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code> SGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This routine is deprecated and has been replaced by routine SGGES.
 SGEGS computes the eigenvalues, real Schur form, and, optionally,
 left and or/right Schur vectors of a real matrix pair (A,B).
 Given two square matrices A and B, the generalized real Schur
 factorization has the form
 
 A = Q*S*Z**T, B = Q*T*Z**T
 where Q and Z are orthogonal matrices, T is upper triangular, and S
 is an upper quasi-triangular matrix with 1-by-1 and 2-by-2 diagonal
 blocks, the 2-by-2 blocks corresponding to complex conjugate pairs
 of eigenvalues of (A,B). The columns of Q are the left Schur vectors
 and the columns of Z are the right Schur vectors.
 
 If only the eigenvalues of (A,B) are needed, the driver routine
 SGEGV should be used instead. See SGEGV for a description of the
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
<pre> A is REAL array, dimension (LDA, N)
 On entry, the matrix A.
 On exit, the upper quasi-triangular matrix S from the
 generalized real Schur factorization.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB, N)
 On entry, the matrix B.
 On exit, the upper triangular matrix T from the generalized
 real Schur factorization.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B. LDB &gt;= max(1,N).</pre>
<p><i>ALPHAR</i> </p>
<pre> ALPHAR is REAL array, dimension (N)
 The real parts of each scalar alpha defining an eigenvalue
 of GNEP.</pre>
<p><i>ALPHAI</i> </p>
<pre> ALPHAI is REAL array, dimension (N)
 The imaginary parts of each scalar alpha defining an
 eigenvalue of GNEP. If ALPHAI(j) is zero, then the j-th
 eigenvalue is real; if positive, then the j-th and (j+1)-st
 eigenvalues are a complex conjugate pair, with
 ALPHAI(j+1) = -ALPHAI(j).</pre>
<p><i>BETA</i> </p>
<pre> BETA is REAL array, dimension (N)
 The scalars beta that define the eigenvalues of GNEP.
 Together, the quantities alpha = (ALPHAR(j),ALPHAI(j)) and
 beta = BETA(j) represent the j-th eigenvalue of the matrix
 pair (A,B), in one of the forms lambda = alpha/beta or
 mu = beta/alpha. Since either lambda or mu may overflow,
 they should not, in general, be computed.</pre>
<p><i>VSL</i> </p>
<pre> VSL is REAL array, dimension (LDVSL,N)
 If JOBVSL = 'V', the matrix of left Schur vectors Q.
 Not referenced if JOBVSL = 'N'.</pre>
<p><i>LDVSL</i> </p>
<pre> LDVSL is INTEGER
 The leading dimension of the matrix VSL. LDVSL &gt;=1, and
 if JOBVSL = 'V', LDVSL &gt;= N.</pre>
<p><i>VSR</i> </p>
<pre> VSR is REAL array, dimension (LDVSR,N)
 If JOBVSR = 'V', the matrix of right Schur vectors Z.
 Not referenced if JOBVSR = 'N'.</pre>
<p><i>LDVSR</i> </p>
<pre> LDVSR is INTEGER
 The leading dimension of the matrix VSR. LDVSR &gt;= 1, and
 if JOBVSR = 'V', LDVSR &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,4*N).
 For good performance, LWORK must generally be larger.
 To compute the optimal value of LWORK, call ILAENV to get
 blocksizes (for SGEQRF, SORMQR, and SORGQR.) Then compute:
 NB -- MAX of the blocksizes for SGEQRF, SORMQR, and SORGQR
 The optimal LWORK is 2*N + N*(NB+1).
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 = 1,...,N:
 The QZ iteration failed. (A,B) are not in Schur
 form, but ALPHAR(j), ALPHAI(j), and BETA(j) should
 be correct for j=INFO+1,...,N.
 &gt; N: errors that usually indicate LAPACK problems:
 =N+1: error return from SGGBAL
 =N+2: error return from SGEQRF
 =N+3: error return from SORMQR
 =N+4: error return from SORGQR
 =N+5: error return from SGGHRD
 =N+6: error return from SHGEQZ (other than failed
 iteration)
 =N+7: error return from SGGBAK (computing VSL)
 =N+8: error return from SGGBAK (computing VSR)
 =N+9: error return from SLASCL (various places)</pre>
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
<p> Definition at line 226 of file sgegs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
