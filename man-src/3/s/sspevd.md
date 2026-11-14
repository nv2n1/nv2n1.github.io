---
title: "sspevd(3)"
name: "sspevd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sspevd/"
description: "sspevd.f –"
---

<h2 class="name">NAME</h2>
<p> sspevd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sspevd</code> (JOBZ, UPLO, N, AP, W, Z, LDZ, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code> SSPEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sspevd (characterJOBZ, characterUPLO, integerN, real, dimension( * )AP, real, dimension( * )W, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code> SSPEVD computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSPEVD computes all the eigenvalues and, optionally, eigenvectors
 of a real symmetric matrix A in packed storage. If eigenvectors are
 desired, it uses a divide and conquer algorithm.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBZ</i> </p>
<pre>
          JOBZ is CHARACTER*1
          = 'N':  Compute eigenvalues only;
          = 'V':  Compute eigenvalues and eigenvectors.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is REAL array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the symmetric matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          On exit, AP is overwritten by values generated during the
          reduction to tridiagonal form.  If UPLO = 'U', the diagonal
          and first superdiagonal of the tridiagonal matrix T overwrite
          the corresponding elements of A, and if UPLO = 'L', the
          diagonal and first subdiagonal of T overwrite the
          corresponding elements of A.
</code></pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          If INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension (LDZ, N)
          If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
          eigenvectors of the matrix A, with the i-th column of Z
          holding the eigenvector associated with W(i).
          If JOBZ = 'N', then Z is not referenced.
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= max(1,N).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the required LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.
          If N &lt;= 1,               LWORK must be at least 1.
          If JOBZ = 'N' and N &gt; 1, LWORK must be at least 2*N.
          If JOBZ = 'V' and N &gt; 1, LWORK must be at least
                                                 1 + 6*N + N**2.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the required sizes of the WORK and IWORK
          arrays, returns these values as the first entries of the WORK
          and IWORK arrays, and no error message related to LWORK or
          LIWORK is issued by XERBLA.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the required LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<pre>
          LIWORK is INTEGER
          The dimension of the array IWORK.
          If JOBZ  = 'N' or N &lt;= 1, LIWORK must be at least 1.
          If JOBZ  = 'V' and N &gt; 1, LIWORK must be at least 3 + 5*N.
          If LIWORK = -1, then a workspace query is assumed; the
          routine only calculates the required sizes of the WORK and
          IWORK arrays, returns these values as the first entries of
          the WORK and IWORK arrays, and no error message related to
          LWORK or LIWORK is issued by XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  if INFO = i, the algorithm failed to converge; i
                off-diagonal elements of an intermediate tridiagonal
                form did not converge to zero.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> November 2011</dl>
<p> Definition at line 178 of file sspevd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
