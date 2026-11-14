---
title: "zlarcm-f(3)"
name: "zlarcm-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlarcm-f/"
description: "zlarcm.f –"
---

<p>zlarcm.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlarcm</code> (M, N, A, LDA, B, LDB, C, LDC, RWORK)<br />
 <i></i><code>ZLARCM</code> copies all or part of a real two-dimensional array to a complex array.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlarcm (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldc, * )C, integerLDC, double precision, dimension( * )RWORK)</h3>
<p><code>ZLARCM</code> copies all or part of a real two-dimensional array to a complex array. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLARCM performs a very simple matrix-matrix multiplication:
 C := A * B,
 where A is M by M and real; B is M by N and complex;
 C is M by N and complex.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
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
<pre> A is DOUBLE PRECISION array, dimension (LDA, M)
 A contains the M by M matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;=max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB, N)
 B contains the M by N matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;=max(1,M).</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16 array, dimension (LDC, N)
 C contains the M by N matrix C.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;=max(1,M).</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*M*N)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 115 of file zlarcm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
