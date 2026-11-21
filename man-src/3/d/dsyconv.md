---

title: "dsyconv(3)"
name: "dsyconv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsyconv/"
description: "dsyconv.f –"
---

<h3>Functions/Subroutines</h3>
<p> subroutine <code>dsyconv</code> (UPLO, WAY, N, A, LDA, IPIV, WORK, INFO)<br />
 <i></i><code>DSYCONV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsyconv (characterUPLO, characterWAY, integerN, double precision, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DSYCONV</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
 DSYCONV convert A given by TRF into L and D and vice-versa.
 Get Non-diag elements of D (returned in workspace) and 
 apply or reverse permutation done in TRF.
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>UPLO</i> </dd>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the details of the factorization are stored
          as an upper or lower triangular matrix.
          = 'U':  Upper triangular, form is A = U*D*U**T;
          = 'L':  Lower triangular, form is A = L*D*L**T.
</pre>
<p> <i>WAY</i> </p>
<pre>
          WAY is CHARACTER*1
          = 'C': Convert 
          = 'R': Revert
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          The block diagonal matrix D and the multipliers used to
          obtain the factor U or L as computed by DSYTRF.
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
          as determined by DSYTRF.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N)
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
</dt><dd> Univ. of Tennessee </dd>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
</dt><dd> November 2011</dd></dl>
<p> Definition at line 113 of file dsyconv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
