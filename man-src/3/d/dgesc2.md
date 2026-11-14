---
title: "dgesc2(3)"
name: "dgesc2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgesc2/"
description: "dgesc2.f –"
---

<h2 class="name">NAME</h2>
<p> dgesc2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgesc2</code> (N, A, LDA, RHS, IPIV, JPIV, SCALE)<br />
 <i></i><code>DGESC2</code> solves a system of linear equations using the LU factorization with complete pivoting computed by sgetc2.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgesc2 (integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )RHS, integer, dimension( * )IPIV, integer, dimension( * )JPIV, double precisionSCALE)</h3>
<p> <code>DGESC2</code> solves a system of linear equations using the LU factorization with complete pivoting computed by sgetc2. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGESC2 solves a system of linear equations
           A * X = scale* RHS
 with a general N-by-N matrix A using the LU factorization with
 complete pivoting computed by DGETC2.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the  LU part of the factorization of the n-by-n
          matrix A computed by DGETC2:  A = P * L * U * Q
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1, N).
</pre>
<p> <i>RHS</i> </p>
<pre>
          RHS is DOUBLE PRECISION array, dimension (N).
          On entry, the right hand side vector b.
          On exit, the solution vector X.
</pre>
<p> <i>IPIV</i> </p>
<pre><code>
IPIV is INTEGER array, dimension(N).The pivot indices; for
1 &lt;= i &lt;= N, row i of the
                 matrix has been interchanged with row
                 IPIV(i)
                     .
</code></pre>
<p> <i>JPIV</i> </p>
<pre><code>
JPIV is INTEGER array, dimension(N).The pivot indices; for
1 &lt;= j &lt;= N, column j of the
                 matrix has been interchanged with column
                 JPIV(j)
                     .
</code></pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is DOUBLE PRECISION
          On exit, SCALE contains the scale factor. SCALE is chosen
          0 &lt;= SCALE &lt;= 1 to prevent owerflow in the solution.
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> Definition at line 115 of file dgesc2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
