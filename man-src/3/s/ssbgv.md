---
title: "ssbgv(3)"
name: "ssbgv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssbgv/"
description: "ssbgv.f –"
---

<h2 class="name">NAME</h2>
<p> ssbgv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssbgv</code> (JOBZ, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, W, Z, LDZ, WORK, INFO)<br />
 <i></i><code>SSBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssbgv (characterJOBZ, characterUPLO, integerN, integerKA, integerKB, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldbb, * )BB, integerLDBB, real, dimension( * )W, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SSBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSBGV computes all the eigenvalues, and optionally, the eigenvectors
 of a real generalized symmetric-definite banded eigenproblem, of
 the form A*x=(lambda)*B*x. Here A and B are assumed to be symmetric
 and banded, and B is also positive definite.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBZ</i> </p>
<pre>
          JOBZ is CHARACTER*1
          = 'N':  Compute eigenvalues only;
          = 'V':  Compute eigenvalues and eigenvectors.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangles of A and B are stored;
          = 'L':  Lower triangles of A and B are stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>KA</i> </p>
<pre>
          KA is INTEGER
          The number of superdiagonals of the matrix A if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'. KA &gt;= 0.
</pre>
<p> <i>KB</i> </p>
<pre>
          KB is INTEGER
          The number of superdiagonals of the matrix B if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'. KB &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre><code>
          AB is REAL array, dimension (LDAB, N)
          On entry, the upper or lower triangle of the symmetric band
          matrix A, stored in the first ka+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+ka).
          On exit, the contents of AB are destroyed.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KA+1.
</pre>
<p> <i>BB</i> </p>
<p>          BB is REAL array, dimension (LDBB, N)<br />
          On entry, the upper or lower triangle of the symmetric band<br />
          matrix B, stored in the first kb+1 rows of the array.  The<br />
          j-th column of B is stored in the j-th column of the array BB<br />
          as follows:<br />
          if UPLO = &#8216;U&#8217;, BB(kb+1+i-j,j) = B(i,j) for max(1,j-kb)&lt;=i&lt;=j;<br />
          if UPLO = &#8216;L&#8217;, BB(1+i-j,j)    = B(i,j) for j&lt;=i&lt;=min(n,j+kb).<br />
          On exit, the factor S from the split Cholesky factorization<br />
          B = S**T*S, as returned by SPBSTF.</p>
<p> <i>LDBB</i> </p>
<pre>
          LDBB is INTEGER
          The leading dimension of the array BB.  LDBB &gt;= KB+1.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          If INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension (LDZ, N)
          If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of
          eigenvectors, with the i-th column of Z holding the
          eigenvector associated with W(i). The eigenvectors are
          normalized so that Z**T*B*Z = I.
          If JOBZ = 'N', then Z is not referenced.
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= N.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (3*N)
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : if INFO = i, and i is : &lt;= N : the algorithm failed to converge : i off - diagonal elements of an intermediate tridiagonal form did not converge to zero;
             &gt; N:   if INFO = N + i, for 1 &lt;= i &lt;= N, then SPBSTF
                    returned INFO = i: B is not positive definite.
                    The factorization of B could not be completed and
                    no eigenvalues or eigenvectors were computed.
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
<dd> November 2011</dl>
<p> Definition at line 177 of file ssbgv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
