---
title: "clarcm-f(3)"
name: "clarcm-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clarcm-f/"
description: "clarcm.f –"
---

<p>clarcm.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clarcm</code> (M, N, A, LDA, B, LDB, C, LDC, RWORK)<br />
 <i></i><code>CLARCM</code> copies all or part of a real two-dimensional array to a complex array.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clarcm (integerM, integerN, real, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldc, * )C, integerLDC, real, dimension( * )RWORK)</h3>
<p><code>CLARCM</code> copies all or part of a real two-dimensional array to a complex array. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLARCM performs a very simple matrix-matrix multiplication:
 C := A * B,
 where A is M by M and real; B is M by N and complex;
 C is M by N and complex.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A and of the matrix C.
 M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns and rows of the matrix B and
 the number of columns of the matrix C.
 N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA, M)
 A contains the M by M matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;=max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB, N)
 B contains the M by N matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;=max(1,M).</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX array, dimension (LDC, N)
 C contains the M by N matrix C.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;=max(1,M).</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (2*M*N)</pre>
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
<p> Definition at line 115 of file clarcm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
