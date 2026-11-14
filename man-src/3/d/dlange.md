---
title: "dlange(3)"
name: "dlange"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlange/"
description: "dlange.f –"
---

<h2 class="name">NAME</h2>
<p> dlange.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dlange</code> (NORM, M, N, A, LDA, WORK)<br />
 <i></i><code>DLANGE</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of a general rectangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dlange (characterNORM, integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )WORK)</h3>
<p> <code>DLANGE</code> returns the value of the 1-norm, Frobenius norm, infinity-norm, or the largest absolute value of any element of a general rectangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLANGE  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the  element of  largest absolute value  of a
 real matrix A.
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> DLANGE </p>
<pre>
    DLANGE = ( max(abs(A(i,j))), NORM = 'M' or 'm'
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
          Specifies the value to be returned in DLANGE as described
          above.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.  When M = 0,
          DLANGE is set to zero.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.  When N = 0,
          DLANGE is set to zero.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          The m by n matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(M,1).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)),
          where LWORK &gt;= M when NORM = 'I'; otherwise, WORK is not
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
<p> Definition at line 115 of file dlange.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
