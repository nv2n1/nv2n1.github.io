---
title: "sorgtr-f(3)"
name: "sorgtr-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorgtr-f/"
description: "sorgtr.f –"
---

<p>sorgtr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sorgtr</code> (UPLO, N, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>SORGTR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sorgtr (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SORGTR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SORGTR generates a real orthogonal matrix Q which is defined as the
 product of n-1 elementary reflectors of order N, as returned by
 SSYTRD:
 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),
 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A contains elementary reflectors
 from SSYTRD;
 = 'L': Lower triangle of A contains elementary reflectors
 from SSYTRD.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix Q. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the vectors which define the elementary reflectors,
 as returned by SSYTRD.
 On exit, the N-by-N orthogonal matrix Q.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension (N-1)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by SSYTRD.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,N-1).
 For optimum performance LWORK &gt;= (N-1)*NB, where NB is
 the optimal blocksize.
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
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 124 of file sorgtr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
