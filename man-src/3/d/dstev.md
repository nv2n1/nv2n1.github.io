---
title: "dstev(3)"
name: "dstev"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dstev/"
description: "dstev.f –"
---

<h2 class="name">NAME</h2>
<p> dstev.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dstev</code> (JOBZ, N, D, E, Z, LDZ, WORK, INFO)<br />
 <i></i><code> DSTEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dstev (characterJOBZ, integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code> DSTEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DSTEV computes all eigenvalues and, optionally, eigenvectors of a
 real symmetric tridiagonal matrix A.
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
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix.  N &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          On entry, the n diagonal elements of the tridiagonal matrix
          A.
          On exit, if INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>E</i> </p>
<pre>
          E is DOUBLE PRECISION array, dimension (N-1)
          On entry, the (n-1) subdiagonal elements of the tridiagonal
          matrix A, stored in elements 1 to N-1 of E.
          On exit, the contents of E are destroyed.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension (LDZ, N)
          If JOBZ = 'V', then if INFO = 0, Z contains the orthonormal
          eigenvectors of the matrix A, with the i-th column of Z
          holding the eigenvector associated with D(i).
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
          WORK is DOUBLE PRECISION array, dimension (max(1,2*N-2))
          If JOBZ = 'N', WORK is not referenced.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the algorithm failed to converge; i
                off-diagonal elements of E did not converge to zero.
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
<p> Definition at line 117 of file dstev.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
