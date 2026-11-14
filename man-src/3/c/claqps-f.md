---
title: "claqps-f(3)"
name: "claqps-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claqps-f/"
description: "claqps.f –"
---

<p>claqps.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>claqps</code> (M, N, OFFSET, NB, KB, A, LDA, JPVT, TAU, VN1, VN2, AUXV, F, LDF)<br />
 <i></i><code>CLAQPS</code> computes a step of QR factorization with column pivoting of a real m-by-n matrix A by using BLAS level 3.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claqps (integerM, integerN, integerOFFSET, integerNB, integerKB, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )JPVT, complex, dimension( * )TAU, real, dimension( * )VN1, real, dimension( * )VN2, complex, dimension( * )AUXV, complex, dimension( ldf, * )F, integerLDF)</h3>
<p><code>CLAQPS</code> computes a step of QR factorization with column pivoting of a real m-by-n matrix A by using BLAS level 3. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLAQPS computes a step of QR factorization with column pivoting
 of a complex M-by-N matrix A by using Blas-3. It tries to factorize
 NB columns from A starting from the row OFFSET+1, and updates all
 of the matrix with Blas-3 xGEMM.
 In some cases, due to catastrophic cancellations, it cannot
 factorize NB columns. Hence, the actual number of factorized
 columns is returned in KB.
 Block A(1:OFFSET,1:N) is accordingly pivoted, but not factorized.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0</pre>
<p><i>OFFSET</i> </p>
<pre> OFFSET is INTEGER
 The number of rows of A that have been factorized in
 previous steps.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The number of columns to factorize.</pre>
<p><i>KB</i> </p>
<pre> KB is INTEGER
 The number of columns actually factorized.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, block A(OFFSET+1:M,1:KB) is the triangular
 factor obtained and block A(1:OFFSET,1:N) has been
 accordingly pivoted, but no factorized.
 The rest of the matrix, block A(OFFSET+1:M,KB+1:N) has
 been updated.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>JPVT</i> </p>
<pre> JPVT is INTEGER array, dimension (N)
 JPVT(I) = K &lt;==&gt; Column K of the full matrix A has been
 permuted into position I in AP.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX array, dimension (KB)
 The scalar factors of the elementary reflectors.</pre>
<p><i>VN1</i> </p>
<pre> VN1 is REAL array, dimension (N)
 The vector with the partial column norms.</pre>
<p><i>VN2</i> </p>
<pre> VN2 is REAL array, dimension (N)
 The vector with the exact column norms.</pre>
<p><i>AUXV</i> </p>
<pre> AUXV is COMPLEX array, dimension (NB)
 Auxiliar vector.</pre>
<p><i>F</i> </p>
<pre> F is COMPLEX array, dimension (LDF,NB)
 Matrix F**H = L * Y**H * A.</pre>
<p><i>LDF</i> </p>
<pre> LDF is INTEGER
 The leading dimension of the array F. LDF &gt;= max(1,N).</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>G. Quintana-Orti, Depto. de Informatica, Universidad Jaime I, Spain X. Sun, Computer Science Dept., Duke University, USA</dl>
<p>&nbsp;<wbr>Partial column norm updating strategy modified on April 2011 Z. Drmac and Z. Bujanovic, Dept. of Mathematics, University of Zagreb, Croatia.&nbsp;<wbr> </p>
<p> <code>References: </code></p>
<dl COMPACT>
<dd>LAPACK Working Note 176</dl>
<p> Definition at line 178 of file claqps.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
