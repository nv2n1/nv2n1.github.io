---
title: "dorml2(3)"
name: "dorml2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dorml2/"
description: "dorml2.f –"
---

<h2 class="name">NAME</h2>
<p> dorml2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dorml2</code> (SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC, WORK, INFO)<br />
 <i></i><code>DORML2</code> multiplies a general matrix by the orthogonal matrix from a LQ factorization determined by sgelqf (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dorml2 (characterSIDE, characterTRANS, integerM, integerN, integerK, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DORML2</code> multiplies a general matrix by the orthogonal matrix from a LQ factorization determined by sgelqf (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
DORML2 overwrites the general real m by n matrix C with
    Q *C if SIDE = 'L' and TRANS = 'N',
            or
                Q **T *C if SIDE = 'L' and TRANS = 'T',
            or
                C *Q if SIDE = 'R' and TRANS = 'N',
            or
                C *Q **T if SIDE = 'R' and TRANS = 'T',
            where Q is a real orthogonal matrix defined as the product of k
                elementary reflectors
                    Q = H(k)...H(2) H(1)
                            as returned by DGELQF.Q is of order m if SIDE = 'L' and of order n if SIDE = 'R'.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'L': apply Q or Q**T from the Left
          = 'R': apply Q or Q**T from the Right
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          = 'N': apply Q  (No transpose)
          = 'T': apply Q**T (Transpose)
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
          A is DOUBLE PRECISION array, dimension
                               (LDA,M) if SIDE = 'L',
                               (LDA,N) if SIDE = 'R'
          The i-th row must contain the vector which defines the
          elementary reflector H(i), for i = 1,2,...,k, as returned by
          DGELQF in the first k rows of its array argument A.
          A is modified by the routine but restored on exit.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,K).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (K)
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i), as returned by DGELQF.
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION array, dimension (LDC,N)
          On entry, the m by n matrix C.
          On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1,M).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension
                                   (N) if SIDE = 'L',
                                   (M) if SIDE = 'R'
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
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
<p> Definition at line 159 of file dorml2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
