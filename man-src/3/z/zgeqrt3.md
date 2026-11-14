---
title: "zgeqrt3(3)"
name: "zgeqrt3"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgeqrt3/"
description: "zgeqrt3.f –"
---

<p>zgeqrt3.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>recursive subroutine <code>zgeqrt3</code> (M, N, A, LDA, T, LDT, INFO)<br />
 <i></i><code>ZGEQRT3</code> recursively computes a QR factorization of a general real or complex matrix using the compact WY representation of Q.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>recursive subroutine zgeqrt3 (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldt, * )T, integerLDT, integerINFO)</h3>
<p><code>ZGEQRT3</code> recursively computes a QR factorization of a general real or complex matrix using the compact WY representation of Q. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGEQRT3 recursively computes a QR factorization of a complex M-by-N 
 matrix A, using the compact WY representation of Q. 
 Based on the algorithm of Elmroth and Gustavson, 
 IBM J. Res. Develop. Vol 44 No. 4 July 2000.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= N.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the complex M-by-N matrix A. On exit, the elements on 
 and above the diagonal contain the N-by-N upper triangular matrix R;
 the elements below the diagonal are the columns of V. See below for
 further details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>T</i> </p>
<pre> T is COMPLEX*16 array, dimension (LDT,N)
 The N-by-N upper triangular factor of the block reflector.
 The elements on and above the diagonal contain the block
 reflector T; the elements below the diagonal are not used.
 See below for further details.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= max(1,N).</pre>
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
<pre> The matrix V stores the elementary reflectors H(i) in the i-th column
 below the diagonal. For example, if M=5 and N=3, the matrix V is
 V = ( 1 )
 ( v1 1 )
 ( v1 v2 1 )
 ( v1 v2 v3 )
 ( v1 v2 v3 )
 where the vi's represent the vectors which define H(i), which are returned
 in the matrix A. The 1's along the diagonal of V are not stored in A. The
 block reflector H is then given by
 H = I - V * T * V**H
 where V**H is the conjugate transpose of V.
 For details of the algorithm, see Elmroth and Gustavson (cited above).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 133 of file zgeqrt3.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
