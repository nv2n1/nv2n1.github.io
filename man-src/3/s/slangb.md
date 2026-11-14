---
title: "slangb(3)"
name: "slangb"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slangb/"
description: "slangb.f –"
---

<h2 class="name">NAME</h2>
<p> slangb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>slangb</code> (NORM, N, KL, KU, AB, LDAB, WORK)<br />
 <i></i><code>SLANGB</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of general band matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function slangb (characterNORM, integerN, integerKL, integerKU, real, dimension( ldab, * )AB, integerLDAB, real, dimension( * )WORK)</h3>
<p> <code>SLANGB</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of general band matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLANGB  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the element of  largest absolute value  of an
 n by n band matrix  A,  with kl sub-diagonals and ku super-diagonals.
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> SLANGB </p>
<pre>
    SLANGB = ( max(abs(A(i,j))), NORM = 'M' or 'm'
             (
             ( norm1(A),         NORM = '1', 'O' or 'o'
             (
             ( normI(A),         NORM = 'I' or 'i'
             (
             ( normF(A),         NORM = 'F', 'f', 'E' or 'e'
 where  norm1  denotes the  one norm of a matrix (maximum column sum),
 normI  denotes the  infinity norm  of a matrix  (maximum row sum) and
 normF  denotes the  Frobenius norm of a matrix (square root of sum of
 squares).  Note that  max(abs(A(i,j)))  is not a consistent matrix norm.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>NORM</i> </p>
<pre>
          NORM is CHARACTER*1
          Specifies the value to be returned in SLANGB as described
          above.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.  When N = 0, SLANGB is
          set to zero.
</pre>
<p> <i>KL</i> </p>
<pre>
          KL is INTEGER
          The number of sub-diagonals of the matrix A.  KL &gt;= 0.
</pre>
<p> <i>KU</i> </p>
<pre>
          KU is INTEGER
          The number of super-diagonals of the matrix A.  KU &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre>
          AB is REAL array, dimension (LDAB,N)
          The band matrix A, stored in rows 1 to KL+KU+1.  The j-th
          column of A is stored in the j-th column of the array AB as
          follows:
          AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(n,j+kl).
</pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KL+KU+1.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK)),
          where LWORK &gt;= N when NORM = 'I'; otherwise, WORK is not
          referenced.
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
<dd> September 2012</dl>
<p> Definition at line 124 of file slangb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
