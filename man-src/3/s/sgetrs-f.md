---
title: "sgetrs-f(3)"
name: "sgetrs-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgetrs-f/"
description: "sgetrs.f –"
---

<p>sgetrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgetrs</code> (TRANS, N, NRHS, A, LDA, IPIV, B, LDB, INFO)<br />
 <i></i><code>SGETRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgetrs (characterTRANS, integerN, integerNRHS, real, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code>SGETRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 SGETRS solves a system of linear equations
    A * X = B  or  A**T * X = B
 with a general N-by-N matrix A using the LU factorization computed
 by SGETRF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations:
          = 'N':  A * X = B  (No transpose)
          = 'T':  A**T* X = B  (Transpose)
          = 'C':  A**T* X = B  (Conjugate transpose = Transpose)
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
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          The factors L and U from the factorization A = P*L*U
          as computed by SGETRF.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          The pivot indices from SGETRF; for 1&lt;=i&lt;=N, row i of the
          matrix was interchanged with row IPIV(i).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
          On entry, the right hand side matrix B.
          On exit, the solution matrix X.
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
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> November 2011</dl>
<p> Definition at line 122 of file sgetrs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
