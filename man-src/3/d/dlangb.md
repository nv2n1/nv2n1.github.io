---
title: "dlangb(3)"
name: "dlangb"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlangb/"
description: "dlangb.f –"
---

<h2 class="name">NAME</h2>
<p> dlangb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dlangb</code> (NORM, N, KL, KU, AB, LDAB, WORK)<br />
 <i></i><code>DLANGB</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of general band matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dlangb (characterNORM, integerN, integerKL, integerKU, double precision, dimension( ldab, * )AB, integerLDAB, double precision, dimension( * )WORK)</h3>
<p> <code>DLANGB</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of general band matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLANGB  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the element of  largest absolute value  of an
 n by n band matrix  A,  with kl sub-diagonals and ku super-diagonals.
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> DLANGB </p>
<pre>
    DLANGB = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
          Specifies the value to be returned in DLANGB as described
          above.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.  When N = 0, DLANGB is
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
          AB is DOUBLE PRECISION array, dimension (LDAB,N)
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
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)),
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
<p> Definition at line 124 of file dlangb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
