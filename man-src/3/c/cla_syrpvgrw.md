---
title: "cla_syrpvgrw(3)"
name: "cla_syrpvgrw"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_syrpvgrw/"
description: "cla_syrpvgrw.f –"
---

<h2 class="name">NAME</h2>
<p> cla_syrpvgrw.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>cla_syrpvgrw</code> (UPLO, N, INFO, A, LDA, AF, LDAF, IPIV, WORK)<br />
 <i></i><code>CLA_SYRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric indefinite matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function cla_syrpvgrw (character*1UPLO, integerN, integerINFO, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, real, dimension( * )WORK)</h3>
<p> <code>CLA_SYRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric indefinite matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLA_SYRPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The &quot;max absolute element&quot; norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.
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
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
     The value of INFO returned from CSYTRF, .i.e., the pivot in
     column INFO is exactly 0.
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
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N)
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
<p> Definition at line 123 of file cla_syrpvgrw.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
