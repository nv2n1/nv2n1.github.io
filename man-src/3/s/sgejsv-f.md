---
title: "sgejsv-f(3)"
name: "sgejsv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgejsv-f/"
description: "sgejsv.f –"
---

<p>sgejsv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sgejsv</code> (JOBA, JOBU, JOBV, JOBR, JOBT, JOBP, M, N, A, LDA, SVA, U, LDU, V, LDV, WORK, LWORK, IWORK, INFO)<br />
 <i></i><code>SGEJSV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgejsv (character*1JOBA, character*1JOBU, character*1JOBV, character*1JOBR, character*1JOBT, character*1JOBP, integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( n )SVA, real, dimension( ldu, * )U, integerLDU, real, dimension( ldv, * )V, integerLDV, real, dimension( lwork )WORK, integerLWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>SGEJSV</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SGEJSV computes the singular value decomposition (SVD) of a real M-by-N
 matrix [A], where M &gt;= N. The SVD of [A] is written as
 [A] = [U] * [SIGMA] * [V]^t,
 where [SIGMA] is an N-by-N (M-by-N) matrix which is zero except for its N
 diagonal elements, [U] is an M-by-N (or M-by-M) orthonormal matrix, and
 [V] is an N-by-N orthogonal matrix. The diagonal elements of [SIGMA] are
 the singular values of [A]. The columns of [U] and [V] are the left and
 the right singular vectors of [A], respectively. The matrices [U] and [V]
 are computed and stored in the arrays U and V, respectively. The diagonal
 of [SIGMA] is computed and stored in the array SVA.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBA</i> </p>
<pre> JOBA is CHARACTER*1
 Specifies the level of accuracy:
 = 'C': This option works well (high relative accuracy) if A = B * D,
 with well-conditioned B and arbitrary diagonal matrix D.
 The accuracy cannot be spoiled by COLUMN scaling. The
 accuracy of the computed output depends on the condition of
 B, and the procedure aims at the best theoretical accuracy.
 The relative error max_{i=1:N}|d sigma_i| / sigma_i is
 bounded by f(M,N)*epsilon* cond(B), independent of D.
 The input matrix is preprocessed with the QRF with column
 pivoting. This initial preprocessing and preconditioning by
 a rank revealing QR factorization is common for all values of
 JOBA. Additional actions are specified as follows:
 = 'E': Computation as with 'C' with an additional estimate of the
 condition number of B. It provides a realistic error bound.
 = 'F': If A = D1 * C * D2 with ill-conditioned diagonal scalings
 D1, D2, and well-conditioned matrix C, this option gives
 higher accuracy than the 'C' option. If the structure of the
 input matrix is not known, and relative accuracy is
 desirable, then this option is advisable. The input matrix A
 is preprocessed with QR factorization with FULL (row and
 column) pivoting.
 = 'G' Computation as with 'F' with an additional estimate of the
 condition number of B, where A=D*B. If A has heavily weighted
 rows, then using this condition number gives too pessimistic
 error bound.
 = 'A': Small singular values are the noise and the matrix is treated
 as numerically rank defficient. The error in the computed
 singular values is bounded by f(m,n)*epsilon*||A||.
 The computed SVD A = U * S * V^t restores A up to
 f(m,n)*epsilon*||A||.
 This gives the procedure the licence to discard (set to zero)
 all singular values below N*epsilon*||A||.
 = 'R': Similar as in 'A'. Rank revealing property of the initial
 QR factorization is used do reveal (using triangular factor)
 a gap sigma_{r+1} &lt; epsilon * sigma_r in which case the
 numerical RANK is declared to be r. The SVD is computed with
 absolute error bounds, but more accurately than with 'A'.</pre>
<p><i>JOBU</i> </p>
<pre> JOBU is CHARACTER*1
 Specifies whether to compute the columns of U:
 = 'U': N columns of U are returned in the array U.
 = 'F': full set of M left sing. vectors is returned in the array U.
 = 'W': U may be used as workspace of length M*N. See the description
 of U.
 = 'N': U is not computed.</pre>
<p><i>JOBV</i> </p>
<pre> JOBV is CHARACTER*1
 Specifies whether to compute the matrix V:
 = 'V': N columns of V are returned in the array V; Jacobi rotations
 are not explicitly accumulated.
 = 'J': N columns of V are returned in the array V, but they are
 computed as the product of Jacobi rotations. This option is
 allowed only if JOBU .NE. 'N', i.e. in computing the full SVD.
 = 'W': V may be used as workspace of length N*N. See the description
 of V.
 = 'N': V is not computed.</pre>
<p><i>JOBR</i> </p>
<pre> JOBR is CHARACTER*1
 Specifies the RANGE for the singular values. Issues the licence to
 set to zero small positive singular values if they are outside
 specified range. If A .NE. 0 is scaled so that the largest singular
 value of c*A is around SQRT(BIG), BIG=SLAMCH('O'), then JOBR issues
 the licence to kill columns of A whose norm in c*A is less than
 SQRT(SFMIN) (for JOBR.EQ.'R'), or less than SMALL=SFMIN/EPSLN,
 where SFMIN=SLAMCH('S'), EPSLN=SLAMCH('E').
 = 'N': Do not kill small columns of c*A. This option assumes that
 BLAS and QR factorizations and triangular solvers are
 implemented to work in that range. If the condition of A
 is greater than BIG, use SGESVJ.
 = 'R': RESTRICTED range for sigma(c*A) is [SQRT(SFMIN), SQRT(BIG)]
 (roughly, as described above). This option is recommended.
 ===========================
 For computing the singular values in the FULL range [SFMIN,BIG]
 use SGESVJ.</pre>
<p><i>JOBT</i> </p>
<pre> JOBT is CHARACTER*1
 If the matrix is square then the procedure may determine to use
 transposed A if A^t seems to be better with respect to convergence.
 If the matrix is not square, JOBT is ignored. This is subject to
 changes in the future.
 The decision is based on two values of entropy over the adjoint
 orbit of A^t * A. See the descriptions of <a href="//www.systutorials.com/docs/linux/man/6-WORK/">WORK</a>(6) and <a href="//www.systutorials.com/docs/linux/man/7-WORK/">WORK</a>(7).
 = 'T': transpose if entropy test indicates possibly faster
 convergence of Jacobi process if A^t is taken as input. If A is
 replaced with A^t, then the row pivoting is included automatically.
 = 'N': do not speculate.
 This option can be used to compute only the singular values, or the
 full SVD (U, SIGMA and V). For only one set of singular vectors
 (U or V), the caller should provide both U and V, as one of the
 matrices is used as workspace if the matrix A is transposed.
 The implementer can easily remove this constraint and make the
 code more complicated. See the descriptions of U and V.</pre>
<p><i>JOBP</i> </p>
<pre> JOBP is CHARACTER*1
 Issues the licence to introduce structured perturbations to drown
 denormalized numbers. This licence should be active if the
 denormals are poorly implemented, causing slow computation,
 especially in cases of fast convergence (!). For details see [1,2].
 For the sake of simplicity, this perturbations are included only
 when the full SVD or only the singular values are requested. The
 implementer/user can easily add the perturbation for the cases of
 computing one set of singular vectors.
 = 'P': introduce perturbation
 = 'N': do not perturb</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the input matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the input matrix A. M &gt;= N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the M-by-N matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>SVA</i> </p>
<pre> SVA is REAL array, dimension (N)
 On exit,
 - For WORK(1)/<a href="//www.systutorials.com/docs/linux/man/2-WORK/">WORK</a>(2) = ONE: The singular values of A. During the
 computation SVA contains Euclidean column norms of the
 iterated matrices in the array A.
 - For WORK(1) .NE. <a href="//www.systutorials.com/docs/linux/man/2-WORK/">WORK</a>(2): The singular values of A are
 (WORK(1)/<a href="//www.systutorials.com/docs/linux/man/2-WORK/">WORK</a>(2)) * SVA(1:N). This factored form is used if
 sigma_max(A) overflows or if small singular values have been
 saved from underflow by scaling the input matrix A.
 - If JOBR='R' then some of the singular values may be returned
 as exact zeros obtained by &quot;set to zero&quot; because they are
 below the numerical rank threshold or are denormalized numbers.</pre>
<p><i>U</i> </p>
<pre> U is REAL array, dimension ( LDU, N )
 If JOBU = 'U', then U contains on exit the M-by-N matrix of
 the left singular vectors.
 If JOBU = 'F', then U contains on exit the M-by-M matrix of
 the left singular vectors, including an ONB
 of the orthogonal complement of the Range(A).
 If JOBU = 'W' .AND. (JOBV.EQ.'V' .AND. JOBT.EQ.'T' .AND. M.EQ.N),
 then U is used as workspace if the procedure
 replaces A with A^t. In that case, [V] is computed
 in U as left singular vectors of A^t and then
 copied back to the V array. This 'W' option is just
 a reminder to the caller that in this case U is
 reserved as workspace of length N*N.
 If JOBU = 'N' U is not referenced.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U, LDU &gt;= 1.
 IF JOBU = 'U' or 'F' or 'W', then LDU &gt;= M.</pre>
<p><i>V</i> </p>
<pre> V is REAL array, dimension ( LDV, N )
 If JOBV = 'V', 'J' then V contains on exit the N-by-N matrix of
 the right singular vectors;
 If JOBV = 'W', AND (JOBU.EQ.'U' AND JOBT.EQ.'T' AND M.EQ.N),
 then V is used as workspace if the pprocedure
 replaces A with A^t. In that case, [U] is computed
 in V as right singular vectors of A^t and then
 copied back to the U array. This 'W' option is just
 a reminder to the caller that in this case V is
 reserved as workspace of length N*N.
 If JOBV = 'N' V is not referenced.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V, LDV &gt;= 1.
 If JOBV = 'V' or 'J' or 'W', then LDV &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension at least LWORK.
 On exit,
 WORK(1) = SCALE = <a href="//www.systutorials.com/docs/linux/man/2-WORK/">WORK</a>(2) / WORK(1) is the scaling factor such
 that SCALE*SVA(1:N) are the computed singular values
 of A. (See the description of SVA().)
 <a href="//www.systutorials.com/docs/linux/man/2-WORK/">WORK</a>(2) = See the description of WORK(1).
 <a href="//www.systutorials.com/docs/linux/man/3-WORK/">WORK</a>(3) = SCONDA is an estimate for the condition number of
 column equilibrated A. (If JOBA .EQ. 'E' or 'G')
 SCONDA is an estimate of SQRT(||(R^t * R)^(-1)||_1).
 It is computed using SPOCON. It holds
 N^(-1/4) * SCONDA &lt;= ||R^(-1)||_2 &lt;= N^(1/4) * SCONDA
 where R is the triangular factor from the QRF of A.
 However, if R is truncated and the numerical rank is
 determined to be strictly smaller than N, SCONDA is
 returned as -1, thus indicating that the smallest
 singular values might be lost.
 If full SVD is needed, the following two condition numbers are
 useful for the analysis of the algorithm. They are provied for
 a developer/implementer who is familiar with the details of
 the method.
 <a href="//www.systutorials.com/docs/linux/man/4-WORK/">WORK</a>(4) = an estimate of the scaled condition number of the
 triangular factor in the first QR factorization.
 <a href="//www.systutorials.com/docs/linux/man/5-WORK/">WORK</a>(5) = an estimate of the scaled condition number of the
 triangular factor in the second QR factorization.
 The following two parameters are computed if JOBT .EQ. 'T'.
 They are provided for a developer/implementer who is familiar
 with the details of the method.
 <a href="//www.systutorials.com/docs/linux/man/6-WORK/">WORK</a>(6) = the entropy of A^t*A :: this is the Shannon entropy
 of diag(A^t*A) / Trace(A^t*A) taken as point in the
 probability simplex.
 <a href="//www.systutorials.com/docs/linux/man/7-WORK/">WORK</a>(7) = the entropy of A*A^t.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 Length of WORK to confirm proper allocation of work space.
 LWORK depends on the job:
 If only SIGMA is needed ( JOBU.EQ.'N', JOBV.EQ.'N' ) and
 -&gt; .. no scaled condition estimate required (JOBE.EQ.'N'):
 LWORK &gt;= max(2*M+N,4*N+1,7). This is the minimal requirement.
 -&gt;&gt; For optimal performance (blocked code) the optimal value
 is LWORK &gt;= max(2*M+N,3*N+(N+1)*NB,7). Here NB is the optimal
 block size for DGEQP3 and DGEQRF.
 In general, optimal LWORK is computed as 
 LWORK &gt;= max(2*M+N,N+LWORK(DGEQP3),N+LWORK(DGEQRF), 7). 
 -&gt; .. an estimate of the scaled condition number of A is
 required (JOBA='E', 'G'). In this case, LWORK is the maximum
 of the above and N*N+4*N, i.e. LWORK &gt;= max(2*M+N,N*N+4*N,7).
 -&gt;&gt; For optimal performance (blocked code) the optimal value 
 is LWORK &gt;= max(2*M+N,3*N+(N+1)*NB, N*N+4*N, 7).
 In general, the optimal length LWORK is computed as
 LWORK &gt;= max(2*M+N,N+LWORK(DGEQP3),N+LWORK(DGEQRF), 
 N+N*N+LWORK(DPOCON),7).
 If SIGMA and the right singular vectors are needed (JOBV.EQ.'V'),
 -&gt; the minimal requirement is LWORK &gt;= max(2*M+N,4*N+1,7).
 -&gt; For optimal performance, LWORK &gt;= max(2*M+N,3*N+(N+1)*NB,7),
 where NB is the optimal block size for DGEQP3, DGEQRF, DGELQ,
 DORMLQ. In general, the optimal length LWORK is computed as
 LWORK &gt;= max(2*M+N,N+LWORK(DGEQP3), N+LWORK(DPOCON), 
 N+LWORK(DGELQ), 2*N+LWORK(DGEQRF), N+LWORK(DORMLQ)).
 If SIGMA and the left singular vectors are needed
 -&gt; the minimal requirement is LWORK &gt;= max(2*M+N,4*N+1,7).
 -&gt; For optimal performance:
 if JOBU.EQ.'U' :: LWORK &gt;= max(2*M+N,3*N+(N+1)*NB,7),
 if JOBU.EQ.'F' :: LWORK &gt;= max(2*M+N,3*N+(N+1)*NB,N+M*NB,7),
 where NB is the optimal block size for DGEQP3, DGEQRF, DORMQR.
 In general, the optimal length LWORK is computed as
 LWORK &gt;= max(2*M+N,N+LWORK(DGEQP3),N+LWORK(DPOCON),
 2*N+LWORK(DGEQRF), N+LWORK(DORMQR)). 
 Here LWORK(DORMQR) equals N*NB (for JOBU.EQ.'U') or 
 M*NB (for JOBU.EQ.'F').
 
 If the full SVD is needed: (JOBU.EQ.'U' or JOBU.EQ.'F') and 
 -&gt; if JOBV.EQ.'V' 
 the minimal requirement is LWORK &gt;= max(2*M+N,6*N+2*N*N). 
 -&gt; if JOBV.EQ.'J' the minimal requirement is 
 LWORK &gt;= max(2*M+N, 4*N+N*N,2*N+N*N+6).
 -&gt; For optimal performance, LWORK should be additionally
 larger than N+M*NB, where NB is the optimal block size
 for DORMQR.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension M+3*N.
 On exit,
 <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) = the numerical rank determined after the initial
 QR factorization with pivoting. See the descriptions
 of JOBA and JOBR.
 <a href="//www.systutorials.com/docs/linux/man/2-IWORK/">IWORK</a>(2) = the number of the computed nonzero singular values
 <a href="//www.systutorials.com/docs/linux/man/3-IWORK/">IWORK</a>(3) = if nonzero, a warning message:
 If <a href="//www.systutorials.com/docs/linux/man/3-IWORK/">IWORK</a>(3).EQ.1 then some of the column norms of A
 were denormalized floats. The requested high accuracy
 is not warranted by the data.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 &lt; 0 : if INFO = -i, then the i-th argument had an illegal value.
 = 0 : successfull exit;
 &gt; 0 : SGEJSV did not converge in the maximal allowed number
 of sweeps. The computed values may be inaccurate.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> SGEJSV implements a preconditioned Jacobi SVD algorithm. It uses SGEQP3,
 SGEQRF, and SGELQF as preprocessors and preconditioners. Optionally, an
 additional row pivoting can be used as a preprocessor, which in some
 cases results in much higher accuracy. An example is matrix A with the
 structure A = D1 * C * D2, where D1, D2 are arbitrarily ill-conditioned
 diagonal matrices and C is well-conditioned matrix. In that case, complete
 pivoting in the first QR factorizations provides accuracy dependent on the
 condition number of C, and independent of D1, D2. Such higher accuracy is
 not completely understood theoretically, but it works well in practice.
 Further, if A can be written as A = B*D, with well-conditioned B and some
 diagonal D, then the high accuracy is guaranteed, both theoretically and
 in software, independent of D. For more details see [1], [2].
 The computational range for the singular values can be the full range
 ( UNDERFLOW,OVERFLOW ), provided that the machine arithmetic and the BLAS
 &amp; LAPACK routines called by SGEJSV are implemented to work in that range.
 If that is not the case, then the restriction for safe computation with
 the singular values in the range of normalized IEEE numbers is that the
 spectral condition number kappa(A)=sigma_max(A)/sigma_min(A) does not
 overflow. This code (SGEJSV) is best used in this restricted range,
 meaning that singular values of magnitude below ||A||_2 / SLAMCH('O') are
 returned as zeros. See JOBR for details on this.
 Further, this implementation is somewhat slower than the one described
 in [1,2] due to replacement of some non-LAPACK components, and because
 the choice of some tuning parameters in the iterative part (SGESVJ) is
 left to the implementer on a particular machine.
 The rank revealing QR factorization (in this code: SGEQP3) should be
 implemented as in [3]. We have a new version of SGEQP3 under development
 that is more robust than the current one in LAPACK, with a cleaner cut in
 rank defficient cases. It will be available in the SIGMA library [4].
 If M is much larger than N, it is obvious that the inital QRF with
 column pivoting can be preprocessed by the QRF without pivoting. That
 well known trick is not used in SGEJSV because in some cases heavy row
 weighting can be treated with complete pivoting. The overhead in cases
 M much larger than N is then only due to pivoting, but the benefits in
 terms of accuracy have prevailed. The implementer/user can incorporate
 this extra QRF step easily. The implementer can also improve data movement
 (matrix transpose, matrix copy, matrix transposed copy) - this
 implementation of SGEJSV uses only the simplest, naive data movement.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Zlatko Drmac (Zagreb, Croatia) and Kresimir Veselic (Hagen, Germany)</dl>
<p> <code>References: </code></p>
<dl>
<dd>
<pre> [1] Z. Drmac and K. Veselic: New fast and accurate Jacobi SVD algorithm I.
 SIAM J. Matrix Anal. Appl. Vol. 35, No. 2 (2008), pp. 1322-1342.
 LAPACK Working note 169.
 [2] Z. Drmac and K. Veselic: New fast and accurate Jacobi SVD algorithm II.
 SIAM J. Matrix Anal. Appl. Vol. 35, No. 2 (2008), pp. 1343-1362.
 LAPACK Working note 170.
 [3] Z. Drmac and Z. Bujanovic: On the failure of rank-revealing QR
 factorization software - a case study.
 ACM Trans. math. Softw. Vol. 35, No 2 (2008), pp. 1-28.
 LAPACK Working note 176.
 [4] Z. Drmac: SIGMA - mathematical software library for accurate SVD, PSV,
 QSVD, (H,K)-SVD computations.
 Department of Mathematics, University of Zagreb, 2008.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Bugs, examples and comments: </code></p>
<dl>
<dd>Please report all bugs and send interesting examples and/or comments to drmac [at] math.hr. Thank you.</dl>
<p> Definition at line 473 of file sgejsv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
