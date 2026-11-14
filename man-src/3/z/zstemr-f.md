---
title: "zstemr-f(3)"
name: "zstemr-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zstemr-f/"
description: "zstemr.f –"
---

<p>zstemr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zstemr</code> (JOBZ, RANGE, N, D, E, VL, VU, IL, IU, M, W, Z, LDZ, NZC, ISUPPZ, TRYRAC, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>ZSTEMR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zstemr (characterJOBZ, characterRANGE, integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precisionVL, double precisionVU, integerIL, integerIU, integerM, double precision, dimension( * )W, complex*16, dimension( ldz, * )Z, integerLDZ, integerNZC, integer, dimension( * )ISUPPZ, logicalTRYRAC, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code>ZSTEMR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSTEMR computes selected eigenvalues and, optionally, eigenvectors
 of a real symmetric tridiagonal matrix T. Any such unreduced matrix has
 a well defined set of pairwise different real eigenvalues, the corresponding
 real eigenvectors are pairwise orthogonal.
 The spectrum may be computed either completely or partially by specifying
 either an interval (VL,VU] or a range of indices IL:IU for the desired
 eigenvalues.
 Depending on the number of desired eigenvalues, these are computed either
 by bisection or the dqds algorithm. Numerically orthogonal eigenvectors are
 computed by the use of various suitable L D L^T factorizations near clusters
 of close eigenvalues (referred to as RRRs, Relatively Robust
 Representations). An informal sketch of the algorithm follows.
 For each unreduced block (submatrix) of T,
 (a) Compute T - sigma I = L D L^T, so that L and D
 define all the wanted eigenvalues to high relative accuracy.
 This means that small relative changes in the entries of D and L
 cause only small relative changes in the eigenvalues and
 eigenvectors. The standard (unfactored) representation of the
 tridiagonal matrix T does not have this property in general.
 (b) Compute the eigenvalues to suitable accuracy.
 If the eigenvectors are desired, the algorithm attains full
 accuracy of the computed eigenvalues only right before
 the corresponding vectors have to be computed, see steps c) and d).
 (c) For each cluster of close eigenvalues, select a new
 shift close to the cluster, find a new factorization, and refine
 the shifted eigenvalues to suitable accuracy.
 (d) For each eigenvalue with a large enough relative separation compute
 the corresponding eigenvector by forming a rank revealing twisted
 factorization. Go back to (c) for any clusters that remain.
 For more details, see:
 - Inderjit S. Dhillon and Beresford N. Parlett: &quot;Multiple representations
 to compute orthogonal eigenvectors of symmetric tridiagonal matrices,&quot;
 Linear Algebra and its Applications, <a href="//www.systutorials.com/docs/linux/man/1-387/">387</a>(1), pp. 1-28, August 2004.
 - Inderjit Dhillon and Beresford Parlett: &quot;Orthogonal Eigenvectors and
 Relative Gaps,&quot; SIAM Journal on Matrix Analysis and Applications, Vol. 25,
 2004. Also LAPACK Working Note 154.
 - Inderjit Dhillon: &quot;A new O(n^2) algorithm for the symmetric
 tridiagonal eigenvalue/eigenvector problem&quot;,
 Computer Science Division Technical Report No. UCB/CSD-97-971,
 UC Berkeley, May 1997.
 Further Details
 1.ZSTEMR works only on machines which follow IEEE-754
 floating-point standard in their handling of infinities and NaNs.
 This permits the use of efficient inner loops avoiding a check for
 zero divisors.
 2. LAPACK routines can be used to reduce a complex Hermitean matrix to
 real symmetric tridiagonal form.
 (Any complex Hermitean tridiagonal matrix has real values on its diagonal
 and potentially complex numbers on its off-diagonals. By applying a
 similarity transform with an appropriate diagonal matrix
 diag(1,e^{i <br>
hy_1}, ... , e^{i <br>
hy_{n-1}}), the complex Hermitean
 matrix can be transformed into a real symmetric matrix and complex
 arithmetic can be entirely avoided.)
 While the eigenvectors of the real symmetric tridiagonal matrix are real,
 the eigenvectors of original complex Hermitean matrix have complex entries
 in general.
 Since LAPACK drivers overwrite the matrix data with the eigenvectors,
 ZSTEMR accepts complex workspace to facilitate interoperability
 with ZUNMTR or ZUPMTR.</pre>
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
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the N diagonal elements of the tridiagonal matrix
 T. On exit, D is overwritten.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N)
 On entry, the (N-1) subdiagonal elements of the tridiagonal
 matrix T in elements 1 to N-1 of E. E(N) need not be set on
 input, but is used internally as workspace.
 On exit, E is overwritten.</pre>
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
 1 &lt;= IL &lt;= IU &lt;= N, if N &gt; 0.
 Not referenced if RANGE = 'A' or 'V'.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The total number of eigenvalues found. 0 &lt;= M &lt;= N.
 If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 The first M elements contain the selected eigenvalues in
 ascending order.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, max(1,M) )
 If JOBZ = 'V', and if INFO = 0, then the first M columns of Z
 contain the orthonormal eigenvectors of the matrix T
 corresponding to the selected eigenvalues, with the i-th
 column of Z holding the eigenvector associated with W(i).
 If JOBZ = 'N', then Z is not referenced.
 Note: the user must ensure that at least max(1,M) columns are
 supplied in the array Z; if RANGE = 'V', the exact value of M
 is not known in advance and can be computed with a workspace
 query by setting NZC = -1, see below.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', then LDZ &gt;= max(1,N).</pre>
<p><i>NZC</i> </p>
<pre> NZC is INTEGER
 The number of eigenvectors to be held in the array Z.
 If RANGE = 'A', then NZC &gt;= max(1,N).
 If RANGE = 'V', then NZC &gt;= the number of eigenvalues in (VL,VU].
 If RANGE = 'I', then NZC &gt;= IU-IL+1.
 If NZC = -1, then a workspace query is assumed; the
 routine calculates the number of columns of the array Z that
 are needed to hold the eigenvectors.
 This value is returned as the first entry of the Z array, and
 no error message related to NZC is issued by XERBLA.</pre>
<p><i>ISUPPZ</i> </p>
<pre> ISUPPZ is INTEGER ARRAY, dimension ( 2*max(1,M) )
 The support of the eigenvectors in Z, i.e., the indices
 indicating the nonzero elements in Z. The i-th computed eigenvector
 is nonzero only in elements ISUPPZ( 2*i-1 ) through
 ISUPPZ( 2*i ). This is relevant in the case when the matrix
 is split. ISUPPZ is only accessed when JOBZ is 'V' and N &gt; 0.</pre>
<p><i>TRYRAC</i> </p>
<pre> TRYRAC is LOGICAL
 If TRYRAC.EQ..TRUE., indicates that the code should check whether
 the tridiagonal matrix defines its eigenvalues to high relative
 accuracy. If so, the code uses relative-accuracy preserving
 algorithms that might be (a bit) slower depending on the matrix.
 If the matrix does not define its eigenvalues to high relative
 accuracy, the code can uses possibly faster algorithms.
 If TRYRAC.EQ..FALSE., the code is not required to guarantee
 relatively accurate eigenvalues and can use the fastest possible
 techniques.
 On exit, a .TRUE. TRYRAC will be set to .FALSE. if the matrix
 does not define its eigenvalues to high relative accuracy.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (LWORK)
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
 &gt; 0: if INFO = 1X, internal error in DLARRE,
 if INFO = 2X, internal error in ZLARRV.
 Here, the digit X = ABS( IINFO ) &lt; 10, where IINFO is
 the nonzero error code returned by DLARRE or
 ZLARRV, respectively.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 328 of file zstemr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
