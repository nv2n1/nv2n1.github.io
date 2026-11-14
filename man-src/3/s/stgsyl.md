---
title: "stgsyl(3)"
name: "stgsyl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stgsyl/"
description: "stgsyl.f –"
---

<h2 class="name">NAME</h2>
<p> stgsyl.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>stgsyl</code> (TRANS, IJOB, M, N, A, LDA, B, LDB, C, LDC, D, LDD, E, LDE, F, LDF, SCALE, DIF, WORK, LWORK, IWORK, INFO)<br />
 <i></i><code>STGSYL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stgsyl (characterTRANS, integerIJOB, integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( ldc, * )C, integerLDC, real, dimension( ldd, * )D, integerLDD, real, dimension( lde, * )E, integerLDE, real, dimension( ldf, * )F, integerLDF, realSCALE, realDIF, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>STGSYL</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
STGSYL solves the generalized Sylvester equation : A *R - L *B = scale * C(1)
                                                                             D *R -
                                                                 L *E = scale * F
                                                                                    where R and
                                                                        L are unknown m - by - n matrices,
                                                            (A, D), (B, E) and (C, F) are given matrix pairs of size m - by - m, n - by - n and m - by - n,
                                                            respectively, with real entries.(A, D) and (B, E) must be in generalized(real) Schur canonical form, i.e. A, B are upper quasi
 triangular and D, E are upper triangular.
 The solution (R, L) overwrites (C, F). 0 &lt;= SCALE &lt;= 1 is an output
 scaling factor chosen to avoid overflow.
 In matrix notation (1) is equivalent to solve  Zx = scale b, where
 Z is defined as
            Z = [ kron(In, A)  -kron(B**T, Im) ]         (2)
                [ kron(In, D)  -kron(E**T, Im) ].
 Here Ik is the identity matrix of size k and X**T is the transpose of
 X. kron(X, Y) is the Kronecker product between the matrices X and Y.
 If TRANS = 'T', STGSYL solves the transposed system Z**T*y = scale*b,
 which is equivalent to solve for R and L in
             A**T * R + D**T * L = scale * C           (3)
             R * B**T + L * E**T = scale * -F
 This case (TRANS = 'T') is used to compute an one-norm-based estimate
 of Dif[(A,D), (B,E)], the separation between the matrix pairs (A,D)
 and (B,E), using SLACON.
 If IJOB &gt;= 1, STGSYL computes a Frobenius norm-based estimate
 of Dif[(A,D),(B,E)]. That is, the reciprocal of a lower bound on the
 reciprocal of the smallest singular value of Z. See [1-2] for more
 information.
 This is a level 3 BLAS algorithm.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N', solve the generalized Sylvester equation (1).
          = 'T', solve the 'transposed' system (3).
</pre>
<p> <i>IJOB</i> </p>
<p>IJOB is INTEGER<br />
    Specifies what kind of functionality to be performed.= 0 : solve(1) only.= 1 : The functionality of 0 and 3. = 2 : The functionality of 0 and 4. = 3 : Only an estimate of Dif[(A, D), (B, E)] is computed.(look ahead strategy IJOB = 1 is used).= 4 : Only an estimate of Dif[(A, D), (B, E)] is computed.(SGECON on sub &#8211; systems is used).Not referenced if TRANS = &#8216;T&#8217;.</p>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The order of the matrices A and D, and the row dimension of
          the matrices C, F, R and L.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices B and E, and the column dimension
          of the matrices C, F, R and L.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA, M)
          The upper quasi triangular matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1, M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB, N)
          The upper quasi triangular matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1, N).
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (LDC, N)
          On entry, C contains the right-hand-side of the first matrix
          equation in (1) or (3).
          On exit, if IJOB = 0, 1 or 2, C has been overwritten by
          the solution R. If IJOB = 3 or 4 and TRANS = 'N', C holds R,
          the solution achieved during the computation of the
          Dif-estimate.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1, M).
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (LDD, M)
          The upper triangular matrix D.
</pre>
<p> <i>LDD</i> </p>
<pre>
          LDD is INTEGER
          The leading dimension of the array D. LDD &gt;= max(1, M).
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (LDE, N)
          The upper triangular matrix E.
</pre>
<p> <i>LDE</i> </p>
<pre>
          LDE is INTEGER
          The leading dimension of the array E. LDE &gt;= max(1, N).
</pre>
<p> <i>F</i> </p>
<pre>
          F is REAL array, dimension (LDF, N)
          On entry, F contains the right-hand-side of the second matrix
          equation in (1) or (3).
          On exit, if IJOB = 0, 1 or 2, F has been overwritten by
          the solution L. If IJOB = 3 or 4 and TRANS = 'N', F holds L,
          the solution achieved during the computation of the
          Dif-estimate.
</pre>
<p> <i>LDF</i> </p>
<pre>
          LDF is INTEGER
          The leading dimension of the array F. LDF &gt;= max(1, M).
</pre>
<p> <i>DIF</i> </p>
<pre>
          DIF is REAL
          On exit DIF is the reciprocal of a lower bound of the
          reciprocal of the Dif-function, i.e. DIF is an upper bound of
          Dif[(A,D), (B,E)] = sigma_min(Z), where Z as in (2).
          IF IJOB = 0 or TRANS = 'T', DIF is not touched.
</pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is REAL
          On exit SCALE is the scaling factor in (1) or (3).
          If 0 &lt; SCALE &lt; 1, C and F hold the solutions R and L, resp.,
          to a slightly perturbed system but the input matrices A, B, D
          and E have not been changed. If SCALE = 0, C and F hold the
          solutions R and L, respectively, to the homogeneous system
          with C = F = 0. Normally, SCALE = 1.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK. LWORK &gt; = 1.
          If IJOB = 1 or 2 and TRANS = 'N', LWORK &gt;= max(1,2*M*N).
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (M+N+6)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
            =0: successful exit
            &lt;0: If INFO = -i, the i-th argument had an illegal value.
            &gt;0: (A, D) and (B, E) have common or close eigenvalues.
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd>
<pre><code>
  [1] B. Kagstrom and P. Poromaa, LAPACK-Style Algorithms and Software
      for Solving the Generalized Sylvester Equation and Estimating the
      Separation between Regular Matrix Pairs, Report UMINF - 93.23,
      Department of Computing Science, Umea University, S-901 87 Umea,
      Sweden, December 1993, Revised April 1994, Also as LAPACK Working
      Note 75.  To appear in ACM Trans. on Math. Software, Vol 22,
      No 1, 1996.
  [2] B. Kagstrom, A Perturbation Analysis of the Generalized Sylvester
      Equation (AR - LB, DR - LE ) = (C, F), SIAM J. Matrix Anal.
      Appl., H(4):1045-1060, 1994
  [3] B. Kagstrom and L. Westin, Generalized Schur Methods with
      Condition Estimators for Solving the Generalized Sylvester
      Equation, IEEE Transactions on Automatic Control, Vol. 34, No. 7,
      July 1989, pp 745-751.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 298 of file stgsyl.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
