---
title: "dgbrfs(3)"
name: "dgbrfs"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgbrfs/"
description: "dgbrfs.f –"
---

<h2 class="name">NAME</h2>
<p> dgbrfs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgbrfs</code> (TRANS, N, KL, KU, NRHS, AB, LDAB, AFB, LDAFB, IPIV, B, LDB, X, LDX, FERR, BERR, WORK, IWORK, INFO)<br />
 <i></i><code>DGBRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgbrfs (characterTRANS, integerN, integerKL, integerKU, integerNRHS, double precision, dimension( ldab, * )AB, integerLDAB, double precision, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldx, * )X, integerLDX, double precision, dimension( * )FERR, double precision, dimension( * )BERR, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DGBRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGBRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is banded, and provides
 error bounds and backward error estimates for the solution.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations:
          = 'N':  A * X = B     (No transpose)
          = 'T':  A**T * X = B  (Transpose)
          = 'C':  A**H * X = B  (Conjugate transpose = Transpose)
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>KL</i> </p>
<pre>
          KL is INTEGER
          The number of subdiagonals within the band of A.  KL &gt;= 0.
</pre>
<p> <i>KU</i> </p>
<pre>
          KU is INTEGER
          The number of superdiagonals within the band of A.  KU &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre>
          AB is DOUBLE PRECISION array, dimension (LDAB,N)
          The original band matrix A, stored in rows 1 to KL+KU+1.
          The j-th column of A is stored in the j-th column of the
          array AB as follows:
          AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(n,j+kl).
</pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KL+KU+1.
</pre>
<p> <i>AFB</i> </p>
<pre>
          AFB is DOUBLE PRECISION array, dimension (LDAFB,N)
          Details of the LU factorization of the band matrix A, as
          computed by DGBTRF.  U is stored as an upper triangular band
          matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
          the multipliers used during the factorization are stored in
          rows KL+KU+2 to 2*KL+KU+1.
</pre>
<p> <i>LDAFB</i> </p>
<pre>
          LDAFB is INTEGER
          The leading dimension of the array AFB.  LDAFB &gt;= 2*KL*KU+1.
</pre>
<p> <i>IPIV</i> </p>
<pre><code>
IPIV is INTEGER array, dimension(N)
                           The pivot indices from DGBTRF; for
1 &lt;= i &lt;= N, row i of the
                 matrix was interchanged with row
                 IPIV(i)
                     .
</code></pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          The right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,NRHS)
          On entry, the solution matrix X, as computed by DGBTRS.
          On exit, the improved solution matrix X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>FERR</i> </p>
<pre>
          FERR is DOUBLE PRECISION array, dimension (NRHS)
          The estimated forward error bound for each solution vector
          X(j) (the j-th column of the solution matrix X).
          If XTRUE is the true solution corresponding to X(j), FERR(j)
          is an estimated upper bound for the magnitude of the largest
          element in (X(j) - XTRUE) divided by the magnitude of the
          largest element in X(j).  The estimate is as reliable as
          the estimate for RCOND, and is almost always a slight
          overestimate of the true error.
</pre>
<p> <i>BERR</i> </p>
<pre>
          BERR is DOUBLE PRECISION array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (3*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre>
  ITMAX is the maximum number of steps of iterative refinement.
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
<p> Definition at line 204 of file dgbrfs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
