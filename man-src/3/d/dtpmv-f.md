---
title: "dtpmv-f(3)"
name: "dtpmv-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtpmv-f/"
description: "dtpmv.f –"
---

<p>dtpmv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dtpmv</code> (UPLO, TRANS, DIAG, N, AP, X, INCX)<br />
 <i></i><code>DTPMV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtpmv (characterUPLO, characterTRANS, characterDIAG, integerN, double precision, dimension(*)AP, double precision, dimension(*)X, integerINCX)</h3>
<p><code>DTPMV</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DTPMV performs one of the matrix-vector operations
 x := A*x, or x := A**T*x,
 where x is an n element vector and A is an n by n unit, or non-unit,
 upper or lower triangular matrix, supplied in packed form.</pre>
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
<p><i>AP</i> </p>
<pre> AP is DOUBLE PRECISION array of DIMENSION at least
 ( ( n*( n + 1 ) )/2 ).
 Before entry with UPLO = 'U' or 'u', the array AP must
 contain the upper triangular matrix packed sequentially,
 column by column, so that AP( 1 ) contains a( 1, 1 ),
 AP( 2 ) and AP( 3 ) contain a( 1, 2 ) and a( 2, 2 )
 respectively, and so on.
 Before entry with UPLO = 'L' or 'l', the array AP must
 contain the lower triangular matrix packed sequentially,
 column by column, so that AP( 1 ) contains a( 1, 1 ),
 AP( 2 ) and AP( 3 ) contain a( 2, 1 ) and a( 3, 1 )
 respectively, and so on.
 Note that when DIAG = 'U' or 'u', the diagonal elements of
 A are not referenced, but are assumed to be unity.</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array of dimension at least
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
 The vector and matrix arguments are not referenced when N = 0, or M = 0
 -- Written on 22-October-1986.
 Jack Dongarra, Argonne National Lab.
 Jeremy Du Croz, Nag Central Office.
 Sven Hammarling, Nag Central Office.
 Richard Hanson, Sandia National Labs.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 143 of file dtpmv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
