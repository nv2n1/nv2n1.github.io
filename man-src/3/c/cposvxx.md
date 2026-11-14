---
title: "cposvxx(3)"
name: "cposvxx"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cposvxx/"
description: "cposvxx.f –"
---

<h2 class="name">NAME</h2>
<p> cposvxx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cposvxx</code> (FACT, UPLO, N, NRHS, A, LDA, AF, LDAF, EQUED, S, B, LDB, X, LDX, RCOND, RPVGRW, BERR, N_ERR_BNDS, ERR_BNDS_NORM, ERR_BNDS_COMP, NPARAMS, PARAMS, WORK, RWORK, INFO)<br />
 <i></i><code> CPOSVXX computes the solution to system of linear equations A * X = B for PO matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cposvxx (characterFACT, characterUPLO, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldaf, * )AF, integerLDAF, characterEQUED, real, dimension( * )S, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldx, * )X, integerLDX, realRCOND, realRPVGRW, real, dimension( * )BERR, integerN_ERR_BNDS, real, dimension( nrhs, * )ERR_BNDS_NORM, real, dimension( nrhs, * )ERR_BNDS_COMP, integerNPARAMS, real, dimension( * )PARAMS, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code> CPOSVXX computes the solution to system of linear equations A * X = B for PO matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
CPOSVXX uses the Cholesky factorization A = U **T *U or A = L *L **T
                                                to compute the solution to a complex system of linear equations
                                                    A *X = B,
                                        where A is an N - by - N symmetric positive definite matrix and X and B are N - by - NRHS matrices.If requested, both normwise and maximum componentwise error bounds are returned.CPOSVXX will return a solution with a tiny guaranteed error(O(eps) where eps is the working machine precision) unless the matrix is very ill - conditioned, in which case a warning is returned.Relevant condition numbers also are calculated and returned.CPOSVXX accepts user - provided factorizations and equilibration factors;
see the definitions of the FACT and EQUED options.Solving with refinement and using a factorization from a previous
    CPOSVXX call will also produce a solution with either
    O(eps)
    errors or warnings, but we cannot make that claim for general
    user-provided factorizations and equilibration factors if they
    differ from what CPOSVXX would itself produce.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dt>
<dd>
<p>    The following steps are performed:<br />
    1. If FACT = &#8216;E&#8217;, real scaling factors are computed to equilibrate<br />
    the system:<br />
      diag(S)*A*diag(S)     *inv(diag(S))*X = diag(S)*B<br />
    Whether or not the system will be equilibrated depends on the<br />
    scaling of the matrix A, but if equilibration is used, A is<br />
    overwritten by diag(S)*A*diag(S) and B by diag(S)*B.<br />
    2. If FACT = &#8216;N&#8217; or &#8216;E&#8217;, the Cholesky decomposition is used to<br />
    factor the matrix A (after equilibration if FACT = &#8216;E&#8217;) as<br />
       A = U**T* U,  if UPLO = &#8216;U&#8217;, or<br />
       A = L * L**T,  if UPLO = &#8216;L&#8217;,<br />
    where U is an upper triangular matrix and L is a lower triangular<br />
    matrix.<br />
    3. If the leading i-by-i principal minor is not positive definite,<br />
    then the routine returns with INFO = i. Otherwise, the factored<br />
    form of A is used to estimate the condition number of the matrix<br />
    A (see argument RCOND).  If the reciprocal of the condition number<br />
    is less than machine precision, the routine still goes on to solve<br />
    for X and compute error bounds as described below.<br />
    4. The system of equations is solved for X using the factored form<br />
    of A.<br />
    5. By default (unless PARAMS(LA_LINRX_ITREF_I) is set to zero),<br />
    the routine will use iterative refinement to try to get a small<br />
    error and error bounds.  Refinement calculates the residual to at<br />
    least twice the working precision.<br />
    6. If equilibration was used, the matrix X is premultiplied by<br />
    diag(S)<br />
    so that it solves the original system before<br />
        equilibration.</p>
<p>&nbsp;<wbr> </p>
<pre>
     Some optional parameters are bundled in the PARAMS array.  These
     settings determine how refinement is performed, but often the
     defaults are acceptable.  If the defaults are acceptable, users
     can pass NPARAMS = 0 which prevents the source code from accessing
     the PARAMS argument.
</pre>
</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>FACT</i> </p>
<pre>
          FACT is CHARACTER*1
     Specifies whether or not the factored form of the matrix A is
     supplied on entry, and if not, whether the matrix A should be
     equilibrated before it is factored.
       = 'F':  On entry, AF contains the factored form of A.
               If EQUED is not 'N', the matrix A has been
               equilibrated with scaling factors given by S.
               A and AF are not modified.
       = 'N':  The matrix A will be copied to AF and factored.
       = 'E':  The matrix A will be equilibrated if necessary, then
               copied to AF and factored.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
       = 'U':  Upper triangle of A is stored;
       = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
     The number of linear equations, i.e., the order of the
     matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
     The number of right hand sides, i.e., the number of columns
     of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<p>A is COMPLEX array, dimension(LDA, N) On entry, the symmetric matrix A, except if FACT = &#8216;F&#8217; and EQUED = &#8216;Y&#8217;, then A must contain the equilibrated matrix diag(S) * A *diag(S).If UPLO = &#8216;U&#8217;, the leading N &#8211; by &#8211; N upper triangular part of A contains the upper triangular part of the matrix A, and the strictly lower triangular part of A is not referenced.If UPLO = &#8216;L&#8217;, the leading N &#8211; by &#8211; N lower triangular part of A contains the lower triangular part of the matrix A, and the strictly upper triangular part of A is not referenced.A is not modified if FACT = &#8216;F&#8217; or &#8216;N&#8217;, or if FACT = &#8216;E&#8217; and EQUED =<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 &#8216;N&#8217; on exit.On exit,<br />
                                                                                  if FACT = &#8216;E&#8217; and EQUED = &#8216;Y&#8217;, A is overwritten by diag(S) * A *diag(S).</p>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
     The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AF</i> </p>
<pre>
          AF is COMPLEX array, dimension (LDAF,N)
     If FACT = 'F', then AF is an input argument and on entry
     contains the triangular factor U or L from the Cholesky
     factorization A = U**T*U or A = L*L**T, in the same storage
     format as A.  If EQUED .ne. 'N', then AF is the factored
     form of the equilibrated matrix diag(S)*A*diag(S).
     If FACT = 'N', then AF is an output argument and on exit
     returns the triangular factor U or L from the Cholesky
     factorization A = U**T*U or A = L*L**T of the original
     matrix A.
     If FACT = 'E', then AF is an output argument and on exit
     returns the triangular factor U or L from the Cholesky
     factorization A = U**T*U or A = L*L**T of the equilibrated
     matrix A (see the description of A for the form of the
     equilibrated matrix).
</pre>
<p> <i>LDAF</i> </p>
<pre>
          LDAF is INTEGER
     The leading dimension of the array AF.  LDAF &gt;= max(1,N).
</pre>
<p> <i>EQUED</i> </p>
<pre>
          EQUED is CHARACTER*1
     Specifies the form of equilibration that was done.
       = 'N':  No equilibration (always true if FACT = 'N').
       = 'Y':  Both row and column equilibration, i.e., A has been
               replaced by diag(S) * A * diag(S).
     EQUED is an input argument if FACT = 'F'; otherwise, it is an
     output argument.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (N)
     The row scale factors for A.  If EQUED = 'Y', A is multiplied on
     the left and right by diag(S).  S is an input argument if FACT =
     'F'; otherwise, S is an output argument.  If FACT = 'F' and EQUED
     = 'Y', each element of S must be positive.  If S is output, each
     element of S is a power of the radix. If S is input, each element
     of S should be a power of the radix to ensure a reliable solution
     and error estimates. Scaling by powers of the radix does not cause
     rounding errors unless the result underflows or overflows.
     Rounding errors during scaling lead to refining with a matrix that
     is not equivalent to the input matrix, producing error estimates
     that may not be reliable.
</pre>
<p> <i>B</i> </p>
<p>B is COMPLEX array, dimension(LDB, NRHS) On entry, the N &#8211; by &#8211; NRHS right hand side matrix B.On exit,<br />
    if EQUED = &#8216;N&#8217;, B is not modified;<br />
if EQUED<br />
    = &#8216;Y&#8217;, B is overwritten by diag(S) * B;</p>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
     The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (LDX,NRHS)
     If INFO = 0, the N-by-NRHS solution matrix X to the original
     system of equations.  Note that A and B are modified on exit if
     EQUED .ne. 'N', and the solution to the equilibrated system is
     inv(diag(S))*X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
     The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
     Reciprocal scaled condition number.  This is an estimate of the
     reciprocal Skeel condition number of the matrix A after
     equilibration (if done).  If this is less than the machine
     precision (in particular, if it is zero), the matrix is singular
     to working precision.  Note that the error may still be small even
     if this number is very small and the matrix appears ill-
     conditioned.
</pre>
<p> <i>RPVGRW</i> </p>
<pre>
          RPVGRW is REAL
     Reciprocal pivot growth.  On exit, this contains the reciprocal
     pivot growth factor norm(A)/norm(U). The &quot;max absolute element&quot;
     norm is used.  If this is much less than 1, then the stability of
     the LU factorization of the (equilibrated) matrix A could be poor.
     This also means that the solution X, estimated condition numbers,
     and error bounds could be unreliable. If factorization fails with
     0&lt;INFO&lt;=N, then this contains the reciprocal pivot growth factor
     for the leading INFO columns of A.
</pre>
<p> <i>BERR</i> </p>
<pre>
          BERR is REAL array, dimension (NRHS)
     Componentwise relative backward error.  This is the
     componentwise relative backward error of each solution vector X(j)
     (i.e., the smallest relative change in any element of A or B that
     makes X(j) an exact solution).
</pre>
<p> <i>N_ERR_BNDS</i> </p>
<pre>
          N_ERR_BNDS is INTEGER
     Number of error bounds to return for each right hand side
     and each type (normwise or componentwise).  See ERR_BNDS_NORM and
     ERR_BNDS_COMP below.
</pre>
<p> <i>ERR_BNDS_NORM</i> </p>
<p>ERR_BNDS_NORM is REAL array, dimension(NRHS, N_ERR_BNDS) For each right &#8211; hand side, this array contains information about various error bounds and condition numbers corresponding to the normwise relative error, which is defined as follows : Normwise relative error in the ith solution vector : max_j(abs(XTRUE(j, i) &#8211; X(j, i)))&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;max_j abs(X(j, i)) The array is indexed by the type of error information as described below.There currently are up to three pieces of information returned.The first index in ERR_BNDS_NORM(i,<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                :) corresponds to the ith right<br />
                                                                                                                                                                                                                        &#8211; hand side.The second index in ERR_BNDS_NORM(<br />
                                                                                                                                                                                                                              :, err) contains the following<br />
     three fields:<br />
     err = 1 &#8220;Trust/don&#8217;t trust&#8221; boolean. Trust the answer if the<br />
              reciprocal condition number is less than the threshold<br />
              sqrt(n) * slamch(&#8216;Epsilon&#8217;).<br />
     err = 2 &#8220;Guaranteed&#8221; error bound: The estimated forward error,<br />
              almost certainly within a factor of 10 of the true error<br />
              so long as the next entry is greater than the threshold<br />
              sqrt(n) * slamch(&#8216;Epsilon&#8217;). This error bound should only<br />
              be trusted if the previous boolean is true.<br />
     err = 3  Reciprocal condition number: Estimated normwise<br />
              reciprocal condition number.  Compared with the threshold<br />
              sqrt(n) * slamch(&#8216;Epsilon&#8217;) to determine if the error<br />
              estimate is &#8220;guaranteed&#8221;. These reciprocal condition<br />
              numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some<br />
              appropriately scaled matrix Z.<br />
              Let Z = S*A, where S scales each row by a power of the<br />
              radix so all absolute row sums of Z are approximately 1.<br />
     See Lapack Working Note 165 for further details and extra<br />
     cautions.</p>
<p> <i>ERR_BNDS_COMP</i> </p>
<p>          ERR_BNDS_COMP is REAL array, dimension (NRHS, N_ERR_BNDS)<br />
     For each right-hand side, this array contains information about<br />
     various error bounds and condition numbers corresponding to the<br />
     componentwise relative error, which is defined as follows:<br />
     Componentwise relative error in the ith solution vector:<br />
                    abs(XTRUE(j,i) &#8211; X(j,i))<br />
             max_j &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
                         abs(X(j,i))<br />
     The array is indexed by the right-hand side i (on which the<br />
     componentwise relative error depends), and the type of error<br />
     information as described below. There currently are up to three<br />
     pieces of information returned for each right-hand side. If<br />
     componentwise accuracy is not requested (PARAMS(3) = 0.0), then<br />
     ERR_BNDS_COMP is not accessed.  If N_ERR_BNDS .LT. 3, then at most<br />
     the first (:,N_ERR_BNDS)<br />
          entries are returned.The first index in ERR_BNDS_COMP(i,<br />
                                                                :) corresponds to the ith<br />
              right<br />
              &#8211; hand side.The second index in ERR_BNDS_COMP(<br />
                    :, err) contains the following<br />
     three fields:<br />
     err = 1 &#8220;Trust/don&#8217;t trust&#8221; boolean. Trust the answer if the<br />
              reciprocal condition number is less than the threshold<br />
              sqrt(n) * slamch(&#8216;Epsilon&#8217;).<br />
     err = 2 &#8220;Guaranteed&#8221; error bound: The estimated forward error,<br />
              almost certainly within a factor of 10 of the true error<br />
              so long as the next entry is greater than the threshold<br />
              sqrt(n) * slamch(&#8216;Epsilon&#8217;). This error bound should only<br />
              be trusted if the previous boolean is true.<br />
     err = 3  Reciprocal condition number: Estimated componentwise<br />
              reciprocal condition number.  Compared with the threshold<br />
              sqrt(n) * slamch(&#8216;Epsilon&#8217;) to determine if the error<br />
              estimate is &#8220;guaranteed&#8221;. These reciprocal condition<br />
              numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some<br />
              appropriately scaled matrix Z.<br />
              Let Z = S*(A*diag(x)), where x is the solution for the<br />
              current right-hand side and S scales each row of<br />
              A*diag(x) by a power of the radix so all absolute row<br />
              sums of Z are approximately 1.<br />
     See Lapack Working Note 165 for further details and extra<br />
     cautions.</p>
<p> <i>NPARAMS</i> </p>
<pre>
          NPARAMS is INTEGER
     Specifies the number of parameters set in PARAMS.  If .LE. 0, the
     PARAMS array is never referenced and default values are used.
</pre>
<p> <i>PARAMS</i> </p>
<pre><code>
          PARAMS is REAL array, dimension NPARAMS
     Specifies algorithm parameters.  If an entry is .LT. 0.0, then
     that entry will be filled with default value used for that
     parameter.  Only positions up to NPARAMS are accessed; defaults
     are used for higher-numbered parameters.
       PARAMS(LA_LINRX_ITREF_I = 1) : Whether to perform iterative
            refinement or not.
         Default: 1.0
            = 0.0 : No refinement is performed, and no error bounds are
                    computed.
            = 1.0 : Use the double-precision refinement algorithm,
                    possibly with doubled-single computations if the
                    compilation environment does not support DOUBLE
                    PRECISION.
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
            relative error in the double-precision algorithm.  Positive
            is true, 0.0 is false.
         Default: 1.0 (attempt componentwise convergence)
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (2*N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
       = 0:  Successful exit. The solution to every right-hand side is
         guaranteed.
       &lt; 0:  If INFO = -i, the i-th argument had an illegal value
       &gt; 0 and &lt;= N:  U(INFO,INFO) is exactly zero.  The factorization
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
         ERR_BNDS_COMP.
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
<dd> April 2012</dl>
<p> Definition at line 494 of file cposvxx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
