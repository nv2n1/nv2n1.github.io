---
title: "dspsv(3)"
name: "dspsv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dspsv/"
description: "dspsv.f –"
---

<h2 class="name">NAME</h2>
<p> dspsv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dspsv</code> (UPLO, N, NRHS, AP, IPIV, B, LDB, INFO)<br />
 <i></i><code> DSPSV computes the solution to system of linear equations A * X = B for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dspsv (characterUPLO, integerN, integerNRHS, double precision, dimension( * )AP, integer, dimension( * )IPIV, double precision, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code> DSPSV computes the solution to system of linear equations A * X = B for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DSPSV computes the solution to a real system of linear equations
    A * X = B,
 where A is an N-by-N symmetric matrix stored in packed format and X
 and B are N-by-NRHS matrices.
 The diagonal pivoting method is used to factor A as
    A = U * D * U**T,  if UPLO = 'U', or
    A = L * D * L**T,  if UPLO = 'L',
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, D is symmetric and block diagonal with 1-by-1
 and 2-by-2 diagonal blocks.  The factored form of A is then used to
 solve the system of equations A * X = B.
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
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is DOUBLE PRECISION array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the symmetric matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          See below for further details.
          On exit, the block diagonal matrix D and the multipliers used
          to obtain the factor U or L from the factorization
          A = U*D*U**T or A = L*D*L**T as computed by DSPTRF, stored as
          a packed triangular matrix in the same storage format as A.
</code></pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D, as
          determined by DSPTRF.  If IPIV(k) &gt; 0, then rows and columns
          k and IPIV(k) were interchanged, and D(k,k) is a 1-by-1
          diagonal block.  If UPLO = 'U' and IPIV(k) = IPIV(k-1) &lt; 0,
          then rows and columns k-1 and -IPIV(k) were interchanged and
          D(k-1:k,k-1:k) is a 2-by-2 diagonal block.  If UPLO = 'L' and
          IPIV(k) = IPIV(k+1) &lt; 0, then rows and columns k+1 and
          -IPIV(k) were interchanged and D(k:k+1,k:k+1) is a 2-by-2
          diagonal block.
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,NRHS)
          On entry, the N-by-NRHS right hand side matrix B.
          On exit, if INFO = 0, the N-by-NRHS solution matrix X.
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
          &gt; 0:  if INFO = i, D(i,i) is exactly zero.  The factorization
                has been completed, but the block diagonal matrix D is
                exactly singular, so the solution could not be
                computed.
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
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The packed storage scheme is illustrated by the following example
  when N = 4, UPLO = 'U':
  Two-dimensional storage of the symmetric matrix A:
     a11 a12 a13 a14
         a22 a23 a24
             a33 a34     (aij = aji)
                 a44
  Packed storage of the upper triangle of A:
  AP = [ a11, a12, a22, a13, a23, a33, a14, a24, a34, a44 ]
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 163 of file dspsv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
