---
title: "slagtf(3)"
name: "slagtf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slagtf/"
description: "slagtf.f –"
---

<h2 class="name">NAME</h2>
<p> slagtf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slagtf</code> (N, A, LAMBDA, B, C, TOL, D, IN, INFO)<br />
 <i></i><code>SLAGTF</code> computes an LU factorization of a matrix T-λI, where T is a general tridiagonal matrix, and λ a scalar, using partial pivoting with row interchanges.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slagtf (integerN, real, dimension( * )A, realLAMBDA, real, dimension( * )B, real, dimension( * )C, realTOL, real, dimension( * )D, integer, dimension( * )IN, integerINFO)</h3>
<p> <code>SLAGTF</code> computes an LU factorization of a matrix T-λI, where T is a general tridiagonal matrix, and λ a scalar, using partial pivoting with row interchanges. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAGTF factorizes the matrix (T - lambda*I), where T is an n by n
 tridiagonal matrix and lambda is a scalar, as
    T - lambda*I = PLU,
 where P is a permutation matrix, L is a unit lower tridiagonal matrix
 with at most one non-zero sub-diagonal elements per column and U is
 an upper triangular matrix with at most two non-zero super-diagonal
 elements per column.
 The factorization is obtained by Gaussian elimination with partial
 pivoting and implicit row scaling.
 The parameter LAMBDA is included in the routine so that SLAGTF may
 be used, in conjunction with SLAGTS, to obtain eigenvectors of T by
 inverse iteration.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix T.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (N)
          On entry, A must contain the diagonal elements of T.
          On exit, A is overwritten by the n diagonal elements of the
          upper triangular matrix U of the factorization of T.
</pre>
<p> <i>LAMBDA</i> </p>
<pre>
          LAMBDA is REAL
          On entry, the scalar lambda.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (N-1)
          On entry, B must contain the (n-1) super-diagonal elements of
          T.
          On exit, B is overwritten by the (n-1) super-diagonal
          elements of the matrix U of the factorization of T.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (N-1)
          On entry, C must contain the (n-1) sub-diagonal elements of
          T.
          On exit, C is overwritten by the (n-1) sub-diagonal elements
          of the matrix L of the factorization of T.
</pre>
<p> <i>TOL</i> </p>
<pre>
          TOL is REAL
          On entry, a relative tolerance used to indicate whether or
          not the matrix (T - lambda*I) is nearly singular. TOL should
          normally be chose as approximately the largest relative error
          in the elements of T. For example, if the elements of T are
          correct to about 4 significant figures, then TOL should be
          set to about 5*10**(-4). If TOL is supplied as less than eps,
          where eps is the relative machine precision, then the value
          eps is used in place of TOL.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N-2)
          On exit, D is overwritten by the (n-2) second super-diagonal
          elements of the matrix U of the factorization of T.
</pre>
<p> <i>IN</i> </p>
<pre>
          IN is INTEGER array, dimension (N)
          On exit, IN contains details of the permutation matrix P. If
          an interchange occurred at the kth step of the elimination,
          then IN(k) = 1, otherwise IN(k) = 0. The element <a href="//www.systutorials.com/docs/linux/man/n-IN/">IN</a>(n)
          returns the smallest positive integer j such that
             abs( u(j,j) ).le. norm( (T - lambda*I)(j) )*TOL,
          where norm( A(j) ) denotes the sum of the absolute values of
          the jth row of the matrix A. If no such j exists then <a href="//www.systutorials.com/docs/linux/man/n-IN/">IN</a>(n)
          is returned as zero. If <a href="//www.systutorials.com/docs/linux/man/n-IN/">IN</a>(n) is returned as positive, then a
          diagonal element of U is small, indicating that
          (T - lambda*I) is singular or nearly singular,
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0   : successful exit
          .lt. 0: if INFO = -k, the kth argument had an illegal value
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
<p> Definition at line 157 of file slagtf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
