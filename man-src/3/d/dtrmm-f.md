---
title: "dtrmm-f(3)"
name: "dtrmm-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtrmm-f/"
description: "dtrmm.f –"
---

<p>dtrmm.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dtrmm</code> (SIDE, UPLO, TRANSA, DIAG, M, N, ALPHA, A, LDA, B, LDB)<br />
 <i></i><code>DTRMM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtrmm (characterSIDE, characterUPLO, characterTRANSA, characterDIAG, integerM, integerN, double precisionALPHA, double precision, dimension(lda,*)A, integerLDA, double precision, dimension(ldb,*)B, integerLDB)</h3>
<p><code>DTRMM</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DTRMM performs one of the matrix-matrix operations
 B := alpha*op( A )*B, or B := alpha*B*op( A ),
 where alpha is a scalar, B is an m by n matrix, A is a unit, or
 non-unit, upper or lower triangular matrix and op( A ) is one of
 op( A ) = A or op( A ) = A**T.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 On entry, SIDE specifies whether op( A ) multiplies B from
 the left or right as follows:
 SIDE = 'L' or 'l' B := alpha*op( A )*B.
 SIDE = 'R' or 'r' B := alpha*B*op( A ).</pre>
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
 TRANSA = 'C' or 'c' op( A ) = A**T.</pre>
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
<pre> ALPHA is DOUBLE PRECISION.
 On entry, ALPHA specifies the scalar alpha. When alpha is
 zero then A is not referenced and B need not be set before
 entry.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array of DIMENSION ( LDA, k ), where k is m
 when SIDE = 'L' or 'l' and is n when SIDE = 'R' or 'r'.
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
<pre> B is DOUBLE PRECISION array of DIMENSION ( LDB, n ).
 Before entry, the leading m by n part of the array B must
 contain the matrix B, and on exit is overwritten by the
 transformed matrix.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 On entry, LDB specifies the first dimension of B as declared
 in the calling (sub) program. LDB must be at least
 max( 1, m ).</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> Level 3 Blas routine.
 -- Written on 8-February-1989.
 Jack Dongarra, Argonne National Laboratory.
 Iain Duff, AERE Harwell.
 Jeremy Du Croz, Numerical Algorithms Group Ltd.
 Sven Hammarling, Numerical Algorithms Group Ltd.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 178 of file dtrmm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
