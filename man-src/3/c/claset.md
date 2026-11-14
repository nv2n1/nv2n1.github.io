---
title: "claset(3)"
name: "claset"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claset/"
description: "claset.f –"
---

<h2 class="name">NAME</h2>
<p> claset.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>claset</code> (UPLO, M, N, ALPHA, BETA, A, LDA)<br />
 <i></i><code>CLASET</code> initializes the off-diagonal elements and the diagonal elements of a matrix to given values.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claset (characterUPLO, integerM, integerN, complexALPHA, complexBETA, complex, dimension( lda, * )A, integerLDA)</h3>
<p> <code>CLASET</code> initializes the off-diagonal elements and the diagonal elements of a matrix to given values. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLASET initializes a 2-D array A to BETA on the diagonal and
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
          = 'U':      Upper triangular part is set. The lower triangle
                      is unchanged.
          = 'L':      Lower triangular part is set. The upper triangle
                      is unchanged.
          Otherwise:  All of the matrix A is set.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          On entry, M specifies the number of rows of A.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          On entry, N specifies the number of columns of A.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is COMPLEX
          All the offdiagonal array elements are set to ALPHA.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is COMPLEX
          All the diagonal array elements are set to BETA.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is COMPLEX array, dimension(LDA, N) On entry, the m by n matrix A.On exit, A(i, j) = ALPHA, 1 &lt;= i &lt;= m, 1 &lt;= j &lt;= n, i.ne.j;
A(i, i) = BETA, 1 &lt;= i &lt;= min(m, n)
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
<p> Definition at line 107 of file claset.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
