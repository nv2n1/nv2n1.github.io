---
title: "zsysvxx(3)"
name: "zsysvxx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zsysvxx/"
description: "zsysvxx.f –"
---

<p>zsysvxx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine zsysvxx (FACT, UPLO, N, NRHS, A, LDA, AF, LDAF, IPIV, EQUED, S, B, LDB, X, LDX, RCOND, RPVGRW, BERR, N_ERR_BNDS, ERR_BNDS_NORM, ERR_BNDS_COMP, NPARAMS, PARAMS, WORK, RWORK, INFO)


ZSYSVXX computes the solution to system of linear equations A * X = B for SY matrices</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zsysvxx (characterFACT, characterUPLO, integerN, integerNRHS, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, characterEQUED, double precision, dimension( * )S, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldx, * )X, integerLDX, double precisionRCOND, double precisionRPVGRW, double precision, dimension( * )BERR, integerN_ERR_BNDS, double precision, dimension( nrhs, * )ERR_BNDS_NORM, double precision, dimension( nrhs, * )ERR_BNDS_COMP, integerNPARAMS, double precision, dimension( * )PARAMS, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code> ZSYSVXX computes the solution to system of linear equations A * X = B for SY matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSYSVXX uses the diagonal pivoting factorization to compute the
 solution to a complex*16 system of linear equations A * X = B, where
 A is an N-by-N symmetric matrix and X and B are N-by-NRHS
 matrices.
 If requested, both normwise and maximum componentwise error bounds
 are returned. ZSYSVXX will return a solution with a tiny
 guaranteed error (O(eps) where eps is the working machine
 precision) unless the matrix is very ill-conditioned, in which
 case a warning is returned. Relevant condition numbers also are
 calculated and returned.
 ZSYSVXX accepts user-provided factorizations and equilibration
 factors; see the definitions of the FACT and EQUED options.
 Solving with refinement and using a factorization from a previous
 ZSYSVXX call will also produce a solution with either O(eps)
 errors or warnings, but we cannot make that claim for general
 user-provided factorizations and equilibration factors if they
 differ from what ZSYSVXX would itself produce.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dd>
<pre> The following steps are performed:
 1. If FACT = 'E', double precision scaling factors are computed to equilibrate
 the system:
 diag(S)*A*diag(S) *inv(diag(S))*X = diag(S)*B
 Whether or not the system will be equilibrated depends on the
 scaling of the matrix A, but if equilibration is used, A is
 overwritten by diag(S)*A*diag(S) and B by diag(S)*B.
 2. If FACT = 'N' or 'E', the LU decomposition is used to factor
 the matrix A (after equilibration if FACT = 'E') as
 A = U * D * U**T, if UPLO = 'U', or
 A = L * D * L**T, if UPLO = 'L',
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and D is symmetric and block diagonal with
 1-by-1 and 2-by-2 diagonal blocks.
 3. If some D(i,i)=0, so that D is exactly singular, then the
 routine returns with INFO = i. Otherwise, the factored form of A
 is used to estimate the condition number of the matrix A (see
 argument RCOND). If the reciprocal of the condition number is
 less than machine precision, the routine still goes on to solve
 for X and compute error bounds as described below.
 4. The system of equations is solved for X using the factored form
 of A.
 5. By default (unless PARAMS(LA_LINRX_ITREF_I) is set to zero),
 the routine will use iterative refinement to try to get a small
 error and error bounds. Refinement calculates the residual to at
 least twice the working precision.
 6. If equilibration was used, the matrix X is premultiplied by
 diag(R) so that it solves the original system before
 equilibration.</pre>
<p>&nbsp;<wbr> </p>
<pre> Some optional parameters are bundled in the PARAMS array. These
 settings determine how refinement is performed, but often the
 defaults are acceptable. If the defaults are acceptable, users
 can pass NPARAMS = 0 which prevents the source code from accessing
 the PARAMS argument.</pre>
</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>FACT</i> </p>
<pre> FACT is CHARACTER*1
 Specifies whether or not the factored form of the matrix A is
 supplied on entry, and if not, whether the matrix A should be
 equilibrated before it is factored.
 = 'F': On entry, AF and IPIV contain the factored form of A.
 If EQUED is not 'N', the matrix A has been
 equilibrated with scaling factors given by S.
 A, AF, and IPIV are not modified.
 = 'N': The matrix A will be copied to AF and factored.
 = 'E': The matrix A will be equilibrated if necessary, then
 copied to AF and factored.</pre>
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
 upper triangular part of A contains the upper triangular
 part of the matrix A, and the strictly lower triangular
 part of A is not referenced. If UPLO = 'L', the leading
 N-by-N lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit, if FACT = 'E' and EQUED = 'Y', A is overwritten by
 diag(S)*A*diag(S).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX*16 array, dimension (LDAF,N)
 If FACT = 'F', then AF is an input argument and on entry
 contains the block diagonal matrix D and the multipliers
 used to obtain the factor U or L from the factorization A =
 U*D*U**T or A = L*D*L**T as computed by DSYTRF.
 If FACT = 'N', then AF is an output argument and on exit
 returns the block diagonal matrix D and the multipliers
 used to obtain the factor U or L from the factorization A =
 U*D*U**T or A = L*D*L**T.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 If FACT = 'F', then IPIV is an input argument and on entry
 contains details of the interchanges and the block
 structure of D, as determined by DSYTRF. If IPIV(k) &gt; 0,
 then rows and columns k and IPIV(k) were interchanged and
 D(k,k) is a 1-by-1 diagonal block. If UPLO = 'U' and
 IPIV(k) = IPIV(k-1) &lt; 0, then rows and columns k-1 and
 -IPIV(k) were interchanged and D(k-1:k,k-1:k) is a 2-by-2
 diagonal block. If UPLO = 'L' and IPIV(k) = IPIV(k+1) &lt; 0,
 then rows and columns k+1 and -IPIV(k) were interchanged
 and D(k:k+1,k:k+1) is a 2-by-2 diagonal block.
 If FACT = 'N', then IPIV is an output argument and on exit
 contains details of the interchanges and the block
 structure of D, as determined by DSYTRF.</pre>
<p><i>EQUED</i> </p>
<pre> EQUED is CHARACTER*1
 Specifies the form of equilibration that was done.
 = 'N': No equilibration (always true if FACT = 'N').
 = 'Y': Both row and column equilibration, i.e., A has been
 replaced by diag(S) * A * diag(S).
 EQUED is an input argument if FACT = 'F'; otherwise, it is an
 output argument.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (N)
 The scale factors for A. If EQUED = 'Y', A is multiplied on
 the left and right by diag(S). S is an input argument if FACT =
 'F'; otherwise, S is an output argument. If FACT = 'F' and EQUED
 = 'Y', each element of S must be positive. If S is output, each
 element of S is a power of the radix. If S is input, each element
 of S should be a power of the radix to ensure a reliable solution
 and error estimates. Scaling by powers of the radix does not cause
 rounding errors unless the result underflows or overflows.
 Rounding errors during scaling lead to refining with a matrix that
 is not equivalent to the input matrix, producing error estimates
 that may not be reliable.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 On entry, the N-by-NRHS right hand side matrix B.
 On exit,
 if EQUED = 'N', B is not modified;
 if EQUED = 'Y', B is overwritten by diag(S)*B;</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (LDX,NRHS)
 If INFO = 0, the N-by-NRHS solution matrix X to the original
 system of equations. Note that A and B are modified on exit if
 EQUED .ne. 'N', and the solution to the equilibrated system is
 inv(diag(S))*X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,N).</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 Reciprocal scaled condition number. This is an estimate of the
 reciprocal Skeel condition number of the matrix A after
 equilibration (if done). If this is less than the machine
 precision (in particular, if it is zero), the matrix is singular
 to working precision. Note that the error may still be small even
 if this number is very small and the matrix appears ill-
 conditioned.</pre>
<p><i>RPVGRW</i> </p>
<pre> RPVGRW is DOUBLE PRECISION
 Reciprocal pivot growth. On exit, this contains the reciprocal
 pivot growth factor norm(A)/norm(U). The &quot;max absolute element&quot;
 norm is used. If this is much less than 1, then the stability of
 the LU factorization of the (equilibrated) matrix A could be poor.
 This also means that the solution X, estimated condition numbers,
 and error bounds could be unreliable. If factorization fails with
 0&lt;INFO&lt;=N, then this contains the reciprocal pivot growth factor
 for the leading INFO columns of A.</pre>
<p><i>BERR</i> </p>
<pre> BERR is DOUBLE PRECISION array, dimension (NRHS)
 Componentwise relative backward error. This is the
 componentwise relative backward error of each solution vector X(j)
 (i.e., the smallest relative change in any element of A or B that
 makes X(j) an exact solution).</pre>
<p><i>N_ERR_BNDS</i> </p>
<pre> N_ERR_BNDS is INTEGER
 Number of error bounds to return for each right hand side
 and each type (normwise or componentwise). See ERR_BNDS_NORM and
 ERR_BNDS_COMP below.</pre>
<p><i>ERR_BNDS_NORM</i> </p>
<pre> ERR_BNDS_NORM is DOUBLE PRECISION array, dimension (NRHS, N_ERR_BNDS)
 For each right-hand side, this array contains information about
 various error bounds and condition numbers corresponding to the
 normwise relative error, which is defined as follows:
 Normwise relative error in the ith solution vector:
 max_j (abs(XTRUE(j,i) - X(j,i)))
 ------------------------------
 max_j abs(X(j,i))
 The array is indexed by the type of error information as described
 below. There currently are up to three pieces of information
 returned.
 The first index in ERR_BNDS_NORM(i,:) corresponds to the ith
 right-hand side.
 The second index in ERR_BNDS_NORM(:,err) contains the following
 three fields:
 err = 1 &quot;Trust/don't trust&quot; boolean. Trust the answer if the
 reciprocal condition number is less than the threshold
 <a href="//www.systutorials.com/docs/linux/man/n-sqrt/">sqrt</a>(n) * dlamch('Epsilon').
 err = 2 &quot;Guaranteed&quot; error bound: The estimated forward error,
 almost certainly within a factor of 10 of the true error
 so long as the next entry is greater than the threshold
 <a href="//www.systutorials.com/docs/linux/man/n-sqrt/">sqrt</a>(n) * dlamch('Epsilon'). This error bound should only
 be trusted if the previous boolean is true.
 err = 3 Reciprocal condition number: Estimated normwise
 reciprocal condition number. Compared with the threshold
 <a href="//www.systutorials.com/docs/linux/man/n-sqrt/">sqrt</a>(n) * dlamch('Epsilon') to determine if the error
 estimate is &quot;guaranteed&quot;. These reciprocal condition
 numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some
 appropriately scaled matrix Z.
 Let Z = S*A, where S scales each row by a power of the
 radix so all absolute row sums of Z are approximately 1.
 See Lapack Working Note 165 for further details and extra
 cautions.</pre>
<p><i>ERR_BNDS_COMP</i> </p>
<pre> ERR_BNDS_COMP is DOUBLE PRECISION array, dimension (NRHS, N_ERR_BNDS)
 For each right-hand side, this array contains information about
 various error bounds and condition numbers corresponding to the
 componentwise relative error, which is defined as follows:
 Componentwise relative error in the ith solution vector:
 abs(XTRUE(j,i) - X(j,i))
 max_j ----------------------
 abs(X(j,i))
 The array is indexed by the right-hand side i (on which the
 componentwise relative error depends), and the type of error
 information as described below. There currently are up to three
 pieces of information returned for each right-hand side. If
 componentwise accuracy is not requested (<a href="//www.systutorials.com/docs/linux/man/3-PARAMS/">PARAMS</a>(3) = 0.0), then
 ERR_BNDS_COMP is not accessed. If N_ERR_BNDS .LT. 3, then at most
 the first (:,N_ERR_BNDS) entries are returned.
 The first index in ERR_BNDS_COMP(i,:) corresponds to the ith
 right-hand side.
 The second index in ERR_BNDS_COMP(:,err) contains the following
 three fields:
 err = 1 &quot;Trust/don't trust&quot; boolean. Trust the answer if the
 reciprocal condition number is less than the threshold
 <a href="//www.systutorials.com/docs/linux/man/n-sqrt/">sqrt</a>(n) * dlamch('Epsilon').
 err = 2 &quot;Guaranteed&quot; error bound: The estimated forward error,
 almost certainly within a factor of 10 of the true error
 so long as the next entry is greater than the threshold
 <a href="//www.systutorials.com/docs/linux/man/n-sqrt/">sqrt</a>(n) * dlamch('Epsilon'). This error bound should only
 be trusted if the previous boolean is true.
 err = 3 Reciprocal condition number: Estimated componentwise
 reciprocal condition number. Compared with the threshold
 <a href="//www.systutorials.com/docs/linux/man/n-sqrt/">sqrt</a>(n) * dlamch('Epsilon') to determine if the error
 estimate is &quot;guaranteed&quot;. These reciprocal condition
 numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some
 appropriately scaled matrix Z.
 Let Z = S*(A*diag(x)), where x is the solution for the
 current right-hand side and S scales each row of
 A*diag(x) by a power of the radix so all absolute row
 sums of Z are approximately 1.
 See Lapack Working Note 165 for further details and extra
 cautions.</pre>
<p><i>NPARAMS</i> </p>
<pre> NPARAMS is INTEGER
 Specifies the number of parameters set in PARAMS. If .LE. 0, the
 PARAMS array is never referenced and default values are used.</pre>
<p><i>PARAMS</i> </p>
<pre> PARAMS is DOUBLE PRECISION array, dimension NPARAMS
 Specifies algorithm parameters. If an entry is .LT. 0.0, then
 that entry will be filled with default value used for that
 parameter. Only positions up to NPARAMS are accessed; defaults
 are used for higher-numbered parameters.
 PARAMS(LA_LINRX_ITREF_I = 1) : Whether to perform iterative
 refinement or not.
 Default: 1.0D+0
 = 0.0 : No refinement is performed, and no error bounds are
 computed.
 = 1.0 : Use the extra-precise refinement algorithm.
 (other values are reserved for future use)
 PARAMS(LA_LINRX_ITHRESH_I = 2) : Maximum number of residual
 computations allowed for refinement.
 Default: 10
 Aggressive: Set to 100 to permit convergence using approximate
 factorizations or factorizations other than LU. If
 the factorization uses a technique other than
 Gaussian elimination, the guarantees in
 err_bnds_norm and err_bnds_comp may no longer be
 trustworthy.
 PARAMS(LA_LINRX_CWISE_I = 3) : Flag determining if the code
 will attempt to find a solution with small componentwise
 relative error in the double-precision algorithm. Positive
 is true, 0.0 is false.
 Default: 1.0 (attempt componentwise convergence)</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: Successful exit. The solution to every right-hand side is
 guaranteed.
 &lt; 0: If INFO = -i, the i-th argument had an illegal value
 &gt; 0 and &lt;= N: U(INFO,INFO) is exactly zero. The factorization
 has been completed, but the factor U is exactly singular, so
 the solution and error bounds could not be computed. RCOND = 0
 is returned.
 = N+J: The solution corresponding to the Jth right-hand side is
 not guaranteed. The solutions corresponding to other right-
 hand sides K with K &gt; J may not be guaranteed as well, but
 only the first such right-hand side is reported. If a small
 componentwise error is not requested (<a href="//www.systutorials.com/docs/linux/man/3-PARAMS/">PARAMS</a>(3) = 0.0) then
 the Jth right-hand side is the first with a normwise error
 bound that is not guaranteed (the smallest J such
 that ERR_BNDS_NORM(J,1) = 0.0). By default (<a href="//www.systutorials.com/docs/linux/man/3-PARAMS/">PARAMS</a>(3) = 1.0)
 the Jth right-hand side is the first with either a normwise or
 componentwise error bound that is not guaranteed (the smallest
 J such that either ERR_BNDS_NORM(J,1) = 0.0 or
 ERR_BNDS_COMP(J,1) = 0.0). See the definition of
 ERR_BNDS_NORM(:,1) and ERR_BNDS_COMP(:,1). To get information
 about all of the right-hand sides check ERR_BNDS_NORM or
 ERR_BNDS_COMP.</pre>
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
<p> Definition at line 504 of file zsysvxx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
