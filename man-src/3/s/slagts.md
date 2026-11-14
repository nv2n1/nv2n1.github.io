---
title: "slagts(3)"
name: "slagts"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slagts/"
description: "slagts.f –"
---

<h2 class="name">NAME</h2>
<p> slagts.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slagts</code> (JOB, N, A, B, C, D, IN, Y, TOL, INFO)<br />
 <i></i><code>SLAGTS</code> solves the system of equations (T-λI)x = y or (T-λI)Tx = y,where T is a general tridiagonal matrix and λ a scalar, using the LU factorization computed by slagtf.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slagts (integerJOB, integerN, real, dimension( * )A, real, dimension( * )B, real, dimension( * )C, real, dimension( * )D, integer, dimension( * )IN, real, dimension( * )Y, realTOL, integerINFO)</h3>
<p> <code>SLAGTS</code> solves the system of equations (T-λI)x = y or (T-λI)Tx = y,where T is a general tridiagonal matrix and λ a scalar, using the LU factorization computed by slagtf. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAGTS may be used to solve one of the systems of equations
    (T - lambda*I)*x = y   or   (T - lambda*I)**T*x = y,
 where T is an n by n tridiagonal matrix, for x, following the
 factorization of (T - lambda*I) as
    (T - lambda*I) = P*L*U ,
 by routine SLAGTF. The choice of equation to be solved is
 controlled by the argument JOB, and in each case there is an option
 to perturb zero or very small diagonal elements of U, this option
 being intended for use in applications such as inverse iteration.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOB</i> </p>
<pre>
          JOB is INTEGER
          Specifies the job to be performed by SLAGTS as follows:
          =  1: The equations  (T - lambda*I)x = y  are to be solved,
                but diagonal elements of U are not to be perturbed.
          = -1: The equations  (T - lambda*I)x = y  are to be solved
                and, if overflow would otherwise occur, the diagonal
                elements of U are to be perturbed. See argument TOL
                below.
          =  2: The equations  (T - lambda*I)**Tx = y  are to be solved,
                but diagonal elements of U are not to be perturbed.
          = -2: The equations  (T - lambda*I)**Tx = y  are to be solved
                and, if overflow would otherwise occur, the diagonal
                elements of U are to be perturbed. See argument TOL
                below.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix T.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (N)
          On entry, A must contain the diagonal elements of U as
          returned from SLAGTF.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (N-1)
          On entry, B must contain the first super-diagonal elements of
          U as returned from SLAGTF.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (N-1)
          On entry, C must contain the sub-diagonal elements of L as
          returned from SLAGTF.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N-2)
          On entry, D must contain the second super-diagonal elements
          of U as returned from SLAGTF.
</pre>
<p> <i>IN</i> </p>
<pre>
          IN is INTEGER array, dimension (N)
          On entry, IN must contain details of the matrix P as returned
          from SLAGTF.
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is REAL array, dimension (N)
          On entry, the right hand side vector y.
          On exit, Y is overwritten by the solution vector x.
</pre>
<p> <i>TOL</i> </p>
<pre>
          TOL is REAL
          On entry, with  JOB .lt. 0, TOL should be the minimum
          perturbation to be made to very small diagonal elements of U.
          TOL should normally be chosen as about eps*norm(U), where eps
          is the relative machine precision, but if TOL is supplied as
          non-positive, then it is reset to eps*max( abs( u(i,j) ) ).
          If  JOB .gt. 0  then TOL is not referenced.
          On exit, TOL is changed as described above, only if TOL is
          non-positive on entry. Otherwise TOL is unchanged.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0   : successful exit
          .lt. 0: if INFO = -i, the i-th argument had an illegal value
          .gt. 0: overflow would occur when computing the INFO(th)
                  element of the solution vector x. This can only occur
                  when JOB is supplied as positive and either means
                  that a diagonal element of U is very small, or that
                  the elements of the right-hand side vector y are very
                  large.
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
<p> Definition at line 162 of file slagts.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
