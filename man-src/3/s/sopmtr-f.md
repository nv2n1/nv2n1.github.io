---
title: "sopmtr-f(3)"
name: "sopmtr-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sopmtr-f/"
description: "sopmtr.f –"
---

<p>sopmtr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sopmtr</code> (SIDE, UPLO, TRANS, M, N, AP, TAU, C, LDC, WORK, INFO)<br />
 <i></i><code>SOPMTR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sopmtr (characterSIDE, characterUPLO, characterTRANS, integerM, integerN, real, dimension( * )AP, real, dimension( * )TAU, real, dimension( ldc, * )C, integerLDC, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SOPMTR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 SOPMTR overwrites the general real M-by-N matrix C with
                 SIDE = 'L'     SIDE = 'R'
 TRANS = 'N':      Q * C          C * Q
 TRANS = 'T':      Q**T * C       C * Q**T
 where Q is a real orthogonal matrix of order nq, with nq = m if
 SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of
 nq-1 elementary reflectors, as returned by SSPTRD using packed
 storage:
 if UPLO = 'U', Q = H(nq-1) . . . H(2) H(1);
 if UPLO = 'L', Q = H(1) H(2) . . . H(nq-1).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'L': apply Q or Q**T from the Left;
          = 'R': apply Q or Q**T from the Right.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U': Upper triangular packed storage used in previous
                 call to SSPTRD;
          = 'L': Lower triangular packed storage used in previous
                 call to SSPTRD.
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
<p> <i>AP</i> </p>
<pre>
          AP is REAL array, dimension
                               (M*(M+1)/2) if SIDE = 'L'
                               (N*(N+1)/2) if SIDE = 'R'
          The vectors which define the elementary reflectors, as
          returned by SSPTRD.  AP is modified by the routine but
          restored on exit.
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is REAL array, dimension (M-1) if SIDE = 'L'
                                     or (N-1) if SIDE = 'R'
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i), as returned by SSPTRD.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (LDC,N)
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
          WORK is REAL array, dimension
                                   (N) if SIDE = 'L'
                                   (M) if SIDE = 'R'
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> November 2011</dl>
<p> Definition at line 150 of file sopmtr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
