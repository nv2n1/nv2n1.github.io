---
title: "dlarzt-f(3)"
name: "dlarzt-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarzt-f/"
description: "dlarzt.f –"
---

<p>dlarzt.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlarzt</code> (DIRECT, STOREV, N, K, V, LDV, TAU, T, LDT)<br />
 <i></i><code>DLARZT</code> forms the triangular factor T of a block reflector H = I &#8211; vtvH.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarzt (characterDIRECT, characterSTOREV, integerN, integerK, double precision, dimension( ldv, * )V, integerLDV, double precision, dimension( * )TAU, double precision, dimension( ldt, * )T, integerLDT)</h3>
<p><code>DLARZT</code> forms the triangular factor T of a block reflector H = I &#8211; vtvH. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLARZT forms the triangular factor T of a real block reflector
 H of order &gt; n, which is defined as a product of k elementary
 reflectors.
 If DIRECT = 'F', H = H(1) H(2) . . . H(k) and T is upper triangular;
 If DIRECT = 'B', H = H(k) . . . H(2) H(1) and T is lower triangular.
 If STOREV = 'C', the vector which defines the elementary reflector
 H(i) is stored in the i-th column of the array V, and
 H = I - V * T * V**T
 If STOREV = 'R', the vector which defines the elementary reflector
 H(i) is stored in the i-th row of the array V, and
 H = I - V**T * T * V
 Currently, only STOREV = 'R' and DIRECT = 'B' are supported.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>DIRECT</i> </p>
<pre> DIRECT is CHARACTER*1
 Specifies the order in which the elementary reflectors are
 multiplied to form the block reflector:
 = 'F': H = H(1) H(2) . . . H(k) (Forward, not supported yet)
 = 'B': H = H(k) . . . H(2) H(1) (Backward)</pre>
<p><i>STOREV</i> </p>
<pre> STOREV is CHARACTER*1
 Specifies how the vectors which define the elementary
 reflectors are stored (see also Further Details):
 = 'C': columnwise (not supported yet)
 = 'R': rowwise</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the block reflector H. N &gt;= 0.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The order of the triangular factor T (= the number of
 elementary reflectors). K &gt;= 1.</pre>
<p><i>V</i> </p>
<pre> V is DOUBLE PRECISION array, dimension
 (LDV,K) if STOREV = 'C'
 (LDV,N) if STOREV = 'R'
 The matrix V. See further details.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V.
 If STOREV = 'C', LDV &gt;= max(1,N); if STOREV = 'R', LDV &gt;= K.</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i).</pre>
<p><i>T</i> </p>
<pre> T is DOUBLE PRECISION array, dimension (LDT,K)
 The k by k triangular factor T of the block reflector.
 If DIRECT = 'F', T is upper triangular; if DIRECT = 'B', T is
 lower triangular. The rest of the array is not used.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= K.</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> The shape of the matrix V and the storage of the vectors which define
 the H(i) is best illustrated by the following example with n = 5 and
 k = 3. The elements equal to 1 are not stored; the corresponding
 array elements are modified but restored on exit. The rest of the
 array is not used.
 DIRECT = 'F' and STOREV = 'C': DIRECT = 'F' and STOREV = 'R':
 ______V_____
 ( v1 v2 v3 ) / ( v1 v2 v3 ) ( v1 v1 v1 v1 v1 . . . . 1 )
 V = ( v1 v2 v3 ) ( v2 v2 v2 v2 v2 . . . 1 )
 ( v1 v2 v3 ) ( v3 v3 v3 v3 v3 . . 1 )
 ( v1 v2 v3 )
 . . .
 . . .
 1 . .
 1 .
 1
 DIRECT = 'B' and STOREV = 'C': DIRECT = 'B' and STOREV = 'R':
 ______V_____
 1 / . 1 ( 1 . . . . v1 v1 v1 v1 v1 )
 . . 1 ( . 1 . . . v2 v2 v2 v2 v2 )
 . . . ( . . 1 . . v3 v3 v3 v3 v3 )
 . . .
 ( v1 v2 v3 )
 ( v1 v2 v3 )
 V = ( v1 v2 v3 )
 ( v1 v2 v3 )
 ( v1 v2 v3 )</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 186 of file dlarzt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
