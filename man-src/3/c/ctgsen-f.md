---
title: "ctgsen-f(3)"
name: "ctgsen-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctgsen-f/"
description: "ctgsen.f –"
---

<p>ctgsen.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ctgsen</code> (IJOB, WANTQ, WANTZ, SELECT, N, A, LDA, B, LDB, ALPHA, BETA, Q, LDQ, Z, LDZ, M, PL, PR, DIF, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>CTGSEN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctgsen (integerIJOB, logicalWANTQ, logicalWANTZ, logical, dimension( * )SELECT, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( * )ALPHA, complex, dimension( * )BETA, complex, dimension( ldq, * )Q, integerLDQ, complex, dimension( ldz, * )Z, integerLDZ, integerM, realPL, realPR, real, dimension( * )DIF, complex, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code>CTGSEN</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CTGSEN reorders the generalized Schur decomposition of a complex
 matrix pair (A, B) (in terms of an unitary equivalence trans-
 formation Q**H * (A, B) * Z), so that a selected cluster of eigenvalues
 appears in the leading diagonal blocks of the pair (A,B). The leading
 columns of Q and Z form unitary bases of the corresponding left and
 right eigenspaces (deflating subspaces). (A, B) must be in
 generalized Schur canonical form, that is, A and B are both upper
 triangular.
 CTGSEN also computes the generalized eigenvalues
 w(j)= ALPHA(j) / BETA(j)
 of the reordered matrix pair (A, B).
 Optionally, the routine computes estimates of reciprocal condition
 numbers for eigenvalues and eigenspaces. These are Difu[(A11,B11),
 (A22,B22)] and Difl[(A11,B11), (A22,B22)], i.e. the separation(s)
 between the matrix pairs (A11, B11) and (A22,B22) that correspond to
 the selected cluster and the eigenvalues outside the cluster, resp.,
 and norms of &quot;projections&quot; onto left and right eigenspaces w.r.t.
 the selected cluster in the (1,1)-block.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>IJOB</i> </p>
<pre> IJOB is integer
 Specifies whether condition numbers are required for the
 cluster of eigenvalues (PL and PR) or the deflating subspaces
 (Difu and Difl):
 =0: Only reorder w.r.t. SELECT. No extras.
 =1: Reciprocal of norms of &quot;projections&quot; onto left and right
 eigenspaces w.r.t. the selected cluster (PL and PR).
 =2: Upper bounds on Difu and Difl. F-norm-based estimate
 (DIF(1:2)).
 =3: Estimate of Difu and Difl. 1-norm-based estimate
 (DIF(1:2)).
 About 5 times as expensive as IJOB = 2.
 =4: Compute PL, PR and DIF (i.e. 0, 1 and 2 above): Economic
 version to get it all.
 =5: Compute PL, PR and DIF (i.e. 0, 1 and 3 above)</pre>
<p><i>WANTQ</i> </p>
<pre> WANTQ is LOGICAL
 .TRUE. : update the left transformation matrix Q;
 .FALSE.: do not update Q.</pre>
<p><i>WANTZ</i> </p>
<pre> WANTZ is LOGICAL
 .TRUE. : update the right transformation matrix Z;
 .FALSE.: do not update Z.</pre>
<p><i>SELECT</i> </p>
<pre> SELECT is LOGICAL array, dimension (N)
 SELECT specifies the eigenvalues in the selected cluster. To
 select an eigenvalue w(j), SELECT(j) must be set to
 .TRUE..</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension(LDA,N)
 On entry, the upper triangular matrix A, in generalized
 Schur canonical form.
 On exit, A is overwritten by the reordered matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension(LDB,N)
 On entry, the upper triangular matrix B, in generalized
 Schur canonical form.
 On exit, B is overwritten by the reordered matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX array, dimension (N)</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX array, dimension (N)
 The diagonal elements of A and B, respectively,
 when the pair (A,B) has been reduced to generalized Schur
 form. ALPHA(i)/BETA(i) i=1,...,N are the generalized
 eigenvalues.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX array, dimension (LDQ,N)
 On entry, if WANTQ = .TRUE., Q is an N-by-N matrix.
 On exit, Q has been postmultiplied by the left unitary
 transformation matrix which reorder (A, B); The leading M
 columns of Q form orthonormal bases for the specified pair of
 left eigenspaces (deflating subspaces).
 If WANTQ = .FALSE., Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= 1.
 If WANTQ = .TRUE., LDQ &gt;= N.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX array, dimension (LDZ,N)
 On entry, if WANTZ = .TRUE., Z is an N-by-N matrix.
 On exit, Z has been postmultiplied by the left unitary
 transformation matrix which reorder (A, B); The leading M
 columns of Z form orthonormal bases for the specified pair of
 left eigenspaces (deflating subspaces).
 If WANTZ = .FALSE., Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1.
 If WANTZ = .TRUE., LDZ &gt;= N.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The dimension of the specified pair of left and right
 eigenspaces, (deflating subspaces) 0 &lt;= M &lt;= N.</pre>
<p><i>PL</i> </p>
<pre> PL is REAL</pre>
<p><i>PR</i> </p>
<pre> PR is REAL
 If IJOB = 1, 4 or 5, PL, PR are lower bounds on the
 reciprocal of the norm of &quot;projections&quot; onto left and right
 eigenspace with respect to the selected cluster.
 0 &lt; PL, PR &lt;= 1.
 If M = 0 or M = N, PL = PR = 1.
 If IJOB = 0, 2 or 3 PL, PR are not referenced.</pre>
<p><i>DIF</i> </p>
<pre> DIF is REAL array, dimension (2).
 If IJOB &gt;= 2, DIF(1:2) store the estimates of Difu and Difl.
 If IJOB = 2 or 4, DIF(1:2) are F-norm-based upper bounds on
 Difu and Difl. If IJOB = 3 or 5, DIF(1:2) are 1-norm-based
 estimates of Difu and Difl, computed using reversed
 communication with CLACN2.
 If M = 0 or N, DIF(1:2) = F-norm([A, B]).
 If IJOB = 0 or 1, DIF is not referenced.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= 1
 If IJOB = 1, 2 or 4, LWORK &gt;= 2*M*(N-M)
 If IJOB = 3 or 5, LWORK &gt;= 4*M*(N-M)
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of the array IWORK. LIWORK &gt;= 1.
 If IJOB = 1, 2 or 4, LIWORK &gt;= N+2;
 If IJOB = 3 or 5, LIWORK &gt;= MAX(N+2, 2*M*(N-M));
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal size of the IWORK array,
 returns this value as the first entry of the IWORK array, and
 no error message related to LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 =0: Successful exit.
 &lt;0: If INFO = -i, the i-th argument had an illegal value.
 =1: Reordering of (A, B) failed because the transformed
 matrix pair (A, B) would be too far from generalized
 Schur form; the problem is very ill-conditioned.
 (A, B) may have been partially reordered.
 If requested, 0 is returned in DIF(*), PL and PR.</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> CTGSEN first collects the selected eigenvalues by computing unitary
 U and W that move them to the top left corner of (A, B). In other
 words, the selected eigenvalues are the eigenvalues of (A11, B11) in
 U**H*(A, B)*W = (A11 A12) (B11 B12) n1
 ( 0 A22),( 0 B22) n2
 n1 n2 n1 n2
 where N = n1+n2 and U**H means the conjugate transpose of U. The first
 n1 columns of U and W span the specified pair of left and right
 eigenspaces (deflating subspaces) of (A, B).
 If (A, B) has been obtained from the generalized real Schur
 decomposition of a matrix pair (C, D) = Q*(A, B)*Z', then the
 reordered generalized Schur form of (C, D) is given by
 (C, D) = (Q*U)*(U**H *(A, B)*W)*(Z*W)**H,
 and the first n1 columns of Q*U and Z*W span the corresponding
 deflating subspaces of (C, D) (Q and Z store Q*U and Z*W, resp.).
 Note that if the selected eigenvalue is sufficiently ill-conditioned,
 then its value may differ significantly from its value before
 reordering.
 The reciprocal condition numbers of the left and right eigenspaces
 spanned by the first n1 columns of U and W (or Q*U and Z*W) may
 be returned in DIF(1:2), corresponding to Difu and Difl, resp.
 The Difu and Difl are defined as:
 Difu[(A11, B11), (A22, B22)] = sigma-min( Zu )
 and
 Difl[(A11, B11), (A22, B22)] = Difu[(A22, B22), (A11, B11)],
 where sigma-min(Zu) is the smallest singular value of the
 (2*n1*n2)-by-(2*n1*n2) matrix
 Zu = [ kron(In2, A11) -kron(A22**H, In1) ]
 [ kron(In2, B11) -kron(B22**H, In1) ].
 Here, Inx is the identity matrix of size nx and A22**H is the
 conjuguate transpose of A22. kron(X, Y) is the Kronecker product between
 the matrices X and Y.
 When <a href="//www.systutorials.com/docs/linux/man/2-DIF/">DIF</a>(2) is small, small changes in (A, B) can cause large changes
 in the deflating subspace. An approximate (asymptotic) bound on the
 maximum angular error in the computed deflating subspaces is
 EPS * norm((A, B)) / <a href="//www.systutorials.com/docs/linux/man/2-DIF/">DIF</a>(2),
 where EPS is the machine precision.
 The reciprocal norm of the projectors on the left and right
 eigenspaces associated with (A11, B11) may be returned in PL and PR.
 They are computed as follows. First we compute L and R so that
 P*(A, B)*Q is block diagonal, where
 P = ( I -L ) n1 Q = ( I R ) n1
 ( 0 I ) n2 and ( 0 I ) n2
 n1 n2 n1 n2
 and (L, R) is the solution to the generalized Sylvester equation
 A11*R - L*A22 = -A12
 B11*R - L*B22 = -B12
 Then PL = (F-norm(L)**2+1)**(-1/2) and PR = (F-norm(R)**2+1)**(-1/2).
 An approximate (asymptotic) bound on the average absolute error of
 the selected eigenvalues is
 EPS * norm((A, B)) / PL.
 There are also global error bounds which valid for perturbations up
 to a certain restriction: A lower bound (x) on the smallest
 F-norm(E,F) for which an eigenvalue of (A11, B11) may move and
 coalesce with an eigenvalue of (A22, B22) under perturbation (E,F),
 (i.e. (A + E, B + F), is
 x = min(Difu,Difl)/((1/(PL*PL)+1/(PR*PR))**(1/2)+2*max(1/PL,1/PR)).
 An approximate bound on x can be computed from DIF(1:2), PL and PR.
 If y = ( F-norm(E,F) / x) &lt;= 1, the angles between the perturbed
 (L', R') and unperturbed (L, R) left and right deflating subspaces
 associated with the selected cluster in the (1,1)-blocks can be
 bounded as
 max-angle(L, L') &lt;= arctan( y * PL / (1 - y * (1 - PL * PL)**(1/2))
 max-angle(R, R') &lt;= arctan( y * PR / (1 - y * (1 - PR * PR)**(1/2))
 See LAPACK User's Guide section 4.11 or the following references
 for more information.
 Note that if the default method for computing the Frobenius-norm-
 based estimate DIF is not wanted (see CLATDF), then the parameter
 IDIFJB (see below) should be changed from 3 to 4 (routine CLATDF
 (IJOB = 2 will be used)). See CTGSYL for more details.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl COMPACT>
<dd>[1] B. Kagstrom; A Direct Method for Reordering Eigenvalues in the Generalized Real Schur Form of a Regular Matrix Pair (A, B), in M.S. Moonen et al (eds), Linear Algebra for Large Scale and Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218. </p>
<p>&nbsp;<wbr>[2]&nbsp;<wbr>B. Kagstrom and P. Poromaa;&nbsp;<wbr>Computing Eigenspaces with Specified Eigenvalues of a Regular Matrix Pair&nbsp;<wbr>(A, B)&nbsp;<wbr>and Condition Estimation: Theory, Algorithms and Software, Report UMINF &#8211; 94.04, Department of Computing Science, Umea University, S-901 87 Umea, Sweden, 1994. Also as LAPACK Working Note 87. To appear in Numerical Algorithms, 1996.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[3]&nbsp;<wbr>B. Kagstrom and P. Poromaa, LAPACK-Style Algorithms and Software for Solving the Generalized Sylvester Equation and Estimating the Separation between Regular Matrix Pairs, Report UMINF &#8211; 93.23, Department of Computing Science, Umea University, S-901 87 Umea, Sweden, December 1993, Revised April 1994, Also as LAPACK working Note 75. To appear in ACM Trans. on Math. Software, Vol 22, No 1, 1996.&nbsp;<wbr></dl>
<p> Definition at line 432 of file ctgsen.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
