---
title: "cpttrf(3)"
name: "cpttrf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpttrf/"
description: "cpttrf.f –"
---

<h2 class="name">NAME</h2>
<p> cpttrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cpttrf</code> (N, D, E, INFO)<br />
 <i></i><code>CPTTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpttrf (integerN, real, dimension( * )D, complex, dimension( * )E, integerINFO)</h3>
<p> <code>CPTTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPTTRF computes the L*D*L**H factorization of a complex Hermitian
 positive definite tridiagonal matrix A.  The factorization may also
 be regarded as having the form A = U**H *D*U.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          On entry, the n diagonal elements of the tridiagonal matrix
          A.  On exit, the n diagonal elements of the diagonal matrix
          D from the L*D*L**H factorization of A.
</pre>
<p> <i>E</i> </p>
<pre>
          E is COMPLEX array, dimension (N-1)
          On entry, the (n-1) subdiagonal elements of the tridiagonal
          matrix A.  On exit, the (n-1) subdiagonal elements of the
          unit bidiagonal factor L from the L*D*L**H factorization of A.
          E can also be regarded as the superdiagonal of the unit
          bidiagonal factor U from the U**H *D*U factorization of A.
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -k, the k - th argument had an illegal value &gt; 0 : if INFO = k, the leading minor of order k is not positive definite;
if k
&lt; N, the factorization could not be completed, while if k = N, the factorization was completed, but D(N) &lt;= 0.
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
<p> Definition at line 93 of file cpttrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
