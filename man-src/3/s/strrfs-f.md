---
title: "strrfs-f(3)"
name: "strrfs-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strrfs-f/"
description: "strrfs.f –"
---

<p>strrfs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>strrfs</code> (UPLO, TRANS, DIAG, N, NRHS, A, LDA, B, LDB, X, LDX, FERR, BERR, WORK, IWORK, INFO)<br />
 <i></i><code>STRRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine strrfs (characterUPLO, characterTRANS, characterDIAG, integerN, integerNRHS, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( ldx, * )X, integerLDX, real, dimension( * )FERR, real, dimension( * )BERR, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>STRRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STRRFS provides error bounds and backward error estimates for the
 solution to a system of linear equations with a triangular
 coefficient matrix.
 The solution matrix X must be computed by STRTRS or some other
 means before entering this routine. STRRFS does not do iterative
 refinement because doing so cannot improve the backward error.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations:
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose = Transpose)</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 = 'N': A is non-unit triangular;
 = 'U': A is unit triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices B and X. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 The triangular matrix A. If UPLO = 'U', the leading N-by-N
 upper triangular part of the array A contains the upper
 triangular matrix, and the strictly lower triangular part of
 A is not referenced. If UPLO = 'L', the leading N-by-N lower
 triangular part of the array A contains the lower triangular
 matrix, and the strictly upper triangular part of A is not
 referenced. If DIAG = 'U', the diagonal elements of A are
 also not referenced and are assumed to be 1.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,NRHS)
 The right hand side matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is REAL array, dimension (LDX,NRHS)
 The solution matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,N).</pre>
<p><i>FERR</i> </p>
<pre> FERR is REAL array, dimension (NRHS)
 The estimated forward error bound for each solution vector
 X(j) (the j-th column of the solution matrix X).
 If XTRUE is the true solution corresponding to X(j), FERR(j)
 is an estimated upper bound for the magnitude of the largest
 element in (X(j) - XTRUE) divided by the magnitude of the
 largest element in X(j). The estimate is as reliable as
 the estimate for RCOND, and is almost always a slight
 overestimate of the true error.</pre>
<p><i>BERR</i> </p>
<pre> BERR is REAL array, dimension (NRHS)
 The componentwise relative backward error of each solution
 vector X(j) (i.e., the smallest relative change in
 any element of A or B that makes X(j) an exact solution).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (3*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 182 of file strrfs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
