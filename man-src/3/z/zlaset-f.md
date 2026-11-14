---
title: "zlaset-f(3)"
name: "zlaset-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaset-f/"
description: "zlaset.f –"
---

<p>zlaset.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaset</code> (UPLO, M, N, ALPHA, BETA, A, LDA)<br />
 <i></i><code>ZLASET</code> initializes the off-diagonal elements and the diagonal elements of a matrix to given values.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaset (characterUPLO, integerM, integerN, complex*16ALPHA, complex*16BETA, complex*16, dimension( lda, * )A, integerLDA)</h3>
<p><code>ZLASET</code> initializes the off-diagonal elements and the diagonal elements of a matrix to given values. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLASET initializes a 2-D array A to BETA on the diagonal and
 ALPHA on the offdiagonals.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies the part of the matrix A to be set.
 = 'U': Upper triangular part is set. The lower triangle
 is unchanged.
 = 'L': Lower triangular part is set. The upper triangle
 is unchanged.
 Otherwise: All of the matrix A is set.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 On entry, M specifies the number of rows of A.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the number of columns of A.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX*16
 All the offdiagonal array elements are set to ALPHA.</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX*16
 All the diagonal array elements are set to BETA.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the m by n matrix A.
 On exit, A(i,j) = ALPHA, 1 &lt;= i &lt;= m, 1 &lt;= j &lt;= n, i.ne.j;
 A(i,i) = BETA , 1 &lt;= i &lt;= min(m,n)</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
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
<p> Definition at line 107 of file zlaset.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
