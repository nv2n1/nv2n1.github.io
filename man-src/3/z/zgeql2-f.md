---
title: "zgeql2-f(3)"
name: "zgeql2-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgeql2-f/"
description: "zgeql2.f –"
---

<p>zgeql2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgeql2</code> (M, N, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>ZGEQL2</code> computes the QL factorization of a general rectangular matrix using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgeql2 (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZGEQL2</code> computes the QL factorization of a general rectangular matrix using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGEQL2 computes a QL factorization of a complex m by n matrix A:
 A = Q * L.</pre>
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
 On exit, if m &gt;= n, the lower triangle of the subarray
 A(m-n+1:m,1:n) contains the n by n lower triangular matrix L;
 if m &lt;= n, the elements on and below the (n-m)-th
 superdiagonal contain the m by n lower trapezoidal matrix L;
 the remaining elements, with the array TAU, represent the
 unitary matrix Q as a product of elementary reflectors
 (see Further Details).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (min(M,N))
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N)</pre>
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
 Q = H(k) . . . H(2) H(1), where k = min(m,n).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(m-k+i+1:m) = 0 and v(m-k+i) = 1; v(1:m-k+i-1) is stored on exit in
 A(1:m-k+i-1,n-k+i), and tau in TAU(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 124 of file zgeql2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
