---
title: "sgerq2(3)"
name: "sgerq2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgerq2/"
description: "sgerq2.f –"
---

<h2 class="name">NAME</h2>
<p> sgerq2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgerq2</code> (M, N, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>SGERQ2</code> computes the RQ factorization of a general rectangular matrix using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgerq2 (integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SGERQ2</code> computes the RQ factorization of a general rectangular matrix using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SGERQ2 computes an RQ factorization of a real m by n matrix A:
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
A is REAL array, dimension(LDA, N) On entry, the m by n matrix A.On exit, if m &lt;= n, the upper triangle of the subarray A(1
                                                                                                                          : m, n - m + 1
                                                                                                                          : n) contains the m by m upper triangular matrix R;
if m
    &gt;= n, the elements on and above the(m - n) - th subdiagonal
              contain the m by n upper trapezoidal matrix R;
the remaining
    elements,
    with the array TAU, represent the orthogonal matrix Q as a product of elementary reflectors(see Further Details).
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is REAL array, dimension (min(M,N))
          The scalar factors of the elementary reflectors (see Further
          Details).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (M)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
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
  v(n-k+i+1:n) = 0 and v(n-k+i) = 1; v(1:n-k+i-1) is stored on exit in
  A(m-k+i,1:n-k+i-1), and tau in TAU(i).
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 124 of file sgerq2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
