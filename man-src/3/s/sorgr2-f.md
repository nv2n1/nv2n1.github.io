---
title: "sorgr2-f(3)"
name: "sorgr2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorgr2-f/"
description: "sorgr2.f –"
---

<p>sorgr2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sorgr2</code> (M, N, K, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>SORGR2</code> generates all or part of the orthogonal matrix Q from an RQ factorization determined by sgerqf (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sorgr2 (integerM, integerN, integerK, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( * )WORK, integerINFO)</h3>
<p><code>SORGR2</code> generates all or part of the orthogonal matrix Q from an RQ factorization determined by sgerqf (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SORGR2 generates an m by n real matrix Q with orthonormal rows,
 which is defined as the last m rows of a product of k elementary
 reflectors of order n
 Q = H(1) H(2) . . . H(k)
 as returned by SGERQF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix Q. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix Q. N &gt;= M.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The number of elementary reflectors whose product defines the
 matrix Q. M &gt;= K &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the (m-k+i)-th row must contain the vector which
 defines the elementary reflector H(i), for i = 1,2,...,k, as
 returned by SGERQF in the last k rows of its array argument
 A.
 On exit, the m by n matrix Q.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The first dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by SGERQF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (M)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument has an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 115 of file sorgr2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
