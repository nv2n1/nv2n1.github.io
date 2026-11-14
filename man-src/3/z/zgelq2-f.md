---
title: "zgelq2-f(3)"
name: "zgelq2-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgelq2-f/"
description: "zgelq2.f –"
---

<p>zgelq2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgelq2</code> (M, N, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>ZGELQ2</code> computes the LQ factorization of a general rectangular matrix using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgelq2 (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZGELQ2</code> computes the LQ factorization of a general rectangular matrix using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGELQ2 computes an LQ factorization of a complex m by n matrix A:
 A = L * Q.</pre>
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
 On entry, the m by n matrix A.
 On exit, the elements on and below the diagonal of the array
 contain the m by min(m,n) lower trapezoidal matrix L (L is
 lower triangular if m &lt;= n); the elements above the diagonal,
 with the array TAU, represent the unitary matrix Q as a
 product of elementary reflectors (see Further Details).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (min(M,N))
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (M)</pre>
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
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The matrix Q is represented as a product of elementary reflectors
 Q = H(k)**H . . . H(2)**H H(1)**H, where k = min(m,n).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(1:i-1) = 0 and v(i) = 1; conjg(v(i+1:n)) is stored on exit in
 A(i,i+1:n), and tau in TAU(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 122 of file zgelq2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
