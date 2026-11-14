---
title: "dgesvx(3)"
name: "dgesvx"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgesvx/"
description: "dgesvx.f –"
---

<h2 class="name">NAME</h2>
<p> dgesvx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgesvx</code> (FACT, TRANS, N, NRHS, A, LDA, AF, LDAF, IPIV, EQUED, R, C, B, LDB, X, LDX, RCOND, FERR, BERR, WORK, IWORK, INFO)<br />
 <i></i><code> DGESVX computes the solution to system of linear equations A * X = B for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgesvx (characterFACT, characterTRANS, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, characterEQUED, double precision, dimension( * )R, double precision, dimension( * )C, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldx, * )X, integerLDX, double precisionRCOND, double precision, dimension( * )FERR, double precision, dimension( * )BERR, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code> DGESVX computes the solution to system of linear equations A * X = B for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGESVX uses the LU factorization to compute the solution to a real
 system of linear equations
    A * X = B,
 where A is an N-by-N matrix and X and B are N-by-NRHS matrices.
 Error bounds on the solution and a condition estimate are also
 provided.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Description: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 The following steps are performed:
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
       A = P * L * U,
    where P is a permutation matrix, L is a unit lower triangular
    matrix, and U is upper triangular.
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
          = 'C':  A**H * X = B  (Transpose)
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
B is DOUBLE PRECISION array, dimension(LDB, NRHS) On entry, the N - by - NRHS right hand side matrix B.On exit,
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
          WORK is DOUBLE PRECISION array, dimension (4*N)
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
                &lt;= N:  U(i,i) is exactly zero.  The factorization has
                       been completed, but the factor U is exactly
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
<p> Definition at line 348 of file dgesvx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
