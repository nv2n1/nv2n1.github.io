---
title: "zlanhe-f(3)"
name: "zlanhe-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlanhe-f/"
description: "zlanhe.f –"
---

<p>zlanhe.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zlanhe</code> (NORM, UPLO, N, A, LDA, WORK)<br />
 <i></i><code>ZLANHE</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a complex Hermitian matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zlanhe (characterNORM, characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, double precision, dimension( * )WORK)</h3>
<p><code>ZLANHE</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a complex Hermitian matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLANHE returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 complex hermitian matrix A.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>ZLANHE </p>
<pre> ZLANHE = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
<dl>
<dd><i>NORM</i> </p>
<pre> NORM is CHARACTER*1
 Specifies the value to be returned in ZLANHE as described
 above.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 hermitian matrix A is to be referenced.
 = 'U': Upper triangular part of A is referenced
 = 'L': Lower triangular part of A is referenced</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0. When N = 0, ZLANHE is
 set to zero.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The hermitian matrix A. If UPLO = 'U', the leading n by n
 upper triangular part of A contains the upper triangular part
 of the matrix A, and the strictly lower triangular part of A
 is not referenced. If UPLO = 'L', the leading n by n lower
 triangular part of A contains the lower triangular part of
 the matrix A, and the strictly upper triangular part of A is
 not referenced. Note that the imaginary parts of the diagonal
 elements need not be set and are assumed to be zero.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(N,1).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)),
 where LWORK &gt;= N when NORM = 'I' or '1' or 'O'; otherwise,
 WORK is not referenced.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 125 of file zlanhe.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
