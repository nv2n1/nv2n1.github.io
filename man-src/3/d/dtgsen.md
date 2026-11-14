---
title: "dtgsen(3)"
name: "dtgsen"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtgsen/"
description: "dtgsen.f –"
---

<h2 class="name">NAME</h2>
<p> dtgsen.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtgsen</code> (IJOB, WANTQ, WANTZ, SELECT, N, A, LDA, B, LDB, ALPHAR, ALPHAI, BETA, Q, LDQ, Z, LDZ, M, PL, PR, DIF, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>DTGSEN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtgsen (integerIJOB, logicalWANTQ, logicalWANTZ, logical, dimension( * )SELECT, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( * )ALPHAR, double precision, dimension( * )ALPHAI, double precision, dimension( * )BETA, double precision, dimension( ldq, * )Q, integerLDQ, double precision, dimension( ldz, * )Z, integerLDZ, integerM, double precisionPL, double precisionPR, double precision, dimension( * )DIF, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code>DTGSEN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DTGSEN reorders the generalized real Schur decomposition of a real
 matrix pair (A, B) (in terms of an orthonormal equivalence trans-
 formation Q**T * (A, B) * Z), so that a selected cluster of eigenvalues
 appears in the leading diagonal blocks of the upper quasi-triangular
 matrix A and the upper triangular B. The leading columns of Q and
 Z form orthonormal bases of the corresponding left and right eigen-
 spaces (deflating subspaces). (A, B) must be in generalized real
 Schur canonical form (as returned by DGGES), i.e. A is block upper
 triangular with 1-by-1 and 2-by-2 diagonal blocks. B is upper
 triangular.
 DTGSEN also computes the generalized eigenvalues
             w(j) = (ALPHAR(j) + i*ALPHAI(j))/BETA(j)
 of the reordered matrix pair (A, B).
 Optionally, DTGSEN computes the estimates of reciprocal condition
 numbers for eigenvalues and eigenspaces. These are Difu[(A11,B11),
 (A22,B22)] and Difl[(A11,B11), (A22,B22)], i.e. the separation(s)
 between the matrix pairs(A11, B11) and (A22, B22) that correspond to
     the selected cluster and the eigenvalues outside the cluster,
     resp.,
     and norms of "projections" onto left and right eigenspaces w.r.t.the selected cluster in the(1, 1) - block.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>IJOB</i> </p>
<pre>
          IJOB is INTEGER
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
           =5: Compute PL, PR and DIF (i.e. 0, 1 and 3 above)
</pre>
<p> <i>WANTQ</i> </p>
<pre>
          WANTQ is LOGICAL
          .TRUE. : update the left transformation matrix Q;
          .FALSE.: do not update Q.
</pre>
<p> <i>WANTZ</i> </p>
<pre>
          WANTZ is LOGICAL
          .TRUE. : update the right transformation matrix Z;
          .FALSE.: do not update Z.
</pre>
<p> <i>SELECT</i> </p>
<pre>
          SELECT is LOGICAL array, dimension (N)
          SELECT specifies the eigenvalues in the selected cluster.
          To select a real eigenvalue w(j), SELECT(j) must be set to
          .TRUE.. To select a complex conjugate pair of eigenvalues
          w(j) and w(j+1), corresponding to a 2-by-2 diagonal block,
          either SELECT(j) or SELECT(j+1) or both must be set to
          .TRUE.; a complex conjugate pair of eigenvalues must be
          either both included in the cluster or both excluded.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A and B. N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension(LDA,N)
          On entry, the upper quasi-triangular matrix A, with (A, B) in
          generalized real Schur canonical form.
          On exit, A is overwritten by the reordered matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension(LDB,N)
          On entry, the upper triangular matrix B, with (A, B) in
          generalized real Schur canonical form.
          On exit, B is overwritten by the reordered matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,N).
</pre>
<p> <i>ALPHAR</i> </p>
<pre>
          ALPHAR is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>ALPHAI</i> </p>
<pre>
          ALPHAI is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>BETA</i> </p>
<p>BETA is DOUBLE PRECISION array, dimension(N) On exit, (ALPHAR(j) + ALPHAI(j) * i) / BETA(j), j = 1, &#8230;, N, will be the generalized eigenvalues.ALPHAR(j) + ALPHAI(j) * i and BETA(j), j = 1, &#8230;, N are the diagonals of the complex Schur form(S, T)<br />
that would result if the 2 &#8211; by &#8211; 2 diagonal blocks of the real generalized Schur form of(A, B)<br />
were further reduced<br />
    to triangular form using complex unitary transformations.If<br />
    ALPHAI(j)<br />
is zero, then the j &#8211; th eigenvalue is real;<br />
if positive<br />
, then the j &#8211; th and (j + 1) &#8211; st eigenvalues are a complex conjugate pair, with ALPHAI(j + 1) negative.</p>
<p> <i>Q</i> </p>
<p>Q is DOUBLE PRECISION array, dimension(LDQ, N) On entry, if WANTQ =.TRUE., Q is an N &#8211; by &#8211; N matrix.On exit, Q has been postmultiplied by the left orthogonal transformation matrix which reorder(A, B); The leading M<br />
          columns of Q form orthonormal bases for the specified pair of<br />
          left eigenspaces (deflating subspaces).<br />
          If WANTQ = .FALSE., Q is not referenced.</p>
<p> <i>LDQ</i> </p>
<p>LDQ is INTEGER<br />
        The leading dimension of the array Q.LDQ &gt;= 1;<br />
and if WANTQ =.TRUE., LDQ &gt;= N.</p>
<p> <i>Z</i> </p>
<p>Z is DOUBLE PRECISION array, dimension(LDZ, N) On entry, if WANTZ =.TRUE., Z is an N &#8211; by &#8211; N matrix.On exit, Z has been postmultiplied by the left orthogonal transformation matrix which reorder(A, B); The leading M<br />
          columns of Z form orthonormal bases for the specified pair of<br />
          left eigenspaces (deflating subspaces).<br />
          If WANTZ = .FALSE., Z is not referenced.</p>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z. LDZ &gt;= 1;
          If WANTZ = .TRUE., LDZ &gt;= N.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The dimension of the specified pair of left and right eigen-
          spaces (deflating subspaces). 0 &lt;= M &lt;= N.
</pre>
<p> <i>PL</i> </p>
<pre>
          PL is DOUBLE PRECISION
</pre>
<p>&nbsp;<wbr><br />
 <i>PR</i> </p>
<pre>
          PR is DOUBLE PRECISION
          If IJOB = 1, 4 or 5, PL, PR are lower bounds on the
          reciprocal of the norm of &quot;projections&quot; onto left and right
          eigenspaces with respect to the selected cluster.
          0 &lt; PL, PR &lt;= 1.
          If M = 0 or M = N, PL = PR  = 1.
          If IJOB = 0, 2 or 3, PL and PR are not referenced.
</pre>
<p> <i>DIF</i> </p>
<pre>
          DIF is DOUBLE PRECISION array, dimension (2).
          If IJOB &gt;= 2, DIF(1:2) store the estimates of Difu and Difl.
          If IJOB = 2 or 4, DIF(1:2) are F-norm-based upper bounds on
          Difu and Difl. If IJOB = 3 or 5, DIF(1:2) are 1-norm-based
          estimates of Difu and Difl.
          If M = 0 or N, DIF(1:2) = F-norm([A, B]).
          If IJOB = 0 or 1, DIF is not referenced.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array,
          dimension (MAX(1,LWORK)) 
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>LWORK is INTEGER<br />
        The dimension of the array WORK.LWORK &gt;= 4 *N + 16. If IJOB = 1,<br />
                                                               2 or 4, LWORK &gt;= MAX(4 * N + 16, 2 * M * (N &#8211; M)).If IJOB = 3 or 5, LWORK &gt;= MAX(4 * N + 16, 4 * M * (N &#8211; M)).If LWORK = -1, then a workspace query is assumed;<br />
the routine<br />
    only calculates the optimal size of the WORK array,<br />
    returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.</p>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<p>LIWORK is INTEGER<br />
        The dimension of the array IWORK.LIWORK &gt;= 1. If IJOB = 1,<br />
                                                         2 or 4, LIWORK &gt;= N + 6. If IJOB = 3 or 5, LIWORK &gt;= MAX(2 * M * (N &#8211; M), N + 6).If LIWORK = -1, then a workspace query is assumed;<br />
the<br />
    routine only calculates the optimal size of the IWORK array,<br />
    returns this value as the first entry of the IWORK array, and no error message related to LIWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
            =0: Successful exit.
            &lt;0: If INFO = -i, the i-th argument had an illegal value.
            =1: Reordering of (A, B) failed because the transformed
                matrix pair (A, B) would be too far from generalized
                Schur form; the problem is very ill-conditioned.
                (A, B) may have been partially reordered.
                If requested, 0 is returned in DIF(*), PL and PR.
</pre>
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
<p>DTGSEN first collects the selected eigenvalues by computing<br />
    orthogonal U and W that move them to the top left corner<br />
    of(A, B)<br />
        .In other words,<br />
    the selected eigenvalues are the eigenvalues of(A11, B11) in : U **T *(A, B) *W = (A11 A12)(B11 B12)n1(0 A22), (0 B22)n2 n1 n2 n1 n2 where N = n1 + n2 and U * *T means the transpose of U.The first n1 columns of U and W span the specified pair of left and right eigenspaces(deflating subspaces) of(A, B).If(A, B) has been obtained from the generalized real Schur decomposition of a matrix pair(C, D) = Q * (A, B) * Z * *T, then the reordered generalized real Schur form of(C, D)<br />
is given by(C, D) = (Q * U) * (U * *T * (A, B) * W) * (Z * W) * *T,<br />
               and the first n1 columns of Q *U and Z *W span the corresponding<br />
                   deflating subspaces of(C, D)(Q and Z store Q *U and Z *W, resp.)<br />
                       .Note that if the selected eigenvalue is sufficiently ill<br />
                   &#8211; conditioned,<br />
               then its value may differ significantly from its value before<br />
               reordering.The reciprocal condition numbers of the left and right eigenspaces<br />
               spanned by the first n1 columns of U and W(or Q * U and Z * W) may<br />
               be returned in DIF(1 : 2),<br />
               corresponding to Difu and Difl, resp.The Difu and Difl are defined as : Difu[(A11, B11), (A22, B22)] = sigma &#8211; min(Zu) and Difl[(A11, B11), (A22, B22)] = Difu[(A22, B22), (A11, B11)],<br />
               where sigma &#8211; min(Zu) is the smallest singular value of the(2 * n1 * n2) &#8211; by &#8211; (2 * n1 * n2) matrix Zu = [kron(In2, A11) &#8211; kron(A22 * *T, In1)]<br />
                                                                                                                             [kron(In2, B11) &#8211; kron(B22 * *T, In1)]<br />
                                                                                                                                 .Here,<br />
               Inx is the identity matrix of size nx and A22 **T is the<br />
               transpose of A22.kron(X, Y) is the Kronecker product between<br />
               the matrices X and Y.When DIF(2) is small,<br />
               small changes in(A, B)<br />
can cause large changes<br />
    in the deflating subspace.An<br />
    approximate(asymptotic)<br />
bound on the<br />
        maximum angular error in the computed deflating subspaces is<br />
            EPS *norm((A, B)) /<br />
    DIF(2),<br />
    where EPS is the machine precision.The reciprocal norm of the projectors on the left and right<br />
    eigenspaces associated with(A11, B11)<br />
may be returned in PL and PR.They are computed as follows.First we compute L and R so that<br />
        P *(A, B) *<br />
    Q is block diagonal,<br />
    where<br />
    P = (I &#8211; L) n1 Q = (I R)n1(0 I) n2 and (0 I) n2 n1 n2 n1 n2<br />
                       and (L, R) is the solution to the generalized Sylvester equation A11 *R &#8211; L *A22 = -A12<br />
                                                                                                          B11 *R<br />
                                                                                                          &#8211; L *B22 = -B12<br />
                                                                                                                     Then PL = (F &#8211; norm(L) * *2 + 1) * *(-1 / 2) and PR = (F &#8211; norm(R) * *2 + 1) * *(-1 / 2).An approximate(asymptotic) bound on the average absolute error of<br />
  the selected eigenvalues is<br />
       EPS * norm((A, B)) / PL.<br />
  There are also global error bounds which valid for perturbations up<br />
  to a certain restriction:  A lower bound (x) on the smallest<br />
  F-norm(E,F) for which an eigenvalue of (A11, B11)<br />
may move and<br />
    coalesce with an eigenvalue<br />
    of(A22, B22) under perturbation (E,F),<br />
  (i.e. (A + E, B + F), is<br />
   x = min(Difu,Difl)/((1/(PL*PL)+1/(PR*PR))**(1/2)+2*max(1/PL,1/PR)).<br />
  An approximate bound on x can be computed from DIF(1:2), PL and PR.<br />
  If y = ( F-norm(E,F) / x) &lt;= 1, the angles between the perturbed<br />
  (L&#8217;, R&#8217;) and unperturbed (L, R) left and right deflating subspaces<br />
  associated with the selected cluster in the (1,1)-blocks can be<br />
  bounded as<br />
   max-angle(L, L&#8217;) &lt;= arctan( y * PL / (1 &#8211; y * (1 &#8211; PL * PL)**(1/2))<br />
   max-angle(R, R&#8217;) &lt;= arctan( y * PR / (1 &#8211; y * (1 &#8211; PR * PR)**(1/2))<br />
  See LAPACK User&#8217;s Guide section 4.11 or the following references<br />
  for more information.<br />
  Note that if the default method for computing the Frobenius-norm-<br />
  based estimate DIF is not wanted (see DLATDF), then the parameter<br />
  IDIFJB (see below) should be changed from 3 to 4 (routine DLATDF<br />
  (IJOB = 2 will be used)). See DTGSYL for more details.</p>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd>
<pre><code>
[1] B.Kagstrom; A Direct Method for Reordering Eigenvalues in the
      Generalized Real Schur Form of a Regular Matrix Pair (A, B), in
      M.S. Moonen et al (eds), Linear Algebra for Large Scale and
      Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218.
  [2] B. Kagstrom and P. Poromaa; Computing Eigenspaces with Specified
      Eigenvalues of a Regular Matrix Pair (A, B) and Condition
      Estimation: Theory, Algorithms and Software,
      Report UMINF - 94.04, Department of Computing Science, Umea
      University, S-901 87 Umea, Sweden, 1994. Also as LAPACK Working
      Note 87. To appear in Numerical Algorithms, 1996.
  [3] B. Kagstrom and P. Poromaa, LAPACK-Style Algorithms and Software
      for Solving the Generalized Sylvester Equation and Estimating the
      Separation between Regular Matrix Pairs, Report UMINF - 93.23,
      Department of Computing Science, Umea University, S-901 87 Umea,
      Sweden, December 1993, Revised April 1994, Also as LAPACK Working
      Note 75. To appear in ACM Trans. on Math. Software, Vol 22, No 1,
      1996.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 451 of file dtgsen.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
