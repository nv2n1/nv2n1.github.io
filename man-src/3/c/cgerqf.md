---
title: "cgerqf(3)"
name: "cgerqf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgerqf/"
description: "cgerqf.f –"
---

<h2 class="name">NAME</h2>
<p> cgerqf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgerqf</code> (M, N, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>CGERQF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgerqf (integerM, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )TAU, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>CGERQF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGERQF computes an RQ factorization of a complex M-by-N matrix A:
 A = R * Q.
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
<pre><code>
A is COMPLEX array, dimension(LDA, N) On entry, the M - by - N matrix A.On exit,
    if m &lt;= n, the upper triangle of the subarray A(1
                                                    : m, n - m + 1
                                                    : n) contains the M
                   - by - M upper triangular matrix R;
if m
    &gt;= n, the elements on and above the(m - n) - th subdiagonal contain the M - by - N upper trapezoidal matrix R;
the remaining elements, with the array TAU, represent the unitary matrix Q as a product of min(m, n)
elementary
reflectors(see Further Details)
    .
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX array, dimension (min(M,N))
          The scalar factors of the elementary reflectors (see Further
          Details).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,M).
          For optimum performance LWORK &gt;= M*NB, where NB is
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
     Q = H(1)**H H(2)**H . . . H(k)**H, where k = min(m,n).
  Each H(i) has the form
     H(i) = I - tau * v * v**H
  where tau is a complex scalar, and v is a complex vector with
  v(n-k+i+1:n) = 0 and v(n-k+i) = 1; conjg(v(1:n-k+i-1)) is stored on
  exit in A(m-k+i,1:n-k+i-1), and tau in TAU(i).
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 139 of file cgerqf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
