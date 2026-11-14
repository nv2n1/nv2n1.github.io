---
title: "chetrs_rook(3)"
name: "chetrs_rook"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chetrs_rook/"
description: "chetrs_rook.f –"
---

<h2 class="name">NAME</h2>
<p> chetrs_rook.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chetrs_rook</code> (UPLO, N, NRHS, A, LDA, IPIV, B, LDB, INFO)<br />
 <i></i><code>CHETRS_ROOK</code> computes the solution to a system of linear equations A * X = B for HE matrices using factorization obtained with one of the bounded diagonal pivoting methods (max 2 interchanges)</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chetrs_rook (characterUPLO, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code>CHETRS_ROOK</code> computes the solution to a system of linear equations A * X = B for HE matrices using factorization obtained with one of the bounded diagonal pivoting methods (max 2 interchanges) </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHETRS_ROOK solves a system of linear equations A*X = B with a complex
 Hermitian matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by CHETRF_ROOK.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the details of the factorization are stored
          as an upper or lower triangular matrix.
          = 'U':  Upper triangular, form is A = U*D*U**H;
          = 'L':  Lower triangular, form is A = L*D*L**H.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          The block diagonal matrix D and the multipliers used to
          obtain the factor U or L as computed by CHETRF_ROOK.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D
          as determined by CHETRF_ROOK.
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
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
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> November 2013</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd>
<pre>
  November 2013,  Igor Kozachenko,
                  Computer Science Division,
                  University of California, Berkeley
  September 2007, Sven Hammarling, Nicholas J. Higham, Craig Lucas,
                  School of Mathematics,
                  University of Manchester
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 136 of file chetrs_rook.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
