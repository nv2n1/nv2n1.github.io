---
title: "dormqr(3)"
name: "dormqr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dormqr/"
description: "dormqr.f –"
---

<h2 class="name">NAME</h2>
<p> dormqr.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dormqr</code> (SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC, WORK, LWORK, INFO)<br />
 <i></i><code>DORMQR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dormqr (characterSIDE, characterTRANS, integerM, integerN, integerK, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DORMQR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DORMQR overwrites the general real M-by-N matrix C with
                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'T':      Q**T * C       C * Q**T
 where Q is a real orthogonal matrix defined as the product of k
 elementary reflectors
       Q = H(1) H(2) . . . H(k)
 as returned by DGEQRF. Q is of order M if SIDE = 'L' and of order N
 if SIDE = 'R'.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'L': apply Q or Q**T from the Left;
          = 'R': apply Q or Q**T from the Right.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N':  No transpose, apply Q;
          = 'T':  Transpose, apply Q**T.
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
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,K)
          The i-th column must contain the vector which defines the
          elementary reflector H(i), for i = 1,2,...,k, as returned by
          DGEQRF in the first k columns of its array argument A.
</pre>
<p> <i>LDA</i> </p>
<p>LDA is INTEGER<br />
    The leading dimension of the array A.If SIDE = &#8216;L&#8217;,<br />
                                            LDA &gt;= max(1, M);<br />
if SIDE<br />
= &#8216;R&#8217;, LDA &gt;= max(1, N).</p>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (K)
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i), as returned by DGEQRF.
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION array, dimension (LDC,N)
          On entry, the M-by-N matrix C.
          On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1,M).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
LWORK is INTEGER
    The dimension of the array WORK.If SIDE = 'L',
                                       LWORK &gt;= max(1, N);
if SIDE
    = 'R', LWORK &gt;= max(1, M).For optimum performance LWORK &gt;= N *NB if SIDE = 'L', and LWORK &gt;= M *NB if SIDE = 'R', where NB is the optimal blocksize.If LWORK = -1, then a workspace query is assumed;
the routine
    only calculates the optimal size of the WORK array,
    returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.
</code></pre>
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
<dd> November 2011</dl>
<p> Definition at line 169 of file dormqr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
