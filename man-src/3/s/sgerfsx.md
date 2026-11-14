---
title: "sgerfsx(3)"
name: "sgerfsx"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgerfsx/"
description: "sgerfsx.f –"
---

<h2 class="name">NAME</h2>
<p> sgerfsx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgerfsx</code> (TRANS, EQUED, N, NRHS, A, LDA, AF, LDAF, IPIV, R, C, B, LDB, X, LDX, RCOND, BERR, N_ERR_BNDS, ERR_BNDS_NORM, ERR_BNDS_COMP, NPARAMS, PARAMS, WORK, IWORK, INFO)<br />
 <i></i><code>SGERFSX</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgerfsx (characterTRANS, characterEQUED, integerN, integerNRHS, real, dimension( lda, * )A, integerLDA, real, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, real, dimension( * )R, real, dimension( * )C, real, dimension( ldb, * )B, integerLDB, real, dimension( ldx , * )X, integerLDX, realRCOND, real, dimension( * )BERR, integerN_ERR_BNDS, real, dimension( nrhs, * )ERR_BNDS_NORM, real, dimension( nrhs, * )ERR_BNDS_COMP, integerNPARAMS, real, dimension( * )PARAMS, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SGERFSX</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
    SGERFSX improves the computed solution to a system of linear
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
<dd> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
     Specifies the form of the system of equations:
       = 'N':  A * X = B     (No transpose)
       = 'T':  A**T * X = B  (Transpose)
       = 'C':  A**H * X = B  (Conjugate transpose = Transpose)
</pre>
<p> <i>EQUED</i> </p>
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
<p> <i>N</i> </p>
<pre>
          N is INTEGER
     The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
     The number of right hand sides, i.e., the number of columns
     of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
     The original N-by-N matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
     The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AF</i> </p>
<pre>
          AF is REAL array, dimension (LDAF,N)
     The factors L and U from the factorization A = P*L*U
     as computed by SGETRF.
</pre>
<p> <i>LDAF</i> </p>
<pre>
          LDAF is INTEGER
     The leading dimension of the array AF.  LDAF &gt;= max(1,N).
</pre>
<p> <i>IPIV</i> </p>
<p>IPIV is INTEGER array, dimension(N)<br />
                           The pivot indices from SGETRF; for<br />
1 &lt;= i &lt;= N, row i of the<br />
                 matrix was interchanged with row<br />
                 IPIV(i)<br />
                     .</p>
<p> <i>R</i> </p>
<p>          R is REAL array, dimension (N)<br />
     The row scale factors for A.  If EQUED = &#8216;R&#8217; or &#8216;B&#8217;, A is<br />
     multiplied on the left by diag(R);<br />
          if EQUED<br />
          = &#8216;N&#8217; or &#8216;C&#8217;, R is not accessed.If R is accessed, each element of R should be a power of the radix to ensure a reliable solution and error estimates.Scaling by powers of the radix does not cause rounding errors unless the result underflows or overflows.Rounding errors during scaling lead to refining with a matrix that is not equivalent to the input matrix, producing error estimates that may not be reliable.</p>
<p> <i>C</i> </p>
<p>          C is REAL array, dimension (N)<br />
     The column scale factors for A.  If EQUED = &#8216;C&#8217; or &#8216;B&#8217;, A is<br />
     multiplied on the right by diag(C);<br />
          if EQUED<br />
          = &#8216;N&#8217; or &#8216;R&#8217;, C is not accessed.If C is accessed, each element of C should be a power of the radix to ensure a reliable solution and error estimates.Scaling by powers of the radix does not cause rounding errors unless the result underflows or overflows.Rounding errors during scaling lead to refining with a matrix that is not equivalent to the input matrix, producing error estimates that may not be reliable.</p>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,NRHS)
     The right hand side matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
     The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension (LDX,NRHS)
     On entry, the solution matrix X, as computed by SGETRS.
     On exit, the improved solution matrix X.
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
          WORK is REAL array, dimension (4*N)
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
<dd> November 2011</dl>
<p> Definition at line 412 of file sgerfsx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
