---
title: "dtprfb-f(3)"
name: "dtprfb-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtprfb-f/"
description: "dtprfb.f –"
---

<p>dtprfb.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dtprfb</code> (SIDE, TRANS, DIRECT, STOREV, M, N, K, L, V, LDV, T, LDT, A, LDA, B, LDB, WORK, LDWORK)<br />
 <i></i><code>DTPRFB</code> applies a real or complex &#8216;triangular-pentagonal&#8217; blocked reflector to a real or complex matrix, which is composed of two blocks.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtprfb (characterSIDE, characterTRANS, characterDIRECT, characterSTOREV, integerM, integerN, integerK, integerL, double precision, dimension( ldv, * )V, integerLDV, double precision, dimension( ldt, * )T, integerLDT, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldwork, * )WORK, integerLDWORK)</h3>
<p><code>DTPRFB</code> applies a real or complex &#8216;triangular-pentagonal&#8217; blocked reflector to a real or complex matrix, which is composed of two blocks. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DTPRFB applies a real &quot;triangular-pentagonal&quot; block reflector H or its 
 transpose H**T to a real matrix C, which is composed of two 
 blocks A and B, either from the left or right.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': apply H or H**T from the Left
 = 'R': apply H or H**T from the Right</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 = 'N': apply H (No transpose)
 = 'T': apply H**T (Transpose)</pre>
<p><i>DIRECT</i> </p>
<pre> DIRECT is CHARACTER*1
 Indicates how H is formed from a product of elementary
 reflectors
 = 'F': H = H(1) H(2) . . . H(k) (Forward)
 = 'B': H = H(k) . . . H(2) H(1) (Backward)</pre>
<p><i>STOREV</i> </p>
<pre> STOREV is CHARACTER*1
 Indicates how the vectors which define the elementary
 reflectors are stored:
 = 'C': Columns
 = 'R': Rows</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix B. 
 M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix B. 
 N &gt;= 0.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The order of the matrix T, i.e. the number of elementary
 reflectors whose product defines the block reflector. 
 K &gt;= 0.</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 The order of the trapezoidal part of V. 
 K &gt;= L &gt;= 0. See Further Details.</pre>
<p><i>V</i> </p>
<pre> V is DOUBLE PRECISION array, dimension
 (LDV,K) if STOREV = 'C'
 (LDV,M) if STOREV = 'R' and SIDE = 'L'
 (LDV,N) if STOREV = 'R' and SIDE = 'R'
 The pentagonal matrix V, which contains the elementary reflectors
 H(1), H(2), ..., H(K). See Further Details.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V.
 If STOREV = 'C' and SIDE = 'L', LDV &gt;= max(1,M);
 if STOREV = 'C' and SIDE = 'R', LDV &gt;= max(1,N);
 if STOREV = 'R', LDV &gt;= K.</pre>
<p><i>T</i> </p>
<pre> T is DOUBLE PRECISION array, dimension (LDT,K)
 The triangular K-by-K matrix T in the representation of the
 block reflector. </pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. 
 LDT &gt;= K.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension
 (LDA,N) if SIDE = 'L' or (LDA,K) if SIDE = 'R'
 On entry, the K-by-N or M-by-K matrix A.
 On exit, A is overwritten by the corresponding block of 
 H*C or H**T*C or C*H or C*H**T. See Futher Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. 
 If SIDE = 'L', LDC &gt;= max(1,K);
 If SIDE = 'R', LDC &gt;= max(1,M). </pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB,N)
 On entry, the M-by-N matrix B.
 On exit, B is overwritten by the corresponding block of
 H*C or H**T*C or C*H or C*H**T. See Further Details.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. 
 LDB &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension
 (LDWORK,N) if SIDE = 'L',
 (LDWORK,K) if SIDE = 'R'.</pre>
<p><i>LDWORK</i> </p>
<pre> LDWORK is INTEGER
 The leading dimension of the array WORK.
 If SIDE = 'L', LDWORK &gt;= K; 
 if SIDE = 'R', LDWORK &gt;= M.</pre>
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
<pre> The matrix C is a composite matrix formed from blocks A and B.
 The block B is of size M-by-N; if SIDE = 'R', A is of size M-by-K, 
 and if SIDE = 'L', A is of size K-by-N.
 If SIDE = 'R' and DIRECT = 'F', C = [A B].
 If SIDE = 'L' and DIRECT = 'F', C = [A] 
 [B].
 If SIDE = 'R' and DIRECT = 'B', C = [B A].
 If SIDE = 'L' and DIRECT = 'B', C = [B]
 [A]. 
 The pentagonal matrix V is composed of a rectangular block V1 and a 
 trapezoidal block V2. The size of the trapezoidal block is determined by 
 the parameter L, where 0&lt;=L&lt;=K. If L=K, the V2 block of V is triangular;
 if L=0, there is no trapezoidal block, thus V = V1 is rectangular.
 If DIRECT = 'F' and STOREV = 'C': V = [V1]
 [V2]
 - V2 is upper trapezoidal (first L rows of K-by-K upper triangular)
 If DIRECT = 'F' and STOREV = 'R': V = [V1 V2]
 - V2 is lower trapezoidal (first L columns of K-by-K lower triangular)
 If DIRECT = 'B' and STOREV = 'C': V = [V2]
 [V1]
 - V2 is lower trapezoidal (last L rows of K-by-K lower triangular)
 If DIRECT = 'B' and STOREV = 'R': V = [V2 V1]
 
 - V2 is upper trapezoidal (last L columns of K-by-K upper triangular)
 If STOREV = 'C' and SIDE = 'L', V is M-by-K with V2 L-by-K.
 If STOREV = 'C' and SIDE = 'R', V is N-by-K with V2 L-by-K.
 If STOREV = 'R' and SIDE = 'L', V is K-by-M with V2 K-by-L.
 If STOREV = 'R' and SIDE = 'R', V is K-by-N with V2 K-by-L.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 251 of file dtprfb.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
