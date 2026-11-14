---
title: "ilazlr-f(3)"
name: "ilazlr-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilazlr-f/"
description: "ilazlr.f –"
---

<p>ilazlr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>ilazlr</code> (M, N, A, LDA)<br />
 <i></i><code>ILAZLR</code> scans a matrix for its last non-zero row.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilazlr (integerM, integerN, complex*16, dimension( lda, * )A, integerLDA)</h3>
<p><code>ILAZLR</code> scans a matrix for its last non-zero row. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> ILAZLR scans A for its last non-zero row.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The m by n matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 79 of file ilazlr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
