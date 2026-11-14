---
title: "dorgtr(3)"
name: "dorgtr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dorgtr/"
description: "dorgtr.f –"
---

<h2 class="name">NAME</h2>
<p> dorgtr.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dorgtr</code> (UPLO, N, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>DORGTR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dorgtr (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DORGTR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DORGTR generates a real orthogonal matrix Q which is defined as the
 product of n-1 elementary reflectors of order N, as returned by
 DSYTRD:
 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),
 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U': Upper triangle of A contains elementary reflectors
                 from DSYTRD;
          = 'L': Lower triangle of A contains elementary reflectors
                 from DSYTRD.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix Q. N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the vectors which define the elementary reflectors,
          as returned by DSYTRD.
          On exit, the N-by-N orthogonal matrix Q.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,N).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (N-1)
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i), as returned by DSYTRD.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK. LWORK &gt;= max(1,N-1).
          For optimum performance LWORK &gt;= (N-1)*NB, where NB is
          the optimal blocksize.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<dd> November 2011</dl>
<p> Definition at line 124 of file dorgtr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
