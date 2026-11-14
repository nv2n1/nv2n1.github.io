---
title: "dorgbr-f(3)"
name: "dorgbr-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dorgbr-f/"
description: "dorgbr.f –"
---

<p>dorgbr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dorgbr</code> (VECT, M, N, K, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>DORGBR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dorgbr (characterVECT, integerM, integerN, integerK, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>DORGBR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DORGBR generates one of the real orthogonal matrices Q or P**T
 determined by DGEBRD when reducing a real matrix A to bidiagonal
 form: A = Q * B * P**T. Q and P**T are defined as products of
 elementary reflectors H(i) or G(i) respectively.
 If VECT = 'Q', A is assumed to have been an M-by-K matrix, and Q
 is of order M:
 if m &gt;= k, Q = H(1) H(2) . . . H(k) and DORGBR returns the first n
 columns of Q, where m &gt;= n &gt;= k;
 if m &lt; k, Q = H(1) H(2) . . . H(m-1) and DORGBR returns Q as an
 M-by-M matrix.
 If VECT = 'P', A is assumed to have been a K-by-N matrix, and P**T
 is of order N:
 if k &lt; n, P**T = G(k) . . . <a href="//www.systutorials.com/docs/linux/man/2-G/">G</a>(2) <a href="//www.systutorials.com/docs/linux/man/1-G/">G</a>(1) and DORGBR returns the first m
 rows of P**T, where n &gt;= m &gt;= k;
 if k &gt;= n, P**T = G(n-1) . . . <a href="//www.systutorials.com/docs/linux/man/2-G/">G</a>(2) <a href="//www.systutorials.com/docs/linux/man/1-G/">G</a>(1) and DORGBR returns P**T as
 an N-by-N matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>VECT</i> </p>
<pre> VECT is CHARACTER*1
 Specifies whether the matrix Q or the matrix P**T is
 required, as defined in the transformation applied by DGEBRD:
 = 'Q': generate Q;
 = 'P': generate P**T.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix Q or P**T to be returned.
 M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix Q or P**T to be returned.
 N &gt;= 0.
 If VECT = 'Q', M &gt;= N &gt;= min(M,K);
 if VECT = 'P', N &gt;= M &gt;= min(N,K).</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 If VECT = 'Q', the number of columns in the original M-by-K
 matrix reduced by DGEBRD.
 If VECT = 'P', the number of rows in the original K-by-N
 matrix reduced by DGEBRD.
 K &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the vectors which define the elementary reflectors,
 as returned by DGEBRD.
 On exit, the M-by-N matrix Q or P**T.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension
 (min(M,K)) if VECT = 'Q'
 (min(N,K)) if VECT = 'P'
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i) or G(i), which determines Q or P**T, as
 returned by DGEBRD in its array argument TAUQ or TAUP.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,min(M,N)).
 For optimum performance LWORK &gt;= min(M,N)*NB, where NB
 is the optimal blocksize.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>April 2012</dl>
<p> Definition at line 158 of file dorgbr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
