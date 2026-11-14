---
title: "clangt(3)"
name: "clangt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clangt/"
description: "clangt.f –"
---

<h2 class="name">NAME</h2>
<p> clangt.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>clangt</code> (NORM, N, DL, D, DU)<br />
 <i></i><code>CLANGT</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of a general tridiagonal matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function clangt (characterNORM, integerN, complex, dimension( * )DL, complex, dimension( * )D, complex, dimension( * )DU)</h3>
<p> <code>CLANGT</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of a general tridiagonal matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLANGT  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 complex tridiagonal matrix A.
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> CLANGT </p>
<pre>
    CLANGT = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
          Specifies the value to be returned in CLANGT as described
          above.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.  When N = 0, CLANGT is
          set to zero.
</pre>
<p> <i>DL</i> </p>
<pre>
          DL is COMPLEX array, dimension (N-1)
          The (n-1) sub-diagonal elements of A.
</pre>
<p> <i>D</i> </p>
<pre>
          D is COMPLEX array, dimension (N)
          The diagonal elements of A.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is COMPLEX array, dimension (N-1)
          The (n-1) super-diagonal elements of A.
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
<p> Definition at line 107 of file clangt.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
