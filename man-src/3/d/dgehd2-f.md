---
title: "dgehd2-f(3)"
name: "dgehd2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgehd2-f/"
description: "dgehd2.f –"
---

<p>dgehd2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgehd2</code> (N, ILO, IHI, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>DGEHD2</code> reduces a general square matrix to upper Hessenberg form using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgehd2 (integerN, integerILO, integerIHI, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DGEHD2</code> reduces a general square matrix to upper Hessenberg form using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGEHD2 reduces a real general matrix A to upper Hessenberg form H by
 an orthogonal similarity transformation: Q**T * A * Q = H .</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 It is assumed that A is already upper triangular in rows
 and columns 1:ILO-1 and IHI+1:N. ILO and IHI are normally
 set by a previous call to DGEBAL; otherwise they should be
 set to 1 and N respectively. See Further Details.
 1 &lt;= ILO &lt;= IHI &lt;= max(1,N).</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the n by n general matrix to be reduced.
 On exit, the upper triangle and the first subdiagonal of A
 are overwritten with the upper Hessenberg matrix H, and the
 elements below the first subdiagonal, with the array TAU,
 represent the orthogonal matrix Q as a product of elementary
 reflectors. See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension (N-1)
 The scalar factors of the elementary reflectors (see Further
 Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
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
<pre> The matrix Q is represented as a product of (ihi-ilo) elementary
 reflectors
 Q = H(ilo) H(ilo+1) . . . H(ihi-1).
 Each H(i) has the form
 H(i) = I - tau * v * v**T
 where tau is a real scalar, and v is a real vector with
 v(1:i) = 0, v(i+1) = 1 and v(ihi+1:n) = 0; v(i+2:ihi) is stored on
 exit in A(i+2:ihi,i), and tau in TAU(i).
 The contents of A are illustrated by the following example, with
 n = 7, ilo = 2 and ihi = 6:
 on entry, on exit,
 ( a a a a a a a ) ( a a h h h h a )
 ( a a a a a a ) ( a h h h h a )
 ( a a a a a a ) ( h h h h h h )
 ( a a a a a a ) ( v2 h h h h h )
 ( a a a a a a ) ( v2 v3 h h h h )
 ( a a a a a a ) ( v2 v3 v4 h h h )
 ( a ) ( a )
 where a denotes an element of the original matrix A, h denotes a
 modified element of the upper Hessenberg matrix H, and vi denotes an
 element of the vector defining H(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 150 of file dgehd2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
