---
title: "zlat2c(3)"
name: "zlat2c"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlat2c/"
description: "zlat2c.f –"
---

<p>zlat2c.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlat2c</code> (UPLO, N, A, LDA, SA, LDSA, INFO)<br />
 <i></i><code>ZLAT2C</code> converts a double complex triangular matrix to a complex triangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlat2c (characterUPLO, integerN, complex*16, dimension( lda, * )A, integerLDA, complex, dimension( ldsa, * )SA, integerLDSA, integerINFO)</h3>
<p><code>ZLAT2C</code> converts a double complex triangular matrix to a complex triangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAT2C converts a COMPLEX*16 triangular matrix, SA, to a COMPLEX
 triangular matrix, A.
 RMAX is the overflow for the SINGLE PRECISION arithmetic
 ZLAT2C checks that all the entries of A are between -RMAX and
 RMAX. If not the convertion is aborted and a flag is raised.
 This is an auxiliary routine so there is no argument checking.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of rows and columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the N-by-N triangular coefficient matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>SA</i> </p>
<pre> SA is COMPLEX array, dimension (LDSA,N)
 Only the UPLO part of SA is referenced. On exit, if INFO=0,
 the N-by-N coefficient matrix SA; if INFO&gt;0, the content of
 the UPLO part of SA is unspecified.</pre>
<p><i>LDSA</i> </p>
<pre> LDSA is INTEGER
 The leading dimension of the array SA. LDSA &gt;= max(1,M).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 = 1: an entry of the matrix A is greater than the SINGLE
 PRECISION overflow threshold, in this case, the content
 of the UPLO part of SA in exit is unspecified.</pre>
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
<p> Definition at line 112 of file zlat2c.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
