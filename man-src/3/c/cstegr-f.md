---
title: "cstegr-f(3)"
name: "cstegr-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cstegr-f/"
description: "cstegr.f –"
---

<p>cstegr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cstegr</code> (JOBZ, RANGE, N, D, E, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, ISUPPZ, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>CSTEGR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cstegr (characterJOBZ, characterRANGE, integerN, real, dimension( * )D, real, dimension( * )E, realVL, realVU, integerIL, integerIU, realABSTOL, integerM, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, integer, dimension( * )ISUPPZ, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code>CSTEGR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CSTEGR computes selected eigenvalues and, optionally, eigenvectors
 of a real symmetric tridiagonal matrix T. Any such unreduced matrix has
 a well defined set of pairwise different real eigenvalues, the corresponding
 real eigenvectors are pairwise orthogonal.
 The spectrum may be computed either completely or partially by specifying
 either an interval (VL,VU] or a range of indices IL:IU for the desired
 eigenvalues.
 CSTEGR is a compatability wrapper around the improved CSTEMR routine.
 See SSTEMR for further details.
 One important change is that the ABSTOL parameter no longer provides any
 benefit and hence is no longer used.
 Note : CSTEGR and CSTEMR work only on machines which follow
 IEEE-754 floating-point standard in their handling of infinities and
 NaNs. Normal execution may create these exceptiona values and hence
 may abort due to a floating point exception in environments which
 do not conform to the IEEE-754 standard.</pre>
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
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the N diagonal elements of the tridiagonal matrix
 T. On exit, D is overwritten.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N)
 On entry, the (N-1) subdiagonal elements of the tridiagonal
 matrix T in elements 1 to N-1 of E. E(N) need not be set on
 input, but is used internally as workspace.
 On exit, E is overwritten.</pre>
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
 1 &lt;= IL &lt;= IU &lt;= N, if N &gt; 0.
 Not referenced if RANGE = 'A' or 'V'.</pre>
<p><i>ABSTOL</i> </p>
<pre> ABSTOL is REAL
 Unused. Was the absolute error tolerance for the
 eigenvalues/eigenvectors in previous versions.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The total number of eigenvalues found. 0 &lt;= M &lt;= N.
 If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 The first M elements contain the selected eigenvalues in
 ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX array, dimension (LDZ, max(1,M) )
 If JOBZ = 'V', and if INFO = 0, then the first M columns of Z
 contain the orthonormal eigenvectors of the matrix T
 corresponding to the selected eigenvalues, with the i-th
 column of Z holding the eigenvector associated with W(i).
 If JOBZ = 'N', then Z is not referenced.
 Note: the user must ensure that at least max(1,M) columns are
 supplied in the array Z; if RANGE = 'V', the exact value of M
 is not known in advance and an upper bound must be used.
 Supplying N columns is always safe.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', then LDZ &gt;= max(1,N).</pre>
<p><i>ISUPPZ</i> </p>
<pre> ISUPPZ is INTEGER ARRAY, dimension ( 2*max(1,M) )
 The support of the eigenvectors in Z, i.e., the indices
 indicating the nonzero elements in Z. The i-th computed eigenvector
 is nonzero only in elements ISUPPZ( 2*i-1 ) through
 ISUPPZ( 2*i ). This is relevant in the case when the matrix
 is split. ISUPPZ is only accessed when JOBZ is 'V' and N &gt; 0.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (LWORK)
 On exit, if INFO = 0, WORK(1) returns the optimal
 (and minimal) LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,18*N)
 if JOBZ = 'V', and LWORK &gt;= max(1,12*N) if JOBZ = 'N'.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (LIWORK)
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of the array IWORK. LIWORK &gt;= max(1,10*N)
 if the eigenvectors are desired, and LIWORK &gt;= max(1,8*N)
 if only the eigenvalues are to be computed.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal size of the IWORK array,
 returns this value as the first entry of the IWORK array, and
 no error message related to LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 On exit, INFO
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = 1X, internal error in SLARRE,
 if INFO = 2X, internal error in CLARRV.
 Here, the digit X = ABS( IINFO ) &lt; 10, where IINFO is
 the nonzero error code returned by SLARRE or
 CLARRV, respectively.</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Inderjit Dhillon, IBM Almaden, USA </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 255 of file cstegr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
