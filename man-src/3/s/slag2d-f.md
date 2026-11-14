---
title: "slag2d-f(3)"
name: "slag2d-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slag2d-f/"
description: "slag2d.f –"
---

<p>slag2d.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slag2d</code> (M, N, SA, LDSA, A, LDA, INFO)<br />
 <i></i><code>SLAG2D</code> converts a single precision matrix to a double precision matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slag2d (integerM, integerN, real, dimension( ldsa, * )SA, integerLDSA, double precision, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p><code>SLAG2D</code> converts a single precision matrix to a double precision matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAG2D converts a SINGLE PRECISION matrix, SA, to a DOUBLE
 PRECISION matrix, A.
 Note that while it is possible to overflow while converting
 from double to single, it is not possible to overflow when
 converting from single to double.
 This is an auxiliary routine so there is no argument checking.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of lines of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>SA</i> </p>
<pre> SA is REAL array, dimension (LDSA,N)
 On entry, the M-by-N coefficient matrix SA.</pre>
<p><i>LDSA</i> </p>
<pre> LDSA is INTEGER
 The leading dimension of the array SA. LDSA &gt;= max(1,M).</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On exit, the M-by-N coefficient matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit</pre>
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
<p> Definition at line 105 of file slag2d.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
