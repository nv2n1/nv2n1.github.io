---
title: "clarft(3)"
name: "clarft"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clarft/"
description: "clarft.f –"
---

<h2 class="name">NAME</h2>
<p> clarft.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clarft</code> (DIRECT, STOREV, N, K, V, LDV, TAU, T, LDT)<br />
 <i></i><code>CLARFT</code> forms the triangular factor T of a block reflector H = I &#8211; vtvH</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clarft (characterDIRECT, characterSTOREV, integerN, integerK, complex, dimension( ldv, * )V, integerLDV, complex, dimension( * )TAU, complex, dimension( ldt, * )T, integerLDT)</h3>
<p> <code>CLARFT</code> forms the triangular factor T of a block reflector H = I &#8211; vtvH </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLARFT forms the triangular factor T of a complex block reflector H
 of order n, which is defined as a product of k elementary reflectors.
 If DIRECT = 'F', H = H(1) H(2) . . . H(k) and T is upper triangular;
 If DIRECT = 'B', H = H(k) . . . H(2) H(1) and T is lower triangular.
 If STOREV = 'C', the vector which defines the elementary reflector
 H(i) is stored in the i-th column of the array V, and
    H  =  I - V * T * V**H
 If STOREV = 'R', the vector which defines the elementary reflector
 H(i) is stored in the i-th row of the array V, and
    H  =  I - V**H * T * V
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>DIRECT</i> </p>
<pre>
          DIRECT is CHARACTER*1
          Specifies the order in which the elementary reflectors are
          multiplied to form the block reflector:
          = 'F': H = H(1) H(2) . . . H(k) (Forward)
          = 'B': H = H(k) . . . H(2) H(1) (Backward)
</pre>
<p> <i>STOREV</i> </p>
<pre>
          STOREV is CHARACTER*1
          Specifies how the vectors which define the elementary
          reflectors are stored (see also Further Details):
          = 'C': columnwise
          = 'R': rowwise
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the block reflector H. N &gt;= 0.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
          The order of the triangular factor T (= the number of
          elementary reflectors). K &gt;= 1.
</pre>
<p> <i>V</i> </p>
<pre>
          V is COMPLEX array, dimension
                               (LDV,K) if STOREV = 'C'
                               (LDV,N) if STOREV = 'R'
          The matrix V. See further details.
</pre>
<p> <i>LDV</i> </p>
<pre><code>
LDV is INTEGER
    The leading dimension of the array V.If STOREV = 'C',
                                            LDV &gt;= max(1, N);
if STOREV
= 'R', LDV &gt;= K.
</code></pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX array, dimension (K)
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i).
</pre>
<p> <i>T</i> </p>
<pre>
          T is COMPLEX array, dimension (LDT,K)
          The k by k triangular factor T of the block reflector.
          If DIRECT = 'F', T is upper triangular; if DIRECT = 'B', T is
          lower triangular. The rest of the array is not used.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= K.
</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The shape of the matrix V and the storage of the vectors which define
  the H(i) is best illustrated by the following example with n = 5 and
  k = 3. The elements equal to 1 are not stored.
  DIRECT = 'F' and STOREV = 'C':         DIRECT = 'F' and STOREV = 'R':
               V = (  1       )                 V = (  1 v1 v1 v1 v1 )
                   ( v1  1    )                     (     1 v2 v2 v2 )
                   ( v1 v2  1 )                     (        1 v3 v3 )
                   ( v1 v2 v3 )
                   ( v1 v2 v3 )
  DIRECT = 'B' and STOREV = 'C':         DIRECT = 'B' and STOREV = 'R':
               V = ( v1 v2 v3 )                 V = ( v1 v1  1       )
                   ( v1 v2 v3 )                     ( v2 v2 v2  1    )
                   (  1 v2 v3 )                     ( v3 v3 v3 v3  1 )
                   (     1 v3 )
                   (        1 )
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 164 of file clarft.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
