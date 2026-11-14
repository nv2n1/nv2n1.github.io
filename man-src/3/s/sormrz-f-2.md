---
title: "sormrz-f-2(3)"
name: "sormrz-f-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sormrz-f-2/"
description: "sormrz.f –"
---

<p>sormrz.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sormrz</code> (SIDE, TRANS, M, N, K, L, A, LDA, TAU, C, LDC, WORK, LWORK, INFO)<br />
 <i></i><code>SORMRZ</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sormrz (characterSIDE, characterTRANS, integerM, integerN, integerK, integerL, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( ldc, * )C, integerLDC, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SORMRZ</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SORMRZ overwrites the general real M-by-N matrix C with
 SIDE = 'L' SIDE = 'R'
 TRANS = 'N': Q * C C * Q
 TRANS = 'T': Q**T * C C * Q**T
 where Q is a real orthogonal matrix defined as the product of k
 elementary reflectors
 Q = H(1) H(2) . . . H(k)
 as returned by STZRZF. Q is of order M if SIDE = 'L' and of order N
 if SIDE = 'R'.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': apply Q or Q**T from the Left;
 = 'R': apply Q or Q**T from the Right.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 = 'N': No transpose, apply Q;
 = 'T': Transpose, apply Q**T.</pre>
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
<pre> A is REAL array, dimension
 (LDA,M) if SIDE = 'L',
 (LDA,N) if SIDE = 'R'
 The i-th row must contain the vector which defines the
 elementary reflector H(i), for i = 1,2,...,k, as returned by
 STZRZF in the last k rows of its array argument A.
 A is modified by the routine but restored on exit.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,K).</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by STZRZF.</pre>
<p><i>C</i> </p>
<pre> C is REAL array, dimension (LDC,N)
 On entry, the M-by-N matrix C.
 On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If SIDE = 'L', LWORK &gt;= max(1,N);
 if SIDE = 'R', LWORK &gt;= max(1,M).
 For optimum performance LWORK &gt;= N*NB if SIDE = 'L', and
 LWORK &gt;= M*NB if SIDE = 'R', where NB is the optimal
 blocksize.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
<dd>November 2011</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>&nbsp;<wbr></dl>
<p> Definition at line 189 of file sormrz.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
