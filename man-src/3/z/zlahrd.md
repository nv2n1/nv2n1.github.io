---
title: "zlahrd(3)"
name: "zlahrd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlahrd/"
description: "zlahrd.f –"
---

<p>zlahrd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlahrd</code> (N, K, NB, A, LDA, TAU, T, LDT, Y, LDY)<br />
 <i></i><code>ZLAHRD</code> reduces the first nb columns of a general rectangular matrix A so that elements below the k-th subdiagonal are zero, and returns auxiliary matrices which are needed to apply the transformation to the unreduced part of A.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlahrd (integerN, integerK, integerNB, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( nb )TAU, complex*16, dimension( ldt, nb )T, integerLDT, complex*16, dimension( ldy, nb )Y, integerLDY)</h3>
<p><code>ZLAHRD</code> reduces the first nb columns of a general rectangular matrix A so that elements below the k-th subdiagonal are zero, and returns auxiliary matrices which are needed to apply the transformation to the unreduced part of A. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAHRD reduces the first NB columns of a complex general n-by-(n-k+1)
 matrix A so that elements below the k-th subdiagonal are zero. The
 reduction is performed by a unitary similarity transformation
 Q**H * A * Q. The routine returns the matrices V and T which determine
 Q as a block reflector I - V*T*V**H, and also the matrix Y = A * V * T.
 This is an OBSOLETE auxiliary routine. 
 This routine will be 'deprecated' in a future release.
 Please use the new routine ZLAHR2 instead.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The offset for the reduction. Elements below the k-th
 subdiagonal in the first NB columns are reduced to zero.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The number of columns to be reduced.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N-K+1)
 On entry, the n-by-(n-k+1) general matrix A.
 On exit, the elements on and above the k-th subdiagonal in
 the first NB columns are overwritten with the corresponding
 elements of the reduced matrix; the elements below the k-th
 subdiagonal, with the array TAU, represent the matrix Q as a
 product of elementary reflectors. The other columns of A are
 unchanged. See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (NB)
 The scalar factors of the elementary reflectors. See Further
 Details.</pre>
<p><i>T</i> </p>
<pre> T is COMPLEX*16 array, dimension (LDT,NB)
 The upper triangular matrix T.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= NB.</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16 array, dimension (LDY,NB)
 The n-by-nb matrix Y.</pre>
<p><i>LDY</i> </p>
<pre> LDY is INTEGER
 The leading dimension of the array Y. LDY &gt;= max(1,N).</pre>
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
<pre> The matrix Q is represented as a product of nb elementary reflectors
 Q = H(1) H(2) . . . H(nb).
 Each H(i) has the form
 H(i) = I - tau * v * v**H
 where tau is a complex scalar, and v is a complex vector with
 v(1:i+k-1) = 0, v(i+k) = 1; v(i+k+1:n) is stored on exit in
 A(i+k+1:n,i), and tau in TAU(i).
 The elements of the vectors v together form the (n-k+1)-by-nb matrix
 V which is needed, with T and Y, to apply the transformation to the
 unreduced part of the matrix, using an update of the form:
 A := (I - V*T*V**H) * (A - Y*V**H).
 The contents of A on exit are illustrated by the following example
 with n = 7, k = 3 and nb = 2:
 ( a h a a a )
 ( a h a a a )
 ( a h a a a )
 ( h h a a a )
 ( v1 h a a a )
 ( v1 v2 a a a )
 ( v1 v2 a a a )
 where a denotes an element of the original matrix A, h denotes a
 modified element of the upper Hessenberg matrix H, and vi denotes an
 element of the vector defining H(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 170 of file zlahrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
