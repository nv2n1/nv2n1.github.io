---
title: "ssyrfs(3)"
name: "ssyrfs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssyrfs/"
description: "ssyrfs.f –"
---

<h2 class="name">NAME</h2>
<p> ssyrfs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssyrfs</code> (UPLO, N, NRHS, A, LDA, AF, LDAF, IPIV, B, LDB, X, LDX, FERR, BERR, WORK, IWORK, INFO)<br />
 <i></i><code>SSYRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssyrfs (characterUPLO, integerN, integerNRHS, real, dimension( lda, * )A, integerLDA, real, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, real, dimension( ldb, * )B, integerLDB, real, dimension( ldx, * )X, integerLDX, real, dimension( * )FERR, real, dimension( * )BERR, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SSYRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSYRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is symmetric indefinite, and
 provides error bounds and backward error estimates for the solution.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          The symmetric matrix A.  If UPLO = 'U', the leading N-by-N
          upper triangular part of A contains the upper triangular part
          of the matrix A, and the strictly lower triangular part of A
          is not referenced.  If UPLO = 'L', the leading N-by-N lower
          triangular part of A contains the lower triangular part of
          the matrix A, and the strictly upper triangular part of A is
          not referenced.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AF</i> </p>
<pre>
          AF is REAL array, dimension (LDAF,N)
          The factored form of the matrix A.  AF contains the block
          diagonal matrix D and the multipliers used to obtain the
          factor U or L from the factorization A = U*D*U**T or
          A = L*D*L**T as computed by SSYTRF.
</pre>
<p> <i>LDAF</i> </p>
<pre>
          LDAF is INTEGER
          The leading dimension of the array AF.  LDAF &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D
          as determined by SSYTRF.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
          The right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension (LDX,NRHS)
          On entry, the solution matrix X, as computed by SSYTRS.
          On exit, the improved solution matrix X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>FERR</i> </p>
<pre>
          FERR is REAL array, dimension (NRHS)
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
          BERR is REAL array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (3*N)
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
<p> Definition at line 191 of file ssyrfs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
