---
title: "ssbtrd(3)"
name: "ssbtrd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssbtrd/"
description: "ssbtrd.f –"
---

<h2 class="name">NAME</h2>
<p> ssbtrd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssbtrd</code> (VECT, UPLO, N, KD, AB, LDAB, D, E, Q, LDQ, WORK, INFO)<br />
 <i></i><code>SSBTRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssbtrd (characterVECT, characterUPLO, integerN, integerKD, real, dimension( ldab, * )AB, integerLDAB, real, dimension( * )D, real, dimension( * )E, real, dimension( ldq, * )Q, integerLDQ, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SSBTRD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSBTRD reduces a real symmetric band matrix A to symmetric
 tridiagonal form T by an orthogonal similarity transformation:
 Q**T * A * Q = T.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>VECT</i> </p>
<pre>
          VECT is CHARACTER*1
          = 'N':  do not form Q;
          = 'V':  form Q;
          = 'U':  update a matrix X, by forming X*Q.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
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
<p> <i>AB</i> </p>
<pre><code>
          AB is REAL array, dimension (LDAB,N)
          On entry, the upper or lower triangle of the symmetric band
          matrix A, stored in the first KD+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
          On exit, the diagonal elements of AB are overwritten by the
          diagonal elements of the tridiagonal matrix T;
          if KD
              &gt; 0, the
                           elements on the first superdiagonal(if UPLO = 'U') or
                       the
                           first subdiagonal(if UPLO = 'L') are overwritten by the
                           off
                           - diagonal elements of T;
          the rest of AB is overwritten by
              values generated during the reduction.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KD+1.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The diagonal elements of the tridiagonal matrix T.
</pre>
<p> <i>E</i> </p>
<p>E is REAL array, dimension(N &#8211; 1)<br />
                         The off<br />
                     &#8211; diagonal elements of the tridiagonal matrix T : E(i) = T(i, i + 1) if UPLO = &#8216;U&#8217;;<br />
E(i) = T(i + 1, i) if UPLO = &#8216;L&#8217;.</p>
<p> <i>Q</i> </p>
<pre><code>
Q is REAL array, dimension(LDQ, N) On entry, if VECT = 'U', then Q must contain an N - by - N matrix X;
if VECT
    = 'N' or 'V', then Q need not be set.On exit : if VECT = 'V', Q contains the N - by - N orthogonal matrix Q;
if VECT
    = 'U', Q contains the product X *Q;
if VECT
= 'N', the array Q is not referenced.
</code></pre>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
          The leading dimension of the array Q.
          LDQ &gt;= 1, and LDQ &gt;= N if VECT = 'V' or 'U'.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (N)
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
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Modified by Linda Kaufman, Bell Labs.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 163 of file ssbtrd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
