---
title: "cungl2(3)"
name: "cungl2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cungl2/"
description: "cungl2.f –"
---

<h2 class="name">NAME</h2>
<p> cungl2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cungl2</code> (M, N, K, A, LDA, TAU, WORK, INFO)<br />
 <i></i><code>CUNGL2</code> generates all or part of the unitary matrix Q from an LQ factorization determined by cgelqf (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cungl2 (integerM, integerN, integerK, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )TAU, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CUNGL2</code> generates all or part of the unitary matrix Q from an LQ factorization determined by cgelqf (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CUNGL2 generates an m-by-n complex matrix Q with orthonormal rows,
 which is defined as the first m rows of a product of k elementary
 reflectors of order n
       Q  =  H(k)**H . . . H(2)**H H(1)**H
 as returned by CGELQF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix Q. M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix Q. N &gt;= M.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
          The number of elementary reflectors whose product defines the
          matrix Q. M &gt;= K &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the i-th row must contain the vector which defines
          the elementary reflector H(i), for i = 1,2,...,k, as returned
          by CGELQF in the first k rows of its array argument A.
          On exit, the m by n matrix Q.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The first dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX array, dimension (K)
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i), as returned by CGELQF.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (M)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument has an illegal value
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
<p> Definition at line 114 of file cungl2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
