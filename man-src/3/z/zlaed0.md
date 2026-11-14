---
title: "zlaed0(3)"
name: "zlaed0"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaed0/"
description: "zlaed0.f –"
---

<p>zlaed0.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaed0</code> (QSIZ, N, D, E, Q, LDQ, QSTORE, LDQS, RWORK, IWORK, INFO)<br />
 <i></i><code>ZLAED0</code> used by sstedc. Computes all eigenvalues and corresponding eigenvectors of an unreduced symmetric tridiagonal matrix using the divide and conquer method.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaed0 (integerQSIZ, integerN, double precision, dimension( * )D, double precision, dimension( * )E, complex*16, dimension( ldq, * )Q, integerLDQ, complex*16, dimension( ldqs, * )QSTORE, integerLDQS, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>ZLAED0</code> used by sstedc. Computes all eigenvalues and corresponding eigenvectors of an unreduced symmetric tridiagonal matrix using the divide and conquer method. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Using the divide and conquer method, ZLAED0 computes all eigenvalues
 of a symmetric tridiagonal matrix which is one diagonal block of
 those from reducing a dense or band Hermitian matrix and
 corresponding eigenvectors of the dense or band matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>QSIZ</i> </p>
<pre> QSIZ is INTEGER
 The dimension of the unitary matrix used to reduce
 the full matrix to tridiagonal form. QSIZ &gt;= N if ICOMPQ = 1.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The dimension of the symmetric tridiagonal matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the diagonal elements of the tridiagonal matrix.
 On exit, the eigenvalues in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 On entry, the off-diagonal elements of the tridiagonal matrix.
 On exit, E has been destroyed.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX*16 array, dimension (LDQ,N)
 On entry, Q must contain an QSIZ x N matrix whose columns
 unitarily orthonormal. It is a part of the unitary matrix
 that reduces the full dense Hermitian matrix to a
 (reducible) symmetric tridiagonal matrix.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N).</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array,
 the dimension of IWORK must be at least
 6 + 6*N + 5*N*lg N
 ( lg( N ) = smallest integer k
 such that 2^k &gt;= N )</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array,
 dimension (1 + 3*N + 2*N*lg N + 3*N**2)
 ( lg( N ) = smallest integer k
 such that 2^k &gt;= N )</pre>
<p><i>QSTORE</i> </p>
<pre> QSTORE is COMPLEX*16 array, dimension (LDQS, N)
 Used to store parts of
 the eigenvector matrix when the updating matrix multiplies
 take place.</pre>
<p><i>LDQS</i> </p>
<pre> LDQS is INTEGER
 The leading dimension of the array QSTORE.
 LDQS &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: The algorithm failed to compute an eigenvalue while
 working on the submatrix lying in rows and columns
 INFO/(N+1) through mod(INFO,N+1).</pre>
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
<p> Definition at line 145 of file zlaed0.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
