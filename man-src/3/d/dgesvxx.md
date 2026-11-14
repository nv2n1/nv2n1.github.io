---
title: "dgesvxx(3)"
name: "dgesvxx"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgesvxx/"
description: "dgesvxx.f –"
---

<h2 class="name">NAME</h2>
<p> dgesvxx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgesvxx</code> (FACT, TRANS, N, NRHS, A, LDA, AF, LDAF, IPIV, EQUED, R, C, B, LDB, X, LDX, RCOND, RPVGRW, BERR, N_ERR_BNDS, ERR_BNDS_NORM, ERR_BNDS_COMP, NPARAMS, PARAMS, WORK, IWORK, INFO)<br />
 <i></i><code> DGESVXX computes the solution to system of linear equations A * X = B for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgesvxx (characterFACT, characterTRANS, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, characterEQUED, double precision, dimension( * )R, double precision, dimension( * )C, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldx , * )X, integerLDX, double precisionRCOND, double precisionRPVGRW, double precision, dimension( * )BERR, integerN_ERR_BNDS, double precision, dimension( nrhs, * )ERR_BNDS_NORM, double precision, dimension( nrhs, * )ERR_BNDS_COMP, integerNPARAMS, double precision, dimension( * )PARAMS, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code> DGESVXX computes the solution to system of linear equations A * X = B for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
DGESVXX uses the LU factorization to compute the solution to a double precision system of linear equations A *X = B, where A is an N - by - N matrix and X and B are N - by - NRHS matrices.If requested, both normwise and maximum componentwise error bounds are returned.DGESVXX will return a solution with a tiny guaranteed error(O(eps) where eps is the working machine precision) unless the matrix is very ill - conditioned, in which case a warning is returned.Relevant condition numbers also are calculated and returned.DGESVXX accepts user - provided factorizations and equilibration factors;
see the definitions of the FACT and EQUED options.Solving with refinement and using a factorization from a previous
    DGESVXX call will also produce a solution with either
    O(eps)
    errors or warnings, but we cannot make that claim for general
    user-provided factorizations and equilibration factors if they
    differ from what DGESVXX would itself produce.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dt>
<dd>
<p>    The following steps are performed:<br />
    1. If FACT = &#8216;E&#8217;, double precision scaling factors are computed to equilibrate<br />
    the system:<br />
      TRANS = &#8216;N&#8217;:  diag(R)*A*diag(C)     *inv(diag(C))*X = diag(R)*B<br />
      TRANS = &#8216;T&#8217;: (diag(R)*A*diag(C))**T *inv(diag(R))*X = diag(C)*B<br />
      TRANS = &#8216;C&#8217;: (diag(R)*A*diag(C))**H *inv(diag(R))*X = diag(C)*B<br />
    Whether or not the system will be equilibrated depends on the<br />
    scaling of the matrix A, but if equilibration is used, A is<br />
    overwritten by diag(R)*A*diag(C) and B by diag(R)*B (if TRANS=&#8217;N&#8217;)<br />
    or diag(C)*B (if TRANS = &#8216;T&#8217; or &#8216;C&#8217;).<br />
    2. If FACT = &#8216;N&#8217; or &#8216;E&#8217;, the LU decomposition is used to factor<br />
    the matrix A (after equilibration if FACT = &#8216;E&#8217;) as<br />
      A = P * L * U,<br />
    where P is a permutation matrix, L is a unit lower triangular<br />
    matrix, and U is upper triangular.<br />
    3. If some U(i,i)=0, so that U is exactly singular, then the<br />
    routine returns with INFO = i. Otherwise, the factored form of A<br />
    is used to estimate the condition number of the matrix A (see<br />
    argument RCOND). If the reciprocal of the condition number is less<br />
    than machine precision, the routine still goes on to solve for X<br />
    and compute error bounds as described below.<br />
    4. The system of equations is solved for X using the factored form<br />
    of A.<br />
    5. By default (unless PARAMS(LA_LINRX_ITREF_I) is set to zero),<br />
    the routine will use iterative refinement to try to get a small<br />
    error and error bounds.  Refinement calculates the residual to at<br />
    least twice the working precision.<br />
    6. If equilibration was used, the matrix X is premultiplied by<br />
    diag(C) (if TRANS = &#8216;N&#8217;) or diag(R) (if TRANS = &#8216;T&#8217; or &#8216;C&#8217;) so<br />
    that it solves the original system before equilibration.</p>
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
       = 'F':  On entry, AF and IPIV contain the factored form of A.
               If EQUED is not 'N', the matrix A has been
               equilibrated with scaling factors given by R and C.
               A, AF, and IPIV are not modified.
       = 'N':  The matrix A will be copied to AF and factored.
       = 'E':  The matrix A will be equilibrated if necessary, then
               copied to AF and factored.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
     Specifies the form of the system of equations:
       = 'N':  A * X = B     (No transpose)
       = 'T':  A**T * X = B  (Transpose)
       = 'C':  A**H * X = B  (Conjugate Transpose = Transpose)
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
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
     On entry, the N-by-N matrix A.  If FACT = 'F' and EQUED is
     not 'N', then A must have been equilibrated by the scaling
     factors in R and/or C.  A is not modified if FACT = 'F' or
     'N', or if FACT = 'E' and EQUED = 'N' on exit.
     On exit, if EQUED .ne. 'N', A is scaled as follows:
     EQUED = 'R':  A := diag(R) * A
     EQUED = 'C':  A := A * diag(C)
     EQUED = 'B':  A := diag(R) * A * diag(C).
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
     The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AF</i> </p>
<pre>
          AF is DOUBLE PRECISION array, dimension (LDAF,N)
     If FACT = 'F', then AF is an input argument and on entry
     contains the factors L and U from the factorization
     A = P*L*U as computed by DGETRF.  If EQUED .ne. 'N', then
     AF is the factored form of the equilibrated matrix A.
     If FACT = 'N', then AF is an output argument and on exit
     returns the factors L and U from the factorization A = P*L*U
     of the original matrix A.
     If FACT = 'E', then AF is an output argument and on exit
     returns the factors L and U from the factorization A = P*L*U
     of the equilibrated matrix A (see the description of A for
     the form of the equilibrated matrix).
</pre>
<p> <i>LDAF</i> </p>
<pre>
          LDAF is INTEGER
     The leading dimension of the array AF.  LDAF &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
     If FACT = 'F', then IPIV is an input argument and on entry
     contains the pivot indices from the factorization A = P*L*U
     as computed by DGETRF; row i of the matrix was interchanged
     with row IPIV(i).
     If FACT = 'N', then IPIV is an output argument and on exit
     contains the pivot indices from the factorization A = P*L*U
     of the original matrix A.
     If FACT = 'E', then IPIV is an output argument and on exit
     contains the pivot indices from the factorization A = P*L*U
     of the equilibrated matrix A.
</pre>
<p> <i>EQUED</i> </p>
<pre>
          EQUED is CHARACTER*1
     Specifies the form of equilibration that was done.
       = 'N':  No equilibration (always true if FACT = 'N').
       = 'R':  Row equilibration, i.e., A has been premultiplied by
               diag(R).
       = 'C':  Column equilibration, i.e., A has been postmultiplied
               by diag(C).
       = 'B':  Both row and column equilibration, i.e., A has been
               replaced by diag(R) * A * diag(C).
     EQUED is an input argument if FACT = 'F'; otherwise, it is an
     output argument.
</pre>
<p> <i>R</i> </p>
<p>          R is DOUBLE PRECISION array, dimension (N)<br />
     The row scale factors for A.  If EQUED = &#8216;R&#8217; or &#8216;B&#8217;, A is<br />
     multiplied on the left by diag(R);<br />
          if EQUED<br />
              = &#8216;N&#8217; or &#8216;C&#8217;, R<br />
                                is not accessed.R is an input argument if FACT = &#8216;F&#8217;;<br />
          otherwise, R is an output argument.If FACT = &#8216;F&#8217; and EQUED = &#8216;R&#8217; or &#8216;B&#8217;, each element of R must be positive.If R is output, each element of R is a power of the radix.If R is input, each element of R should be a power of the radix to ensure a reliable solution and error estimates.Scaling by powers of the radix does not cause rounding errors unless the result underflows or overflows.Rounding errors during scaling lead to refining with a matrix that is not equivalent to the input matrix, producing error estimates that may not be reliable.</p>
<p> <i>C</i> </p>
<p>          C is DOUBLE PRECISION array, dimension (N)<br />
     The column scale factors for A.  If EQUED = &#8216;C&#8217; or &#8216;B&#8217;, A is<br />
     multiplied on the right by diag(C);<br />
          if EQUED<br />
              = &#8216;N&#8217; or &#8216;R&#8217;, C<br />
                                is not accessed.C is an input argument if FACT = &#8216;F&#8217;;<br />
          otherwise, C is an output argument.If FACT = &#8216;F&#8217; and EQUED = &#8216;C&#8217; or &#8216;B&#8217;, each element of C must be positive.If C is output, each element of C is a power of the radix.If C is input, each element of C should be a power of the radix to ensure a reliable solution and error estimates.Scaling by powers of the radix does not cause rounding errors unless the result underflows or overflows.Rounding errors during scaling lead to refining with a matrix that is not equivalent to the input matrix, producing error estimates that may not be reliable.</p>
<p> <i>B</i> </p>
<p>B is DOUBLE PRECISION array, dimension(LDB, NRHS) On entry, the N &#8211; by &#8211; NRHS right hand side matrix B.On exit,<br />
    if EQUED = &#8216;N&#8217;, B is not modified;<br />
if TRANS<br />
    = &#8216;N&#8217; and EQUED = &#8216;R&#8217; or &#8216;B&#8217;, B is overwritten by<br />
                                          diag(R) *<br />
                                      B;<br />
if TRANS<br />
= &#8216;T&#8217; or &#8216;C&#8217; and EQUED = &#8216;C&#8217; or &#8216;B&#8217;, B is<br />
                                             overwritten by<br />
                                             diag(C) *<br />
                                         B.</p>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
     The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,NRHS)
     If INFO = 0, the N-by-NRHS solution matrix X to the original
     system of equations.  Note that A and B are modified on exit
     if EQUED .ne. 'N', and the solution to the equilibrated system is
     inv(diag(C))*X if TRANS = 'N' and EQUED = 'C' or 'B', or
     inv(diag(R))*X if TRANS = 'T' or 'C' and EQUED = 'R' or 'B'.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
     The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is DOUBLE PRECISION
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
          RPVGRW is DOUBLE PRECISION
     Reciprocal pivot growth.  On exit, this contains the reciprocal
     pivot growth factor norm(A)/norm(U). The &quot;max absolute element&quot;
     norm is used.  If this is much less than 1, then the stability of
     the LU factorization of the (equilibrated) matrix A could be poor.
     This also means that the solution X, estimated condition numbers,
     and error bounds could be unreliable. If factorization fails with
     0&lt;INFO&lt;=N, then this contains the reciprocal pivot growth factor
     for the leading INFO columns of A.  In DGESVX, this quantity is
     returned in WORK(1).
</pre>
<p> <i>BERR</i> </p>
<pre>
          BERR is DOUBLE PRECISION array, dimension (NRHS)
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
<p>ERR_BNDS_NORM is DOUBLE PRECISION array, dimension(NRHS, N_ERR_BNDS) For each right &#8211; hand side, this array contains information about various error bounds and condition numbers corresponding to the normwise relative error, which is defined as follows : Normwise relative error in the ith solution vector : max_j(abs(XTRUE(j, i) &#8211; X(j, i)))&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;max_j abs(X(j, i)) The array is indexed by the type of error information as described below.There currently are up to three pieces of information returned.The first index in ERR_BNDS_NORM(i,<br />
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            :) corresponds to the ith right<br />
                                                                                                                                                                                                                                    &#8211; hand side.The second index in ERR_BNDS_NORM(<br />
                                                                                                                                                                                                                                          :, err) contains the following<br />
     three fields:<br />
     err = 1 &#8220;Trust/don&#8217;t trust&#8221; boolean. Trust the answer if the<br />
              reciprocal condition number is less than the threshold<br />
              sqrt(n) * dlamch(&#8216;Epsilon&#8217;).<br />
     err = 2 &#8220;Guaranteed&#8221; error bound: The estimated forward error,<br />
              almost certainly within a factor of 10 of the true error<br />
              so long as the next entry is greater than the threshold<br />
              sqrt(n) * dlamch(&#8216;Epsilon&#8217;). This error bound should only<br />
              be trusted if the previous boolean is true.<br />
     err = 3  Reciprocal condition number: Estimated normwise<br />
              reciprocal condition number.  Compared with the threshold<br />
              sqrt(n) * dlamch(&#8216;Epsilon&#8217;) to determine if the error<br />
              estimate is &#8220;guaranteed&#8221;. These reciprocal condition<br />
              numbers are 1 / (norm(Z^{-1},inf) * norm(Z,inf)) for some<br />
              appropriately scaled matrix Z.<br />
              Let Z = S*A, where S scales each row by a power of the<br />
              radix so all absolute row sums of Z are approximately 1.<br />
     See Lapack Working Note 165 for further details and extra<br />
     cautions.</p>
<p> <i>ERR_BNDS_COMP</i> </p>
<p>          ERR_BNDS_COMP is DOUBLE PRECISION array, dimension (NRHS, N_ERR_BNDS)<br />
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
              sqrt(n) * dlamch(&#8216;Epsilon&#8217;).<br />
     err = 2 &#8220;Guaranteed&#8221; error bound: The estimated forward error,<br />
              almost certainly within a factor of 10 of the true error<br />
              so long as the next entry is greater than the threshold<br />
              sqrt(n) * dlamch(&#8216;Epsilon&#8217;). This error bound should only<br />
              be trusted if the previous boolean is true.<br />
     err = 3  Reciprocal condition number: Estimated componentwise<br />
              reciprocal condition number.  Compared with the threshold<br />
              sqrt(n) * dlamch(&#8216;Epsilon&#8217;) to determine if the error<br />
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
          PARAMS is DOUBLE PRECISION array, dimension (NPARAMS)
     Specifies algorithm parameters.  If an entry is .LT. 0.0, then
     that entry will be filled with default value used for that
     parameter.  Only positions up to NPARAMS are accessed; defaults
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
            relative error in the double-precision algorithm.  Positive
            is true, 0.0 is false.
         Default: 1.0 (attempt componentwise convergence)
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (4*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
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
<p> Definition at line 537 of file dgesvxx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
