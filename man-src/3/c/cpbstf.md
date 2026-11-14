---
title: "cpbstf(3)"
name: "cpbstf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpbstf/"
description: "cpbstf.f –"
---

<h2 class="name">NAME</h2>
<p> cpbstf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cpbstf</code> (UPLO, N, KD, AB, LDAB, INFO)<br />
 <i></i><code>CPBSTF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpbstf (characterUPLO, integerN, integerKD, complex, dimension( ldab, * )AB, integerLDAB, integerINFO)</h3>
<p> <code>CPBSTF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPBSTF computes a split Cholesky factorization of a complex
 Hermitian positive definite band matrix A.
 This routine is designed to be used in conjunction with CHBGST.
 The factorization has the form  A = S**H*S  where S is a band matrix
 of the same bandwidth as A and the following structure:
   S = ( U    )
       ( M  L )
 where U is upper triangular of order m = (n+kd)/2, and L is lower
 triangular of order n-m.
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
          AB is COMPLEX array, dimension (LDAB,N)
          On entry, the upper or lower triangle of the Hermitian band
          matrix A, stored in the first kd+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
          On exit, if INFO = 0, the factor S from the split Cholesky
          factorization A = S**H*S. See Further Details.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KD+1.
</pre>
<p> <i>INFO</i> </p>
<p>INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i &#8211; th argument had an illegal value &gt; 0 : if INFO = i, the factorization could not be completed,<br />
        because the updated element a(i, i)<br />
was negative;<br />
the<br />
    matrix A is not positive definite.</p>
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
<pre><code>
The band storage scheme is illustrated by the following example, when N = 7, KD = 2 : S = (s11 s12 s13)(s22 s23 s24)(s33 s34)(s44)(s53 s54 s55)(s64 s65 s66)(s75 s76 s77)If UPLO = 'U', the array AB holds : on entry : on exit : **a13 a24 a35 a46 a57 **s13 s24 s53 **H s64 **H s75 **H *a12 a23 a34 a45 a56 a67 *s12 s23 s34 s54 **H s65 **H s76 **H a11 a22 a33 a44 a55 a66 a77 s11 s22 s33 s44 s55 s66 s77 If UPLO = 'L', the array AB holds : on entry : on exit : a11 a22 a33 a44 a55 a66 a77 s11 s22 s33 s44 s55 s66 s77 a21 a32 a43 a54 a65 a76 *s12 **H s23 **H s34 **H s54 s65 s76 *a31 a42 a53 a64 a64 **s13 **H s24 **H s53 s64 s75 **Array elements marked *are not used by the routine;
s12 **H denotes
    conjg(s12);
the diagonal elements of S are real.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 154 of file cpbstf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
