---
title: "chetri_rook(3)"
name: "chetri_rook"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chetri_rook/"
description: "chetri_rook.f –"
---

<h2 class="name">NAME</h2>
<p> chetri_rook.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chetri_rook</code> (UPLO, N, A, LDA, IPIV, WORK, INFO)<br />
 <i></i><code>CHETRI_ROOK</code> computes the inverse of HE matrix using the factorization obtained with the bounded Bunch-Kaufman (&#8216;rook&#8217;) diagonal pivoting method.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chetri_rook (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CHETRI_ROOK</code> computes the inverse of HE matrix using the factorization obtained with the bounded Bunch-Kaufman (&#8216;rook&#8217;) diagonal pivoting method. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHETRI_ROOK computes the inverse of a complex Hermitian indefinite matrix
 A using the factorization A = U*D*U**H or A = L*D*L**H computed by
 CHETRF_ROOK.
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
          On entry, the block diagonal matrix D and the multipliers
          used to obtain the factor U or L as computed by CHETRF_ROOK.
          On exit, if INFO = 0, the (Hermitian) inverse of the original
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
          as determined by CHETRF_ROOK.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (N)
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
<p> Definition at line 129 of file chetri_rook.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
