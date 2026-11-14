---
title: "dsyevx-f(3)"
name: "dsyevx-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsyevx-f/"
description: "dsyevx.f –"
---

<p>dsyevx.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dsyevx</code> (JOBZ, RANGE, UPLO, N, A, LDA, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, LWORK, IWORK, IFAIL, INFO)<br />
 <i></i><code> DSYEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for SY matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsyevx (characterJOBZ, characterRANGE, characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, double precisionVL, double precisionVU, integerIL, integerIU, double precisionABSTOL, integerM, double precision, dimension( * )W, double precision, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p><code> DSYEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for SY matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSYEVX computes selected eigenvalues and, optionally, eigenvectors
 of a real symmetric matrix A. Eigenvalues and eigenvectors can be
 selected by specifying either a range of values or a range of indices
 for the desired eigenvalues.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA, N)
 On entry, the symmetric matrix A. If UPLO = 'U', the
 leading N-by-N upper triangular part of A contains the
 upper triangular part of the matrix A. If UPLO = 'L',
 the leading N-by-N lower triangular part of A contains
 the lower triangular part of the matrix A.
 On exit, the lower triangle (if UPLO='L') or the upper
 triangle (if UPLO='U') of A, including the diagonal, is
 destroyed.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
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
 by reducing A to tridiagonal form.
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
 On normal exit, the first M elements contain the selected
 eigenvalues in ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension (LDZ, max(1,M))
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
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The length of the array WORK. LWORK &gt;= 1, when N &lt;= 1;
 otherwise 8*N.
 For optimal efficiency, LWORK &gt;= (NB+3)*N,
 where NB is the max of the blocksize for DSYTRD and DORMTR
 returned by ILAENV.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 245 of file dsyevx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
