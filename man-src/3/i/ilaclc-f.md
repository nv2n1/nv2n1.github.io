---
title: "ilaclc-f(3)"
name: "ilaclc-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilaclc-f/"
description: "ilaclc.f –"
---

<p>ilaclc.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>ilaclc</code> (M, N, A, LDA)<br />
 <i></i><code>ILACLC</code> scans a matrix for its last non-zero column.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilaclc (integerM, integerN, complex, dimension( lda, * )A, integerLDA)</h3>
<p><code>ILACLC</code> scans a matrix for its last non-zero column. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> ILACLC scans A for its last non-zero column.</pre>
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
<pre> A is COMPLEX array, dimension (LDA,N)
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
<p> Definition at line 79 of file ilaclc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
