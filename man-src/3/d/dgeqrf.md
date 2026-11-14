---
title: "dgeqrf(3)"
name: "dgeqrf"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgeqrf/"
description: "dgeqrf.f –"
---

<h2 class="name">NAME</h2>
<p> dgeqrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgeqrf</code> (M, N, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>DGEQRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgeqrf (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DGEQRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGEQRF computes a QR factorization of a real M-by-N matrix A:
 A = Q * R.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit, the elements on and above the diagonal of the array
          contain the min(M,N)-by-N upper trapezoidal matrix R (R is
          upper triangular if m &gt;= n); the elements below the diagonal,
          with the array TAU, represent the orthogonal matrix Q as a
          product of min(m,n) elementary reflectors (see Further
          Details).
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (min(M,N))
          The scalar factors of the elementary reflectors (see Further
          Details).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,N).
          For optimum performance LWORK &gt;= N*NB, where NB is
          the optimal blocksize.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The matrix Q is represented as a product of elementary reflectors
     Q = H(1) H(2) . . . H(k), where k = min(m,n).
  Each H(i) has the form
     H(i) = I - tau * v * v**T
  where tau is a real scalar, and v is a real vector with
  v(1:i-1) = 0 and v(i) = 1; v(i+1:m) is stored on exit in A(i+1:m,i),
  and tau in TAU(i).
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 137 of file dgeqrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
