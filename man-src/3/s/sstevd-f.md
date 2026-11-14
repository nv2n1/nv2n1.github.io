---
title: "sstevd-f(3)"
name: "sstevd-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sstevd-f/"
description: "sstevd.f –"
---

<p>sstevd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sstevd</code> (JOBZ, N, D, E, Z, LDZ, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code> SSTEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sstevd (characterJOBZ, integerN, real, dimension( * )D, real, dimension( * )E, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code> SSTEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSTEVD computes all eigenvalues and, optionally, eigenvectors of a
 real symmetric tridiagonal matrix. If eigenvectors are desired, it
 uses a divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBZ</i> </p>
<pre> JOBZ is CHARACTER*1
 = 'N': Compute eigenvalues only;
 = 'V': Compute eigenvalues and eigenvectors.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the n diagonal elements of the tridiagonal matrix
 A.
 On exit, if INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N-1)
 On entry, the (n-1) subdiagonal elements of the tridiagonal
 matrix A, stored in elements 1 to N-1 of E.
 On exit, the contents of E are destroyed.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ, N)
 If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
 eigenvectors of the matrix A, with the i-th column of Z
 holding the eigenvector associated with D(i).
 If JOBZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array,
 dimension (LWORK)
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If JOBZ = 'N' or N &lt;= 1 then LWORK must be at least 1.
 If JOBZ = 'V' and N &gt; 1 then LWORK must be at least
 ( 1 + 4*N + N**2 ).
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal sizes of the WORK and IWORK
 arrays, returns these values as the first entries of the WORK
 and IWORK arrays, and no error message related to LWORK or
 LIWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of the array IWORK.
 If JOBZ = 'N' or N &lt;= 1 then LIWORK must be at least 1.
 If JOBZ = 'V' and N &gt; 1 then LIWORK must be at least 3+5*N.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal sizes of the WORK and
 IWORK arrays, returns these values as the first entries of
 the WORK and IWORK arrays, and no error message related to
 LWORK or LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the algorithm failed to converge; i
 off-diagonal elements of E did not converge to zero.</pre>
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
<p> Definition at line 163 of file sstevd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
