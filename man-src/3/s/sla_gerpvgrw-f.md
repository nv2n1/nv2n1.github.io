---
title: "sla_gerpvgrw-f(3)"
name: "sla_gerpvgrw-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sla_gerpvgrw-f/"
description: "sla_gerpvgrw.f –"
---

<p>sla_gerpvgrw.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>sla_gerpvgrw</code> (N, NCOLS, A, LDA, AF, LDAF)<br />
 <i></i><code>SLA_GERPVGRW</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function sla_gerpvgrw (integerN, integerNCOLS, real, dimension( lda, * )A, integerLDA, real, dimension( ldaf, * )AF, integerLDAF)</h3>
<p><code>SLA_GERPVGRW</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLA_GERPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The &quot;max absolute element&quot; norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>NCOLS</i> </p>
<pre> NCOLS is INTEGER
 The number of columns of the matrix A. NCOLS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the N-by-N matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is REAL array, dimension (LDAF,N)
 The factors L and U from the factorization
 A = P*L*U as computed by SGETRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 98 of file sla_gerpvgrw.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
