---
title: "zporfs-f(3)"
name: "zporfs-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zporfs-f/"
description: "zporfs.f –"
---

<p>zporfs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zporfs</code> (UPLO, N, NRHS, A, LDA, AF, LDAF, B, LDB, X, LDX, FERR, BERR, WORK, RWORK, INFO)<br />
 <i></i><code>ZPORFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zporfs (characterUPLO, integerN, integerNRHS, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldaf, * )AF, integerLDAF, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldx, * )X, integerLDX, double precision, dimension( * )FERR, double precision, dimension( * )BERR, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZPORFS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPORFS improves the computed solution to a system of linear
 equations when the coefficient matrix is Hermitian positive definite,
 and provides error bounds and backward error estimates for the
 solution.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices B and X. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The Hermitian matrix A. If UPLO = 'U', the leading N-by-N
 upper triangular part of A contains the upper triangular part
 of the matrix A, and the strictly lower triangular part of A
 is not referenced. If UPLO = 'L', the leading N-by-N lower
 triangular part of A contains the lower triangular part of
 the matrix A, and the strictly upper triangular part of A is
 not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX*16 array, dimension (LDAF,N)
 The triangular factor U or L from the Cholesky factorization
 A = U**H*U or A = L*L**H, as computed by ZPOTRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 The right hand side matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (LDX,NRHS)
 On entry, the solution matrix X, as computed by ZPOTRS.
 On exit, the improved solution matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,N).</pre>
<p><i>FERR</i> </p>
<pre> FERR is DOUBLE PRECISION array, dimension (NRHS)
 The estimated forward error bound for each solution vector
 X(j) (the j-th column of the solution matrix X).
 If XTRUE is the true solution corresponding to X(j), FERR(j)
 is an estimated upper bound for the magnitude of the largest
 element in (X(j) - XTRUE) divided by the magnitude of the
 largest element in X(j). The estimate is as reliable as
 the estimate for RCOND, and is almost always a slight
 overestimate of the true error.</pre>
<p><i>BERR</i> </p>
<pre> BERR is DOUBLE PRECISION array, dimension (NRHS)
 The componentwise relative backward error of each solution
 vector X(j) (i.e., the smallest relative change in
 any element of A or B that makes X(j) an exact solution).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dd>
<pre> ITMAX is the maximum number of steps of iterative refinement.</pre>
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
<p> Definition at line 183 of file zporfs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
