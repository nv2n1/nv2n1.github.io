---
title: "strsv-f(3)"
name: "strsv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strsv-f/"
description: "strsv.f –"
---

<p>strsv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>strsv</code> (UPLO, TRANS, DIAG, N, A, LDA, X, INCX)<br />
 <i></i><code>STRSV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine strsv (characterUPLO, characterTRANS, characterDIAG, integerN, real, dimension(lda,*)A, integerLDA, real, dimension(*)X, integerINCX)</h3>
<p><code>STRSV</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STRSV solves one of the systems of equations
 A*x = b, or A**T*x = b,
 where b and x are n element vectors and A is an n by n unit, or
 non-unit, upper or lower triangular matrix.
 No test for singularity or near-singularity is included in this
 routine. Such tests must be performed before calling this routine.</pre>
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
 On entry, TRANS specifies the equations to be solved as
 follows:
 TRANS = 'N' or 'n' A*x = b.
 TRANS = 'T' or 't' A**T*x = b.
 TRANS = 'C' or 'c' A**T*x = b.</pre>
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
 element right-hand side vector b. On exit, X is overwritten
 with the solution vector x.</pre>
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
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 150 of file strsv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
