---
title: "cgetri(3)"
name: "cgetri"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgetri/"
description: "cgetri.f –"
---

<h2 class="name">NAME</h2>
<p> cgetri.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgetri</code> (N, A, LDA, IPIV, WORK, LWORK, INFO)<br />
 <i></i><code>CGETRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgetri (integerN, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>CGETRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGETRI computes the inverse of a matrix using the LU factorization
 computed by CGETRF.
 This method inverts U and then computes inv(A) by solving the system
 inv(A)*L = inv(U) for inv(A).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the factors L and U from the factorization
          A = P*L*U as computed by CGETRF.
          On exit, if INFO = 0, the inverse of the original matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre><code>
IPIV is INTEGER array, dimension(N)
                           The pivot indices from CGETRF; for
1 &lt;= i &lt;= N, row i of the
                 matrix was interchanged with row
                 IPIV(i)
                     .
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO=0, then WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,N).
          For optimal performance LWORK &gt;= N*NB, where NB is
          the optimal blocksize returned by ILAENV.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : if INFO = i, U(i, i) is exactly zero;
the matrix is
    singular and its inverse could not be computed.
</code></pre>
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
<p> Definition at line 115 of file cgetri.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
