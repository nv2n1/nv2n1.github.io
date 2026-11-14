---
title: "dormbr(3)"
name: "dormbr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dormbr/"
description: "dormbr.f –"
---

<h2 class="name">NAME</h2>
<p> dormbr.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dormbr</code> (VECT, SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC, WORK, LWORK, INFO)<br />
 <i></i><code>DORMBR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dormbr (characterVECT, characterSIDE, characterTRANS, integerM, integerN, integerK, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DORMBR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
If VECT = 'Q', DORMBR overwrites the general real M - by - N matrix C with SIDE = 'L' SIDE = 'R' TRANS = 'N' : Q *C C *Q TRANS = 'T' : Q **T *C C *Q **T If VECT = 'P', DORMBR overwrites the general real M - by - N matrix C with SIDE = 'L' SIDE = 'R' TRANS = 'N' : P *C C *P TRANS = 'T' : P **T *C C *P **T Here Q and P **T are the orthogonal matrices determined by DGEBRD when reducing a real matrix A to bidiagonal form : A = Q * B * P * *T.Q and P * *T are defined as products of elementary reflectors H(i) and G(i) respectively.Let nq = m if SIDE = 'L' and nq = n if SIDE = 'R'.Thus nq is the order of the orthogonal matrix Q or P **T that is applied.If VECT = 'Q', A is assumed to have been an NQ - by - K matrix : if nq &gt;= k, Q = H(1) H(2)...H(k);
if nq
    &lt; k, Q = H(1) H(2)...H(nq - 1).If VECT = 'P', A is assumed to have been a K - by - NQ matrix : if k &lt; nq, P = G(1) G(2)...G(k);
if k
&gt;= nq, P = G(1) G(2)...G(nq - 1).
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>VECT</i> </p>
<pre>
          VECT is CHARACTER*1
          = 'Q': apply Q or Q**T;
          = 'P': apply P or P**T.
</pre>
<p> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'L': apply Q, Q**T, P or P**T from the Left;
          = 'R': apply Q, Q**T, P or P**T from the Right.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N':  No transpose, apply Q  or P;
          = 'T':  Transpose, apply Q**T or P**T.
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
<pre>
          K is INTEGER
          If VECT = 'Q', the number of columns in the original
          matrix reduced by DGEBRD.
          If VECT = 'P', the number of rows in the original
          matrix reduced by DGEBRD.
          K &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension
                                (LDA,min(nq,K)) if VECT = 'Q'
                                (LDA,nq)        if VECT = 'P'
          The vectors which define the elementary reflectors H(i) and
          G(i), whose products determine the matrices Q and P, as
          returned by DGEBRD.
</pre>
<p> <i>LDA</i> </p>
<p>LDA is INTEGER<br />
    The leading dimension of the array A.If VECT = &#8216;Q&#8217;,<br />
                                            LDA &gt;= max(1, nq);<br />
if VECT<br />
= &#8216;P&#8217;, LDA &gt;= max(1, min(nq, K)).</p>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (min(nq,K))
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i) or G(i) which determines Q or P, as returned
          by DGEBRD in the array argument TAUQ or TAUP.
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION array, dimension (LDC,N)
          On entry, the M-by-N matrix C.
          On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q
          or P*C or P**T*C or C*P or C*P**T.
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
<p> Definition at line 195 of file dormbr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
