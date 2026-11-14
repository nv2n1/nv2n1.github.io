---
title: "sorbdb6(3)"
name: "sorbdb6"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorbdb6/"
description: "sorbdb6.f –"
---

<p>sorbdb6.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sorbdb6</code> (M1, M2, N, X1, INCX1, X2, INCX2, Q1, LDQ1, Q2, LDQ2, WORK, LWORK, INFO)<br />
 <i></i><code>SORBDB6</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sorbdb6 (integerM1, integerM2, integerN, real, dimension(*)X1, integerINCX1, real, dimension(*)X2, integerINCX2, real, dimension(ldq1,*)Q1, integerLDQ1, real, dimension(ldq2,*)Q2, integerLDQ2, real, dimension(*)WORK, integerLWORK, integerINFO)</h3>
<p><code>SORBDB6</code> .SH &quot;Purpose:&quot; </p>
<pre> SORBDB6 orthogonalizes the column vector
 X = [ X1 ]
 [ X2 ]
 with respect to the columns of
 Q = [ Q1 ] .
 [ Q2 ]
 The columns of Q must be orthonormal.
 If the projection is zero according to Kahan's &quot;twice is enough&quot;
 criterion, then the zero vector is returned..fi
 
<code>Parameters:</code>
<dl><dt><dd><i>M1</i> 
 M1 is INTEGER
 The dimension of X1 and the number of rows in Q1. 0 &lt;= M1.</pre>
<p><i>M2</i> </p>
<pre> M2 is INTEGER
 The dimension of X2 and the number of rows in Q2. 0 &lt;= M2.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns in Q1 and Q2. 0 &lt;= N.</pre>
<p><i>X1</i> </p>
<pre> X1 is REAL array, dimension (M1)
 On entry, the top part of the vector to be orthogonalized.
 On exit, the top part of the projected vector.</pre>
<p><i>INCX1</i> </p>
<pre> INCX1 is INTEGER
 Increment for entries of X1.</pre>
<p><i>X2</i> </p>
<pre> X2 is REAL array, dimension (M2)
 On entry, the bottom part of the vector to be
 orthogonalized. On exit, the bottom part of the projected
 vector.</pre>
<p><i>INCX2</i> </p>
<pre> INCX2 is INTEGER
 Increment for entries of X2.</pre>
<p><i>Q1</i> </p>
<pre> Q1 is REAL array, dimension (LDQ1, N)
 The top part of the orthonormal basis matrix.</pre>
<p><i>LDQ1</i> </p>
<pre> LDQ1 is INTEGER
 The leading dimension of Q1. LDQ1 &gt;= M1.</pre>
<p><i>Q2</i> </p>
<pre> Q2 is REAL array, dimension (LDQ2, N)
 The bottom part of the orthonormal basis matrix.</pre>
<p><i>LDQ2</i> </p>
<pre> LDQ2 is INTEGER
 The leading dimension of Q2. LDQ2 &gt;= M2.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (LWORK)</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= N.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>July 2012</dl>
<p> Definition at line 154 of file sorbdb6.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
