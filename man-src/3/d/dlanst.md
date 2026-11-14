---
title: "dlanst(3)"
name: "dlanst"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlanst/"
description: "dlanst.f –"
---

<h2 class="name">NAME</h2>
<p> dlanst.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dlanst</code> (NORM, N, D, E)<br />
 <i></i><code>DLANST</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a real symmetric tridiagonal matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dlanst (characterNORM, integerN, double precision, dimension( * )D, double precision, dimension( * )E)</h3>
<p> <code>DLANST</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a real symmetric tridiagonal matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLANST  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 real symmetric tridiagonal matrix A.
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> DLANST </p>
<pre>
    DLANST = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
          Specifies the value to be returned in DLANST as described
          above.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.  When N = 0, DLANST is
          set to zero.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          The diagonal elements of A.
</pre>
<p> <i>E</i> </p>
<pre>
          E is DOUBLE PRECISION array, dimension (N-1)
          The (n-1) sub-diagonal or super-diagonal elements of A.
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
<p> Definition at line 101 of file dlanst.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
