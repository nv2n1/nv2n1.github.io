---
title: "dlarfb-f(3)"
name: "dlarfb-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarfb-f/"
description: "dlarfb.f –"
---

<p>dlarfb.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlarfb</code> (SIDE, TRANS, DIRECT, STOREV, M, N, K, V, LDV, T, LDT, C, LDC, WORK, LDWORK)<br />
 <i></i><code>DLARFB</code> applies a block reflector or its transpose to a general rectangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarfb (characterSIDE, characterTRANS, characterDIRECT, characterSTOREV, integerM, integerN, integerK, double precision, dimension( ldv, * )V, integerLDV, double precision, dimension( ldt, * )T, integerLDT, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( ldwork, * )WORK, integerLDWORK)</h3>
<p><code>DLARFB</code> applies a block reflector or its transpose to a general rectangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLARFB applies a real block reflector H or its transpose H**T to a
 real m by n matrix C, from either the left or the right.</pre>
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
 = 'C': Columnwise
 = 'R': Rowwise</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix C.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix C.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The order of the matrix T (= the number of elementary
 reflectors whose product defines the block reflector).</pre>
<p><i>V</i> </p>
<pre> V is DOUBLE PRECISION array, dimension
 (LDV,K) if STOREV = 'C'
 (LDV,M) if STOREV = 'R' and SIDE = 'L'
 (LDV,N) if STOREV = 'R' and SIDE = 'R'
 The matrix V. See Further Details.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V.
 If STOREV = 'C' and SIDE = 'L', LDV &gt;= max(1,M);
 if STOREV = 'C' and SIDE = 'R', LDV &gt;= max(1,N);
 if STOREV = 'R', LDV &gt;= K.</pre>
<p><i>T</i> </p>
<pre> T is DOUBLE PRECISION array, dimension (LDT,K)
 The triangular k by k matrix T in the representation of the
 block reflector.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= K.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (LDC,N)
 On entry, the m by n matrix C.
 On exit, C is overwritten by H*C or H**T*C or C*H or C*H**T.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (LDWORK,K)</pre>
<p><i>LDWORK</i> </p>
<pre> LDWORK is INTEGER
 The leading dimension of the array WORK.
 If SIDE = 'L', LDWORK &gt;= max(1,N);
 if SIDE = 'R', LDWORK &gt;= max(1,M).</pre>
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
<pre> The shape of the matrix V and the storage of the vectors which define
 the H(i) is best illustrated by the following example with n = 5 and
 k = 3. The elements equal to 1 are not stored; the corresponding
 array elements are modified but restored on exit. The rest of the
 array is not used.
 DIRECT = 'F' and STOREV = 'C': DIRECT = 'F' and STOREV = 'R':
 V = ( 1 ) V = ( 1 v1 v1 v1 v1 )
 ( v1 1 ) ( 1 v2 v2 v2 )
 ( v1 v2 1 ) ( 1 v3 v3 )
 ( v1 v2 v3 )
 ( v1 v2 v3 )
 DIRECT = 'B' and STOREV = 'C': DIRECT = 'B' and STOREV = 'R':
 V = ( v1 v2 v3 ) V = ( v1 v1 1 )
 ( v1 v2 v3 ) ( v2 v2 v2 1 )
 ( 1 v2 v3 ) ( v3 v3 v3 v3 1 )
 ( 1 v3 )
 ( 1 )</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 195 of file dlarfb.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
