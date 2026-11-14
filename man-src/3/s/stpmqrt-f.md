---
title: "stpmqrt-f(3)"
name: "stpmqrt-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stpmqrt-f/"
description: "stpmqrt.f –"
---

<p>stpmqrt.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>stpmqrt</code> (SIDE, TRANS, M, N, K, L, NB, V, LDV, T, LDT, A, LDA, B, LDB, WORK, INFO)<br />
 <i></i><code>STPMQRT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stpmqrt (characterSIDE, characterTRANS, integerM, integerN, integerK, integerL, integerNB, real, dimension( ldv, * )V, integerLDV, real, dimension( ldt, * )T, integerLDT, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( * )WORK, integerINFO)</h3>
<p><code>STPMQRT</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STPMQRT applies a real orthogonal matrix Q obtained from a 
 &quot;triangular-pentagonal&quot; real block reflector H to a general
 real matrix C, which consists of two blocks A and B.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': apply Q or Q^H from the Left;
 = 'R': apply Q or Q^H from the Right.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 = 'N': No transpose, apply Q;
 = 'C': Transpose, apply Q^H.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix B. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix B. N &gt;= 0.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The number of elementary reflectors whose product defines
 the matrix Q.</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 The order of the trapezoidal part of V. 
 K &gt;= L &gt;= 0. See Further Details.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The block size used for the storage of T. K &gt;= NB &gt;= 1.
 This must be the same value of NB used to generate T
 in CTPQRT.</pre>
<p><i>V</i> </p>
<pre> V is REAL array, dimension (LDA,K)
 The i-th column must contain the vector which defines the
 elementary reflector H(i), for i = 1,2,...,k, as returned by
 CTPQRT in B. See Further Details.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V.
 If SIDE = 'L', LDV &gt;= max(1,M);
 if SIDE = 'R', LDV &gt;= max(1,N).</pre>
<p><i>T</i> </p>
<pre> T is REAL array, dimension (LDT,K)
 The upper triangular factors of the block reflectors
 as returned by CTPQRT, stored as a NB-by-K matrix.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= NB.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension
 (LDA,N) if SIDE = 'L' or 
 (LDA,K) if SIDE = 'R'
 On entry, the K-by-N or M-by-K matrix A.
 On exit, A is overwritten by the corresponding block of 
 Q*C or Q^H*C or C*Q or C*Q^H. See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. 
 If SIDE = 'L', LDC &gt;= max(1,K);
 If SIDE = 'R', LDC &gt;= max(1,M). </pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,N)
 On entry, the M-by-N matrix B.
 On exit, B is overwritten by the corresponding block of
 Q*C or Q^H*C or C*Q or C*Q^H. See Further Details.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. 
 LDB &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array. The dimension of WORK is
 N*NB if SIDE = 'L', or M*NB if SIDE = 'R'.</pre>
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
<dd>April 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The columns of the pentagonal matrix V contain the elementary reflectors
 H(1), H(2), ..., H(K); V is composed of a rectangular block V1 and a 
 trapezoidal block V2:
 V = [V1]
 [V2].
 The size of the trapezoidal block V2 is determined by the parameter L, 
 where 0 &lt;= L &lt;= K; V2 is upper trapezoidal, consisting of the first L
 rows of a K-by-K upper triangular matrix. If L=K, V2 is upper triangular;
 if L=0, there is no trapezoidal block, hence V = V1 is rectangular.
 If SIDE = 'L': C = [A] where A is K-by-N, B is M-by-N and V is M-by-K. 
 [B] 
 
 If SIDE = 'R': C = [A B] where A is M-by-K, B is M-by-N and V is N-by-K.
 The real orthogonal matrix Q is formed from V and T.
 If TRANS='N' and SIDE='L', C is on exit replaced with Q * C.
 If TRANS='C' and SIDE='L', C is on exit replaced with Q^H * C.
 If TRANS='N' and SIDE='R', C is on exit replaced with C * Q.
 If TRANS='C' and SIDE='R', C is on exit replaced with C * Q^H.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 216 of file stpmqrt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
