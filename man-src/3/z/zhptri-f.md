---
title: "zhptri-f(3)"
name: "zhptri-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhptri-f/"
description: "zhptri.f –"
---

<p>zhptri.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhptri</code> (UPLO, N, AP, IPIV, WORK, INFO)<br />
 <i></i><code>ZHPTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhptri (characterUPLO, integerN, complex*16, dimension( * )AP, integer, dimension( * )IPIV, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZHPTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPTRI computes the inverse of a complex Hermitian indefinite matrix
 A in packed storage using the factorization A = U*D*U**H or
 A = L*D*L**H computed by ZHPTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**H;
 = 'L': Lower triangular, form is A = L*D*L**H.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the block diagonal matrix D and the multipliers
 used to obtain the factor U or L as computed by ZHPTRF,
 stored as a packed triangular matrix.
 On exit, if INFO = 0, the (Hermitian) inverse of the original
 matrix, stored as a packed triangular matrix. The j-th column
 of inv(A) is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = inv(A)(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L',
 AP(i + (j-1)*(2n-j)/2) = inv(A)(i,j) for j&lt;=i&lt;=n.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by ZHPTRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, D(i,i) = 0; the matrix is singular and its
 inverse could not be computed.</pre>
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
<p> Definition at line 110 of file zhptri.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
