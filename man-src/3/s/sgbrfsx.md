---
title: "sgbrfsx(3)"
name: "sgbrfsx"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbrfsx/"
---

<h2 class="name">NAME</h2>
 

 sgbrfsx.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbrfsx</b> (TRANS, EQUED, N, KL, KU, NRHS, AB, LDAB, AFB, LDAFB, IPIV, R, C, B, LDB, X, LDX, RCOND, BERR, N_ERR_BNDS, ERR_BNDS_NORM, ERR_BNDS_COMP, NPARAMS, PARAMS, WORK, IWORK, INFO) 
 <i></i><b>SGBRFSX</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbrfsx (characterTRANS, characterEQUED, integerN, integerKL, integerKU, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, real, dimension( * )R, real, dimension( * )C, real, dimension( ldb, * )B, integerLDB, real, dimension( ldx , * )X, integerLDX, realRCOND, real, dimension( * )BERR, integerN_ERR_BNDS, real, dimension( nrhs, * )ERR_BNDS_NORM, real, dimension( nrhs, * )ERR_BNDS_COMP, integerNPARAMS, real, dimension( * )PARAMS, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>

 

 

 <b>SGBRFSX</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre><code>
    SGBRFSX improves the computed solution to a system of linear
    equations and provides error bounds and backward error estimates
    for the solution.  In addition to normwise error bound, the code
    provides maximum componentwise error bound if possible.  See
    comments for ERR_BNDS_NORM and ERR_BNDS_COMP for details of the
    error bounds.
    The original system of linear equations may have been equilibrated
    before calling this routine, as described by arguments EQUED, R
    and C below. In this case, the solution and error bounds returned
    are for the original unequilibrated system.
</code></pre> 

 
&nbsp;<wbr> 

 <pre>
     Some optional parameters are bundled in the PARAMS array.  These
     settings determine how refinement is performed, but often the
     defaults are acceptable.  If the defaults are acceptable, users
     can pass NPARAMS = 0 which prevents the source code from accessing
     the PARAMS argument.
</pre> 

</dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>TRANS</i> 

 <pre>
          TRANS is CHARACTER*1
     Specifies the form of the system of equations:
       = 'N':  A * X = B     (No transpose)
       = 'T':  A**T * X = B  (Transpose)
       = 'C':  A**H * X = B  (Conjugate transpose = Transpose)
</pre> 

 
 <i>EQUED</i> 

 <pre>
          EQUED is CHARACTER*1
     Specifies the form of equilibration that was done to A
     before calling this routine. This is needed to compute
     the solution and error bounds correctly.
       = 'N':  No equilibration
       = 'R':  Row equilibration, i.e., A has been premultiplied by
               diag(R).
       = 'C':  Column equilibration, i.e., A has been postmultiplied
               by diag(C).
       = 'B':  Both row and column equilibration, i.e., A has been
               replaced by diag(R) * A * diag(C).
               The right hand side B has been changed accordingly.
</pre> 

 
 <i>N</i> 

 <pre>
          N is INTEGER
     The order of the matrix A.  N &gt;= 0.
</pre> 

 
 <i>KL</i> 

 <pre>
          KL is INTEGER
     The number of subdiagonals within the band of A.  KL &gt;= 0.
</pre> 

 
 <i>KU</i> 

 <pre>
          KU is INTEGER
     The number of superdiagonals within the band of A.  KU &gt;= 0.
</pre> 

 
 <i>NRHS</i> 

 <pre>
          NRHS is INTEGER
     The number of right hand sides, i.e., the number of columns
     of the matrices B and X.  NRHS &gt;= 0.
</pre> 

 
 <i>AB</i> 

 <pre>
          AB is DOUBLE PRECISION array, dimension (LDAB,N)
     The original band matrix A, stored in rows 1 to KL+KU+1.
     The j-th column of A is stored in the j-th column of the
     array AB as follows:
     AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(n,j+kl).
</pre> 

 
 <i>LDAB</i> 

 <pre>
          LDAB is INTEGER
     The leading dimension of the array AB.  LDAB &gt;= KL+KU+1.
</pre> 

 
 <i>AFB</i> 

 <pre>
          AFB is DOUBLE PRECISION array, dimension (LDAFB,N)
     Details of the LU factorization of the band matrix A, as
     computed by DGBTRF.  U is stored as an upper triangular band
     matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
     the multipliers used during the factorization are stored in
     rows KL+KU+2 to 2*KL+KU+1.
</pre> 

 
 <i>LDAFB</i> 

 <pre>
          LDAFB is INTEGER
     The leading dimension of the array AFB.  LDAFB &gt;= 2*KL*KU+1.
</pre> 

 
 <i>IPIV</i> 

 
IPIV is INTEGER array, dimension(N)
                           The pivot indices from SGETRF; for
1 &lt;= i &lt;= N, row i of the
                 matrix was interchanged with row
                 IPIV(i)
                     .
 

 
 <i>R</i> 

 
          R is REAL array, dimension (N)
     The row scale factors for A.  If EQUED = 'R' or 'B', A is
     multiplied on the left by diag(R);
          if EQUED
              = 'N' or 'C', R
                                is not accessed.R is an input argument if FACT = 'F';
          otherwise, R is an output argument.If FACT = 'F' and EQUED = 'R' or 'B', each element of R must be positive.If R is output, each element of R is a power of the radix.If R is input, each element of R should be a power of the radix to ensure a reliable solution and error estimates.Scaling by powers of the radix does not cause rounding errors unless the result underflows or overflows.Rounding errors during scaling lead to refining with a matrix that is not equivalent to the input matrix, producing error estimates that may not be reliable.
 

 
 <i>C</i> 

 
          C is REAL array, dimension (N)
     The column scale factors for A.  If EQUED = 'C' or 'B', A is
     multiplied on the right by diag(C);
          if EQUED
              = 'N' or 'R', C
                                is not accessed.C is an input argument if FACT = 'F';
          otherwise, C is an output argument.If FACT = 'F' and EQUED = 'C' or 'B', each element of C must be positive.If C is output, each element of C is a power of the radix.If C is input, each element of C should be a power of the radix to ensure a reliable solution and error estimates.Scaling by powers of the radix does not cause rounding errors unless the result underflows or overflows.Rounding errors during scaling lead to refining with a matrix that is not equivalent to the input matrix, producing error estimates that may not be reliable.
 

 
 <i>B</i> 

 <pre>
          B is REAL array, dimension (LDB,NRHS)
     The right hand side matrix B.
</pre> 

 
 <i>LDB</i> 

 <pre>
          LDB is INTEGER
     The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre> 

 
 <i>X</i> 

 <pre>
          X is REAL array, dimension (LDX,NRHS)
     On entry, the solution matrix X, as computed by SGETRS.
     On exit, the improved solution matrix X.
</pre> 

 
 <i>LDX</i> 

 <pre>
          LDX is INTEGER
     The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre> 

 
 <i>RCOND</i> 

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

 
 <i>BERR</i> 

 <pre>
          BERR is REAL array, dimension (NRHS)
     Componentwise relative backward error.  This is the
     componentwise relative backward error of each solution vector X(j)
     (i.e., the smallest relative change in any element of A or B that
     makes X(j) an exact solution).
</pre> 

 
 <i>N_ERR_BNDS</i> 

 <pre>
          N_ERR_BNDS is INTEGER
     Number of error bounds to return for each right hand side
     and each type (normwise or componentwise).  See ERR_BNDS_NORM and
     ERR_BNDS_COMP below.
</pre> 

 
 <i>ERR_BNDS_NORM</i> 

 
ERR_BNDS_NORM is REAL array, dimension(NRHS, N_ERR_BNDS) For each right - hand side, this array contains information about various error bounds and condition numbers corresponding to the normwise relative error, which is defined as follows : Normwise relative error in the ith solution vector : max_j(abs(XTRUE(j, i) - X(j, i)))-- -- -- -- -- -- -- -- -- -- -- -- -- -- --max_j abs(X(j, i)) The array is indexed by the type of error information as described below.There currently are up to three pieces of information returned.The first index in ERR_BNDS_NORM(i,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                :) corresponds to the ith right
                                                                                                                                                                                                                        - hand side.The second index in ERR_BNDS_NORM(
                                                                                                                                                                                                                              :, err) contains the following
     three fields:
     err = 1 "Trust/don't trust" boolean. Trust the answer if the
              reciprocal condition number is less than the threshold
              sqrt(n) * slamch('Epsilon').
     err = 2 "Guaranteed" error bound: The estimated forward error,
              almost certainly within a factor of 10 of the true error
              so long as the next entry is greater than the threshold
              sqrt(n) * slamch('Epsilon'). This error bound should only
              be trusted if the previous boolean is true.
     err = 3  Reciprocal condition number: Estimated normwise
              reciprocal condition number.  Compared with the threshold
              sqrt(n) * slamch('Epsilon') to determine if the error
              estimate is "guaranteed". These reciprocal condition
              numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some
              appropriately scaled matrix Z.
              Let Z = S*A, where S scales each row by a power of the
              radix so all absolute row sums of Z are approximately 1.
     See Lapack Working Note 165 for further details and extra
     cautions.
 

 
 <i>ERR_BNDS_COMP</i> 

 
          ERR_BNDS_COMP is REAL array, dimension (NRHS, N_ERR_BNDS)
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
     componentwise accuracy is not requested (PARAMS(3) = 0.0), then
     ERR_BNDS_COMP is not accessed.  If N_ERR_BNDS .LT. 3, then at most
     the first (:,N_ERR_BNDS)
          entries are returned.The first index in ERR_BNDS_COMP(i,
                                                                :) corresponds to the ith
              right
              - hand side.The second index in ERR_BNDS_COMP(
                    :, err) contains the following
     three fields:
     err = 1 "Trust/don't trust" boolean. Trust the answer if the
              reciprocal condition number is less than the threshold
              sqrt(n) * slamch('Epsilon').
     err = 2 "Guaranteed" error bound: The estimated forward error,
              almost certainly within a factor of 10 of the true error
              so long as the next entry is greater than the threshold
              sqrt(n) * slamch('Epsilon'). This error bound should only
              be trusted if the previous boolean is true.
     err = 3  Reciprocal condition number: Estimated componentwise
              reciprocal condition number.  Compared with the threshold
              sqrt(n) * slamch('Epsilon') to determine if the error
              estimate is "guaranteed". These reciprocal condition
              numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some
              appropriately scaled matrix Z.
              Let Z = S*(A*diag(x)), where x is the solution for the
              current right-hand side and S scales each row of
              A*diag(x) by a power of the radix so all absolute row
              sums of Z are approximately 1.
     See Lapack Working Note 165 for further details and extra
     cautions.
 

 
 <i>NPARAMS</i> 

 <pre>
          NPARAMS is INTEGER
     Specifies the number of parameters set in PARAMS.  If .LE. 0, the
     PARAMS array is never referenced and default values are used.
</pre> 

 
 <i>PARAMS</i> 

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

 
 <i>WORK</i> 

 <pre>
          WORK is REAL array, dimension (4*N)
</pre> 

 
 <i>IWORK</i> 

 <pre>
          IWORK is INTEGER array, dimension (N)
</pre> 

 
 <i>INFO</i> 

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
         componentwise error is not requested (<a HREF="//www.systutorials.com/docs/linux/man/3-PARAMS/">PARAMS</a>(3) = 0.0) then
         the Jth right-hand side is the first with a normwise error
         bound that is not guaranteed (the smallest J such
         that ERR_BNDS_NORM(J,1) = 0.0). By default (<a HREF="//www.systutorials.com/docs/linux/man/3-PARAMS/">PARAMS</a>(3) = 1.0)
         the Jth right-hand side is the first with either a normwise or
         componentwise error bound that is not guaranteed (the smallest
         J such that either ERR_BNDS_NORM(J,1) = 0.0 or
         ERR_BNDS_COMP(J,1) = 0.0). See the definition of
         ERR_BNDS_NORM(:,1) and ERR_BNDS_COMP(:,1). To get information
         about all of the right-hand sides check ERR_BNDS_NORM or
         ERR_BNDS_COMP.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl>
<dt>
<dd> Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl>
<dt>
<dd> April 2012</dl>
 

 

 

 Definition at line 437 of file sgbrfsx.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


