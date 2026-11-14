---
title: "dgeql2-f(3)"
name: "dgeql2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgeql2-f/"
description: "dgeql2.f –"
---

<p>dgeql2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgeql2</code> (M, N, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>DGEQL2</code> computes the QL factorization of a general rectangular matrix using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgeql2 (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DGEQL2</code> computes the QL factorization of a general rectangular matrix using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGEQL2 computes a QL factorization of a real m by n matrix A:
 A = Q * L.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the m by n matrix A.
 On exit, if m &gt;= n, the lower triangle of the subarray
 A(m-n+1:m,1:n) contains the n by n lower triangular matrix L;
 if m &lt;= n, the elements on and below the (n-m)-th
 superdiagonal contain the m by n lower trapezoidal matrix L;
 the remaining elements, with the array TAU, represent the
 orthogonal matrix Q as a product of elementary reflectors
 (see Further Details).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension (min(M,N))
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> The matrix Q is represented as a product of elementary reflectors
 Q = H(k) . . . H(2) H(1), where k = min(m,n).
 Each H(i) has the form
 H(i) = I - tau * v * v**T
 where tau is a real scalar, and v is a real vector with
 v(m-k+i+1:m) = 0 and v(m-k+i) = 1; v(1:m-k+i-1) is stored on exit in
 A(1:m-k+i-1,n-k+i), and tau in TAU(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 124 of file dgeql2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
