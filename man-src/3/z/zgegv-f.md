---
title: "zgegv-f(3)"
name: "zgegv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgegv-f/"
description: "zgegv.f –"
---

<p>zgegv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgegv</code> (JOBVL, JOBVR, N, A, LDA, B, LDB, ALPHA, BETA, VL, LDVL, VR, LDVR, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code> ZGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgegv (characterJOBVL, characterJOBVR, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( * )ALPHA, complex*16, dimension( * )BETA, complex*16, dimension( ldvl, * )VL, integerLDVL, complex*16, dimension( ldvr, * )VR, integerLDVR, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code> ZGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This routine is deprecated and has been replaced by routine ZGGEV.
 ZGEGV computes the eigenvalues and, optionally, the left and/or right
 eigenvectors of a complex matrix pair (A,B).
 Given two square matrices A and B,
 the generalized nonsymmetric eigenvalue problem (GNEP) is to find the
 eigenvalues lambda and corresponding (non-zero) eigenvectors x such
 that
 A*x = lambda*B*x.
 An alternate form is to find the eigenvalues mu and corresponding
 eigenvectors y such that
 mu*A*y = B*y.
 These two forms are equivalent with mu = 1/lambda and x = y if
 neither lambda nor mu is zero. In order to deal with the case that
 lambda or mu is zero or small, two values alpha and beta are returned
 for each eigenvalue, such that lambda = alpha/beta and
 mu = beta/alpha.
 The vectors x and y in the above equations are right eigenvectors of
 the matrix pair (A,B). Vectors u and v satisfying
 u**H*A = lambda*u**H*B or mu*v**H*A = v**H*B
 are left eigenvectors of (A,B).
 Note: this routine performs &quot;full balancing&quot; on A and B</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBVL</i> </p>
<pre> JOBVL is CHARACTER*1
 = 'N': do not compute the left generalized eigenvectors;
 = 'V': compute the left generalized eigenvectors (returned
 in VL).</pre>
<p><i>JOBVR</i> </p>
<pre> JOBVR is CHARACTER*1
 = 'N': do not compute the right generalized eigenvectors;
 = 'V': compute the right generalized eigenvectors (returned
 in VR).</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A, B, VL, and VR. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA, N)
 On entry, the matrix A.
 If JOBVL = 'V' or JOBVR = 'V', then on exit A
 contains the Schur form of A from the generalized Schur
 factorization of the pair (A,B) after balancing. If no
 eigenvectors were computed, then only the diagonal elements
 of the Schur form will be correct. See ZGGHRD and ZHGEQZ
 for details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB, N)
 On entry, the matrix B.
 If JOBVL = 'V' or JOBVR = 'V', then on exit B contains the
 upper triangular matrix obtained from B in the generalized
 Schur factorization of the pair (A,B) after balancing.
 If no eigenvectors were computed, then only the diagonal
 elements of B will be correct. See ZGGHRD and ZHGEQZ for
 details.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B. LDB &gt;= max(1,N).</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16 array, dimension (N)
 The complex scalars alpha that define the eigenvalues of
 GNEP.</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX*16 array, dimension (N)
 The complex scalars beta that define the eigenvalues of GNEP.
 
 Together, the quantities alpha = ALPHA(j) and beta = BETA(j)
 represent the j-th eigenvalue of the matrix pair (A,B), in
 one of the forms lambda = alpha/beta or mu = beta/alpha.
 Since either lambda or mu may overflow, they should not,
 in general, be computed.</pre>
<p><i>VL</i> </p>
<pre> VL is COMPLEX*16 array, dimension (LDVL,N)
 If JOBVL = 'V', the left eigenvectors u(j) are stored
 in the columns of VL, in the same order as their eigenvalues.
 Each eigenvector is scaled so that its largest component has
 abs(real part) + abs(imag. part) = 1, except for eigenvectors
 corresponding to an eigenvalue with alpha = beta = 0, which
 are set to zero.
 Not referenced if JOBVL = 'N'.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the matrix VL. LDVL &gt;= 1, and
 if JOBVL = 'V', LDVL &gt;= N.</pre>
<p><i>VR</i> </p>
<pre> VR is COMPLEX*16 array, dimension (LDVR,N)
 If JOBVR = 'V', the right eigenvectors x(j) are stored
 in the columns of VR, in the same order as their eigenvalues.
 Each eigenvector is scaled so that its largest component has
 abs(real part) + abs(imag. part) = 1, except for eigenvectors
 corresponding to an eigenvalue with alpha = beta = 0, which
 are set to zero.
 Not referenced if JOBVR = 'N'.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the matrix VR. LDVR &gt;= 1, and
 if JOBVR = 'V', LDVR &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,2*N).
 For good performance, LWORK must generally be larger.
 To compute the optimal value of LWORK, call ILAENV to get
 blocksizes (for ZGEQRF, ZUNMQR, and ZUNGQR.) Then compute:
 NB -- MAX of the blocksizes for ZGEQRF, ZUNMQR, and ZUNGQR;
 The optimal LWORK is MAX( 2*N, N*(NB+1) ).
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (8*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 =1,...,N:
 The QZ iteration failed. No eigenvectors have been
 calculated, but ALPHA(j) and BETA(j) should be
 correct for j=INFO+1,...,N.
 &gt; N: errors that usually indicate LAPACK problems:
 =N+1: error return from ZGGBAL
 =N+2: error return from ZGEQRF
 =N+3: error return from ZUNMQR
 =N+4: error return from ZUNGQR
 =N+5: error return from ZGGHRD
 =N+6: error return from ZHGEQZ (other than failed
 iteration)
 =N+7: error return from ZTGEVC
 =N+8: error return from ZGGBAK (computing VL)
 =N+9: error return from ZGGBAK (computing VR)
 =N+10: error return from ZLASCL (various calls)</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> Balancing
 ---------
 This driver calls ZGGBAL to both permute and scale rows and columns
 of A and B. The permutations PL and PR are chosen so that PL*A*PR
 and PL*B*R will be upper triangular except for the diagonal blocks
 A(i:j,i:j) and B(i:j,i:j), with i and j as close together as
 possible. The diagonal scaling matrices DL and DR are chosen so
 that the pair DL*PL*A*PR*DR, DL*PL*B*PR*DR have elements close to
 one (except for the elements that start out zero.)
 After the eigenvalues and eigenvectors of the balanced matrices
 have been computed, ZGGBAK transforms the eigenvectors back to what
 they would have been (in perfect arithmetic) if they had not been
 balanced.
 Contents of A and B on Exit
 -------- -- - --- - -- ----
 If any eigenvectors are computed (either JOBVL='V' or JOBVR='V' or
 both), then on exit the arrays A and B will contain the complex Schur
 form[*] of the &quot;balanced&quot; versions of A and B. If no eigenvectors
 are computed, then only the diagonal blocks will be correct.
 [*] In other words, upper triangular form.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 282 of file zgegv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
