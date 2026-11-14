---
title: "zlansb-f(3)"
name: "zlansb-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlansb-f/"
description: "zlansb.f –"
---

<p>zlansb.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zlansb</code> (NORM, UPLO, N, K, AB, LDAB, WORK)<br />
 <i></i><code>ZLANSB</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a symmetric band matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zlansb (characterNORM, characterUPLO, integerN, integerK, complex*16, dimension( ldab, * )AB, integerLDAB, double precision, dimension( * )WORK)</h3>
<p><code>ZLANSB</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a symmetric band matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLANSB returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of an
 n by n symmetric band matrix A, with k super-diagonals.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>ZLANSB </p>
<pre> ZLANSB = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
 Specifies the value to be returned in ZLANSB as described
 above.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 band matrix A is supplied.
 = 'U': Upper triangular part is supplied
 = 'L': Lower triangular part is supplied</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0. When N = 0, ZLANSB is
 set to zero.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The number of super-diagonals or sub-diagonals of the
 band matrix A. K &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB,N)
 The upper or lower triangle of the symmetric band matrix A,
 stored in the first K+1 rows of AB. The j-th column of A is
 stored in the j-th column of the array AB as follows:
 if UPLO = 'U', AB(k+1+i-j,j) = A(i,j) for max(1,j-k)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+k).</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= K+1.</pre>
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
<p> Definition at line 130 of file zlansb.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
