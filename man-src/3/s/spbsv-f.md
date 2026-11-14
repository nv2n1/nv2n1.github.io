---
title: "spbsv-f(3)"
name: "spbsv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spbsv-f/"
description: "spbsv.f –"
---

<p>spbsv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine spbsv (UPLO, N, KD, NRHS, AB, LDAB, B, LDB, INFO)


SPBSV computes the solution to system of linear equations A * X = B for OTHER matrices</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spbsv (characterUPLO, integerN, integerKD, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code> SPBSV computes the solution to system of linear equations A * X = B for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPBSV computes the solution to a real system of linear equations
 A * X = B,
 where A is an N-by-N symmetric positive definite band matrix and X
 and B are N-by-NRHS matrices.
 The Cholesky decomposition is used to factor A as
 A = U**T * U, if UPLO = 'U', or
 A = L * L**T, if UPLO = 'L',
 where U is an upper triangular band matrix, and L is a lower
 triangular band matrix, with the same number of superdiagonals or
 subdiagonals as A. The factored form of A is then used to solve the
 system of equations A * X = B.</pre>
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
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of superdiagonals of the matrix A if UPLO = 'U',
 or the number of subdiagonals if UPLO = 'L'. KD &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is REAL array, dimension (LDAB,N)
 On entry, the upper or lower triangle of the symmetric band
 matrix A, stored in the first KD+1 rows of the array. The
 j-th column of A is stored in the j-th column of the array AB
 as follows:
 if UPLO = 'U', AB(KD+1+i-j,j) = A(i,j) for max(1,j-KD)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(N,j+KD).
 See below for further details.
 On exit, if INFO = 0, the triangular factor U or L from the
 Cholesky factorization A = U**T*U or A = L*L**T of the band
 matrix A, in the same storage format as A.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KD+1.</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,NRHS)
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
<pre> The band storage scheme is illustrated by the following example, when
 N = 6, KD = 2, and UPLO = 'U':
 On entry: On exit:
 * * a13 a24 a35 a46 * * u13 u24 u35 u46
 * a12 a23 a34 a45 a56 * u12 u23 u34 u45 u56
 a11 a22 a33 a44 a55 a66 u11 u22 u33 u44 u55 u66
 Similarly, if UPLO = 'L' the format of A is as follows:
 On entry: On exit:
 a11 a22 a33 a44 a55 a66 l11 l22 l33 l44 l55 l66
 a21 a32 a43 a54 a65 * l21 l32 l43 l54 l65 *
 a31 a42 a53 a64 * * l31 l42 l53 l64 * *
 Array elements marked * are not used by the routine.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 165 of file spbsv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
