---
title: "spbtrs-f(3)"
name: "spbtrs-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spbtrs-f/"
description: "spbtrs.f –"
---

<p>spbtrs.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>spbtrs</code> (UPLO, N, KD, NRHS, AB, LDAB, B, LDB, INFO)<br />
 <i></i><code>SPBTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spbtrs (characterUPLO, integerN, integerKD, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code>SPBTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 SPBTRS solves a system of linear equations A*X = B with a symmetric
 positive definite band matrix A using the Cholesky factorization
 A = U**T*U or A = L*L**T computed by SPBTRF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangular factor stored in AB;
          = 'L':  Lower triangular factor stored in AB.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>KD</i> </p>
<pre>
          KD is INTEGER
          The number of superdiagonals of the matrix A if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'.  KD &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre>
          AB is REAL array, dimension (LDAB,N)
          The triangular factor U or L from the Cholesky factorization
          A = U**T*U or A = L*L**T of the band matrix A, stored in the
          first KD+1 rows of the array.  The j-th column of U or L is
          stored in the j-th column of the array AB as follows:
          if UPLO ='U', AB(kd+1+i-j,j) = U(i,j) for max(1,j-kd)&lt;=i&lt;=j;
          if UPLO ='L', AB(1+i-j,j)    = L(i,j) for j&lt;=i&lt;=min(n,j+kd).
</pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KD+1.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
          On entry, the right hand side matrix B.
          On exit, the solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> November 2011</dl>
<p> Definition at line 122 of file spbtrs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
