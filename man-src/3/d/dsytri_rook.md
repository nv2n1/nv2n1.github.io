---
title: "dsytri_rook(3)"
name: "dsytri_rook"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsytri_rook/"
description: "dsytri_rook.f –"
---

<h2 class="name">NAME</h2>
<p> dsytri_rook.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dsytri_rook</code> (UPLO, N, A, LDA, IPIV, WORK, INFO)<br />
 <i></i><code>DSYTRI_ROOK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsytri_rook (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DSYTRI_ROOK</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DSYTRI_ROOK computes the inverse of a real symmetric
 matrix A using the factorization A = U*D*U**T or A = L*D*L**T
 computed by DSYTRF_ROOK.
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
          = 'U':  Upper triangular, form is A = U*D*U**T;
          = 'L':  Lower triangular, form is A = L*D*L**T.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the block diagonal matrix D and the multipliers
          used to obtain the factor U or L as computed by DSYTRF_ROOK.
          On exit, if INFO = 0, the (symmetric) inverse of the original
          matrix.  If UPLO = 'U', the upper triangular part of the
          inverse is formed and the part of A below the diagonal is not
          referenced; if UPLO = 'L' the lower triangular part of the
          inverse is formed and the part of A above the diagonal is
          not referenced.
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
          as determined by DSYTRF_ROOK.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : if INFO = i, D(i, i) = 0;
the matrix is singular and its
    inverse could not be computed.
</code></pre>
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
<dd> April 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd>
<pre>
   April 2012, Igor Kozachenko,
                  Computer Science Division,
                  University of California, Berkeley
  September 2007, Sven Hammarling, Nicholas J. Higham, Craig Lucas,
                  School of Mathematics,
                  University of Manchester
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 130 of file dsytri_rook.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
