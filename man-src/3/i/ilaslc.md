---
title: "ilaslc(3)"
name: "ilaslc"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilaslc/"
description: "ilaslc.f –"
---

<h2 class="name">NAME</h2>
<p> ilaslc.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>ilaslc</code> (M, N, A, LDA)<br />
 <i></i><code>ILASLC</code> scans a matrix for its last non-zero column.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilaslc (integerM, integerN, real, dimension( lda, * )A, integerLDA)</h3>
<p> <code>ILASLC</code> scans a matrix for its last non-zero column. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 ILASLC scans A for its last non-zero column.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          The m by n matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
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
<p> Definition at line 79 of file ilaslc.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
