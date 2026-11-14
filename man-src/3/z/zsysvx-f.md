---
title: "zsysvx-f(3)"
name: "zsysvx-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zsysvx-f/"
description: "zsysvx.f –"
---

<p>zsysvx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine zsysvx (FACT, UPLO, N, NRHS, A, LDA, AF, LDAF, IPIV, B, LDB, X, LDX, RCOND, FERR, BERR, WORK, LWORK, RWORK, INFO)


ZSYSVX computes the solution to system of linear equations A * X = B for SY matrices</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zsysvx (characterFACT, characterUPLO, integerN, integerNRHS, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldx, * )X, integerLDX, double precisionRCOND, double precision, dimension( * )FERR, double precision, dimension( * )BERR, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code> ZSYSVX computes the solution to system of linear equations A * X = B for SY matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSYSVX uses the diagonal pivoting factorization to compute the
 solution to a complex system of linear equations A * X = B,
 where A is an N-by-N symmetric matrix and X and B are N-by-NRHS
 matrices.
 Error bounds on the solution and a condition estimate are also
 provided.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dd>
<pre> The following steps are performed:
 1. If FACT = 'N', the diagonal pivoting method is used to factor A.
 The form of the factorization is
 A = U * D * U**T, if UPLO = 'U', or
 A = L * D * L**T, if UPLO = 'L',
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and D is symmetric and block diagonal with
 1-by-1 and 2-by-2 diagonal blocks.
 2. If some D(i,i)=0, so that D is exactly singular, then the routine
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
<dl>
<dd><i>FACT</i> </p>
<pre> FACT is CHARACTER*1
 Specifies whether or not the factored form of A has been
 supplied on entry.
 = 'F': On entry, AF and IPIV contain the factored form
 of A. A, AF and IPIV will not be modified.
 = 'N': The matrix A will be copied to AF and factored.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices B and X. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The symmetric matrix A. If UPLO = 'U', the leading N-by-N
 upper triangular part of A contains the upper triangular part
 of the matrix A, and the strictly lower triangular part of A
 is not referenced. If UPLO = 'L', the leading N-by-N lower
 triangular part of A contains the lower triangular part of
 the matrix A, and the strictly upper triangular part of A is
 not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX*16 array, dimension (LDAF,N)
 If FACT = 'F', then AF is an input argument and on entry
 contains the block diagonal matrix D and the multipliers used
 to obtain the factor U or L from the factorization
 A = U*D*U**T or A = L*D*L**T as computed by ZSYTRF.
 If FACT = 'N', then AF is an output argument and on exit
 returns the block diagonal matrix D and the multipliers used
 to obtain the factor U or L from the factorization
 A = U*D*U**T or A = L*D*L**T.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 If FACT = 'F', then IPIV is an input argument and on entry
 contains details of the interchanges and the block structure
 of D, as determined by ZSYTRF.
 If IPIV(k) &gt; 0, then rows and columns k and IPIV(k) were
 interchanged and D(k,k) is a 1-by-1 diagonal block.
 If UPLO = 'U' and IPIV(k) = IPIV(k-1) &lt; 0, then rows and
 columns k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k)
 is a 2-by-2 diagonal block. If UPLO = 'L' and IPIV(k) =
 IPIV(k+1) &lt; 0, then rows and columns k+1 and -IPIV(k) were
 interchanged and D(k:k+1,k:k+1) is a 2-by-2 diagonal block.
 If FACT = 'N', then IPIV is an output argument and on exit
 contains details of the interchanges and the block structure
 of D, as determined by ZSYTRF.</pre>
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
 The estimate of the reciprocal condition number of the matrix
 A. If RCOND is less than the machine precision (in
 particular, if RCOND = 0), the matrix is singular to working
 precision. This condition is indicated by a return code of
 INFO &gt; 0.</pre>
<p><i>FERR</i> </p>
<pre> FERR is DOUBLE PRECISION array, dimension (NRHS)
 The estimated forward error bound for each solution vector
 X(j) (the j-th column of the solution matrix X).
 If XTRUE is the true solution corresponding to X(j), FERR(j)
 is an estimated upper bound for the magnitude of the largest
 element in (X(j) - XTRUE) divided by the magnitude of the
 largest element in X(j). The estimate is as reliable as
 the estimate for RCOND, and is almost always a slight
 overestimate of the true error.</pre>
<p><i>BERR</i> </p>
<pre> BERR is DOUBLE PRECISION array, dimension (NRHS)
 The componentwise relative backward error of each solution
 vector X(j) (i.e., the smallest relative change in
 any element of A or B that makes X(j) an exact solution).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The length of WORK. LWORK &gt;= max(1,2*N), and for best
 performance, when FACT = 'N', LWORK &gt;= max(1,2*N,N*NB), where
 NB is the optimal blocksize for ZSYTRF.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, and i is
 &lt;= N: D(i,i) is exactly zero. The factorization
 has been completed but the factor D is exactly
 singular, so the solution and error bounds could
 not be computed. RCOND = 0 is returned.
 = N+1: D is nonsingular, but RCOND is less than machine
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
<dd>April 2012</dl>
<p> Definition at line 284 of file zsysvx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
