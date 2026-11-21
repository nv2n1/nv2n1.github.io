---
title: "iladlr(3)"
name: "iladlr"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iladlr/"
description: "iladlr.f –"
---

<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>iladlr</code> (M, N, A, LDA)<br />
 <i></i><code>ILADLR</code> scans a matrix for its last non-zero row.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function iladlr (integerM, integerN, double precision, dimension( lda, * )A, integerLDA)</h3>
<p> <code>ILADLR</code> scans a matrix for its last non-zero row. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
 ILADLR scans A for its last non-zero row.
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>M</i> </dd>
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
          A is DOUBLE PRECISION array, dimension (LDA,N)
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
</dt><dd> Univ. of Tennessee </dd>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
</dt><dd> September 2012</dd></dl>
<p> Definition at line 79 of file iladlr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
