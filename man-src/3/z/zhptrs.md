---
title: "zhptrs(3)"
name: "zhptrs"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhptrs/"
description: "zhptrs.f –"
---

<p>zhptrs.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhptrs</code> (UPLO, N, NRHS, AP, IPIV, B, LDB, INFO)<br />
 <i></i><code>ZHPTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhptrs (characterUPLO, integerN, integerNRHS, complex*16, dimension( * )AP, integer, dimension( * )IPIV, complex*16, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>ZHPTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZHPTRS solves a system of linear equations A*X = B with a complex
 Hermitian matrix A stored in packed format using the factorization
 A = U*D*U**H or A = L*D*L**H computed by ZHPTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**H;
 = 'L': Lower triangular, form is A = L*D*L**H.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by ZHPTRF, stored as a
 packed triangular matrix.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by ZHPTRF.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
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
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 116 of file zhptrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
