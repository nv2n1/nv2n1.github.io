---
title: "slarzb(3)"
name: "slarzb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slarzb/"
description: "slarzb.f –"
---

<h2 class="name">NAME</h2>
<p> slarzb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slarzb</code> (SIDE, TRANS, DIRECT, STOREV, M, N, K, L, V, LDV, T, LDT, C, LDC, WORK, LDWORK)<br />
 <i></i><code>SLARZB</code> applies a block reflector or its transpose to a general matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slarzb (characterSIDE, characterTRANS, characterDIRECT, characterSTOREV, integerM, integerN, integerK, integerL, real, dimension( ldv, * )V, integerLDV, real, dimension( ldt, * )T, integerLDT, real, dimension( ldc, * )C, integerLDC, real, dimension( ldwork, * )WORK, integerLDWORK)</h3>
<p> <code>SLARZB</code> applies a block reflector or its transpose to a general matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLARZB applies a real block reflector H or its transpose H**T to
 a real distributed M-by-N  C from the left or the right.
 Currently, only STOREV = 'R' and DIRECT = 'B' are supported.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'L': apply H or H**T from the Left
          = 'R': apply H or H**T from the Right
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N': apply H (No transpose)
          = 'C': apply H**T (Transpose)
</pre>
<p> <i>DIRECT</i> </p>
<pre>
          DIRECT is CHARACTER*1
          Indicates how H is formed from a product of elementary
          reflectors
          = 'F': H = H(1) H(2) . . . H(k) (Forward, not supported yet)
          = 'B': H = H(k) . . . H(2) H(1) (Backward)
</pre>
<p> <i>STOREV</i> </p>
<pre>
          STOREV is CHARACTER*1
          Indicates how the vectors which define the elementary
          reflectors are stored:
          = 'C': Columnwise                        (not supported yet)
          = 'R': Rowwise
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix C.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix C.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
          The order of the matrix T (= the number of elementary
          reflectors whose product defines the block reflector).
</pre>
<p> <i>L</i> </p>
<pre>
          L is INTEGER
          The number of columns of the matrix V containing the
          meaningful part of the Householder reflectors.
          If SIDE = 'L', M &gt;= L &gt;= 0, if SIDE = 'R', N &gt;= L &gt;= 0.
</pre>
<p> <i>V</i> </p>
<pre>
          V is REAL array, dimension (LDV,NV).
          If STOREV = 'C', NV = K; if STOREV = 'R', NV = L.
</pre>
<p> <i>LDV</i> </p>
<pre><code>
LDV is INTEGER
    The leading dimension of the array V.If STOREV = 'C',
                                            LDV &gt;= L;
if STOREV
= 'R', LDV &gt;= K.
</code></pre>
<p> <i>T</i> </p>
<pre>
          T is REAL array, dimension (LDT,K)
          The triangular K-by-K matrix T in the representation of the
          block reflector.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= K.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (LDC,N)
          On entry, the M-by-N matrix C.
          On exit, C is overwritten by H*C or H**T*C or C*H or C*H**T.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1,M).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (LDWORK,K)
</pre>
<p> <i>LDWORK</i> </p>
<pre><code>
LDWORK is INTEGER
    The leading dimension of the array WORK.If SIDE = 'L',
                                               LDWORK &gt;= max(1, N);
if SIDE
= 'R', LDWORK &gt;= max(1, M).
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<p>&nbsp;<wbr></dl>
<p> Definition at line 183 of file slarzb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
