---
title: "zhpgvx(3)"
name: "zhpgvx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhpgvx/"
description: "zhpgvx.f –"
---

<p>zhpgvx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhpgvx</code> (ITYPE, JOBZ, RANGE, UPLO, N, AP, BP, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, RWORK, IWORK, IFAIL, INFO)<br />
 <i></i><code>ZHPGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhpgvx (integerITYPE, characterJOBZ, characterRANGE, characterUPLO, integerN, complex*16, dimension( * )AP, complex*16, dimension( * )BP, double precisionVL, double precisionVU, integerIL, integerIU, double precisionABSTOL, integerM, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p><code>ZHPGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPGVX computes selected eigenvalues and, optionally, eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x, A*Bx=(lambda)*x, or B*A*x=(lambda)*x. Here A and
 B are assumed to be Hermitian, stored in packed format, and B is also
 positive definite. Eigenvalues and eigenvectors can be selected by
 specifying either a range of values or a range of indices for the
 desired eigenvalues.</pre>
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
<p><i>RANGE</i> </p>
<pre> RANGE is CHARACTER*1
 = 'A': all eigenvalues will be found;
 = 'V': all eigenvalues in the half-open interval (VL,VU]
 will be found;
 = 'I': the IL-th through IU-th eigenvalues will be found.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangles of A and B are stored;
 = 'L': Lower triangles of A and B are stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 A, packed columnwise in a linear array. The j-th column of A
 is stored in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 On exit, the contents of AP are destroyed.</pre>
<p><i>BP</i> </p>
<pre> BP is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the upper or lower triangle of the Hermitian matrix
 B, packed columnwise in a linear array. The j-th column of B
 is stored in the array BP as follows:
 if UPLO = 'U', BP(i + (j-1)*j/2) = B(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j&lt;=i&lt;=n.
 On exit, the triangular factor U or L from the Cholesky
 factorization B = U**H*U or B = L*L**H, in the same storage
 format as B.</pre>
<p><i>VL</i> </p>
<pre> VL is DOUBLE PRECISION</pre>
<p><i>VU</i> </p>
<pre> VU is DOUBLE PRECISION
 If RANGE='V', the lower and upper bounds of the interval to
 be searched for eigenvalues. VL &lt; VU.
 Not referenced if RANGE = 'A' or 'I'.</pre>
<p><i>IL</i> </p>
<pre> IL is INTEGER</pre>
<p><i>IU</i> </p>
<pre> IU is INTEGER
 If RANGE='I', the indices (in ascending order) of the
 smallest and largest eigenvalues to be returned.
 1 &lt;= IL &lt;= IU &lt;= N, if N &gt; 0; IL = 1 and IU = 0 if N = 0.
 Not referenced if RANGE = 'A' or 'V'.</pre>
<p><i>ABSTOL</i> </p>
<pre> ABSTOL is DOUBLE PRECISION
 The absolute error tolerance for the eigenvalues.
 An approximate eigenvalue is accepted as converged
 when it is determined to lie in an interval [a,b]
 of width less than or equal to
 ABSTOL + EPS * max( |a|,|b| ) ,
 where EPS is the machine precision. If ABSTOL is less than
 or equal to zero, then EPS*|T| will be used in its place,
 where |T| is the 1-norm of the tridiagonal matrix obtained
 by reducing AP to tridiagonal form.
 Eigenvalues will be computed most accurately when ABSTOL is
 set to twice the underflow threshold 2*DLAMCH('S'), not zero.
 If this routine returns with INFO&gt;0, indicating that some
 eigenvectors did not converge, try setting ABSTOL to
 2*DLAMCH('S').</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The total number of eigenvalues found. 0 &lt;= M &lt;= N.
 If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 On normal exit, the first M elements contain the selected
 eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, N)
 If JOBZ = 'N', then Z is not referenced.
 If JOBZ = 'V', then if INFO = 0, the first M columns of Z
 contain the orthonormal eigenvectors of the matrix A
 corresponding to the selected eigenvalues, with the i-th
 column of Z holding the eigenvector associated with W(i).
 The eigenvectors are normalized as follows:
 if ITYPE = 1 or 2, Z**H*B*Z = I;
 if ITYPE = 3, Z**H*inv(B)*Z = I.
 If an eigenvector fails to converge, then that column of Z
 contains the latest approximation to the eigenvector, and the
 index of the eigenvector is returned in IFAIL.
 Note: the user must ensure that at least max(1,M) columns are
 supplied in the array Z; if RANGE = 'V', the exact value of M
 is not known in advance and an upper bound must be used.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (7*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (5*N)</pre>
<p><i>IFAIL</i> </p>
<pre> IFAIL is INTEGER array, dimension (N)
 If JOBZ = 'V', then if INFO = 0, the first M elements of
 IFAIL are zero. If INFO &gt; 0, then IFAIL contains the
 indices of the eigenvectors that failed to converge.
 If JOBZ = 'N', then IFAIL is not referenced.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: ZPPTRF or ZHPEVX returned an error code:
 &lt;= N: if INFO = i, ZHPEVX failed to converge;
 i eigenvectors failed to converge. Their indices
 are stored in array IFAIL.
 &gt; N: if INFO = N + i, for 1 &lt;= i &lt;= n, then the leading
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Mark Fahey, Department of Mathematics, Univ. of Kentucky, USA</dl>
<p> Definition at line 267 of file zhpgvx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
