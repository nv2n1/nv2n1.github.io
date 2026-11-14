---
title: "cpptrs-f(3)"
name: "cpptrs-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpptrs-f/"
description: "cpptrs.f –"
---

<p>cpptrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cpptrs</code> (UPLO, N, NRHS, AP, B, LDB, INFO)<br />
 <i></i><code>CPPTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpptrs (characterUPLO, integerN, integerNRHS, complex, dimension( * )AP, complex, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p><code>CPPTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CPPTRS solves a system of linear equations A*X = B with a Hermitian
 positive definite matrix A in packed storage using the Cholesky
 factorization A = U**H*U or A = L*L**H computed by CPPTRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX array, dimension (N*(N+1)/2)
 The triangular factor U or L from the Cholesky factorization
 A = U**H*U or A = L*L**H, packed columnwise in a linear
 array. The j-th column of U or L is stored in the array AP
 as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j&lt;=i&lt;=n.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,NRHS)
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
<p> Definition at line 109 of file cpptrs.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
