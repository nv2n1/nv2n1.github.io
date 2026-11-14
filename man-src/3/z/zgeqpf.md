---
title: "zgeqpf(3)"
name: "zgeqpf"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgeqpf/"
description: "zgeqpf.f –"
---

<p>zgeqpf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgeqpf</code> (M, N, A, LDA, JPVT, TAU, WORK, RWORK, INFO)<br />
 <i></i><code>ZGEQPF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgeqpf (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )JPVT, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZGEQPF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This routine is deprecated and has been replaced by routine ZGEQP3.
 ZGEQPF computes a QR factorization with column pivoting of a
 complex M-by-N matrix A: A*P = Q*R.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, the upper triangle of the array contains the
 min(M,N)-by-N upper triangular matrix R; the elements
 below the diagonal, together with the array TAU,
 represent the unitary matrix Q as a product of
 min(m,n) elementary reflectors.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>JPVT</i> </p>
<pre> JPVT is INTEGER array, dimension (N)
 On entry, if JPVT(i) .ne. 0, the i-th column of A is permuted
 to the front of A*P (a leading column); if JPVT(i) = 0,
 the i-th column of A is a free column.
 On exit, if JPVT(i) = k, then the i-th column of A*P
 was the k-th column of A.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (min(M,N))
 The scalar factors of the elementary reflectors.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The matrix Q is represented as a product of elementary reflectors
 Q = H(1) H(2) . . . <a href="//www.systutorials.com/docs/linux/man/n-H/">H</a>(n)
 Each H(i) has the form
 H = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(1:i-1) = 0 and v(i) = 1; v(i+1:m) is stored on exit in A(i+1:m,i).
 The matrix P is represented in jpvt as follows: If
 jpvt(j) = i
 then the jth column of P is the ith canonical unit vector.
 Partial column norm updating strategy modified by
 Z. Drmac and Z. Bujanovic, Dept. of Mathematics,
 University of Zagreb, Croatia.
 -- April 2011 --
 For more details see LAPACK Working Note 176.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 149 of file zgeqpf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
