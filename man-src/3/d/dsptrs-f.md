---
title: "dsptrs-f(3)"
name: "dsptrs-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsptrs-f/"
description: "dsptrs.f –"
---

<p>dsptrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dsptrs</code> (UPLO, N, NRHS, AP, IPIV, B, LDB, INFO)<br />
 <i></i><code>DSPTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsptrs (characterUPLO, integerN, integerNRHS, double precision, dimension( * )AP, integer, dimension( * )IPIV, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>DSPTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSPTRS solves a system of linear equations A*X = B with a real
 symmetric matrix A stored in packed format using the factorization
 A = U*D*U**T or A = L*D*L**T computed by DSPTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**T;
 = 'L': Lower triangular, form is A = L*D*L**T.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is DOUBLE PRECISION array, dimension (N*(N+1)/2)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by DSPTRF, stored as a
 packed triangular matrix.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by DSPTRF.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB,NRHS)
 On entry, the right hand side matrix B.
 On exit, the solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 116 of file dsptrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
