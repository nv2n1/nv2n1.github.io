---
title: "dorg2r-f(3)"
name: "dorg2r-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dorg2r-f/"
description: "dorg2r.f –"
---

<p>dorg2r.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dorg2r</code> (M, N, K, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>DORG2R</code> generates all or part of the orthogonal matrix Q from a QR factorization determined by sgeqrf (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dorg2r (integerM, integerN, integerK, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DORG2R</code> generates all or part of the orthogonal matrix Q from a QR factorization determined by sgeqrf (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DORG2R generates an m by n real matrix Q with orthonormal columns,
 which is defined as the first n columns of a product of k elementary
 reflectors of order m
 Q = H(1) H(2) . . . H(k)
 as returned by DGEQRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the i-th column must contain the vector which
 defines the elementary reflector H(i), for i = 1,2,...,k, as
 returned by DGEQRF in the first k columns of its array
 argument A.
 On exit, the m-by-n matrix Q.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The first dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by DGEQRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument has an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 115 of file dorg2r.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
