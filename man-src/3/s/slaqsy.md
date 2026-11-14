---
title: "slaqsy(3)"
name: "slaqsy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaqsy/"
description: "slaqsy.f –"
---

<h2 class="name">NAME</h2>
<p> slaqsy.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaqsy</code> (UPLO, N, A, LDA, S, SCOND, AMAX, EQUED)<br />
 <i></i><code>SLAQSY</code> scales a symmetric/Hermitian matrix, using scaling factors computed by spoequ.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaqsy (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )S, realSCOND, realAMAX, characterEQUED)</h3>
<p> <code>SLAQSY</code> scales a symmetric/Hermitian matrix, using scaling factors computed by spoequ. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAQSY equilibrates a symmetric matrix A using the scaling factors
 in the vector S.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the upper or lower triangular part of the
          symmetric matrix A is stored.
          = 'U':  Upper triangular
          = 'L':  Lower triangular
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          On entry, the symmetric matrix A.  If UPLO = 'U', the leading
          n by n upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading n by n lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if EQUED = 'Y', the equilibrated matrix:
          diag(S) * A * diag(S).
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(N,1).
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (N)
          The scale factors for A.
</pre>
<p> <i>SCOND</i> </p>
<pre>
          SCOND is REAL
          Ratio of the smallest S(i) to the largest S(i).
</pre>
<p> <i>AMAX</i> </p>
<pre>
          AMAX is REAL
          Absolute value of largest matrix entry.
</pre>
<p> <i>EQUED</i> </p>
<pre>
          EQUED is CHARACTER*1
          Specifies whether or not equilibration was done.
          = 'N':  No equilibration.
          = 'Y':  Equilibration was done, i.e., A has been replaced by
                  diag(S) * A * diag(S).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre>
  THRESH is a threshold value used to decide if scaling should be done
  based on the ratio of the scaling factors.  If SCOND &lt; THRESH,
  scaling is done.
  LARGE and SMALL are threshold values used to decide if scaling should
  be done based on the absolute size of the largest matrix element.
  If AMAX &gt; LARGE or AMAX &lt; SMALL, scaling is done.
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
<p> Definition at line 134 of file slaqsy.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
