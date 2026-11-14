---
title: "cunmhr-f(3)"
name: "cunmhr-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cunmhr-f/"
description: "cunmhr.f –"
---

<p>cunmhr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cunmhr</code> (SIDE, TRANS, M, N, ILO, IHI, A, LDA, TAU, C, LDC, WORK, LWORK, INFO)<br />
 <i></i><code>CUNMHR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cunmhr (characterSIDE, characterTRANS, integerM, integerN, integerILO, integerIHI, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )TAU, complex, dimension( ldc, * )C, integerLDC, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>CUNMHR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CUNMHR overwrites the general complex M-by-N matrix C with
 SIDE = 'L' SIDE = 'R'
 TRANS = 'N': Q * C C * Q
 TRANS = 'C': Q**H * C C * Q**H
 where Q is a complex unitary matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 IHI-ILO elementary reflectors, as returned by CGEHRD:
 Q = H(ilo) H(ilo+1) . . . H(ihi-1).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': apply Q or Q**H from the Left;
 = 'R': apply Q or Q**H from the Right.</pre>
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
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI must have the same values as in the previous call
 of CGEHRD. Q is equal to the unit matrix except in the
 submatrix Q(ilo+1:ihi,ilo+1:ihi).
 If SIDE = 'L', then 1 &lt;= ILO &lt;= IHI &lt;= M, if M &gt; 0, and
 ILO = 1 and IHI = 0, if M = 0;
 if SIDE = 'R', then 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0, and
 ILO = 1 and IHI = 0, if N = 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension
 (LDA,M) if SIDE = 'L'
 (LDA,N) if SIDE = 'R'
 The vectors which define the elementary reflectors, as
 returned by CGEHRD.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A.
 LDA &gt;= max(1,M) if SIDE = 'L'; LDA &gt;= max(1,N) if SIDE = 'R'.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX array, dimension
 (M-1) if SIDE = 'L'
 (N-1) if SIDE = 'R'
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by CGEHRD.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX array, dimension (LDC,N)
 On entry, the M-by-N matrix C.
 On exit, C is overwritten by Q*C or Q**H*C or C*Q**H or C*Q.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
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
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 179 of file cunmhr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
