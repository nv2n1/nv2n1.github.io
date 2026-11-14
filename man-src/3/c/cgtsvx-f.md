---
title: "cgtsvx-f(3)"
name: "cgtsvx-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgtsvx-f/"
description: "cgtsvx.f –"
---

<p>cgtsvx.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgtsvx</code> (FACT, TRANS, N, NRHS, DL, D, DU, DLF, DF, DUF, DU2, IPIV, B, LDB, X, LDX, RCOND, FERR, BERR, WORK, RWORK, INFO)<br />
 <i></i><code> CGTSVX computes the solution to system of linear equations A * X = B for GT matrices </code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgtsvx (characterFACT, characterTRANS, integerN, integerNRHS, complex, dimension( * )DL, complex, dimension( * )D, complex, dimension( * )DU, complex, dimension( * )DLF, complex, dimension( * )DF, complex, dimension( * )DUF, complex, dimension( * )DU2, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldx, * )X, integerLDX, realRCOND, real, dimension( * )FERR, real, dimension( * )BERR, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code> CGTSVX computes the solution to system of linear equations A * X = B for GT matrices </code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGTSVX uses the LU factorization to compute the solution to a complex
 system of linear equations A * X = B, A**T * X = B, or A**H * X = B,
 where A is a tridiagonal matrix of order N and X and B are N-by-NRHS
 matrices.
 Error bounds on the solution and a condition estimate are also
 provided.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl COMPACT>
<dd>
<pre> The following steps are performed:
 1. If FACT = 'N', the LU decomposition is used to factor the matrix A
 as A = L * U, where L is a product of permutation and unit lower
 bidiagonal matrices and U is upper triangular with nonzeros in
 only the main diagonal and first two superdiagonals.
 2. If some U(i,i)=0, so that U is exactly singular, then the routine
 returns with INFO = i. Otherwise, the factored form of A is used
 to estimate the condition number of the matrix A. If the
 reciprocal of the condition number is less than machine precision,
 INFO = N+1 is returned as a warning, but the routine still goes on
 to solve for X and compute error bounds as described below.
 3. The system of equations is solved for X using the factored form
 of A.
 4. Iterative refinement is applied to improve the computed solution
 matrix and calculate error bounds and backward error estimates
 for it.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>FACT</i> </p>
<pre> FACT is CHARACTER*1
 Specifies whether or not the factored form of A has been
 supplied on entry.
 = 'F': DLF, DF, DUF, DU2, and IPIV contain the factored form
 of A; DL, D, DU, DLF, DF, DUF, DU2 and IPIV will not
 be modified.
 = 'N': The matrix will be copied to DLF, DF, and DUF
 and factored.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 Specifies the form of the system of equations:
 = 'N': A * X = B (No transpose)
 = 'T': A**T * X = B (Transpose)
 = 'C': A**H * X = B (Conjugate transpose)</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>DL</i> </p>
<pre> DL is COMPLEX array, dimension (N-1)
 The (n-1) subdiagonal elements of A.</pre>
<p><i>D</i> </p>
<pre> D is COMPLEX array, dimension (N)
 The n diagonal elements of A.</pre>
<p><i>DU</i> </p>
<pre> DU is COMPLEX array, dimension (N-1)
 The (n-1) superdiagonal elements of A.</pre>
<p><i>DLF</i> </p>
<pre> DLF is COMPLEX array, dimension (N-1)
 If FACT = 'F', then DLF is an input argument and on entry
 contains the (n-1) multipliers that define the matrix L from
 the LU factorization of A as computed by CGTTRF.
 If FACT = 'N', then DLF is an output argument and on exit
 contains the (n-1) multipliers that define the matrix L from
 the LU factorization of A.</pre>
<p><i>DF</i> </p>
<pre> DF is COMPLEX array, dimension (N)
 If FACT = 'F', then DF is an input argument and on entry
 contains the n diagonal elements of the upper triangular
 matrix U from the LU factorization of A.
 If FACT = 'N', then DF is an output argument and on exit
 contains the n diagonal elements of the upper triangular
 matrix U from the LU factorization of A.</pre>
<p><i>DUF</i> </p>
<pre> DUF is COMPLEX array, dimension (N-1)
 If FACT = 'F', then DUF is an input argument and on entry
 contains the (n-1) elements of the first superdiagonal of U.
 If FACT = 'N', then DUF is an output argument and on exit
 contains the (n-1) elements of the first superdiagonal of U.</pre>
<p><i>DU2</i> </p>
<pre> DU2 is COMPLEX array, dimension (N-2)
 If FACT = 'F', then DU2 is an input argument and on entry
 contains the (n-2) elements of the second superdiagonal of
 U.
 If FACT = 'N', then DU2 is an output argument and on exit
 contains the (n-2) elements of the second superdiagonal of
 U.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 If FACT = 'F', then IPIV is an input argument and on entry
 contains the pivot indices from the LU factorization of A as
 computed by CGTTRF.
 If FACT = 'N', then IPIV is an output argument and on exit
 contains the pivot indices from the LU factorization of A;
 row i of the matrix was interchanged with row IPIV(i).
 IPIV(i) will always be either i or i+1; IPIV(i) = i indicates
 a row interchange was not required.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,NRHS)
 The N-by-NRHS right hand side matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension (LDX,NRHS)
 If INFO = 0 or INFO = N+1, the N-by-NRHS solution matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,N).</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is REAL
 The estimate of the reciprocal condition number of the matrix
 A. If RCOND is less than the machine precision (in
 particular, if RCOND = 0), the matrix is singular to working
 precision. This condition is indicated by a return code of
 INFO &gt; 0.</pre>
<p><i>FERR</i> </p>
<pre> FERR is REAL array, dimension (NRHS)
 The estimated forward error bound for each solution vector
 X(j) (the j-th column of the solution matrix X).
 If XTRUE is the true solution corresponding to X(j), FERR(j)
 is an estimated upper bound for the magnitude of the largest
 element in (X(j) - XTRUE) divided by the magnitude of the
 largest element in X(j). The estimate is as reliable as
 the estimate for RCOND, and is almost always a slight
 overestimate of the true error.</pre>
<p><i>BERR</i> </p>
<pre> BERR is REAL array, dimension (NRHS)
 The componentwise relative backward error of each solution
 vector X(j) (i.e., the smallest relative change in
 any element of A or B that makes X(j) an exact solution).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, and i is
 &lt;= N: U(i,i) is exactly zero. The factorization
 has not been completed unless i = N, but the
 factor U is exactly singular, so the solution
 and error bounds could not be computed.
 RCOND = 0 is returned.
 = N+1: U is nonsingular, but RCOND is less than machine
 precision, meaning that the matrix is singular
 to working precision. Nevertheless, the
 solution and error bounds are computed because
 there are a number of situations where the
 computed solution can be more accurate than the
 value of RCOND would suggest.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 293 of file cgtsvx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
