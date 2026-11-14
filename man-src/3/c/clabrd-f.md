---
title: "clabrd-f(3)"
name: "clabrd-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clabrd-f/"
description: "clabrd.f –"
---

<p>clabrd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clabrd</code> (M, N, NB, A, LDA, D, E, TAUQ, TAUP, X, LDX, Y, LDY)<br />
 <i></i><code>CLABRD</code> reduces the first nb rows and columns of a general matrix to a bidiagonal form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clabrd (integerM, integerN, integerNB, complex, dimension( lda, * )A, integerLDA, real, dimension( * )D, real, dimension( * )E, complex, dimension( * )TAUQ, complex, dimension( * )TAUP, complex, dimension( ldx, * )X, integerLDX, complex, dimension( ldy, * )Y, integerLDY)</h3>
<p><code>CLABRD</code> reduces the first nb rows and columns of a general matrix to a bidiagonal form. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLABRD reduces the first NB rows and columns of a complex general
 m by n matrix A to upper or lower real bidiagonal form by a unitary
 transformation Q**H * A * P, and returns the matrices X and Y which
 are needed to apply the transformation to the unreduced part of A.
 If m &gt;= n, A is reduced to upper bidiagonal form; if m &lt; n, to lower
 bidiagonal form.
 This is an auxiliary routine called by CGEBRD</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows in the matrix A.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns in the matrix A.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The number of leading rows and columns of A to be reduced.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the m by n general matrix to be reduced.
 On exit, the first NB rows and columns of the matrix are
 overwritten; the rest of the array is unchanged.
 If m &gt;= n, elements on and below the diagonal in the first NB
 columns, with the array TAUQ, represent the unitary
 matrix Q as a product of elementary reflectors; and
 elements above the diagonal in the first NB rows, with the
 array TAUP, represent the unitary matrix P as a product
 of elementary reflectors.
 If m &lt; n, elements below the diagonal in the first NB
 columns, with the array TAUQ, represent the unitary
 matrix Q as a product of elementary reflectors, and
 elements on and above the diagonal in the first NB rows,
 with the array TAUP, represent the unitary matrix P as
 a product of elementary reflectors.
 See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (NB)
 The diagonal elements of the first NB rows and columns of
 the reduced matrix. D(i) = A(i,i).</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (NB)
 The off-diagonal elements of the first NB rows and columns of
 the reduced matrix.</pre>
<p><i>TAUQ</i> </p>
<pre> TAUQ is COMPLEX array dimension (NB)
 The scalar factors of the elementary reflectors which
 represent the unitary matrix Q. See Further Details.</pre>
<p><i>TAUP</i> </p>
<pre> TAUP is COMPLEX array, dimension (NB)
 The scalar factors of the elementary reflectors which
 represent the unitary matrix P. See Further Details.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension (LDX,NB)
 The m-by-nb matrix X required to update the unreduced part
 of A.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,M).</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX array, dimension (LDY,NB)
 The n-by-nb matrix Y required to update the unreduced part
 of A.</pre>
<p><i>LDY</i> </p>
<pre> LDY is INTEGER
 The leading dimension of the array Y. LDY &gt;= max(1,N).</pre>
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
<pre> The matrices Q and P are represented as products of elementary
 reflectors:
 Q = H(1) H(2) . . . H(nb) and P = <a href="//www.systutorials.com/docs/linux/man/1-G/">G</a>(1) <a href="//www.systutorials.com/docs/linux/man/2-G/">G</a>(2) . . . G(nb)
 Each H(i) and G(i) has the form:
 H(i) = I - tauq * v * v**H and G(i) = I - taup * u * u**H
 where tauq and taup are complex scalars, and v and u are complex
 vectors.
 If m &gt;= n, v(1:i-1) = 0, v(i) = 1, and v(i:m) is stored on exit in
 A(i:m,i); u(1:i) = 0, u(i+1) = 1, and u(i+1:n) is stored on exit in
 A(i,i+1:n); tauq is stored in TAUQ(i) and taup in TAUP(i).
 If m &lt; n, v(1:i) = 0, v(i+1) = 1, and v(i+1:m) is stored on exit in
 A(i+2:m,i); u(1:i-1) = 0, u(i) = 1, and u(i:n) is stored on exit in
 A(i,i+1:n); tauq is stored in TAUQ(i) and taup in TAUP(i).
 The elements of the vectors v and u together form the m-by-nb matrix
 V and the nb-by-n matrix U**H which are needed, with X and Y, to apply
 the transformation to the unreduced part of the matrix, using a block
 update of the form: A := A - V*Y**H - X*U**H.
 The contents of A on exit are illustrated by the following examples
 with nb = 2:
 m = 6 and n = 5 (m &gt; n): m = 5 and n = 6 (m &lt; n):
 ( 1 1 u1 u1 u1 ) ( 1 u1 u1 u1 u1 u1 )
 ( v1 1 1 u2 u2 ) ( 1 1 u2 u2 u2 u2 )
 ( v1 v2 a a a ) ( v1 1 a a a a )
 ( v1 v2 a a a ) ( v1 v2 a a a a )
 ( v1 v2 a a a ) ( v1 v2 a a a a )
 ( v1 v2 a a a )
 where a denotes an element of the original matrix which is unchanged,
 vi denotes an element of the vector defining H(i), and ui an element
 of the vector defining G(i).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 212 of file clabrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
