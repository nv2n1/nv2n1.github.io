---
title: "dgees-f(3)"
name: "dgees-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgees-f/"
description: "dgees.f –"
---

<p>dgees.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgees</code> (JOBVS, SORT, SELECT, N, A, LDA, SDIM, WR, WI, VS, LDVS, WORK, LWORK, BWORK, INFO)<br />
 <i></i><code> DGEES computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgees (characterJOBVS, characterSORT, logical, externalSELECT, integerN, double precision, dimension( lda, * )A, integerLDA, integerSDIM, double precision, dimension( * )WR, double precision, dimension( * )WI, double precision, dimension( ldvs, * )VS, integerLDVS, double precision, dimension( * )WORK, integerLWORK, logical, dimension( * )BWORK, integerINFO)</h3>
<p><code> DGEES computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGEES computes for an N-by-N real nonsymmetric matrix A, the
 eigenvalues, the real Schur form T, and, optionally, the matrix of
 Schur vectors Z. This gives the Schur factorization A = Z*T*(Z**T).
 Optionally, it also orders the eigenvalues on the diagonal of the
 real Schur form so that selected eigenvalues are at the top left.
 The leading columns of Z then form an orthonormal basis for the
 invariant subspace corresponding to the selected eigenvalues.
 A matrix is in real Schur form if it is upper quasi-triangular with
 1-by-1 and 2-by-2 blocks. 2-by-2 blocks will be standardized in the
 form
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
<pre> SELECT is a LOGICAL FUNCTION of two DOUBLE PRECISION arguments
 SELECT must be declared EXTERNAL in the calling subroutine.
 If SORT = 'S', SELECT is used to select eigenvalues to sort
 to the top left of the Schur form.
 If SORT = 'N', SELECT is not referenced.
 An eigenvalue WR(j)+sqrt(-1)*WI(j) is selected if
 SELECT(WR(j),WI(j)) is true; i.e., if either one of a complex
 conjugate pair of eigenvalues is selected, then both complex
 eigenvalues are selected.
 Note that a selected complex eigenvalue may no longer
 satisfy SELECT(WR(j),WI(j)) = .TRUE. after ordering, since
 ordering may change the value of complex eigenvalues
 (especially if the eigenvalue is ill-conditioned); in this
 case INFO is set to N+2 (see INFO below).</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the N-by-N matrix A.
 On exit, A has been overwritten by its real Schur form T.</pre>
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
 WR and WI contain the real and imaginary parts,
 respectively, of the computed eigenvalues in the same order
 that they appear on the diagonal of the output Schur form T.
 Complex conjugate pairs of eigenvalues will appear
 consecutively with the eigenvalue having the positive
 imaginary part first.</pre>
<p><i>VS</i> </p>
<pre> VS is DOUBLE PRECISION array, dimension (LDVS,N)
 If JOBVS = 'V', VS contains the orthogonal matrix Z of Schur
 vectors.
 If JOBVS = 'N', VS is not referenced.</pre>
<p><i>LDVS</i> </p>
<pre> LDVS is INTEGER
 The leading dimension of the array VS. LDVS &gt;= 1; if
 JOBVS = 'V', LDVS &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) contains the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,3*N).
 For good performance, LWORK must generally be larger.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
 JOBVS = 'V', VS contains the matrix which reduces A
 to its partially converged Schur form.
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
<p> Definition at line 216 of file dgees.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
