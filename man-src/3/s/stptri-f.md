---
title: "stptri-f(3)"
name: "stptri-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stptri-f/"
description: "stptri.f –"
---

<p>stptri.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>stptri</code> (UPLO, DIAG, N, AP, INFO)<br />
 <i></i><code>STPTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stptri (characterUPLO, characterDIAG, integerN, real, dimension( * )AP, integerINFO)</h3>
<p><code>STPTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STPTRI computes the inverse of a real upper or lower triangular
 matrix A stored in packed format.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 = 'N': A is non-unit triangular;
 = 'U': A is unit triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is REAL array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangular matrix A, stored
 columnwise in a linear array. The j-th column of A is stored
 in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*((2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 See below for further details.
 On exit, the (triangular) inverse of the original matrix, in
 the same packed storage format.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, A(i,i) is exactly zero. The triangular
 matrix is singular and its inverse can not be computed.</pre>
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
<pre> A triangular matrix A can be transferred to packed storage using one
 of the following program segments:
 UPLO = 'U': UPLO = 'L':
 JC = 1 JC = 1
 DO 2 J = 1, N DO 2 J = 1, N
 DO 1 I = 1, J DO 1 I = J, N
 AP(JC+I-1) = A(I,J) AP(JC+I-J) = A(I,J)
 1 CONTINUE 1 CONTINUE
 JC = JC + J JC = JC + N - J + 1
 2 CONTINUE 2 CONTINUE</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 118 of file stptri.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
