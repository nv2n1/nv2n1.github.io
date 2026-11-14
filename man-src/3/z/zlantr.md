---
title: "zlantr(3)"
name: "zlantr"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlantr/"
description: "zlantr.f –"
---

<p>zlantr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zlantr</code> (NORM, UPLO, DIAG, M, N, A, LDA, WORK)<br />
 <i></i><code>ZLANTR</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a trapezoidal or triangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zlantr (characterNORM, characterUPLO, characterDIAG, integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, double precision, dimension( * )WORK)</h3>
<p><code>ZLANTR</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a trapezoidal or triangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLANTR returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 trapezoidal or triangular matrix A.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>ZLANTR </p>
<pre> ZLANTR = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
 Specifies the value to be returned in ZLANTR as described
 above.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the matrix A is upper or lower trapezoidal.
 = 'U': Upper trapezoidal
 = 'L': Lower trapezoidal
 Note that A is triangular instead of trapezoidal if M = N.</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 Specifies whether or not the matrix A has unit diagonal.
 = 'N': Non-unit diagonal
 = 'U': Unit diagonal</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0, and if
 UPLO = 'U', M &lt;= N. When M = 0, ZLANTR is set to zero.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0, and if
 UPLO = 'L', N &lt;= M. When N = 0, ZLANTR is set to zero.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The trapezoidal matrix A (A is triangular if M = N).
 If UPLO = 'U', the leading m by n upper trapezoidal part of
 the array A contains the upper trapezoidal matrix, and the
 strictly lower triangular part of A is not referenced.
 If UPLO = 'L', the leading m by n lower trapezoidal part of
 the array A contains the lower trapezoidal matrix, and the
 strictly upper triangular part of A is not referenced. Note
 that when DIAG = 'U', the diagonal elements of A are not
 referenced and are assumed to be one.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(M,1).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)),
 where LWORK &gt;= M when NORM = 'I'; otherwise, WORK is not
 referenced.</pre>
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
<p> Definition at line 142 of file zlantr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
