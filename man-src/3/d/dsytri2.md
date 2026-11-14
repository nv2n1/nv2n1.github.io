---
title: "dsytri2(3)"
name: "dsytri2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsytri2/"
description: "dsytri2.f –"
---

<h2 class="name">NAME</h2>
<p> dsytri2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dsytri2</code> (UPLO, N, A, LDA, IPIV, WORK, LWORK, INFO)<br />
 <i></i><code>DSYTRI2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsytri2 (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DSYTRI2</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DSYTRI2 computes the inverse of a DOUBLE PRECISION symmetric indefinite matrix
 A using the factorization A = U*D*U**T or A = L*D*L**T computed by
 DSYTRF. DSYTRI2 sets the LEADING DIMENSION of the workspace
 before calling DSYTRI2X that actually computes the inverse.
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
          On entry, the NB diagonal matrix D and the multipliers
          used to obtain the factor U or L as computed by DSYTRF.
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
          Details of the interchanges and the NB structure of D
          as determined by DSYTRF.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N+NB+1)*(NB+3)
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.
          WORK is size &gt;= (N+NB+1)*(NB+3)
          If LDWORK = -1, then a workspace query is assumed; the routine
           calculates:
              - the optimal size of the WORK array, returns
          this value as the first entry of the WORK array,
              - and no error message related to LDWORK is issued by XERBLA.
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
<dd> September 2012</dl>
<p> Definition at line 128 of file dsytri2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
