---
title: "clansy-f(3)"
name: "clansy-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clansy-f/"
description: "clansy.f –"
---

<p>clansy.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>clansy</code> (NORM, UPLO, N, A, LDA, WORK)<br />
 <i></i><code>CLANSY</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a complex symmetric matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function clansy (characterNORM, characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, real, dimension( * )WORK)</h3>
<p><code>CLANSY</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a complex symmetric matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLANSY returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 complex symmetric matrix A.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>CLANSY </p>
<pre> CLANSY = ( max(abs(A(i,j))), NORM = 'M' or 'm'
 (
 ( norm1(A), NORM = '1', 'O' or 'o'
 (
 ( normI(A), NORM = 'I' or 'i'
 (
 ( normF(A), NORM = 'F', 'f', 'E' or 'e'
 where norm1 denotes the one norm of a matrix (maximum column sum),
 normI denotes the infinity norm of a matrix (maximum row sum) and
 normF denotes the Frobenius norm of a matrix (square root of sum of
 squares). Note that max(abs(A(i,j))) is not a consistent matrix norm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>NORM</i> </p>
<pre> NORM is CHARACTER*1
 Specifies the value to be returned in CLANSY as described
 above.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 symmetric matrix A is to be referenced.
 = 'U': Upper triangular part of A is referenced
 = 'L': Lower triangular part of A is referenced</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0. When N = 0, CLANSY is
 set to zero.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 The symmetric matrix A. If UPLO = 'U', the leading n by n
 upper triangular part of A contains the upper triangular part
 of the matrix A, and the strictly lower triangular part of A
 is not referenced. If UPLO = 'L', the leading n by n lower
 triangular part of A contains the lower triangular part of
 the matrix A, and the strictly upper triangular part of A is
 not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(N,1).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK)),
 where LWORK &gt;= N when NORM = 'I' or '1' or 'O'; otherwise,
 WORK is not referenced.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 124 of file clansy.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
