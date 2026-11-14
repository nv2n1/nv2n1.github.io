---
title: "dtptrs(3)"
name: "dtptrs"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtptrs/"
description: "dtptrs.f –"
---

<h2 class="name">NAME</h2>
<p> dtptrs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtptrs</code> (UPLO, TRANS, DIAG, N, NRHS, AP, B, LDB, INFO)<br />
 <i></i><code>DTPTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtptrs (characterUPLO, characterTRANS, characterDIAG, integerN, integerNRHS, double precision, dimension( * )AP, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code>DTPTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTPTRS solves a triangular system of the form
    A * X = B  or  A**T * X = B,
 where A is a triangular matrix of order N stored in packed format,
 and B is an N-by-NRHS matrix.  A check is made to verify that A is
 nonsingular.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  A is upper triangular;
          = 'L':  A is lower triangular.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations:
          = 'N':  A * X = B  (No transpose)
          = 'T':  A**T * X = B  (Transpose)
          = 'C':  A**H * X = B  (Conjugate transpose = Transpose)
</pre>
<p> <i>DIAG</i> </p>
<pre>
          DIAG is CHARACTER*1
          = 'N':  A is non-unit triangular;
          = 'U':  A is unit triangular.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is DOUBLE PRECISION array, dimension (N*(N+1)/2)
          The upper or lower triangular matrix A, packed columnwise in
          a linear array.  The j-th column of A is stored in the array
          AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
</code></pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          On entry, the right hand side matrix B.
          On exit, if INFO = 0, the solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the i-th diagonal element of A is zero,
                indicating that the matrix is singular and the
                solutions X have not been computed.
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
<p> Definition at line 131 of file dtptrs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
