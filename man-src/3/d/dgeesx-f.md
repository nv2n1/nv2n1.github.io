---
title: "dgeesx-f(3)"
name: "dgeesx-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgeesx-f/"
description: "dgeesx.f –"
---

<p>dgeesx.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgeesx</code> (JOBVS, SORT, SELECT, SENSE, N, A, LDA, SDIM, WR, WI, VS, LDVS, RCONDE, RCONDV, WORK, LWORK, IWORK, LIWORK, BWORK, INFO)<br />
 <i></i><code> DGEESX computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgeesx (characterJOBVS, characterSORT, logical, externalSELECT, characterSENSE, integerN, double precision, dimension( lda, * )A, integerLDA, integerSDIM, double precision, dimension( * )WR, double precision, dimension( * )WI, double precision, dimension( ldvs, * )VS, integerLDVS, double precisionRCONDE, double precisionRCONDV, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, logical, dimension( * )BWORK, integerINFO)</h3>
<p><code> DGEESX computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGEESX computes for an N-by-N real nonsymmetric matrix A, the
 eigenvalues, the real Schur form T, and, optionally, the matrix of
 Schur vectors Z. This gives the Schur factorization A = Z*T*(Z**T).
 Optionally, it also orders the eigenvalues on the diagonal of the
 real Schur form so that selected eigenvalues are at the top left;
 computes a reciprocal condition number for the average of the
 selected eigenvalues (RCONDE); and computes a reciprocal condition
 number for the right invariant subspace corresponding to the
 selected eigenvalues (RCONDV). The leading columns of Z form an
 orthonormal basis for this invariant subspace.
 For further explanation of the reciprocal condition numbers RCONDE
 and RCONDV, see Section 4.10 of the LAPACK Users' Guide (where
 these quantities are called s and sep respectively).
 A real matrix is in real Schur form if it is upper quasi-triangular
 with 1-by-1 and 2-by-2 blocks. 2-by-2 blocks will be standardized in
 the form
 [ a b ]
 [ c a ]
 where b*c &lt; 0. The eigenvalues of such a block are a +- sqrt(bc).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBVS</i> </p>
<pre> JOBVS is CHARACTER*1
 = 'N': Schur vectors are not computed;
 = 'V': Schur vectors are computed.</pre>
<p><i>SORT</i> </p>
<pre> SORT is CHARACTER*1
 Specifies whether or not to order the eigenvalues on the
 diagonal of the Schur form.
 = 'N': Eigenvalues are not ordered;
 = 'S': Eigenvalues are ordered (see SELECT).</pre>
<p><i>SELECT</i> </p>
<pre> SELECT is procedure) LOGICAL FUNCTION of two DOUBLE PRECISION arguments
 SELECT must be declared EXTERNAL in the calling subroutine.
 If SORT = 'S', SELECT is used to select eigenvalues to sort
 to the top left of the Schur form.
 If SORT = 'N', SELECT is not referenced.
 An eigenvalue WR(j)+sqrt(-1)*WI(j) is selected if
 SELECT(WR(j),WI(j)) is true; i.e., if either one of a
 complex conjugate pair of eigenvalues is selected, then both
 are. Note that a selected complex eigenvalue may no longer
 satisfy SELECT(WR(j),WI(j)) = .TRUE. after ordering, since
 ordering may change the value of complex eigenvalues
 (especially if the eigenvalue is ill-conditioned); in this
 case INFO may be set to N+3 (see INFO below).</pre>
<p><i>SENSE</i> </p>
<pre> SENSE is CHARACTER*1
 Determines which reciprocal condition numbers are computed.
 = 'N': None are computed;
 = 'E': Computed for average of selected eigenvalues only;
 = 'V': Computed for selected right invariant subspace only;
 = 'B': Computed for both.
 If SENSE = 'E', 'V' or 'B', SORT must equal 'S'.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA, N)
 On entry, the N-by-N matrix A.
 On exit, A is overwritten by its real Schur form T.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>SDIM</i> </p>
<pre> SDIM is INTEGER
 If SORT = 'N', SDIM = 0.
 If SORT = 'S', SDIM = number of eigenvalues (after sorting)
 for which SELECT is true. (Complex conjugate
 pairs for which SELECT is true for either
 eigenvalue count as 2.)</pre>
<p><i>WR</i> </p>
<pre> WR is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>WI</i> </p>
<pre> WI is DOUBLE PRECISION array, dimension (N)
 WR and WI contain the real and imaginary parts, respectively,
 of the computed eigenvalues, in the same order that they
 appear on the diagonal of the output Schur form T. Complex
 conjugate pairs of eigenvalues appear consecutively with the
 eigenvalue having the positive imaginary part first.</pre>
<p><i>VS</i> </p>
<pre> VS is DOUBLE PRECISION array, dimension (LDVS,N)
 If JOBVS = 'V', VS contains the orthogonal matrix Z of Schur
 vectors.
 If JOBVS = 'N', VS is not referenced.</pre>
<p><i>LDVS</i> </p>
<pre> LDVS is INTEGER
 The leading dimension of the array VS. LDVS &gt;= 1, and if
 JOBVS = 'V', LDVS &gt;= N.</pre>
<p><i>RCONDE</i> </p>
<pre> RCONDE is DOUBLE PRECISION
 If SENSE = 'E' or 'B', RCONDE contains the reciprocal
 condition number for the average of the selected eigenvalues.
 Not referenced if SENSE = 'N' or 'V'.</pre>
<p><i>RCONDV</i> </p>
<pre> RCONDV is DOUBLE PRECISION
 If SENSE = 'V' or 'B', RCONDV contains the reciprocal
 condition number for the selected right invariant subspace.
 Not referenced if SENSE = 'N' or 'E'.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,3*N).
 Also, if SENSE = 'E' or 'V' or 'B',
 LWORK &gt;= N+2*SDIM*(N-SDIM), where SDIM is the number of
 selected eigenvalues computed by this routine. Note that
 N+2*SDIM*(N-SDIM) &lt;= N+N*N/2. Note also that an error is only
 returned if LWORK &lt; max(1,3*N), but if SENSE = 'E' or 'V' or
 'B' this may not be large enough.
 For good performance, LWORK must generally be larger.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates upper bounds on the optimal sizes of the
 arrays WORK and IWORK, returns these values as the first
 entries of the WORK and IWORK arrays, and no error messages
 related to LWORK or LIWORK are issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of the array IWORK.
 LIWORK &gt;= 1; if SENSE = 'V' or 'B', LIWORK &gt;= SDIM*(N-SDIM).
 Note that SDIM*(N-SDIM) &lt;= N*N/4. Note also that an error is
 only returned if LIWORK &lt; 1, but if SENSE = 'V' or 'B' this
 may not be large enough.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates upper bounds on the optimal sizes of
 the arrays WORK and IWORK, returns these values as the first
 entries of the WORK and IWORK arrays, and no error messages
 related to LWORK or LIWORK are issued by XERBLA.</pre>
<p><i>BWORK</i> </p>
<pre> BWORK is LOGICAL array, dimension (N)
 Not referenced if SORT = 'N'.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = i, and i is
 &lt;= N: the QR algorithm failed to compute all the
 eigenvalues; elements 1:ILO-1 and i+1:N of WR and WI
 contain those eigenvalues which have converged; if
 JOBVS = 'V', VS contains the transformation which
 reduces A to its partially converged Schur form.
 = N+1: the eigenvalues could not be reordered because some
 eigenvalues were too close to separate (the problem
 is very ill-conditioned);
 = N+2: after reordering, roundoff changed values of some
 complex eigenvalues so that leading eigenvalues in
 the Schur form no longer satisfy SELECT=.TRUE. This
 could also be caused by underflow due to scaling.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 280 of file dgeesx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
