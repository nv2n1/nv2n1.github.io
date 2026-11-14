---
title: "strmv(3)"
name: "strmv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strmv/"
description: "strmv.f –"
---

<p>strmv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>strmv</code> (UPLO, TRANS, DIAG, N, A, LDA, X, INCX)<br />
 <i></i><code>STRMV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine strmv (characterUPLO, characterTRANS, characterDIAG, integerN, real, dimension(lda,*)A, integerLDA, real, dimension(*)X, integerINCX)</h3>
<p><code>STRMV</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STRMV performs one of the matrix-vector operations
 x := A*x, or x := A**T*x,
 where x is an n element vector and A is an n by n unit, or non-unit,
 upper or lower triangular matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the matrix is an upper or
 lower triangular matrix as follows:
 UPLO = 'U' or 'u' A is an upper triangular matrix.
 UPLO = 'L' or 'l' A is a lower triangular matrix.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 On entry, TRANS specifies the operation to be performed as
 follows:
 TRANS = 'N' or 'n' x := A*x.
 TRANS = 'T' or 't' x := A**T*x.
 TRANS = 'C' or 'c' x := A**T*x.</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 On entry, DIAG specifies whether or not A is unit
 triangular as follows:
 DIAG = 'U' or 'u' A is assumed to be unit triangular.
 DIAG = 'N' or 'n' A is not assumed to be unit
 triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix A.
 N must be at least zero.</pre>
<p><i>A</i> </p>
<pre> A is REAL array of DIMENSION ( LDA, n ).
 Before entry with UPLO = 'U' or 'u', the leading n by n
 upper triangular part of the array A must contain the upper
 triangular matrix and the strictly lower triangular part of
 A is not referenced.
 Before entry with UPLO = 'L' or 'l', the leading n by n
 lower triangular part of the array A must contain the lower
 triangular matrix and the strictly upper triangular part of
 A is not referenced.
 Note that when DIAG = 'U' or 'u', the diagonal elements of
 A are not referenced either, but are assumed to be unity.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. LDA must be at least
 max( 1, n ).</pre>
<p><i>X</i> </p>
<pre> X is REAL array of dimension at least
 ( 1 + ( n - 1 )*abs( INCX ) ).
 Before entry, the incremented array X must contain the n
 element vector x. On exit, X is overwritten with the
 tranformed vector x.</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 On entry, INCX specifies the increment for the elements of
 X. INCX must not be zero.</pre>
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
<pre> Level 2 Blas routine.
 The vector and matrix arguments are not referenced when N = 0, or M = 0
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 148 of file strmv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
