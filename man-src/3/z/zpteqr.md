---
title: "zpteqr(3)"
name: "zpteqr"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zpteqr/"
description: "zpteqr.f –"
---

<p>zpteqr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zpteqr</code> (COMPZ, N, D, E, Z, LDZ, WORK, INFO)<br />
 <i></i><code>ZPTEQR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zpteqr (characterCOMPZ, integerN, double precision, dimension( * )D, double precision, dimension( * )E, complex*16, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>ZPTEQR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPTEQR computes all eigenvalues and, optionally, eigenvectors of a
 symmetric positive definite tridiagonal matrix by first factoring the
 matrix using DPTTRF and then calling ZBDSQR to compute the singular
 values of the bidiagonal factor.
 This routine computes the eigenvalues of the positive definite
 tridiagonal matrix to high relative accuracy. This means that if the
 eigenvalues range over many orders of magnitude in size, then the
 small eigenvalues and corresponding eigenvectors will be computed
 more accurately than, for example, with the standard QR method.
 The eigenvectors of a full or band positive definite Hermitian matrix
 can also be found if ZHETRD, ZHPTRD, or ZHBTRD has been used to
 reduce this matrix to tridiagonal form. (The reduction to
 tridiagonal form, however, may preclude the possibility of obtaining
 high relative accuracy in the small eigenvalues of the original
 matrix, if these eigenvalues range over many orders of magnitude.)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>COMPZ</i> </p>
<pre> COMPZ is CHARACTER*1
 = 'N': Compute eigenvalues only.
 = 'V': Compute eigenvectors of original Hermitian
 matrix also. Array Z contains the unitary matrix
 used to reduce the original matrix to tridiagonal
 form.
 = 'I': Compute eigenvectors of tridiagonal matrix also.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the n diagonal elements of the tridiagonal matrix.
 On normal exit, D contains the eigenvalues, in descending
 order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 On entry, the (n-1) subdiagonal elements of the tridiagonal
 matrix.
 On exit, E has been destroyed.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, N)
 On entry, if COMPZ = 'V', the unitary matrix used in the
 reduction to tridiagonal form.
 On exit, if COMPZ = 'V', the orthonormal eigenvectors of the
 original Hermitian matrix;
 if COMPZ = 'I', the orthonormal eigenvectors of the
 tridiagonal matrix.
 If INFO &gt; 0 on exit, Z contains the eigenvectors associated
 with only the stored eigenvalues.
 If COMPZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 COMPZ = 'V' or 'I', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (4*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = i, and i is:
 &lt;= N the Cholesky factorization of the matrix could
 not be performed because the i-th principal minor
 was not positive definite.
 &gt; N the SVD algorithm failed to converge;
 if INFO = N+i, i off-diagonal elements of the
 bidiagonal factor did not converge to zero.</pre>
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
<p> Definition at line 146 of file zpteqr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
