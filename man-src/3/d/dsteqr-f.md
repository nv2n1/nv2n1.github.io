---
title: "dsteqr-f(3)"
name: "dsteqr-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsteqr-f/"
description: "dsteqr.f –"
---

<p>dsteqr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dsteqr</code> (COMPZ, N, D, E, Z, LDZ, WORK, INFO)<br />
 <i></i><code>DSTEQR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsteqr (characterCOMPZ, integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DSTEQR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSTEQR computes all eigenvalues and, optionally, eigenvectors of a
 symmetric tridiagonal matrix using the implicit QL or QR method.
 The eigenvectors of a full or band symmetric matrix can also be found
 if DSYTRD or DSPTRD or DSBTRD has been used to reduce this matrix to
 tridiagonal form.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>COMPZ</i> </p>
<pre> COMPZ is CHARACTER*1
 = 'N': Compute eigenvalues only.
 = 'V': Compute eigenvalues and eigenvectors of the original
 symmetric matrix. On entry, Z must contain the
 orthogonal matrix used to reduce the original matrix
 to tridiagonal form.
 = 'I': Compute eigenvalues and eigenvectors of the
 tridiagonal matrix. Z is initialized to the identity
 matrix.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the diagonal elements of the tridiagonal matrix.
 On exit, if INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 On entry, the (n-1) subdiagonal elements of the tridiagonal
 matrix.
 On exit, E has been destroyed.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension (LDZ, N)
 On entry, if COMPZ = 'V', then Z contains the orthogonal
 matrix used in the reduction to tridiagonal form.
 On exit, if INFO = 0, then if COMPZ = 'V', Z contains the
 orthonormal eigenvectors of the original symmetric matrix,
 and if COMPZ = 'I', Z contains the orthonormal eigenvectors
 of the symmetric tridiagonal matrix.
 If COMPZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 eigenvectors are desired, then LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (max(1,2*N-2))
 If COMPZ = 'N', then WORK is not referenced.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: the algorithm has failed to find all the eigenvalues in
 a total of 30*N iterations; if INFO = i, then i
 elements of E have not converged to zero; on exit, D
 and E contain the elements of a symmetric tridiagonal
 matrix which is orthogonally similar to the original
 matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 132 of file dsteqr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
