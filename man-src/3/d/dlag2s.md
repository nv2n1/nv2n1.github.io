---
title: "dlag2s(3)"
name: "dlag2s"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlag2s/"
description: "dlag2s.f –"
---

<h2 class="name">NAME</h2>
<p> dlag2s.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlag2s</code> (M, N, A, LDA, SA, LDSA, INFO)<br />
 <i></i><code>DLAG2S</code> converts a double precision matrix to a single precision matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlag2s (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, real, dimension( ldsa, * )SA, integerLDSA, integerINFO)</h3>
<p> <code>DLAG2S</code> converts a double precision matrix to a single precision matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAG2S converts a DOUBLE PRECISION matrix, SA, to a SINGLE
 PRECISION matrix, A.
 RMAX is the overflow for the SINGLE PRECISION arithmetic
 DLAG2S checks that all the entries of A are between -RMAX and
 RMAX. If not the convertion is aborted and a flag is raised.
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
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the M-by-N coefficient matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>SA</i> </p>
<pre>
          SA is REAL array, dimension (LDSA,N)
          On exit, if INFO=0, the M-by-N coefficient matrix SA; if
          INFO&gt;0, the content of SA is unspecified.
</pre>
<p> <i>LDSA</i> </p>
<pre>
          LDSA is INTEGER
          The leading dimension of the array SA.  LDSA &gt;= max(1,M).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          = 1:  an entry of the matrix A is greater than the SINGLE
                PRECISION overflow threshold, in this case, the content
                of SA in exit is unspecified.
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
<p> Definition at line 109 of file dlag2s.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
