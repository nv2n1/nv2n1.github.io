---
title: "ztrsm(3)"
name: "ztrsm"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztrsm/"
description: "ztrsm.f –"
---

<p>ztrsm.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztrsm</code> (SIDE, UPLO, TRANSA, DIAG, M, N, ALPHA, A, LDA, B, LDB)<br />
 <i></i><code>ZTRSM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztrsm (characterSIDE, characterUPLO, characterTRANSA, characterDIAG, integerM, integerN, complex*16ALPHA, complex*16, dimension(lda,*)A, integerLDA, complex*16, dimension(ldb,*)B, integerLDB)</h3>
<p><code>ZTRSM</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTRSM solves one of the matrix equations
 op( A )*X = alpha*B, or X*op( A ) = alpha*B,
 where alpha is a scalar, X and B are m by n matrices, A is a unit, or
 non-unit, upper or lower triangular matrix and op( A ) is one of
 op( A ) = A or op( A ) = A**T or op( A ) = A**H.
 The matrix X is overwritten on B.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 On entry, SIDE specifies whether op( A ) appears on the left
 or right of X as follows:
 SIDE = 'L' or 'l' op( A )*X = alpha*B.
 SIDE = 'R' or 'r' X*op( A ) = alpha*B.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the matrix A is an upper or
 lower triangular matrix as follows:
 UPLO = 'U' or 'u' A is an upper triangular matrix.
 UPLO = 'L' or 'l' A is a lower triangular matrix.</pre>
<p><i>TRANSA</i> </p>
<pre> TRANSA is CHARACTER*1
 On entry, TRANSA specifies the form of op( A ) to be used in
 the matrix multiplication as follows:
 TRANSA = 'N' or 'n' op( A ) = A.
 TRANSA = 'T' or 't' op( A ) = A**T.
 TRANSA = 'C' or 'c' op( A ) = A**H.</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 On entry, DIAG specifies whether or not A is unit triangular
 as follows:
 DIAG = 'U' or 'u' A is assumed to be unit triangular.
 DIAG = 'N' or 'n' A is not assumed to be unit
 triangular.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 On entry, M specifies the number of rows of B. M must be at
 least zero.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the number of columns of B. N must be
 at least zero.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16
 On entry, ALPHA specifies the scalar alpha. When alpha is
 zero then A is not referenced and B need not be set before
 entry.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array of DIMENSION ( LDA, k ),
 where k is m when SIDE = 'L' or 'l' 
 and k is n when SIDE = 'R' or 'r'.
 Before entry with UPLO = 'U' or 'u', the leading k by k
 upper triangular part of the array A must contain the upper
 triangular matrix and the strictly lower triangular part of
 A is not referenced.
 Before entry with UPLO = 'L' or 'l', the leading k by k
 lower triangular part of the array A must contain the lower
 triangular matrix and the strictly upper triangular part of
 A is not referenced.
 Note that when DIAG = 'U' or 'u', the diagonal elements of
 A are not referenced either, but are assumed to be unity.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. When SIDE = 'L' or 'l' then
 LDA must be at least max( 1, m ), when SIDE = 'R' or 'r'
 then LDA must be at least max( 1, n ).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array of DIMENSION ( LDB, n ).
 Before entry, the leading m by n part of the array B must
 contain the right-hand side matrix B, and on exit is
 overwritten by the solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 On entry, LDB specifies the first dimension of B as declared
 in the calling (sub) program. LDB must be at least
 max( 1, m ).</pre>
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
<pre> Level 3 Blas routine.
 -- Written on 8-February-1989.
 Jack Dongarra, Argonne National Laboratory.
 Iain Duff, AERE Harwell.
 Jeremy Du Croz, Numerical Algorithms Group Ltd.
 Sven Hammarling, Numerical Algorithms Group Ltd.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 181 of file ztrsm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
