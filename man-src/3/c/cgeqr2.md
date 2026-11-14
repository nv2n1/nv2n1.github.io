---
title: "cgeqr2(3)"
name: "cgeqr2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgeqr2/"
description: "cgeqr2.f –"
---

<h2 class="name">NAME</h2>
<p> cgeqr2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgeqr2</code> (M, N, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>CGEQR2</code> computes the QR factorization of a general rectangular matrix using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgeqr2 (integerM, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )TAU, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CGEQR2</code> computes the QR factorization of a general rectangular matrix using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGEQR2 computes a QR factorization of a complex m by n matrix A:
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
          A is COMPLEX array, dimension (LDA,N)
          On entry, the m by n matrix A.
          On exit, the elements on and above the diagonal of the array
          contain the min(m,n) by n upper trapezoidal matrix R (R is
          upper triangular if m &gt;= n); the elements below the diagonal,
          with the array TAU, represent the unitary matrix Q as a
          product of elementary reflectors (see Further Details).
</pre>
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
          WORK is COMPLEX array, dimension (N)
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
     H(i) = I - tau * v * v**H
  where tau is a complex scalar, and v is a complex vector with
  v(1:i-1) = 0 and v(i) = 1; v(i+1:m) is stored on exit in A(i+1:m,i),
  and tau in TAU(i).
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 122 of file cgeqr2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
