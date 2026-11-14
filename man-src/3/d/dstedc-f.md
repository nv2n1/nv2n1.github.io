---
title: "dstedc-f(3)"
name: "dstedc-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dstedc-f/"
description: "dstedc.f –"
---

<p>dstedc.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dstedc</code> (COMPZ, N, D, E, Z, LDZ, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>DSTEBZ</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dstedc (characterCOMPZ, integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p><code>DSTEBZ</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSTEDC computes all eigenvalues and, optionally, eigenvectors of a
 symmetric tridiagonal matrix using the divide and conquer method.
 The eigenvectors of a full or band real symmetric matrix can also be
 found if DSYTRD or DSPTRD or DSBTRD has been used to reduce this
 matrix to tridiagonal form.
 This code makes very mild assumptions about floating point
 arithmetic. It will work on machines with a guard digit in
 add/subtract, or on those binary machines without guard digits
 which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or Cray-2.
 It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none. See DLAED3 for details.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>COMPZ</i> </p>
<pre> COMPZ is CHARACTER*1
 = 'N': Compute eigenvalues only.
 = 'I': Compute eigenvectors of tridiagonal matrix also.
 = 'V': Compute eigenvectors of original dense symmetric
 matrix also. On entry, Z contains the orthogonal
 matrix used to reduce the original matrix to
 tridiagonal form.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The dimension of the symmetric tridiagonal matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the diagonal elements of the tridiagonal matrix.
 On exit, if INFO = 0, the eigenvalues in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 On entry, the subdiagonal elements of the tridiagonal matrix.
 On exit, E has been destroyed.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension (LDZ,N)
 On entry, if COMPZ = 'V', then Z contains the orthogonal
 matrix used in the reduction to tridiagonal form.
 On exit, if INFO = 0, then if COMPZ = 'V', Z contains the
 orthonormal eigenvectors of the original symmetric matrix,
 and if COMPZ = 'I', Z contains the orthonormal eigenvectors
 of the symmetric tridiagonal matrix.
 If COMPZ = 'N', then Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1.
 If eigenvectors are desired, then LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array,
 dimension (LWORK)
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If COMPZ = 'N' or N &lt;= 1 then LWORK must be at least 1.
 If COMPZ = 'V' and N &gt; 1 then LWORK must be at least
 ( 1 + 3*N + 2*N*lg N + 4*N**2 ),
 where lg( N ) = smallest integer k such
 that 2**k &gt;= N.
 If COMPZ = 'I' and N &gt; 1 then LWORK must be at least
 ( 1 + 4*N + N**2 ).
 Note that for COMPZ = 'I' or 'V', then if N is less than or
 equal to the minimum divide size, usually 25, then LWORK need
 only be max(1,2*(N-1)).
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MAX(1,LIWORK))
 On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.</pre>
<p><i>LIWORK</i> </p>
<pre> LIWORK is INTEGER
 The dimension of the array IWORK.
 If COMPZ = 'N' or N &lt;= 1 then LIWORK must be at least 1.
 If COMPZ = 'V' and N &gt; 1 then LIWORK must be at least
 ( 6 + 6*N + 5*N*lg N ).
 If COMPZ = 'I' and N &gt; 1 then LIWORK must be at least
 ( 3 + 5*N ).
 Note that for COMPZ = 'I' or 'V', then if N is less than or
 equal to the minimum divide size, usually 25, then LIWORK
 need only be 1.
 If LIWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal size of the IWORK array,
 returns this value as the first entry of the IWORK array, and
 no error message related to LIWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: The algorithm failed to compute an eigenvalue while
 working on the submatrix lying in rows and columns
 INFO/(N+1) through mod(INFO,N+1).</pre>
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
<dd>Jeff Rutter, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Modified by Francoise Tisseur, University of Tennessee&nbsp;<wbr></dl>
<p> Definition at line 189 of file dstedc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
