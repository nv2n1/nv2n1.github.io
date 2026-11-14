---
title: "zptsvx-f(3)"
name: "zptsvx-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zptsvx-f/"
description: "zptsvx.f –"
---

<p>zptsvx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine zptsvx (FACT, N, NRHS, D, E, DF, EF, B, LDB, X, LDX, RCOND, FERR, BERR, WORK, RWORK, INFO)


ZPTSVX computes the solution to system of linear equations A * X = B for PT matrices</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zptsvx (characterFACT, integerN, integerNRHS, double precision, dimension( * )D, complex*16, dimension( * )E, double precision, dimension( * )DF, complex*16, dimension( * )EF, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldx, * )X, integerLDX, double precisionRCOND, double precision, dimension( * )FERR, double precision, dimension( * )BERR, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code> ZPTSVX computes the solution to system of linear equations A * X = B for PT matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPTSVX uses the factorization A = L*D*L**H to compute the solution
 to a complex system of linear equations A*X = B, where A is an
 N-by-N Hermitian positive definite tridiagonal matrix and X and B
 are N-by-NRHS matrices.
 Error bounds on the solution and a condition estimate are also
 provided.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dd>
<pre> The following steps are performed:
 1. If FACT = 'N', the matrix A is factored as A = L*D*L**H, where L
 is a unit lower bidiagonal matrix and D is diagonal. The
 factorization can also be regarded as having the form
 A = U**H*D*U.
 2. If the leading i-by-i principal minor is not positive definite,
 then the routine returns with INFO = i. Otherwise, the factored
 form of A is used to estimate the condition number of the matrix
 A. If the reciprocal of the condition number is less than machine
 precision, INFO = N+1 is returned as a warning, but the routine
 still goes on to solve for X and compute error bounds as
 described below.
 3. The system of equations is solved for X using the factored form
 of A.
 4. Iterative refinement is applied to improve the computed solution
 matrix and calculate error bounds and backward error estimates
 for it.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>FACT</i> </p>
<pre> FACT is CHARACTER*1
 Specifies whether or not the factored form of the matrix
 A is supplied on entry.
 = 'F': On entry, DF and EF contain the factored form of A.
 D, E, DF, and EF will not be modified.
 = 'N': The matrix A will be copied to DF and EF and
 factored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices B and X. NRHS &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The n diagonal elements of the tridiagonal matrix A.</pre>
<p><i>E</i> </p>
<pre> E is COMPLEX*16 array, dimension (N-1)
 The (n-1) subdiagonal elements of the tridiagonal matrix A.</pre>
<p><i>DF</i> </p>
<pre> DF is DOUBLE PRECISION array, dimension (N)
 If FACT = 'F', then DF is an input argument and on entry
 contains the n diagonal elements of the diagonal matrix D
 from the L*D*L**H factorization of A.
 If FACT = 'N', then DF is an output argument and on exit
 contains the n diagonal elements of the diagonal matrix D
 from the L*D*L**H factorization of A.</pre>
<p><i>EF</i> </p>
<pre> EF is COMPLEX*16 array, dimension (N-1)
 If FACT = 'F', then EF is an input argument and on entry
 contains the (n-1) subdiagonal elements of the unit
 bidiagonal factor L from the L*D*L**H factorization of A.
 If FACT = 'N', then EF is an output argument and on exit
 contains the (n-1) subdiagonal elements of the unit
 bidiagonal factor L from the L*D*L**H factorization of A.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 The N-by-NRHS right hand side matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (LDX,NRHS)
 If INFO = 0 or INFO = N+1, the N-by-NRHS solution matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,N).</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal condition number of the matrix A. If RCOND
 is less than the machine precision (in particular, if
 RCOND = 0), the matrix is singular to working precision.
 This condition is indicated by a return code of INFO &gt; 0.</pre>
<p><i>FERR</i> </p>
<pre> FERR is DOUBLE PRECISION array, dimension (NRHS)
 The forward error bound for each solution vector
 X(j) (the j-th column of the solution matrix X).
 If XTRUE is the true solution corresponding to X(j), FERR(j)
 is an estimated upper bound for the magnitude of the largest
 element in (X(j) - XTRUE) divided by the magnitude of the
 largest element in X(j).</pre>
<p><i>BERR</i> </p>
<pre> BERR is DOUBLE PRECISION array, dimension (NRHS)
 The componentwise relative backward error of each solution
 vector X(j) (i.e., the smallest relative change in any
 element of A or B that makes X(j) an exact solution).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, and i is
 &lt;= N: the leading minor of order i of A is
 not positive definite, so the factorization
 could not be completed, and the solution has not
 been computed. RCOND = 0 is returned.
 = N+1: U is nonsingular, but RCOND is less than machine
 precision, meaning that the matrix is singular
 to working precision. Nevertheless, the
 solution and error bounds are computed because
 there are a number of situations where the
 computed solution can be more accurate than the
 value of RCOND would suggest.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 234 of file zptsvx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
