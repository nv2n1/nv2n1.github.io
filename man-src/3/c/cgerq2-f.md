---
title: "cgerq2-f(3)"
name: "cgerq2-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgerq2-f/"
description: "cgerq2.f –"
---

<p>cgerq2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgerq2</code> (M, N, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>CGERQ2</code> computes the RQ factorization of a general rectangular matrix using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgerq2 (integerM, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )TAU, complex, dimension( * )WORK, integerINFO)</h3>
<p><code>CGERQ2</code> computes the RQ factorization of a general rectangular matrix using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGERQ2 computes an RQ factorization of a complex m by n matrix A:
 A = R * Q.</pre>
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
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the m by n matrix A.
 On exit, if m &lt;= n, the upper triangle of the subarray
 A(1:m,n-m+1:n) contains the m by m upper triangular matrix R;
 if m &gt;= n, the elements on and above the (m-n)-th subdiagonal
 contain the m by n upper trapezoidal matrix R; the remaining
 elements, with the array TAU, represent the unitary matrix
 Q as a product of elementary reflectors (see Further
 Details).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX array, dimension (min(M,N))
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (M)</pre>
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
 Q = H(1)**H H(2)**H . . . H(k)**H, where k = min(m,n).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(n-k+i+1:n) = 0 and v(n-k+i) = 1; conjg(v(1:n-k+i-1)) is stored on
 exit in A(m-k+i,1:n-k+i-1), and tau in TAU(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 124 of file cgerq2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
