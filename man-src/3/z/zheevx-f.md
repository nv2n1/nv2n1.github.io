---
title: "zheevx-f(3)"
name: "zheevx-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zheevx-f/"
---

zheevx.f -

<h2>Synopsis</h2>



<h3>Functions/Subroutines</h3>

subroutine <b>zheevx</b> (JOBZ, RANGE, UPLO, N, A, LDA, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, LWORK, RWORK, IWORK, IFAIL, INFO) 
 <i></i><b> ZHEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for HE matrices</b>

<h2>Function/Subroutine Documentation</h2>

<h3>subroutine zheevx (characterJOBZ, characterRANGE, characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, double precisionVL, double precisionVU, integerIL, integerIU, double precisionABSTOL, integerM, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>

<b> ZHEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for HE matrices</b> 

 <b>Purpose: </b>
<dl><dd><pre> ZHEEVX computes selected eigenvalues and, optionally, eigenvectors
 of a complex Hermitian matrix A. Eigenvalues and eigenvectors can
 be selected by specifying either a range of values or a range of
 indices for the desired eigenvalues.</pre>&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl><dd><i>JOBZ</i> 

 <pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre><i>RANGE</i> 

 <pre> RANGE is CHARACTER*1
 = 'A': all eigenvalues will be found.
 = 'V': all eigenvalues in the half-open interval (VL,VU]
 will be found.
 = 'I': the IL-th through IU-th eigenvalues will be found.</pre><i>UPLO</i> 

 <pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre><i>N</i> 

 <pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre><i>A</i> 

 <pre> A is COMPLEX*16 array, dimension (LDA, N)
 On entry, the Hermitian matrix A. If UPLO = 'U', the
 leading N-by-N upper triangular part of A contains the
 upper triangular part of the matrix A. If UPLO = 'L',
 the leading N-by-N lower triangular part of A contains
 the lower triangular part of the matrix A.
 On exit, the lower triangle (if UPLO='L') or the upper
 triangle (if UPLO='U') of A, including the diagonal, is
 destroyed.</pre><i>LDA</i> 

 <pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre><i>VL</i> 

 <pre> VL is DOUBLE PRECISION</pre><i>VU</i> 

 <pre> VU is DOUBLE PRECISION
 If RANGE='V', the lower and upper bounds of the interval to
 be searched for eigenvalues. VL &lt; VU.
 Not referenced if RANGE = 'A' or 'I'.</pre><i>IL</i> 

 <pre> IL is INTEGER</pre><i>IU</i> 

 <pre> IU is INTEGER
 If RANGE='I', the indices (in ascending order) of the
 smallest and largest eigenvalues to be returned.
 1 &lt;= IL &lt;= IU &lt;= N, if N &gt; 0; IL = 1 and IU = 0 if N = 0.
 Not referenced if RANGE = 'A' or 'V'.</pre><i>ABSTOL</i> 

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
 Kahan, LAPACK Working Note #3.</pre><i>M</i> 

 <pre> M is INTEGER
 The total number of eigenvalues found. 0 &lt;= M &lt;= N.
 If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.</pre><i>W</i> 

 <pre> W is DOUBLE PRECISION array, dimension (N)
 On normal exit, the first M elements contain the selected
 eigenvalues in ascending order.</pre><i>Z</i> 

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
 is not known in advance and an upper bound must be used.</pre><i>LDZ</i> 

 <pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre><i>WORK</i> 

 <pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre><i>LWORK</i> 

 <pre> LWORK is INTEGER
 The length of the array WORK. LWORK &gt;= 1, when N &lt;= 1;
 otherwise 2*N.
 For optimal efficiency, LWORK &gt;= (NB+1)*N,
 where NB is the max of the blocksize for ZHETRD and for
 ZUNMTR as returned by ILAENV.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre><i>RWORK</i> 

 <pre> RWORK is DOUBLE PRECISION array, dimension (7*N)</pre><i>IWORK</i> 

 <pre> IWORK is INTEGER array, dimension (5*N)</pre><i>IFAIL</i> 

 <pre> IFAIL is INTEGER array, dimension (N)
 If JOBZ = 'V', then if INFO = 0, the first M elements of
 IFAIL are zero. If INFO &gt; 0, then IFAIL contains the
 indices of the eigenvectors that failed to converge.
 If JOBZ = 'N', then IFAIL is not referenced.</pre><i>INFO</i> 

 <pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, then i eigenvectors failed to converge.
 Their indices are stored in array IFAIL.</pre>&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl><dd>Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl><dd>November 2011</dl>
 

 

 

 Definition at line 251 of file zheevx.f.

<h2>Author</h2>

Generated automatically by Doxygen for LAPACK from the source code.
