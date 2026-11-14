---
title: "cla_syrcond_x(3)"
name: "cla_syrcond_x"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_syrcond_x/"
description: "cla_syrcond_x.f –"
---

<h2 class="name">NAME</h2>
<p> cla_syrcond_x.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>cla_syrcond_x</code> (UPLO, N, A, LDA, AF, LDAF, IPIV, X, INFO, WORK, RWORK)<br />
 <i></i><code>CLA_SYRCOND_X</code> computes the infinity norm condition number of op(A)*diag(x) for symmetric indefinite matrices.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function cla_syrcond_x (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, complex, dimension( * )X, integerINFO, complex, dimension( * )WORK, real, dimension( * )RWORK)</h3>
<p> <code>CLA_SYRCOND_X</code> computes the infinity norm condition number of op(A)*diag(x) for symmetric indefinite matrices. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    CLA_SYRCOND_X Computes the infinity norm condition number of
    op(A) * diag(X) where X is a COMPLEX vector.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
       = 'U':  Upper triangle of A is stored;
       = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
     The number of linear equations, i.e., the order of the
     matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
     On entry, the N-by-N matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
     The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AF</i> </p>
<pre>
          AF is COMPLEX array, dimension (LDAF,N)
     The block diagonal matrix D and the multipliers used to
     obtain the factor U or L as computed by CSYTRF.
</pre>
<p> <i>LDAF</i> </p>
<pre>
          LDAF is INTEGER
     The leading dimension of the array AF.  LDAF &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
     Details of the interchanges and the block structure of D
     as determined by CSYTRF.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (N)
     The vector X in the formula op(A) * diag(X).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
       = 0:  Successful exit.
     i &gt; 0:  The ith argument is invalid.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N).
     Workspace.
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N).
     Workspace.
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
<p> Definition at line 131 of file cla_syrcond_x.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
