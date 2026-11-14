---
title: "zhbevx(3)"
name: "zhbevx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhbevx/"
description: "zhbevx.f –"
---

<p>zhbevx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhbevx</code> (JOBZ, RANGE, UPLO, N, KD, AB, LDAB, Q, LDQ, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, RWORK, IWORK, IFAIL, INFO)<br />
 <i></i><code> ZHBEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhbevx (characterJOBZ, characterRANGE, characterUPLO, integerN, integerKD, complex*16, dimension( ldab, * )AB, integerLDAB, complex*16, dimension( ldq, * )Q, integerLDQ, double precisionVL, double precisionVU, integerIL, integerIU, double precisionABSTOL, integerM, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p><code> ZHBEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHBEVX computes selected eigenvalues and, optionally, eigenvectors
 of a complex Hermitian band matrix A. Eigenvalues and eigenvectors
 can be selected by specifying either a range of values or a range of
 indices for the desired eigenvalues.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBZ</i> </p>
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
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of superdiagonals of the matrix A if UPLO = 'U',
 or the number of subdiagonals if UPLO = 'L'. KD &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB, N)
 On entry, the upper or lower triangle of the Hermitian band
 matrix A, stored in the first KD+1 rows of the array. The
 j-th column of A is stored in the j-th column of the array AB
 as follows:
 if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
 On exit, AB is overwritten by values generated during the
 reduction to tridiagonal form.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KD + 1.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX*16 array, dimension (LDQ, N)
 If JOBZ = 'V', the N-by-N unitary matrix used in the
 reduction to tridiagonal form.
 If JOBZ = 'N', the array Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. If JOBZ = 'V', then
 LDQ &gt;= max(1,N).</pre>
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
 by reducing AB to tridiagonal form.
 Eigenvalues will be computed most accurately when ABSTOL is
 set to twice the underflow threshold 2*DLAMCH('S'), not zero.
 If this routine returns with INFO&gt;0, indicating that some
 eigenvectors did not converge, try setting ABSTOL to
 2*DLAMCH('S').
 See &quot;Computing Small Singular Values of Bidiagonal Matrices
 with Guaranteed High Relative Accuracy,&quot; by Demmel and
 Kahan, LAPACK Working Note #3.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The total number of eigenvalues found. 0 &lt;= M &lt;= N.
 If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 The first M elements contain the selected eigenvalues in
 ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, max(1,M))
 If JOBZ = 'V', then if INFO = 0, the first M columns of Z
 contain the orthonormal eigenvectors of the matrix A
 corresponding to the selected eigenvalues, with the i-th
 column of Z holding the eigenvector associated with W(i).
 If an eigenvector fails to converge, then that column of Z
 contains the latest approximation to the eigenvector, and the
 index of the eigenvector is returned in IFAIL.
 If JOBZ = 'N', then Z is not referenced.
 Note: the user must ensure that at least max(1,M) columns are
 supplied in the array Z; if RANGE = 'V', the exact value of M
 is not known in advance and an upper bound must be used.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N)</pre>
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
 &gt; 0: if INFO = i, then i eigenvectors failed to converge.
 Their indices are stored in array IFAIL.</pre>
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
<p> Definition at line 259 of file zhbevx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
