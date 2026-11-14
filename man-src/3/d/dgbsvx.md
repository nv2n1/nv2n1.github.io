---
title: "dgbsvx(3)"
name: "dgbsvx"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgbsvx/"
description: "dgbsvx.f –"
---

<h2 class="name">NAME</h2>
<p> dgbsvx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgbsvx</code> (FACT, TRANS, N, KL, KU, NRHS, AB, LDAB, AFB, LDAFB, IPIV, EQUED, R, C, B, LDB, X, LDX, RCOND, FERR, BERR, WORK, IWORK, INFO)<br />
 <i></i><code> DGBSVX computes the solution to system of linear equations A * X = B for GB matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgbsvx (characterFACT, characterTRANS, integerN, integerKL, integerKU, integerNRHS, double precision, dimension( ldab, * )AB, integerLDAB, double precision, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, characterEQUED, double precision, dimension( * )R, double precision, dimension( * )C, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldx, * )X, integerLDX, double precisionRCOND, double precision, dimension( * )FERR, double precision, dimension( * )BERR, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code> DGBSVX computes the solution to system of linear equations A * X = B for GB matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGBSVX uses the LU factorization to compute the solution to a real
 system of linear equations A * X = B, A**T * X = B, or A**H * X = B,
 where A is a band matrix of order N with KL subdiagonals and KU
 superdiagonals, and X and B are N-by-NRHS matrices.
 Error bounds on the solution and a condition estimate are also
 provided.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 The following steps are performed by this subroutine:
 1. If FACT = 'E', real scaling factors are computed to equilibrate
    the system:
       TRANS = 'N':  diag(R)*A*diag(C)     *inv(diag(C))*X = diag(R)*B
       TRANS = 'T': (diag(R)*A*diag(C))**T *inv(diag(R))*X = diag(C)*B
       TRANS = 'C': (diag(R)*A*diag(C))**H *inv(diag(R))*X = diag(C)*B
    Whether or not the system will be equilibrated depends on the
    scaling of the matrix A, but if equilibration is used, A is
    overwritten by diag(R)*A*diag(C) and B by diag(R)*B (if TRANS='N')
    or diag(C)*B (if TRANS = 'T' or 'C').
 2. If FACT = 'N' or 'E', the LU decomposition is used to factor the
    matrix A (after equilibration if FACT = 'E') as
       A = L * U,
    where L is a product of permutation and unit lower triangular
    matrices with KL subdiagonals, and U is upper triangular with
    KL+KU superdiagonals.
 3. If some U(i,i)=0, so that U is exactly singular, then the routine
    returns with INFO = i. Otherwise, the factored form of A is used
    to estimate the condition number of the matrix A.  If the
    reciprocal of the condition number is less than machine precision,
    INFO = N+1 is returned as a warning, but the routine still goes on
    to solve for X and compute error bounds as described below.
 4. The system of equations is solved for X using the factored form
    of A.
 5. Iterative refinement is applied to improve the computed solution
    matrix and calculate error bounds and backward error estimates
    for it.
 6. If equilibration was used, the matrix X is premultiplied by
    diag(C) (if TRANS = 'N') or diag(R) (if TRANS = 'T' or 'C') so
    that it solves the original system before equilibration.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>FACT</i> </p>
<pre>
          FACT is CHARACTER*1
          Specifies whether or not the factored form of the matrix A is
          supplied on entry, and if not, whether the matrix A should be
          equilibrated before it is factored.
          = 'F':  On entry, AFB and IPIV contain the factored form of
                  A.  If EQUED is not 'N', the matrix A has been
                  equilibrated with scaling factors given by R and C.
                  AB, AFB, and IPIV are not modified.
          = 'N':  The matrix A will be copied to AFB and factored.
          = 'E':  The matrix A will be equilibrated if necessary, then
                  copied to AFB and factored.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations.
          = 'N':  A * X = B     (No transpose)
          = 'T':  A**T * X = B  (Transpose)
          = 'C':  A**H * X = B  (Transpose)
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of linear equations, i.e., the order of the
          matrix A.  N &gt;= 0.
</pre>
<p> <i>KL</i> </p>
<pre>
          KL is INTEGER
          The number of subdiagonals within the band of A.  KL &gt;= 0.
</pre>
<p> <i>KU</i> </p>
<pre>
          KU is INTEGER
          The number of superdiagonals within the band of A.  KU &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<p>          AB is DOUBLE PRECISION array, dimension (LDAB,N)<br />
          On entry, the matrix A in band storage, in rows 1 to KL+KU+1.<br />
          The j-th column of A is stored in the j-th column of the<br />
          array AB as follows:<br />
          AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)&lt;=i&lt;=min(N,j+kl)<br />
          If FACT = &#8216;F&#8217; and EQUED is not &#8216;N&#8217;, then A must have been<br />
          equilibrated by the scaling factors in R and/or C.  AB is not<br />
          modified if FACT = &#8216;F&#8217; or &#8216;N&#8217;, or if FACT = &#8216;E&#8217; and<br />
          EQUED = &#8216;N&#8217; on exit.<br />
          On exit, if EQUED .ne. &#8216;N&#8217;, A is scaled as follows:<br />
          EQUED = &#8216;R&#8217;:  A := diag(R) * A<br />
          EQUED = &#8216;C&#8217;:  A := A * diag(C)<br />
          EQUED = &#8216;B&#8217;:  A := diag(R) * A * diag(C).</p>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KL+KU+1.
</pre>
<p> <i>AFB</i> </p>
<pre>
          AFB is DOUBLE PRECISION array, dimension (LDAFB,N)
          If FACT = 'F', then AFB is an input argument and on entry
          contains details of the LU factorization of the band matrix
          A, as computed by DGBTRF.  U is stored as an upper triangular
          band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1,
          and the multipliers used during the factorization are stored
          in rows KL+KU+2 to 2*KL+KU+1.  If EQUED .ne. 'N', then AFB is
          the factored form of the equilibrated matrix A.
          If FACT = 'N', then AFB is an output argument and on exit
          returns details of the LU factorization of A.
          If FACT = 'E', then AFB is an output argument and on exit
          returns details of the LU factorization of the equilibrated
          matrix A (see the description of AB for the form of the
          equilibrated matrix).
</pre>
<p> <i>LDAFB</i> </p>
<pre>
          LDAFB is INTEGER
          The leading dimension of the array AFB.  LDAFB &gt;= 2*KL+KU+1.
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          If FACT = 'F', then IPIV is an input argument and on entry
          contains the pivot indices from the factorization A = L*U
          as computed by DGBTRF; row i of the matrix was interchanged
          with row IPIV(i).
          If FACT = 'N', then IPIV is an output argument and on exit
          contains the pivot indices from the factorization A = L*U
          of the original matrix A.
          If FACT = 'E', then IPIV is an output argument and on exit
          contains the pivot indices from the factorization A = L*U
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
          otherwise, R is an output argument.If FACT = &#8216;F&#8217; and EQUED = &#8216;R&#8217; or &#8216;B&#8217;, each element of R must be positive.</p>
<p> <i>C</i> </p>
<p>          C is DOUBLE PRECISION array, dimension (N)<br />
          The column scale factors for A.  If EQUED = &#8216;C&#8217; or &#8216;B&#8217;, A is<br />
          multiplied on the right by diag(C);<br />
          if EQUED<br />
              = &#8216;N&#8217; or &#8216;R&#8217;, C<br />
                                is not accessed.C is an input argument if FACT = &#8216;F&#8217;;<br />
          otherwise, C is an output argument.If FACT = &#8216;F&#8217; and EQUED = &#8216;C&#8217; or &#8216;B&#8217;, each element of C must be positive.</p>
<p> <i>B</i> </p>
<pre><code>
B is DOUBLE PRECISION array, dimension(LDB, NRHS) On entry, the right hand side matrix B.On exit,
    if EQUED = 'N', B is not modified;
if TRANS
    = 'N' and EQUED = 'R' or 'B', B is overwritten by
                                          diag(R) *
                                      B;
if TRANS
= 'T' or 'C' and EQUED = 'C' or 'B', B is
                                             overwritten by
                                             diag(C) *
                                         B.
</code></pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (LDX,NRHS)
          If INFO = 0 or INFO = N+1, the N-by-NRHS solution matrix X
          to the original system of equations.  Note that A and B are
          modified on exit if EQUED .ne. 'N', and the solution to the
          equilibrated system is inv(diag(C))*X if TRANS = 'N' and
          EQUED = 'C' or 'B', or inv(diag(R))*X if TRANS = 'T' or 'C'
          and EQUED = 'R' or 'B'.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is DOUBLE PRECISION
          The estimate of the reciprocal condition number of the matrix
          A after equilibration (if done).  If RCOND is less than the
          machine precision (in particular, if RCOND = 0), the matrix
          is singular to working precision.  This condition is
          indicated by a return code of INFO &gt; 0.
</pre>
<p> <i>FERR</i> </p>
<pre>
          FERR is DOUBLE PRECISION array, dimension (NRHS)
          The estimated forward error bound for each solution vector
          X(j) (the j-th column of the solution matrix X).
          If XTRUE is the true solution corresponding to X(j), FERR(j)
          is an estimated upper bound for the magnitude of the largest
          element in (X(j) - XTRUE) divided by the magnitude of the
          largest element in X(j).  The estimate is as reliable as
          the estimate for RCOND, and is almost always a slight
          overestimate of the true error.
</pre>
<p> <i>BERR</i> </p>
<pre>
          BERR is DOUBLE PRECISION array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (3*N)
          On exit, WORK(1) contains the reciprocal pivot growth
          factor norm(A)/norm(U). The &quot;max absolute element&quot; norm is
          used. If WORK(1) is much less than 1, then the stability
          of the LU factorization of the (equilibrated) matrix A
          could be poor. This also means that the solution X, condition
          estimator RCOND, and forward error bound FERR could be
          unreliable. If factorization fails with 0&lt;INFO&lt;=N, then
          WORK(1) contains the reciprocal pivot growth factor for the
          leading INFO columns of A.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, and i is
                &lt;= N:  U(i,i) is exactly zero.  The factorization
                       has been completed, but the factor U is exactly
                       singular, so the solution and error bounds
                       could not be computed. RCOND = 0 is returned.
                = N+1: U is nonsingular, but RCOND is less than machine
                       precision, meaning that the matrix is singular
                       to working precision.  Nevertheless, the
                       solution and error bounds are computed because
                       there are a number of situations where the
                       computed solution can be more accurate than the
                       value of RCOND would suggest.
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
<p> Definition at line 368 of file dgbsvx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
