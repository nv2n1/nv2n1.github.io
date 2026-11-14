---
title: "slaed0(3)"
name: "slaed0"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed0/"
description: "slaed0.f –"
---

<h2 class="name">NAME</h2>
<p> slaed0.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaed0</code> (ICOMPQ, QSIZ, N, D, E, Q, LDQ, QSTORE, LDQS, WORK, IWORK, INFO)<br />
 <i></i><code>SLAED0</code> used by sstedc. Computes all eigenvalues and corresponding eigenvectors of an unreduced symmetric tridiagonal matrix using the divide and conquer method.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed0 (integerICOMPQ, integerQSIZ, integerN, real, dimension( * )D, real, dimension( * )E, real, dimension( ldq, * )Q, integerLDQ, real, dimension( ldqs, * )QSTORE, integerLDQS, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SLAED0</code> used by sstedc. Computes all eigenvalues and corresponding eigenvectors of an unreduced symmetric tridiagonal matrix using the divide and conquer method. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAED0 computes all eigenvalues and corresponding eigenvectors of a
 symmetric tridiagonal matrix using the divide and conquer method.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ICOMPQ</i> </p>
<pre>
          ICOMPQ is INTEGER
          = 0:  Compute eigenvalues only.
          = 1:  Compute eigenvectors of original dense symmetric matrix
                also.  On entry, Q contains the orthogonal matrix used
                to reduce the original matrix to tridiagonal form.
          = 2:  Compute eigenvalues and eigenvectors of tridiagonal
                matrix.
</pre>
<p> <i>QSIZ</i> </p>
<pre>
          QSIZ is INTEGER
         The dimension of the orthogonal matrix used to reduce
         the full matrix to tridiagonal form.  QSIZ &gt;= N if ICOMPQ = 1.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
         The dimension of the symmetric tridiagonal matrix.  N &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
         On entry, the main diagonal of the tridiagonal matrix.
         On exit, its eigenvalues.
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
         The off-diagonal elements of the tridiagonal matrix.
         On exit, E has been destroyed.
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is REAL array, dimension (LDQ, N)
         On entry, Q must contain an N-by-N orthogonal matrix.
         If ICOMPQ = 0    Q is not referenced.
         If ICOMPQ = 1    On entry, Q is a subset of the columns of the
                          orthogonal matrix used to reduce the full
                          matrix to tridiagonal form corresponding to
                          the subset of the full matrix which is being
                          decomposed at this time.
         If ICOMPQ = 2    On entry, Q will be the identity matrix.
                          On exit, Q contains the eigenvectors of the
                          tridiagonal matrix.
</pre>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
         The leading dimension of the array Q.  If eigenvectors are
         desired, then  LDQ &gt;= max(1,N).  In any case,  LDQ &gt;= 1.
</pre>
<p> <i>QSTORE</i> </p>
<pre>
          QSTORE is REAL array, dimension (LDQS, N)
         Referenced only when ICOMPQ = 1.  Used to store parts of
         the eigenvector matrix when the updating matrix multiplies
         take place.
</pre>
<p> <i>LDQS</i> </p>
<pre>
          LDQS is INTEGER
         The leading dimension of the array QSTORE.  If ICOMPQ = 1,
         then  LDQS &gt;= max(1,N).  In any case,  LDQS &gt;= 1.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array,
         If ICOMPQ = 0 or 1, the dimension of WORK must be at least
                     1 + 3*N + 2*N*lg N + 3*N**2
                     ( lg( N ) = smallest integer k
                                 such that 2^k &gt;= N )
         If ICOMPQ = 2, the dimension of WORK must be at least
                     4*N + N**2.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array,
         If ICOMPQ = 0 or 1, the dimension of IWORK must be at least
                        6 + 6*N + 5*N*lg N.
                        ( lg( N ) = smallest integer k
                                    such that 2^k &gt;= N )
         If ICOMPQ = 2, the dimension of IWORK must be at least
                        3 + 5*N.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  The algorithm failed to compute an eigenvalue while
                working on the submatrix lying in rows and columns
                INFO/(N+1) through mod(INFO,N+1).
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
<dd> September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Jeff Rutter, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 172 of file slaed0.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
