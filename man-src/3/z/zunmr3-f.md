---
title: "zunmr3-f(3)"
name: "zunmr3-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zunmr3-f/"
description: "zunmr3.f –"
---

<p>zunmr3.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zunmr3</code> (SIDE, TRANS, M, N, K, L, A, LDA, TAU, C, LDC, WORK, INFO)<br />
 <i></i><code>ZUNMR3</code> multiplies a general matrix by the unitary matrix from a RZ factorization determined by ctzrzf (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zunmr3 (characterSIDE, characterTRANS, integerM, integerN, integerK, integerL, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )TAU, complex*16, dimension( ldc, * )C, integerLDC, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZUNMR3</code> multiplies a general matrix by the unitary matrix from a RZ factorization determined by ctzrzf (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZUNMR3 overwrites the general complex m by n matrix C with
 Q * C if SIDE = 'L' and TRANS = 'N', or
 Q**H* C if SIDE = 'L' and TRANS = 'C', or
 C * Q if SIDE = 'R' and TRANS = 'N', or
 C * Q**H if SIDE = 'R' and TRANS = 'C',
 where Q is a complex unitary matrix defined as the product of k
 elementary reflectors
 Q = H(1) H(2) . . . H(k)
 as returned by ZTZRZF. Q is of order m if SIDE = 'L' and of order n
 if SIDE = 'R'.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': apply Q or Q**H from the Left
 = 'R': apply Q or Q**H from the Right</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 = 'N': apply Q (No transpose)
 = 'C': apply Q**H (Conjugate transpose)</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix C. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix C. N &gt;= 0.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The number of elementary reflectors whose product defines
 the matrix Q.
 If SIDE = 'L', M &gt;= K &gt;= 0;
 if SIDE = 'R', N &gt;= K &gt;= 0.</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 The number of columns of the matrix A containing
 the meaningful part of the Householder reflectors.
 If SIDE = 'L', M &gt;= L &gt;= 0, if SIDE = 'R', N &gt;= L &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension
 (LDA,M) if SIDE = 'L',
 (LDA,N) if SIDE = 'R'
 The i-th row must contain the vector which defines the
 elementary reflector H(i), for i = 1,2,...,k, as returned by
 ZTZRZF in the last k rows of its array argument A.
 A is modified by the routine but restored on exit.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,K).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by ZTZRZF.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16 array, dimension (LDC,N)
 On entry, the m-by-n matrix C.
 On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension
 (N) if SIDE = 'L',
 (M) if SIDE = 'R'</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>&nbsp;<wbr></dl>
<p> Definition at line 178 of file zunmr3.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
