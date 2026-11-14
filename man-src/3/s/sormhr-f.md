---
title: "sormhr-f(3)"
name: "sormhr-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sormhr-f/"
description: "sormhr.f –"
---

<p>sormhr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sormhr</code> (SIDE, TRANS, M, N, ILO, IHI, A, LDA, TAU, C, LDC, WORK, LWORK, INFO)<br />
 <i></i><code>SORMHR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sormhr (characterSIDE, characterTRANS, integerM, integerN, integerILO, integerIHI, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( ldc, * )C, integerLDC, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SORMHR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SORMHR overwrites the general real M-by-N matrix C with
 SIDE = 'L' SIDE = 'R'
 TRANS = 'N': Q * C C * Q
 TRANS = 'T': Q**T * C C * Q**T
 where Q is a real orthogonal matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 IHI-ILO elementary reflectors, as returned by SGEHRD:
 Q = H(ilo) H(ilo+1) . . . H(ihi-1).</pre>
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
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI must have the same values as in the previous call
 of SGEHRD. Q is equal to the unit matrix except in the
 submatrix Q(ilo+1:ihi,ilo+1:ihi).
 If SIDE = 'L', then 1 &lt;= ILO &lt;= IHI &lt;= M, if M &gt; 0, and
 ILO = 1 and IHI = 0, if M = 0;
 if SIDE = 'R', then 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0, and
 ILO = 1 and IHI = 0, if N = 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension
 (LDA,M) if SIDE = 'L'
 (LDA,N) if SIDE = 'R'
 The vectors which define the elementary reflectors, as
 returned by SGEHRD.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A.
 LDA &gt;= max(1,M) if SIDE = 'L'; LDA &gt;= max(1,N) if SIDE = 'R'.</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension
 (M-1) if SIDE = 'L'
 (N-1) if SIDE = 'R'
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by SGEHRD.</pre>
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
<p> Definition at line 179 of file sormhr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
