---
title: "chpev-f(3)"
name: "chpev-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chpev-f/"
description: "chpev.f –"
---

<p>chpev.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>chpev</code> (JOBZ, UPLO, N, AP, W, Z, LDZ, WORK, RWORK, INFO)<br />
 <i></i><code> CHPEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chpev (characterJOBZ, characterUPLO, integerN, complex, dimension( * )AP, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code> CHPEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CHPEV computes all the eigenvalues and, optionally, eigenvectors of a
 complex Hermitian matrix in packed storage.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBZ</i> </p>
<pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 A, packed columnwise in a linear array. The j-th column of A
 is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 On exit, AP is overwritten by values generated during the
 reduction to tridiagonal form. If UPLO = 'U', the diagonal
 and first superdiagonal of the tridiagonal matrix T overwrite
 the corresponding elements of A, and if UPLO = 'L', the
 diagonal and first subdiagonal of T overwrite the
 corresponding elements of A.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX array, dimension (LDZ, N)
 If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
 eigenvectors of the matrix A, with the i-th column of Z
 holding the eigenvector associated with W(i).
 If JOBZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (max(1, 2*N-1))</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (max(1, 3*N-2))</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = i, the algorithm failed to converge; i
 off-diagonal elements of an intermediate tridiagonal
 form did not converge to zero.</pre>
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
<p> Definition at line 138 of file chpev.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
