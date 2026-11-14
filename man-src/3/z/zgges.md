---
title: "zgges(3)"
name: "zgges"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgges/"
description: "zgges.f –"
---

<p>zgges.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgges</code> (JOBVSL, JOBVSR, SORT, SELCTG, N, A, LDA, B, LDB, SDIM, ALPHA, BETA, VSL, LDVSL, VSR, LDVSR, WORK, LWORK, RWORK, BWORK, INFO)<br />
 <i></i><code> ZGGES computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgges (characterJOBVSL, characterJOBVSR, characterSORT, logical, externalSELCTG, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, integerSDIM, complex*16, dimension( * )ALPHA, complex*16, dimension( * )BETA, complex*16, dimension( ldvsl, * )VSL, integerLDVSL, complex*16, dimension( ldvsr, * )VSR, integerLDVSR, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, logical, dimension( * )BWORK, integerINFO)</h3>
<p><code> ZGGES computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGGES computes for a pair of N-by-N complex nonsymmetric matrices
 (A,B), the generalized eigenvalues, the generalized complex Schur
 form (S, T), and optionally left and/or right Schur vectors (VSL
 and VSR). This gives the generalized Schur factorization
 (A,B) = ( (VSL)*S*(VSR)**H, (VSL)*T*(VSR)**H )
 where (VSR)**H is the conjugate-transpose of VSR.
 Optionally, it also orders the eigenvalues so that a selected cluster
 of eigenvalues appears in the leading diagonal blocks of the upper
 triangular matrix S and the upper triangular matrix T. The leading
 columns of VSL and VSR then form an unitary basis for the
 corresponding left and right eigenspaces (deflating subspaces).
 (If only the generalized eigenvalues are needed, use the driver
 ZGGEV instead, which is faster.)
 A generalized eigenvalue for a pair of matrices (A,B) is a scalar w
 or a ratio alpha/beta = w, such that A - w*B is singular. It is
 usually represented as the pair (alpha,beta), as there is a
 reasonable interpretation for beta=0, and even for both being zero.
 A pair of matrices (S,T) is in generalized complex Schur form if S
 and T are upper triangular and, in addition, the diagonal elements
 of T are non-negative real numbers.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBVSL</i> </p>
<pre> JOBVSL is CHARACTER*1
 = 'N': do not compute the left Schur vectors;
 = 'V': compute the left Schur vectors.</pre>
<p><i>JOBVSR</i> </p>
<pre> JOBVSR is CHARACTER*1
 = 'N': do not compute the right Schur vectors;
 = 'V': compute the right Schur vectors.</pre>
<p><i>SORT</i> </p>
<pre> SORT is CHARACTER*1
 Specifies whether or not to order the eigenvalues on the
 diagonal of the generalized Schur form.
 = 'N': Eigenvalues are not ordered;
 = 'S': Eigenvalues are ordered (see SELCTG).</pre>
<p><i>SELCTG</i> </p>
<pre> SELCTG is a LOGICAL FUNCTION of two COMPLEX*16 arguments
 SELCTG must be declared EXTERNAL in the calling subroutine.
 If SORT = 'N', SELCTG is not referenced.
 If SORT = 'S', SELCTG is used to select eigenvalues to sort
 to the top left of the Schur form.
 An eigenvalue ALPHA(j)/BETA(j) is selected if
 SELCTG(ALPHA(j),BETA(j)) is true.
 Note that a selected complex eigenvalue may no longer satisfy
 SELCTG(ALPHA(j),BETA(j)) = .TRUE. after ordering, since
 ordering may change the value of complex eigenvalues
 (especially if the eigenvalue is ill-conditioned), in this
 case INFO is set to N+2 (See INFO below).</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A, B, VSL, and VSR. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA, N)
 On entry, the first of the pair of matrices.
 On exit, A has been overwritten by its generalized Schur
 form S.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB, N)
 On entry, the second of the pair of matrices.
 On exit, B has been overwritten by its generalized Schur
 form T.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B. LDB &gt;= max(1,N).</pre>
<p><i>SDIM</i> </p>
<pre> SDIM is INTEGER
 If SORT = 'N', SDIM = 0.
 If SORT = 'S', SDIM = number of eigenvalues (after sorting)
 for which SELCTG is true.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16 array, dimension (N)</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX*16 array, dimension (N)
 On exit, ALPHA(j)/BETA(j), j=1,...,N, will be the
 generalized eigenvalues. ALPHA(j), j=1,...,N and BETA(j),
 j=1,...,N are the diagonals of the complex Schur form (A,B)
 output by ZGGES. The BETA(j) will be non-negative real.
 Note: the quotients ALPHA(j)/BETA(j) may easily over- or
 underflow, and BETA(j) may even be zero. Thus, the user
 should avoid naively computing the ratio alpha/beta.
 However, ALPHA will be always less than and usually
 comparable with norm(A) in magnitude, and BETA always less
 than and usually comparable with norm(B).</pre>
<p><i>VSL</i> </p>
<pre> VSL is COMPLEX*16 array, dimension (LDVSL,N)
 If JOBVSL = 'V', VSL will contain the left Schur vectors.
 Not referenced if JOBVSL = 'N'.</pre>
<p><i>LDVSL</i> </p>
<pre> LDVSL is INTEGER
 The leading dimension of the matrix VSL. LDVSL &gt;= 1, and
 if JOBVSL = 'V', LDVSL &gt;= N.</pre>
<p><i>VSR</i> </p>
<pre> VSR is COMPLEX*16 array, dimension (LDVSR,N)
 If JOBVSR = 'V', VSR will contain the right Schur vectors.
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
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (8*N)</pre>
<p><i>BWORK</i> </p>
<pre> BWORK is LOGICAL array, dimension (N)
 Not referenced if SORT = 'N'.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 =1,...,N:
 The QZ iteration failed. (A,B) are not in Schur
 form, but ALPHA(j) and BETA(j) should be correct for
 j=INFO+1,...,N.
 &gt; N: =N+1: other than QZ iteration failed in ZHGEQZ
 =N+2: after reordering, roundoff changed values of
 some complex eigenvalues so that leading
 eigenvalues in the Generalized Schur form no
 longer satisfy SELCTG=.TRUE. This could also
 be caused due to scaling.
 =N+3: reordering falied in ZTGSEN.</pre>
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
<p> Definition at line 269 of file zgges.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
