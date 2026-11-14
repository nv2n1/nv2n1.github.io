---
title: "cgesv(3)"
name: "cgesv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgesv/"
description: "cgesv.f –"
---

<h2 class="name">NAME</h2>
<p> cgesv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgesv</code> (N, NRHS, A, LDA, IPIV, B, LDB, INFO)<br />
 <i></i><code> CGESV computes the solution to system of linear equations A * X = B for GE matrices</code> (simple driver)</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgesv (integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code> CGESV computes the solution to system of linear equations A * X = B for GE matrices</code> (simple driver) </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGESV computes the solution to a complex system of linear equations
    A * X = B,
 where A is an N-by-N matrix and X and B are N-by-NRHS matrices.
 The LU decomposition with partial pivoting and row interchanges is
 used to factor A as
    A = P * L * U,
 where P is a permutation matrix, L is unit lower triangular, and U is
 upper triangular.  The factored form of A is then used to solve the
 system of equations A * X = B.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of linear equations, i.e., the order of the
          matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the N-by-N coefficient matrix A.
          On exit, the factors L and U from the factorization
          A = P*L*U; the unit diagonal elements of L are not stored.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          The pivot indices that define the permutation matrix P;
          row i of the matrix was interchanged with row IPIV(i).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
          On entry, the N-by-NRHS matrix of right hand side matrix B.
          On exit, if INFO = 0, the N-by-NRHS solution matrix X.
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
          &gt; 0:  if INFO = i, U(i,i) is exactly zero.  The factorization
                has been completed, but the factor U is exactly
                singular, so the solution could not be computed.
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
<p> Definition at line 123 of file cgesv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
