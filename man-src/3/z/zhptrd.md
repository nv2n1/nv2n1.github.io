---
title: "zhptrd(3)"
name: "zhptrd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhptrd/"
description: "zhptrd.f –"
---

<p>zhptrd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhptrd</code> (UPLO, N, AP, D, E, TAU, INFO)<br />
 <i></i><code>ZHPTRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhptrd (characterUPLO, integerN, complex*16, dimension( * )AP, double precision, dimension( * )D, double precision, dimension( * )E, complex*16, dimension( * )TAU, integerINFO)</h3>
<p><code>ZHPTRD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPTRD reduces a complex Hermitian matrix A stored in packed form to
 real symmetric tridiagonal form T by a unitary similarity
 transformation: Q**H * A * Q = T.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 A, packed columnwise in a linear array. The j-th column of A
 is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 On exit, if UPLO = 'U', the diagonal and first superdiagonal
 of A are overwritten by the corresponding elements of the
 tridiagonal matrix T, and the elements above the first
 superdiagonal, with the array TAU, represent the unitary
 matrix Q as a product of elementary reflectors; if UPLO
 = 'L', the diagonal and first subdiagonal of A are over-
 written by the corresponding elements of the tridiagonal
 matrix T, and the elements below the first subdiagonal, with
 the array TAU, represent the unitary matrix Q as a product
 of elementary reflectors. See Further Details.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The diagonal elements of the tridiagonal matrix T:
 D(i) = A(i,i).</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 The off-diagonal elements of the tridiagonal matrix T:
 E(i) = A(i,i+1) if UPLO = 'U', E(i) = A(i+1,i) if UPLO = 'L'.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (N-1)
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<pre> If UPLO = 'U', the matrix Q is represented as a product of elementary
 reflectors
 Q = H(n-1) . . . H(2) H(1).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(i+1:n) = 0 and v(i) = 1; v(1:i-1) is stored on exit in AP,
 overwriting A(1:i-1,i+1), and tau is stored in TAU(i).
 If UPLO = 'L', the matrix Q is represented as a product of elementary
 reflectors
 Q = H(1) H(2) . . . H(n-1).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(1:i) = 0 and v(i+1) = 1; v(i+2:n) is stored on exit in AP,
 overwriting A(i+2:n,i), and tau is stored in TAU(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 152 of file zhptrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
