---
title: "clansp-f(3)"
name: "clansp-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clansp-f/"
description: "clansp.f –"
---

<p>clansp.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>clansp</code> (NORM, UPLO, N, AP, WORK)<br />
 <i></i><code>CLANSP</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a symmetric matrix supplied in packed form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function clansp (characterNORM, characterUPLO, integerN, complex, dimension( * )AP, real, dimension( * )WORK)</h3>
<p><code>CLANSP</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a symmetric matrix supplied in packed form. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLANSP returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 complex symmetric matrix A, supplied in packed form.</pre>
</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>CLANSP </p>
<pre> CLANSP = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
 Specifies the value to be returned in CLANSP as described
 above.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 symmetric matrix A is supplied.
 = 'U': Upper triangular part of A is supplied
 = 'L': Lower triangular part of A is supplied</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0. When N = 0, CLANSP is
 set to zero.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX array, dimension (N*(N+1)/2)
 The upper or lower triangle of the symmetric matrix A, packed
 columnwise in a linear array. The j-th column of A is stored
 in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.</pre>
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
<p> Definition at line 116 of file clansp.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
