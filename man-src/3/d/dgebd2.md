---
title: "dgebd2(3)"
name: "dgebd2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgebd2/"
description: "dgebd2.f –"
---

<h2 class="name">NAME</h2>
<p> dgebd2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgebd2</code> (M, N, A, LDA, D, E, TAUQ, TAUP, WORK, INFO)<br />
 <i></i><code>DGEBD2</code> reduces a general matrix to bidiagonal form using an unblocked algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgebd2 (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( * )TAUQ, double precision, dimension( * )TAUP, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DGEBD2</code> reduces a general matrix to bidiagonal form using an unblocked algorithm. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGEBD2 reduces a real general m by n matrix A to upper or lower
 bidiagonal form B by an orthogonal transformation: Q**T * A * P = B.
 If m &gt;= n, B is upper bidiagonal; if m &lt; n, B is lower bidiagonal.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows in the matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns in the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is DOUBLE PRECISION array, dimension(LDA, N) On entry, the m by n general matrix to be reduced.On exit,
    if m &gt;= n, the diagonal and the first superdiagonal are overwritten with the upper bidiagonal matrix B;
the
    elements below the diagonal,
    with the array TAUQ, represent the orthogonal matrix Q as a product of elementary reflectors, and the elements above the first superdiagonal,
    with the array TAUP, represent the orthogonal matrix P as a product of elementary reflectors;
if m
    &lt; n, the diagonal and the first subdiagonal are
             overwritten with the lower bidiagonal matrix B;
the
    elements below the first subdiagonal,
    with the array TAUQ,
    represent the orthogonal matrix Q as a product of
        elementary reflectors,
    and the elements above the diagonal,
    with the array TAUP, represent the orthogonal matrix P as a product of elementary reflectors.See Further Details.
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (min(M,N))
          The diagonal elements of the bidiagonal matrix B:
          D(i) = A(i,i).
</pre>
<p> <i>E</i> </p>
<p>          E is DOUBLE PRECISION array, dimension (min(M,N)-1)<br />
          The off-diagonal elements of the bidiagonal matrix B:<br />
          if m &gt;= n, E(i) = A(i,i+1) for i = 1,2,&#8230;,n-1;<br />
          if m &lt; n, E(i) = A(i+1,i) for i = 1,2,&#8230;,m-1.</p>
<p> <i>TAUQ</i> </p>
<pre>
          TAUQ is DOUBLE PRECISION array dimension (min(M,N))
          The scalar factors of the elementary reflectors which
          represent the orthogonal matrix Q. See Further Details.
</pre>
<p> <i>TAUP</i> </p>
<pre>
          TAUP is DOUBLE PRECISION array, dimension (min(M,N))
          The scalar factors of the elementary reflectors which
          represent the orthogonal matrix P. See Further Details.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (max(M,N))
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit.
          &lt; 0: if INFO = -i, the i-th argument had an illegal value.
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
<pre><code>
The matrices Q and P are represented as products of elementary
        reflectors : If m &gt;= n,
    Q = H(1) H(2)...H(n) and P = G(1) G(2)...G(n - 1)
                                     Each H(i) and
                                 G(i) has the form : H(i) = I - tauq * v * v * *T and G(i) = I - taup * u * u * *T where tauq and taup are real scalars,
    and v and u are real vectors;
v(1
  : i - 1) = 0,
        v(i) = 1, and v(i + 1
                        : m) is stored on exit in A(i + 1
                                                    : m, i);
u(1
  : i) = 0,
    u(i + 1) = 1, and u(i + 2
                        : n) is stored on exit in A(i, i + 2
                                                    : n);
tauq is stored in TAUQ(i) and taup in TAUP(i).If m &lt; n,
    Q = H(1) H(2)...H(m - 1) and P = G(1) G(2)...G(m)
                                         Each H(i) and
                                     G(i) has the form : H(i) = I - tauq * v * v * *T and G(i) = I - taup * u * u * *T where tauq and taup are real scalars,
    and v and u are real vectors;
v(1
  : i) = 0,
    v(i + 1) = 1, and v(i + 2
                        : m) is stored on exit in A(i + 2
                                                    : m, i);
u(1
  : i - 1) = 0,
        u(i) = 1, and u(i + 1
                        : n) is stored on exit in A(i, i + 1
                                                    : n);
tauq is stored in TAUQ(i) and taup in TAUP(i).The contents of A on exit are illustrated by the following examples : m = 6 and n = 5(m &gt; n)
    : m = 5 and n = 6(m &lt; n)
    : (d e u1 u1 u1)(d u1 u1 u1 u1 u1)(v1 d e u2 u2)(e d u2 u2 u2 u2)(v1 v2 d e u3)(v1 e d u3 u3 u3)(v1 v2 v3 d e)(v1 v2 e d u4 u4)(v1 v2 v3 v4 d)(v1 v2 v3 e d u5)(v1 v2 v3 v4 v5)
          where d
      and e denote diagonal and off - diagonal elements of B,
                                                                                                                    vi
    denotes an element of the vector defining H(i),
                                                                                                                    and ui an element of
                                                                                                                        the vector defining G(i)
                                                                                                                            .
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 190 of file dgebd2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
