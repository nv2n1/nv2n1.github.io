---
title: "chesv(3)"
name: "chesv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chesv/"
description: "chesv.f –"
---

<h2 class="name">NAME</h2>
<p> chesv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chesv</code> (UPLO, N, NRHS, A, LDA, IPIV, B, LDB, WORK, LWORK, INFO)<br />
 <i></i><code> CHESV computes the solution to system of linear equations A * X = B for HE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chesv (characterUPLO, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code> CHESV computes the solution to system of linear equations A * X = B for HE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHESV computes the solution to a complex system of linear equations
    A * X = B,
 where A is an N-by-N Hermitian matrix and X and B are N-by-NRHS
 matrices.
 The diagonal pivoting method is used to factor A as
    A = U * D * U**H,  if UPLO = 'U', or
    A = L * D * L**H,  if UPLO = 'L',
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and D is Hermitian and block diagonal with
 1-by-1 and 2-by-2 diagonal blocks.  The factored form of A is then
 used to solve the system of equations A * X = B.
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
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the Hermitian matrix A.  If UPLO = 'U', the leading
          N-by-N upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading N-by-N lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
          On exit, if INFO = 0, the block diagonal matrix D and the
          multipliers used to obtain the factor U or L from the
          factorization A = U*D*U**H or A = L*D*L**H as computed by
          CHETRF.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D, as
          determined by CHETRF.  If IPIV(k) &gt; 0, then rows and columns
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
          B is COMPLEX array, dimension (LDB,NRHS)
          On entry, the N-by-NRHS right hand side matrix B.
          On exit, if INFO = 0, the N-by-NRHS solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
          LWORK is INTEGER
          The length of WORK.  LWORK &gt;= 1, and for best performance
          LWORK &gt;= max(1,N*NB), where NB is the optimal blocksize for
          CHETRF.
          for LWORK &lt; N, TRS will be done with Level BLAS 2
          for LWORK &gt;= N, TRS will be done with Level BLAS 3
          If LWORK = -1, then a workspace query is assumed;
          the routine
              only calculates the optimal size of the WORK array,
              returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = i, D(i,i) is exactly zero.  The factorization
               has been completed, but the block diagonal matrix D is
               exactly singular, so the solution could not be computed.
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
<p> Definition at line 171 of file chesv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
