---
title: "zppsv-f(3)"
name: "zppsv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zppsv-f/"
description: "zppsv.f –"
---

<p>zppsv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine zppsv (UPLO, N, NRHS, AP, B, LDB, INFO)


ZPPSV computes the solution to system of linear equations A * X = B for OTHER matrices</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zppsv (characterUPLO, integerN, integerNRHS, complex*16, dimension( * )AP, complex*16, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code> ZPPSV computes the solution to system of linear equations A * X = B for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPPSV computes the solution to a complex system of linear equations
 A * X = B,
 where A is an N-by-N Hermitian positive definite matrix stored in
 packed format and X and B are N-by-NRHS matrices.
 The Cholesky decomposition is used to factor A as
 A = U**H * U, if UPLO = 'U', or
 A = L * L**H, if UPLO = 'L',
 where U is an upper triangular matrix and L is a lower triangular
 matrix. The factored form of A is then used to solve the system of
 equations A * X = B.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 A, packed columnwise in a linear array. The j-th column of A
 is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 See below for further details.
 On exit, if INFO = 0, the factor U or L from the Cholesky
 factorization A = U**H*U or A = L*L**H, in the same storage
 format as A.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 On entry, the N-by-NRHS right hand side matrix B.
 On exit, if INFO = 0, the N-by-NRHS solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the leading minor of order i of A is not
 positive definite, so the factorization could not be
 completed, and the solution has not been computed.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The packed storage scheme is illustrated by the following example
 when N = 4, UPLO = 'U':
 Two-dimensional storage of the Hermitian matrix A:
 a11 a12 a13 a14
 a22 a23 a24
 a33 a34 (aij = conjg(aji))
 a44
 Packed storage of the upper triangle of A:
 AP = [ a11, a12, a22, a13, a23, a33, a14, a24, a34, a44 ]</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 145 of file zppsv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
