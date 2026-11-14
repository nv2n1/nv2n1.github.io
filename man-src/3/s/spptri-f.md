---
title: "spptri-f(3)"
name: "spptri-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spptri-f/"
description: "spptri.f –"
---

<p>spptri.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>spptri</code> (UPLO, N, AP, INFO)<br />
 <i></i><code>SPPTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spptri (characterUPLO, integerN, real, dimension( * )AP, integerINFO)</h3>
<p><code>SPPTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPPTRI computes the inverse of a real symmetric positive definite
 matrix A using the Cholesky factorization A = U**T*U or A = L*L**T
 computed by SPPTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangular factor is stored in AP;
 = 'L': Lower triangular factor is stored in AP.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is REAL array, dimension (N*(N+1)/2)
 On entry, the triangular factor U or L from the Cholesky
 factorization A = U**T*U or A = L*L**T, packed columnwise as
 a linear array. The j-th column of U or L is stored in the
 array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j&lt;=i&lt;=n.
 On exit, the upper or lower triangle of the (symmetric)
 inverse of A, overwriting the input factor U or L.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the (i,i) element of the factor U or L is
 zero, and the inverse could not be computed.</pre>
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
<p> Definition at line 94 of file spptri.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
