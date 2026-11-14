---
title: "sormtr-f(3)"
name: "sormtr-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sormtr-f/"
description: "sormtr.f –"
---

<p>sormtr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sormtr</code> (SIDE, UPLO, TRANS, M, N, A, LDA, TAU, C, LDC, WORK, LWORK, INFO)<br />
 <i></i><code>SORMTR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sormtr (characterSIDE, characterUPLO, characterTRANS, integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( ldc, * )C, integerLDC, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SORMTR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SORMTR overwrites the general real M-by-N matrix C with
 SIDE = 'L' SIDE = 'R'
 TRANS = 'N': Q * C C * Q
 TRANS = 'T': Q**T * C C * Q**T
 where Q is a real orthogonal matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 nq-1 elementary reflectors, as returned by SSYTRD:
 if UPLO = 'U', Q = H(nq-1) . . . H(2) H(1);
 if UPLO = 'L', Q = H(1) H(2) . . . H(nq-1).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': apply Q or Q**T from the Left;
 = 'R': apply Q or Q**T from the Right.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A contains elementary reflectors
 from SSYTRD;
 = 'L': Lower triangle of A contains elementary reflectors
 from SSYTRD.</pre>
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
<p><i>A</i> </p>
<pre> A is REAL array, dimension
 (LDA,M) if SIDE = 'L'
 (LDA,N) if SIDE = 'R'
 The vectors which define the elementary reflectors, as
 returned by SSYTRD.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A.
 LDA &gt;= max(1,M) if SIDE = 'L'; LDA &gt;= max(1,N) if SIDE = 'R'.</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension
 (M-1) if SIDE = 'L'
 (N-1) if SIDE = 'R'
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by SSYTRD.</pre>
<p><i>C</i> </p>
<pre> C is REAL array, dimension (LDC,N)
 On entry, the M-by-N matrix C.
 On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.</pre>
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
<p> Definition at line 172 of file sormtr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
