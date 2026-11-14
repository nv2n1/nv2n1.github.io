---
title: "cla_herfsx_extended(3)"
name: "cla_herfsx_extended"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_herfsx_extended/"
description: "cla_herfsx_extended.f –"
---

<h2 class="name">NAME</h2>
<p> cla_herfsx_extended.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cla_herfsx_extended</code> (PREC_TYPE, UPLO, N, NRHS, A, LDA, AF, LDAF, IPIV, COLEQU, C, B, LDB, Y, LDY, BERR_OUT, N_NORMS, ERR_BNDS_NORM, ERR_BNDS_COMP, RES, AYB, DY, Y_TAIL, RCOND, ITHRESH, RTHRESH, DZ_UB, IGNORE_CWISE, INFO)<br />
 <i></i><code>CLA_HERFSX_EXTENDED</code> improves the computed solution to a system of linear equations for Hermitian indefinite matrices by performing extra-precise iterative refinement and provides error bounds and backward error estimates for the solution.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cla_herfsx_extended (integerPREC_TYPE, characterUPLO, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, logicalCOLEQU, real, dimension( * )C, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldy, * )Y, integerLDY, real, dimension( * )BERR_OUT, integerN_NORMS, real, dimension( nrhs, * )ERR_BNDS_NORM, real, dimension( nrhs, * )ERR_BNDS_COMP, complex, dimension( * )RES, real, dimension( * )AYB, complex, dimension( * )DY, complex, dimension( * )Y_TAIL, realRCOND, integerITHRESH, realRTHRESH, realDZ_UB, logicalIGNORE_CWISE, integerINFO)</h3>
<p> <code>CLA_HERFSX_EXTENDED</code> improves the computed solution to a system of linear equations for Hermitian indefinite matrices by performing extra-precise iterative refinement and provides error bounds and backward error estimates for the solution. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 CLA_HERFSX_EXTENDED improves the computed solution to a system of
 linear equations by performing extra-precise iterative refinement
 and provides error bounds and backward error estimates for the solution.
 This subroutine is called by CHERFSX to perform iterative refinement.
 In addition to normwise error bound, the code provides maximum
 componentwise error bound if possible. See comments for ERR_BNDS_NORM
 and ERR_BNDS_COMP for details of the error bounds. Note that this
 subroutine is only resonsible for setting the second fields of
 ERR_BNDS_NORM and ERR_BNDS_COMP.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>PREC_TYPE</i> </p>
<pre>
          PREC_TYPE is INTEGER
     Specifies the intermediate precision to be used in refinement.
     The value is defined by ILAPREC(P) where P is a CHARACTER and
     P    = 'S':  Single
          = 'D':  Double
          = 'I':  Indigenous
          = 'X', 'E':  Extra
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
     The number of right-hand-sides, i.e., the number of columns of the
     matrix B.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
     On entry, the N-by-N matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
     The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AF</i> </p>
<pre>
          AF is COMPLEX array, dimension (LDAF,N)
     The block diagonal matrix D and the multipliers used to
     obtain the factor U or L as computed by CHETRF.
</pre>
<p> <i>LDAF</i> </p>
<pre>
          LDAF is INTEGER
     The leading dimension of the array AF.  LDAF &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
     Details of the interchanges and the block structure of D
     as determined by CHETRF.
</pre>
<p> <i>COLEQU</i> </p>
<pre>
          COLEQU is LOGICAL
     If .TRUE. then column equilibration was done to A before calling
     this routine. This is needed to compute the solution and error
     bounds correctly.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (N)
     The column scale factors for A. If COLEQU = .FALSE., C
     is not accessed. If C is input, each element of C should be a power
     of the radix to ensure a reliable solution and error estimates.
     Scaling by powers of the radix does not cause rounding errors unless
     the result underflows or overflows. Rounding errors during scaling
     lead to refining with a matrix that is not equivalent to the
     input matrix, producing error estimates that may not be
     reliable.
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
     The right-hand-side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
     The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>Y</i> </p>
<pre>
          Y is COMPLEX array, dimension
                    (LDY,NRHS)
     On entry, the solution matrix X, as computed by CHETRS.
     On exit, the improved solution matrix Y.
</pre>
<p> <i>LDY</i> </p>
<pre>
          LDY is INTEGER
     The leading dimension of the array Y.  LDY &gt;= max(1,N).
</pre>
<p> <i>BERR_OUT</i> </p>
<pre>
          BERR_OUT is REAL array, dimension (NRHS)
     On exit, BERR_OUT(j) contains the componentwise relative backward
     error for right-hand-side j from the formula
         max(i) ( abs(RES(i)) / ( abs(op(A_s))*abs(Y) + abs(B_s) )(i) )
     where abs(Z) is the componentwise absolute value of the matrix
     or vector Z. This is computed by CLA_LIN_BERR.
</pre>
<p> <i>N_NORMS</i> </p>
<p>N_NORMS is INTEGER<br />
        Determines which error bounds to return (see ERR_BNDS_NORM and ERR_BNDS_COMP)<br />
            .If N_NORMS &gt;= 1 return normwise error bounds.If N_NORMS &gt;= 2 return componentwise error bounds.</p>
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
     This subroutine is only responsible for setting the second field<br />
     above.<br />
     See Lapack Working Note 165 for further details and extra<br />
     cautions.</p>
<p> <i>ERR_BNDS_COMP</i> </p>
<p>          ERR_BNDS_COMP is REAL array, dimension<br />
                    (NRHS, N_ERR_BNDS)<br />
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
     This subroutine is only responsible for setting the second field<br />
     above.<br />
     See Lapack Working Note 165 for further details and extra<br />
     cautions.</p>
<p> <i>RES</i> </p>
<pre>
          RES is COMPLEX array, dimension (N)
     Workspace to hold the intermediate residual.
</pre>
<p> <i>AYB</i> </p>
<pre>
          AYB is REAL array, dimension (N)
     Workspace.
</pre>
<p> <i>DY</i> </p>
<pre>
          DY is COMPLEX array, dimension (N)
     Workspace to hold the intermediate solution.
</pre>
<p> <i>Y_TAIL</i> </p>
<pre>
          Y_TAIL is COMPLEX array, dimension (N)
     Workspace to hold the trailing bits of the intermediate solution.
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
<p> <i>ITHRESH</i> </p>
<pre>
          ITHRESH is INTEGER
     The maximum number of residual computations allowed for
     refinement. The default is 10. For 'aggressive' set to 100 to
     permit convergence using approximate factorizations or
     factorizations other than LU. If the factorization uses a
     technique other than Gaussian elimination, the guarantees in
     ERR_BNDS_NORM and ERR_BNDS_COMP may no longer be trustworthy.
</pre>
<p> <i>RTHRESH</i> </p>
<pre><code>
RTHRESH is REAL
        Determines when to stop refinement if the error estimate stops
            decreasing.Refinement will stop when the next solution no longer
                satisfies
                norm(dx_{i + 1}) &lt; RTHRESH *norm(dx_i)
where norm(Z) is
     the infinity norm of Z. RTHRESH satisfies 0 &lt; RTHRESH &lt;= 1. The
     default value is 0.5. For 'aggressive' set to 0.9 to permit
     convergence on extremely ill-conditioned matrices. See LAWN 165
     for more details.
</code></pre>
<p> <i>DZ_UB</i> </p>
<pre>
          DZ_UB is REAL
     Determines when to start considering componentwise convergence.
     Componentwise convergence is only considered after each component
     of the solution Y is stable, which we definte as the relative
     change in each component being less than DZ_UB. The default value
     is 0.25, requiring the first bit to be stable. See LAWN 165 for
     more details.
</pre>
<p> <i>IGNORE_CWISE</i> </p>
<pre>
          IGNORE_CWISE is LOGICAL
     If .TRUE. then ignore componentwise convergence. Default value
     is .FALSE..
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
       = 0:  Successful exit.
       &lt; 0:  if INFO = -i, the ith argument to CLA_HERFSX_EXTENDED had an illegal
             value
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
<p> Definition at line 393 of file cla_herfsx_extended.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
