---
title: "zgeqp3(3)"
name: "zgeqp3"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgeqp3/"
description: "zgeqp3.f –"
---

<p>zgeqp3.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgeqp3</code> (M, N, A, LDA, JPVT, TAU, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code>ZGEQP3</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgeqp3 (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )JPVT, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZGEQP3</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGEQP3 computes a QR factorization with column pivoting of a
 matrix A: A*P = Q*R using Level 3 BLAS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, the upper triangle of the array contains the
 min(M,N)-by-N upper trapezoidal matrix R; the elements below
 the diagonal, together with the array TAU, represent the
 unitary matrix Q as a product of min(M,N) elementary
 reflectors.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>JPVT</i> </p>
<pre> JPVT is INTEGER array, dimension (N)
 On entry, if JPVT(J).ne.0, the J-th column of A is permuted
 to the front of A*P (a leading column); if JPVT(J)=0,
 the J-th column of A is a free column.
 On exit, if JPVT(J)=K, then the J-th column of A*P was the
 the K-th column of A.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (min(M,N))
 The scalar factors of the elementary reflectors.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO=0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= N+1.
 For optimal performance LWORK &gt;= ( N+1 )*NB, where NB
 is the optimal blocksize.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The matrix Q is represented as a product of elementary reflectors
 Q = H(1) H(2) . . . H(k), where k = min(m,n).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a real/complex vector
 with v(1:i-1) = 0 and v(i) = 1; v(i+1:m) is stored on exit in
 A(i+1:m,i), and tau in TAU(i).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>G. Quintana-Orti, Depto. de Informatica, Universidad Jaime I, Spain X. Sun, Computer Science Dept., Duke University, USA</dl>
<p> Definition at line 159 of file zgeqp3.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
