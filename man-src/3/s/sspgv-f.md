---
title: "sspgv-f(3)"
name: "sspgv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sspgv-f/"
description: "sspgv.f –"
---

<p>sspgv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sspgv</code> (ITYPE, JOBZ, UPLO, N, AP, BP, W, Z, LDZ, WORK, INFO)<br />
 <i></i><code>SSPGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sspgv (integerITYPE, characterJOBZ, characterUPLO, integerN, real, dimension( * )AP, real, dimension( * )BP, real, dimension( * )W, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integerINFO)</h3>
<p><code>SSPGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSPGV computes all the eigenvalues and, optionally, the eigenvectors
 of a real generalized symmetric-definite eigenproblem, of the form
 A*x=(lambda)*B*x, A*Bx=(lambda)*x, or B*A*x=(lambda)*x.
 Here A and B are assumed to be symmetric, stored in packed format,
 and B is also positive definite.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ITYPE</i> </p>
<pre> ITYPE is INTEGER
 Specifies the problem type to be solved:
 = 1: A*x = (lambda)*B*x
 = 2: A*B*x = (lambda)*x
 = 3: B*A*x = (lambda)*x</pre>
<p><i>JOBZ</i> </p>
<pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangles of A and B are stored;
 = 'L': Lower triangles of A and B are stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is REAL array, dimension
 (N*(N+1)/2)
 On entry, the upper or lower triangle of the symmetric matrix
 A, packed columnwise in a linear array. The j-th column of A
 is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 On exit, the contents of AP are destroyed.</pre>
<p><i>BP</i> </p>
<pre> BP is REAL array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the symmetric matrix
 B, packed columnwise in a linear array. The j-th column of B
 is stored in the array BP as follows:
 if UPLO = 'U', BP(i + (j-1)*j/2) = B(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j&lt;=i&lt;=n.
 On exit, the triangular factor U or L from the Cholesky
 factorization B = U**T*U or B = L*L**T, in the same storage
 format as B.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 If INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ, N)
 If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of
 eigenvectors. The eigenvectors are normalized as follows:
 if ITYPE = 1 or 2, Z**T*B*Z = I;
 if ITYPE = 3, Z**T*inv(B)*Z = I.
 If JOBZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (3*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: SPPTRF or SSPEV returned an error code:
 &lt;= N: if INFO = i, SSPEV failed to converge;
 i off-diagonal elements of an intermediate
 tridiagonal form did not converge to zero.
 &gt; N: if INFO = n + i, for 1 &lt;= i &lt;= n, then the leading
 minor of order i of B is not positive definite.
 The factorization of B could not be completed and
 no eigenvalues or eigenvectors were computed.</pre>
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
<p> Definition at line 161 of file sspgv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
