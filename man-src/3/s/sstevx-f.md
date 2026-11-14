---
title: "sstevx-f(3)"
name: "sstevx-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sstevx-f/"
description: "sstevx.f –"
---

<p>sstevx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sstevx</code> (JOBZ, RANGE, N, D, E, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, IWORK, IFAIL, INFO)<br />
 <i></i><code> SSTEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sstevx (characterJOBZ, characterRANGE, integerN, real, dimension( * )D, real, dimension( * )E, realVL, realVU, integerIL, integerIU, realABSTOL, integerM, real, dimension( * )W, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p><code> SSTEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSTEVX computes selected eigenvalues and, optionally, eigenvectors
 of a real symmetric tridiagonal matrix A. Eigenvalues and
 eigenvectors can be selected by specifying either a range of values
 or a range of indices for the desired eigenvalues.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBZ</i> </p>
<pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre>
<p><i>RANGE</i> </p>
<pre> RANGE is CHARACTER*1
 = 'A': all eigenvalues will be found.
 = 'V': all eigenvalues in the half-open interval (VL,VU]
 will be found.
 = 'I': the IL-th through IU-th eigenvalues will be found.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the n diagonal elements of the tridiagonal matrix
 A.
 On exit, D may be multiplied by a constant factor chosen
 to avoid over/underflow in computing the eigenvalues.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (max(1,N-1))
 On entry, the (n-1) subdiagonal elements of the tridiagonal
 matrix A in elements 1 to N-1 of E.
 On exit, E may be multiplied by a constant factor chosen
 to avoid over/underflow in computing the eigenvalues.</pre>
<p><i>VL</i> </p>
<pre> VL is REAL</pre>
<p><i>VU</i> </p>
<pre> VU is REAL
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
<pre> ABSTOL is REAL
 The absolute error tolerance for the eigenvalues.
 An approximate eigenvalue is accepted as converged
 when it is determined to lie in an interval [a,b]
 of width less than or equal to
 ABSTOL + EPS * max( |a|,|b| ) ,
 where EPS is the machine precision. If ABSTOL is less
 than or equal to zero, then EPS*|T| will be used in
 its place, where |T| is the 1-norm of the tridiagonal
 matrix.
 Eigenvalues will be computed most accurately when ABSTOL is
 set to twice the underflow threshold 2*SLAMCH('S'), not zero.
 If this routine returns with INFO&gt;0, indicating that some
 eigenvectors did not converge, try setting ABSTOL to
 2*SLAMCH('S').
 See &quot;Computing Small Singular Values of Bidiagonal Matrices
 with Guaranteed High Relative Accuracy,&quot; by Demmel and
 Kahan, LAPACK Working Note #3.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The total number of eigenvalues found. 0 &lt;= M &lt;= N.
 If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 The first M elements contain the selected eigenvalues in
 ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ, max(1,M) )
 If JOBZ = 'V', then if INFO = 0, the first M columns of Z
 contain the orthonormal eigenvectors of the matrix A
 corresponding to the selected eigenvalues, with the i-th
 column of Z holding the eigenvector associated with W(i).
 If an eigenvector fails to converge (INFO &gt; 0), then that
 column of Z contains the latest approximation to the
 eigenvector, and the index of the eigenvector is returned
 in IFAIL. If JOBZ = 'N', then Z is not referenced.
 Note: the user must ensure that at least max(1,M) columns are
 supplied in the array Z; if RANGE = 'V', the exact value of M
 is not known in advance and an upper bound must be used.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (5*N)</pre>
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
<p> Definition at line 220 of file sstevx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
