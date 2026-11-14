---
title: "checon_rook(3)"
name: "checon_rook"
section: "3"
letter: "c"
url: "/docs/linux/man/3-checon_rook/"
description: "checon_rook.f –"
---

<h2 class="name">NAME</h2>
<p> checon_rook.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>checon_rook</code> (UPLO, N, A, LDA, IPIV, ANORM, RCOND, WORK, INFO)<br />
 <i></i><code>CHECON_ROOK</code> estimates the reciprocal of the condition number fort HE matrices using factorization obtained with one of the bounded diagonal pivoting methods (max 2 interchanges)</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine checon_rook (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, realANORM, realRCOND, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CHECON_ROOK</code> estimates the reciprocal of the condition number fort HE matrices using factorization obtained with one of the bounded diagonal pivoting methods (max 2 interchanges) </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHECON_ROOK estimates the reciprocal of the condition number of a complex
 Hermitian matrix A using the factorization A = U*D*U**H or
 A = L*D*L**H computed by CHETRF_ROOK.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).
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
<p> <i>ANORM</i> </p>
<pre>
          ANORM is REAL
          The 1-norm of the original matrix A.
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
          estimate of the 1-norm of inv(A) computed in this routine.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N)
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
</dl>
<p> November 2013, Igor Kozachenko, Computer Science Division, University of California, Berkeley </p>
<p> September 2007, Sven Hammarling, Nicholas J. Higham, Craig Lucas, School of Mathematics, University of Manchester </p>
<p> Definition at line 139 of file checon_rook.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
