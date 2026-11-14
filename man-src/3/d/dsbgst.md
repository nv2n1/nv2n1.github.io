---
title: "dsbgst(3)"
name: "dsbgst"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsbgst/"
description: "dsbgst.f –"
---

<h2 class="name">NAME</h2>
<p> dsbgst.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dsbgst</code> (VECT, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, X, LDX, WORK, INFO)<br />
 <i></i><code>DSBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dsbgst (characterVECT, characterUPLO, integerN, integerKA, integerKB, double precision, dimension( ldab, * )AB, integerLDAB, double precision, dimension( ldbb, * )BB, integerLDBB, double precision, dimension( ldx, * )X, integerLDX, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DSBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DSBGST reduces a real symmetric-definite banded generalized
 eigenproblem  A*x = lambda*B*x  to standard form  C*y = lambda*y,
 such that C has the same bandwidth as A.
 B must have been previously factorized as S**T*S by DPBSTF, using a
 split Cholesky factorization. A is overwritten by C = X**T*A*X, where
 X = S**(-1)*Q and Q is an orthogonal matrix chosen to preserve the
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
          AB is DOUBLE PRECISION array, dimension (LDAB,N)
          On entry, the upper or lower triangle of the symmetric band
          matrix A, stored in the first ka+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+ka).
          On exit, the transformed matrix X**T*A*X, stored in the same
          format as A.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KA+1.
</pre>
<p> <i>BB</i> </p>
<pre>
          BB is DOUBLE PRECISION array, dimension (LDBB,N)
          The banded factor S from the split Cholesky factorization of
          B, as returned by DPBSTF, stored in the first KB+1 rows of
          the array.
</pre>
<p> <i>LDBB</i> </p>
<pre>
          LDBB is INTEGER
          The leading dimension of the array BB.  LDBB &gt;= KB+1.
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,N)
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
          WORK is DOUBLE PRECISION array, dimension (2*N)
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
<p> Definition at line 159 of file dsbgst.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
