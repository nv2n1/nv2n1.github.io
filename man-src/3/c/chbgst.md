---
title: "chbgst(3)"
name: "chbgst"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chbgst/"
description: "chbgst.f –"
---

<h2 class="name">NAME</h2>
<p> chbgst.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chbgst</code> (VECT, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, X, LDX, WORK, RWORK, INFO)<br />
 <i></i><code>CHBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chbgst (characterVECT, characterUPLO, integerN, integerKA, integerKB, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldbb, * )BB, integerLDBB, complex, dimension( ldx, * )X, integerLDX, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CHBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHBGST reduces a complex Hermitian-definite banded generalized
 eigenproblem  A*x = lambda*B*x  to standard form  C*y = lambda*y,
 such that C has the same bandwidth as A.
 B must have been previously factorized as S**H*S by CPBSTF, using a
 split Cholesky factorization. A is overwritten by C = X**H*A*X, where
 X = S**(-1)*Q and Q is a unitary matrix chosen to preserve the
 bandwidth of A.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>VECT</i> </p>
<pre>
          VECT is CHARACTER*1
          = 'N':  do not form the transformation matrix X;
          = 'V':  form X.
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
          The order of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>KA</i> </p>
<pre>
          KA is INTEGER
          The number of superdiagonals of the matrix A if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'.  KA &gt;= 0.
</pre>
<p> <i>KB</i> </p>
<pre>
          KB is INTEGER
          The number of superdiagonals of the matrix B if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'.  KA &gt;= KB &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre><code>
          AB is COMPLEX array, dimension (LDAB,N)
          On entry, the upper or lower triangle of the Hermitian band
          matrix A, stored in the first ka+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+ka).
          On exit, the transformed matrix X**H*A*X, stored in the same
          format as A.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KA+1.
</pre>
<p> <i>BB</i> </p>
<pre>
          BB is COMPLEX array, dimension (LDBB,N)
          The banded factor S from the split Cholesky factorization of
          B, as returned by CPBSTF, stored in the first kb+1 rows of
          the array.
</pre>
<p> <i>LDBB</i> </p>
<pre>
          LDBB is INTEGER
          The leading dimension of the array BB.  LDBB &gt;= KB+1.
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (LDX,N)
          If VECT = 'V', the n-by-n matrix X.
          If VECT = 'N', the array X is not referenced.
</pre>
<p> <i>LDX</i> </p>
<pre><code>
LDX is INTEGER
        The leading dimension of the array X.LDX &gt;= max(1, N) if VECT = 'V';
LDX &gt;= 1 otherwise.
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
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
<p> Definition at line 165 of file chbgst.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
