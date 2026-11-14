---
title: "clag2z(3)"
name: "clag2z"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clag2z/"
description: "clag2z.f –"
---

<h2 class="name">NAME</h2>
<p> clag2z.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clag2z</code> (M, N, SA, LDSA, A, LDA, INFO)<br />
 <i></i><code>CLAG2Z</code> converts a complex single precision matrix to a complex double precision matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clag2z (integerM, integerN, complex, dimension( ldsa, * )SA, integerLDSA, complex*16, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p> <code>CLAG2Z</code> converts a complex single precision matrix to a complex double precision matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLAG2Z converts a COMPLEX matrix, SA, to a COMPLEX*16 matrix, A.
 Note that while it is possible to overflow while converting
 from double to single, it is not possible to overflow when
 converting from single to double.
 This is an auxiliary routine so there is no argument checking.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of lines of the matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
</pre>
<p> <i>SA</i> </p>
<pre>
          SA is COMPLEX array, dimension (LDSA,N)
          On entry, the M-by-N coefficient matrix SA.
</pre>
<p> <i>LDSA</i> </p>
<pre>
          LDSA is INTEGER
          The leading dimension of the array SA.  LDSA &gt;= max(1,M).
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX*16 array, dimension (LDA,N)
          On exit, the M-by-N coefficient matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> Definition at line 104 of file clag2z.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
