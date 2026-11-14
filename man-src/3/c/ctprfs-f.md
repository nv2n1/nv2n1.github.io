---
title: "ctprfs-f(3)"
name: "ctprfs-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctprfs-f/"
description: "ctprfs.f –"
---

<p>ctprfs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ctprfs</code> (UPLO, TRANS, DIAG, N, NRHS, AP, B, LDB, X, LDX, FERR, BERR, WORK, RWORK, INFO)<br />
 <i></i><code>CTPRFS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctprfs (characterUPLO, characterTRANS, characterDIAG, integerN, integerNRHS, complex, dimension( * )AP, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldx, * )X, integerLDX, real, dimension( * )FERR, real, dimension( * )BERR, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code>CTPRFS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CTPRFS provides error bounds and backward error estimates for the
 solution to a system of linear equations with a triangular packed
 coefficient matrix.
 The solution matrix X must be computed by CTPTRS or some other
 means before entering this routine. CTPRFS does not do iterative
 refinement because doing so cannot improve the backward error.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations:
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose)</pre>
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
<p><i>AP</i> </p>
<pre> AP is COMPLEX array, dimension (N*(N+1)/2)
 The upper or lower triangular matrix A, packed columnwise in
 a linear array. The j-th column of A is stored in the array
 AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 If DIAG = 'U', the diagonal elements of A are not referenced
 and are assumed to be 1.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,NRHS)
 The right hand side matrix B. </pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension (LDX,NRHS)
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
<pre> WORK is COMPLEX array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 174 of file ctprfs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
