---
title: "cgemqrt(3)"
name: "cgemqrt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgemqrt/"
description: "cgemqrt.f –"
---

<h2 class="name">NAME</h2>
<p> cgemqrt.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgemqrt</code> (SIDE, TRANS, M, N, K, NB, V, LDV, T, LDT, C, LDC, WORK, INFO)<br />
 <i></i><code>CGEMQRT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgemqrt (characterSIDE, characterTRANS, integerM, integerN, integerK, integerNB, complex, dimension( ldv, * )V, integerLDV, complex, dimension( ldt, * )T, integerLDT, complex, dimension( ldc, * )C, integerLDC, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CGEMQRT</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGEMQRT overwrites the general complex M-by-N matrix C with
                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q C            C Q
 TRANS = 'C':    Q**H C            C Q**H
 where Q is a complex orthogonal matrix defined as the product of K
 elementary reflectors:
       Q = H(1) H(2) . . . H(K) = I - V T V**H
 generated using the compact WY representation as returned by CGEQRT. 
 Q is of order M if SIDE = 'L' and of order N  if SIDE = 'R'.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'L': apply Q or Q**H from the Left;
          = 'R': apply Q or Q**H from the Right.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N':  No transpose, apply Q;
          = 'C':  Transpose, apply Q**H.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix C. M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix C. N &gt;= 0.
</pre>
<p> <i>K</i> </p>
<pre><code>
K is INTEGER
    The number of elementary reflectors whose product defines
        the matrix Q.If SIDE = 'L',
                        M &gt;= K &gt;= 0;
if SIDE
= 'R', N &gt;= K &gt;= 0.
</code></pre>
<p> <i>NB</i> </p>
<pre>
          NB is INTEGER
          The block size used for the storage of T.  K &gt;= NB &gt;= 1.
          This must be the same value of NB used to generate T
          in CGEQRT.
</pre>
<p> <i>V</i> </p>
<pre>
          V is COMPLEX array, dimension (LDV,K)
          The i-th column must contain the vector which defines the
          elementary reflector H(i), for i = 1,2,...,k, as returned by
          CGEQRT in the first K columns of its array argument A.
</pre>
<p> <i>LDV</i> </p>
<pre><code>
LDV is INTEGER
    The leading dimension of the array V.If SIDE = 'L',
                                            LDA &gt;= max(1, M);
if SIDE
= 'R', LDA &gt;= max(1, N).
</code></pre>
<p> <i>T</i> </p>
<pre>
          T is COMPLEX array, dimension (LDT,K)
          The upper triangular factors of the block reflectors
          as returned by CGEQRT, stored as a NB-by-N matrix.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T.  LDT &gt;= NB.
</pre>
<p> <i>C</i> </p>
<pre>
          C is COMPLEX array, dimension (LDC,N)
          On entry, the M-by-N matrix C.
          On exit, C is overwritten by Q C, Q**H C, C Q**H or C Q.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1,M).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array. The dimension of WORK is
           N*NB if SIDE = 'L', or  M*NB if SIDE = 'R'.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<dd> November 2013</dl>
<p> Definition at line 168 of file cgemqrt.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
