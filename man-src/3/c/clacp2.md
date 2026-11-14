---
title: "clacp2(3)"
name: "clacp2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clacp2/"
description: "clacp2.f –"
---

<h2 class="name">NAME</h2>
<p> clacp2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clacp2</code> (UPLO, M, N, A, LDA, B, LDB)<br />
 <i></i><code>CLACP2</code> copies all or part of a real two-dimensional array to a complex array.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clacp2 (characterUPLO, integerM, integerN, real, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB)</h3>
<p> <code>CLACP2</code> copies all or part of a real two-dimensional array to a complex array. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLACP2 copies all or part of a real two-dimensional matrix A to a
 complex matrix B.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies the part of the matrix A to be copied to B.
          = 'U':      Upper triangular part
          = 'L':      Lower triangular part
          Otherwise:  All of the matrix A
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
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          The m by n matrix A.  If UPLO = 'U', only the upper trapezium
          is accessed; if UPLO = 'L', only the lower trapezium is
          accessed.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,N)
          On exit, B = A in the locations specified by UPLO.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,M).
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
<p> Definition at line 105 of file clacp2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
