---
title: "sorg2l-f(3)"
name: "sorg2l-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorg2l-f/"
description: "sorg2l.f –"
---

<p>sorg2l.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sorg2l</code> (M, N, K, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>SORG2L</code> generates all or part of the orthogonal matrix Q from a QL factorization determined by sgeqlf (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sorg2l (integerM, integerN, integerK, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( * )WORK, integerINFO)</h3>
<p><code>SORG2L</code> generates all or part of the orthogonal matrix Q from a QL factorization determined by sgeqlf (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SORG2L generates an m by n real matrix Q with orthonormal columns,
 which is defined as the last n columns of a product of k elementary
 reflectors of order m
 Q = H(k) . . . H(2) H(1)
 as returned by SGEQLF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix Q. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix Q. M &gt;= N &gt;= 0.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The number of elementary reflectors whose product defines the
 matrix Q. N &gt;= K &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the (n-k+i)-th column must contain the vector which
 defines the elementary reflector H(i), for i = 1,2,...,k, as
 returned by SGEQLF in the last k columns of its array
 argument A.
 On exit, the m by n matrix Q.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The first dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by SGEQLF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (N)</pre>
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
<p> Definition at line 115 of file sorg2l.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
