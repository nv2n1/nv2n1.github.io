---
title: "zlantp(3)"
name: "zlantp"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlantp/"
description: "zlantp.f –"
---

<p>zlantp.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zlantp</code> (NORM, UPLO, DIAG, N, AP, WORK)<br />
 <i></i><code>ZLANTP</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a triangular matrix supplied in packed form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zlantp (characterNORM, characterUPLO, characterDIAG, integerN, complex*16, dimension( * )AP, double precision, dimension( * )WORK)</h3>
<p><code>ZLANTP</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a triangular matrix supplied in packed form. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLANTP returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 triangular matrix A, supplied in packed form.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>ZLANTP </p>
<pre> ZLANTP = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
 Specifies the value to be returned in ZLANTP as described
 above.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the matrix A is upper or lower triangular.
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 Specifies whether or not the matrix A is unit triangular.
 = 'N': Non-unit triangular
 = 'U': Unit triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0. When N = 0, ZLANTP is
 set to zero.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 The upper or lower triangular matrix A, packed columnwise in
 a linear array. The j-th column of A is stored in the array
 AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 Note that when DIAG = 'U', the elements of the array AP
 corresponding to the diagonal elements of the matrix A are
 not referenced, but are assumed to be one.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)),
 where LWORK &gt;= N when NORM = 'I'; otherwise, WORK is not
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
<p> Definition at line 126 of file zlantp.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
