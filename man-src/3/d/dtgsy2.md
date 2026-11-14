---
title: "dtgsy2(3)"
name: "dtgsy2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtgsy2/"
description: "dtgsy2.f –"
---

<h2 class="name">NAME</h2>
<p> dtgsy2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtgsy2</code> (TRANS, IJOB, M, N, A, LDA, B, LDB, C, LDC, D, LDD, E, LDE, F, LDF, SCALE, RDSUM, RDSCAL, IWORK, PQ, INFO)<br />
 <i></i><code>DTGSY2</code> solves the generalized Sylvester equation (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtgsy2 (characterTRANS, integerIJOB, integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( ldd, * )D, integerLDD, double precision, dimension( lde, * )E, integerLDE, double precision, dimension( ldf, * )F, integerLDF, double precisionSCALE, double precisionRDSUM, double precisionRDSCAL, integer, dimension( * )IWORK, integerPQ, integerINFO)</h3>
<p> <code>DTGSY2</code> solves the generalized Sylvester equation (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DTGSY2 solves the generalized Sylvester equation:
             A * R - L * B = scale * C                (1)
             D * R - L * E = scale * F,
 using Level 1 and 2 BLAS. where R and L are unknown M-by-N matrices,
 (A, D), (B, E) and (C, F) are given matrix pairs of size M-by-M,
 N-by-N and M-by-N, respectively, with real entries. (A, D) and (B, E)
 must be in generalized Schur canonical form, i.e. A, B are upper
 quasi triangular and D, E are upper triangular. The solution (R, L)
 overwrites (C, F). 0 &lt;= SCALE &lt;= 1 is an output scaling factor
 chosen to avoid overflow.
 In matrix notation solving equation (1) corresponds to solve
 Z*x = scale*b, where Z is defined as
        Z = [ kron(In, A)  -kron(B**T, Im) ]             (2)
            [ kron(In, D)  -kron(E**T, Im) ],
 Ik is the identity matrix of size k and X**T is the transpose of X.
 kron(X, Y) is the Kronecker product between the matrices X and Y.
 In the process of solving (1), we solve a number of such systems
 where Dim(In), Dim(In) = 1 or 2.
 If TRANS = 'T', solve the transposed system Z**T*y = scale*b for y,
 which is equivalent to solve for R and L in
             A**T * R  + D**T * L   = scale * C           (3)
             R  * B**T + L  * E**T  = scale * -F
 This case is used to compute an estimate of Dif[(A, D), (B, E)] =
 sigma_min(Z) using reverse communicaton with DLACON.
 DTGSY2 also (IJOB &gt;= 1) contributes to the computation in DTGSYL
 of an upper bound on the separation between to matrix pairs. Then
 the input (A, D), (B, E) are sub-pencils of the matrix pair in
 DTGSYL. See DTGSYL for details.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N', solve the generalized Sylvester equation (1).
          = 'T': solve the 'transposed' system (3).
</pre>
<p> <i>IJOB</i> </p>
<pre>
          IJOB is INTEGER
          Specifies what kind of functionality to be performed.
          = 0: solve (1) only.
          = 1: A contribution from this subsystem to a Frobenius
               norm-based estimate of the separation between two matrix
               pairs is computed. (look ahead strategy is used).
          = 2: A contribution from this subsystem to a Frobenius
               norm-based estimate of the separation between two matrix
               pairs is computed. (DGECON on sub-systems is used.)
          Not referenced if TRANS = 'T'.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          On entry, M specifies the order of A and D, and the row
          dimension of C, F, R and L.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          On entry, N specifies the order of B and E, and the column
          dimension of C, F, R and L.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA, M)
          On entry, A contains an upper quasi triangular matrix.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the matrix A. LDA &gt;= max(1, M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB, N)
          On entry, B contains an upper quasi triangular matrix.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the matrix B. LDB &gt;= max(1, N).
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION array, dimension (LDC, N)
          On entry, C contains the right-hand-side of the first matrix
          equation in (1).
          On exit, if IJOB = 0, C has been overwritten by the
          solution R.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the matrix C. LDC &gt;= max(1, M).
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (LDD, M)
          On entry, D contains an upper triangular matrix.
</pre>
<p> <i>LDD</i> </p>
<pre>
          LDD is INTEGER
          The leading dimension of the matrix D. LDD &gt;= max(1, M).
</pre>
<p> <i>E</i> </p>
<pre>
          E is DOUBLE PRECISION array, dimension (LDE, N)
          On entry, E contains an upper triangular matrix.
</pre>
<p> <i>LDE</i> </p>
<pre>
          LDE is INTEGER
          The leading dimension of the matrix E. LDE &gt;= max(1, N).
</pre>
<p> <i>F</i> </p>
<pre>
          F is DOUBLE PRECISION array, dimension (LDF, N)
          On entry, F contains the right-hand-side of the second matrix
          equation in (1).
          On exit, if IJOB = 0, F has been overwritten by the
          solution L.
</pre>
<p> <i>LDF</i> </p>
<pre>
          LDF is INTEGER
          The leading dimension of the matrix F. LDF &gt;= max(1, M).
</pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is DOUBLE PRECISION
          On exit, 0 &lt;= SCALE &lt;= 1. If 0 &lt; SCALE &lt; 1, the solutions
          R and L (C and F on entry) will hold the solutions to a
          slightly perturbed system but the input matrices A, B, D and
          E have not been changed. If SCALE = 0, R and L will hold the
          solutions to the homogeneous system with C = F = 0. Normally,
          SCALE = 1.
</pre>
<p> <i>RDSUM</i> </p>
<pre>
          RDSUM is DOUBLE PRECISION
          On entry, the sum of squares of computed contributions to
          the Dif-estimate under computation by DTGSYL, where the
          scaling factor RDSCAL (see below) has been factored out.
          On exit, the corresponding sum of squares updated with the
          contributions from the current sub-system.
          If TRANS = 'T' RDSUM is not touched.
          NOTE: RDSUM only makes sense when DTGSY2 is called by DTGSYL.
</pre>
<p> <i>RDSCAL</i> </p>
<pre>
          RDSCAL is DOUBLE PRECISION
          On entry, scaling factor used to prevent overflow in RDSUM.
          On exit, RDSCAL is updated w.r.t. the current contributions
          in RDSUM.
          If TRANS = 'T', RDSCAL is not touched.
          NOTE: RDSCAL only makes sense when DTGSY2 is called by
                DTGSYL.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (M+N+2)
</pre>
<p> <i>PQ</i> </p>
<pre>
          PQ is INTEGER
          On exit, the number of subsystems (of size 2-by-2, 4-by-4 and
          8-by-8) solved by this routine.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          On exit, if INFO is set to
            =0: Successful exit
            &lt;0: If INFO = -i, the i-th argument had an illegal value.
            &gt;0: The matrix pairs (A, D) and (B, E) have common or very
                close eigenvalues.
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
<dd> September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> Definition at line 273 of file dtgsy2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
