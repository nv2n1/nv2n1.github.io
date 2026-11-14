---
title: "zungql(3)"
name: "zungql"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zungql/"
description: "zungql.f –"
---

<p>zungql.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zungql</code> (M, N, K, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>ZUNGQL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zungql (integerM, integerN, integerK, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>ZUNGQL</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZUNGQL generates an M-by-N complex matrix Q with orthonormal columns,
 which is defined as the last N columns of a product of K elementary
 reflectors of order M
 Q = H(k) . . . H(2) H(1)
 as returned by ZGEQLF.</pre>
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
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the (n-k+i)-th column must contain the vector which
 defines the elementary reflector H(i), for i = 1,2,...,k, as
 returned by ZGEQLF in the last k columns of its array
 argument A.
 On exit, the M-by-N matrix Q.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The first dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (K)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by ZGEQLF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,N).
 For optimum performance LWORK &gt;= N*NB, where NB is the
 optimal blocksize.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
<dd>November 2011</dl>
<p> Definition at line 129 of file zungql.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
