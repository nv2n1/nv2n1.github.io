---
title: "dlaset(3)"
name: "dlaset"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaset/"
description: "dlaset.f –"
---

<h2 class="name">NAME</h2>
<p> dlaset.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaset</code> (UPLO, M, N, ALPHA, BETA, A, LDA)<br />
 <i></i><code>DLASET</code> initializes the off-diagonal elements and the diagonal elements of a matrix to given values.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaset (characterUPLO, integerM, integerN, double precisionALPHA, double precisionBETA, double precision, dimension( lda, * )A, integerLDA)</h3>
<p> <code>DLASET</code> initializes the off-diagonal elements and the diagonal elements of a matrix to given values. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLASET initializes an m-by-n matrix A to BETA on the diagonal and
 ALPHA on the offdiagonals.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies the part of the matrix A to be set.
          = 'U':      Upper triangular part is set; the strictly lower
                      triangular part of A is not changed.
          = 'L':      Lower triangular part is set; the strictly upper
                      triangular part of A is not changed.
          Otherwise:  All of the matrix A is set.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is DOUBLE PRECISION
          The constant to which the offdiagonal elements are to be set.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is DOUBLE PRECISION
          The constant to which the diagonal elements are to be set.
</pre>
<p> <i>A</i> </p>
<pre><code>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On exit, the leading m-by-n submatrix of A is set as follows:
          if UPLO = 'U', A(i,j) = ALPHA, 1&lt;=i&lt;=j-1, 1&lt;=j&lt;=n,
          if UPLO = 'L', A(i,j) = ALPHA, j+1&lt;=i&lt;=m, 1&lt;=j&lt;=n,
          otherwise,     A(i,j) = ALPHA, 1&lt;=i&lt;=m, 1&lt;=j&lt;=n, i.ne.j,
          and, for all UPLO, A(i,i) = BETA, 1&lt;=i&lt;=min(m,n).
</code></pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
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
<p> Definition at line 111 of file dlaset.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
