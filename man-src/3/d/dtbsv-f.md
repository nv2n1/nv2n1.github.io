---
title: "dtbsv-f(3)"
name: "dtbsv-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtbsv-f/"
description: "dtbsv.f –"
---

<p>dtbsv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dtbsv</code> (UPLO, TRANS, DIAG, N, K, A, LDA, X, INCX)<br />
 <i></i><code>DTBSV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtbsv (characterUPLO, characterTRANS, characterDIAG, integerN, integerK, double precision, dimension(lda,*)A, integerLDA, double precision, dimension(*)X, integerINCX)</h3>
<p><code>DTBSV</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DTBSV solves one of the systems of equations
 A*x = b, or A**T*x = b,
 where b and x are n element vectors and A is an n by n unit, or
 non-unit, upper or lower triangular band matrix, with ( k + 1 )
 diagonals.
 No test for singularity or near-singularity is included in this
 routine. Such tests must be performed before calling this routine.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<p><i>K</i> </p>
<pre> K is INTEGER
 On entry with UPLO = 'U' or 'u', K specifies the number of
 super-diagonals of the matrix A.
 On entry with UPLO = 'L' or 'l', K specifies the number of
 sub-diagonals of the matrix A.
 K must satisfy 0 .le. K.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array of DIMENSION ( LDA, n ).
 Before entry with UPLO = 'U' or 'u', the leading ( k + 1 )
 by n part of the array A must contain the upper triangular
 band part of the matrix of coefficients, supplied column by
 column, with the leading diagonal of the matrix in row
 ( k + 1 ) of the array, the first super-diagonal starting at
 position 2 in row k, and so on. The top left k by k triangle
 of the array A is not referenced.
 The following program segment will transfer an upper
 triangular band matrix from conventional full matrix storage
 to band storage:
 DO 20, J = 1, N
 M = K + 1 - J
 DO 10, I = MAX( 1, J - K ), J
 A( M + I, J ) = matrix( I, J )
 10 CONTINUE
 20 CONTINUE
 Before entry with UPLO = 'L' or 'l', the leading ( k + 1 )
 by n part of the array A must contain the lower triangular
 band part of the matrix of coefficients, supplied column by
 column, with the leading diagonal of the matrix in row 1 of
 the array, the first sub-diagonal starting at position 1 in
 row 2, and so on. The bottom right k by k triangle of the
 array A is not referenced.
 The following program segment will transfer a lower
 triangular band matrix from conventional full matrix storage
 to band storage:
 DO 20, J = 1, N
 M = 1 - J
 DO 10, I = J, MIN( N, J + K )
 A( M + I, J ) = matrix( I, J )
 10 CONTINUE
 20 CONTINUE
 Note that when DIAG = 'U' or 'u' the elements of the array A
 corresponding to the diagonal elements of the matrix are not
 referenced, but are assumed to be unity.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. LDA must be at least
 ( k + 1 ).</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array of dimension at least
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
<pre> Level 2 Blas routine.
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 190 of file dtbsv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
