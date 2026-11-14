---
title: "cpbsvx(3)"
name: "cpbsvx"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpbsvx/"
description: "cpbsvx.f –"
---

<h2 class="name">NAME</h2>
<p> cpbsvx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cpbsvx</code> (FACT, UPLO, N, KD, NRHS, AB, LDAB, AFB, LDAFB, EQUED, S, B, LDB, X, LDX, RCOND, FERR, BERR, WORK, RWORK, INFO)<br />
 <i></i><code> CPBSVX computes the solution to system of linear equations A * X = B for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpbsvx (characterFACT, characterUPLO, integerN, integerKD, integerNRHS, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldafb, * )AFB, integerLDAFB, characterEQUED, real, dimension( * )S, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldx, * )X, integerLDX, realRCOND, real, dimension( * )FERR, real, dimension( * )BERR, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code> CPBSVX computes the solution to system of linear equations A * X = B for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPBSVX uses the Cholesky factorization A = U**H*U or A = L*L**H to
 compute the solution to a complex system of linear equations
    A * X = B,
 where A is an N-by-N Hermitian positive definite band matrix and X
 and B are N-by-NRHS matrices.
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
       diag(S) * A * diag(S) * inv(diag(S)) * X = diag(S) * B
    Whether or not the system will be equilibrated depends on the
    scaling of the matrix A, but if equilibration is used, A is
    overwritten by diag(S)*A*diag(S) and B by diag(S)*B.
 2. If FACT = 'N' or 'E', the Cholesky decomposition is used to
    factor the matrix A (after equilibration if FACT = 'E') as
       A = U**H * U,  if UPLO = 'U', or
       A = L * L**H,  if UPLO = 'L',
    where U is an upper triangular band matrix, and L is a lower
    triangular band matrix.
 3. If the leading i-by-i principal minor is not positive definite,
    then the routine returns with INFO = i. Otherwise, the factored
    form of A is used to estimate the condition number of the matrix
    A.  If the reciprocal of the condition number is less than machine
    precision, INFO = N+1 is returned as a warning, but the routine
    still goes on to solve for X and compute error bounds as
    described below.
 4. The system of equations is solved for X using the factored form
    of A.
 5. Iterative refinement is applied to improve the computed solution
    matrix and calculate error bounds and backward error estimates
    for it.
 6. If equilibration was used, the matrix X is premultiplied by
    diag(S)
 so that it solves the original system before
     equilibration.
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
          = 'F':  On entry, AFB contains the factored form of A.
                  If EQUED = 'Y', the matrix A has been equilibrated
                  with scaling factors given by S.  AB and AFB will not
                  be modified.
          = 'N':  The matrix A will be copied to AFB and factored.
          = 'E':  The matrix A will be equilibrated if necessary, then
                  copied to AFB and factored.
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
<p> <i>KD</i> </p>
<pre>
          KD is INTEGER
          The number of superdiagonals of the matrix A if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'.  KD &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right-hand sides, i.e., the number of columns
          of the matrices B and X.  NRHS &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<p>          AB is COMPLEX array, dimension (LDAB,N)<br />
          On entry, the upper or lower triangle of the Hermitian band<br />
          matrix A, stored in the first KD+1 rows of the array, except<br />
          if FACT = &#8216;F&#8217; and EQUED = &#8216;Y&#8217;, then A must contain the<br />
          equilibrated matrix diag(S)*A*diag(S).  The j-th column of A<br />
          is stored in the j-th column of the array AB as follows:<br />
          if UPLO = &#8216;U&#8217;, AB(KD+1+i-j,j) = A(i,j) for max(1,j-KD)&lt;=i&lt;=j;<br />
          if UPLO = &#8216;L&#8217;, AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(N,j+KD).<br />
          See below for further details.<br />
          On exit, if FACT = &#8216;E&#8217; and EQUED = &#8216;Y&#8217;, A is overwritten by<br />
          diag(S)*A*diag(S).</p>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array A.  LDAB &gt;= KD+1.
</pre>
<p> <i>AFB</i> </p>
<pre>
          AFB is COMPLEX array, dimension (LDAFB,N)
          If FACT = 'F', then AFB is an input argument and on entry
          contains the triangular factor U or L from the Cholesky
          factorization A = U**H*U or A = L*L**H of the band matrix
          A, in the same storage format as A (see AB).  If EQUED = 'Y',
          then AFB is the factored form of the equilibrated matrix A.
          If FACT = 'N', then AFB is an output argument and on exit
          returns the triangular factor U or L from the Cholesky
          factorization A = U**H*U or A = L*L**H.
          If FACT = 'E', then AFB is an output argument and on exit
          returns the triangular factor U or L from the Cholesky
          factorization A = U**H*U or A = L*L**H of the equilibrated
          matrix A (see the description of A for the form of the
          equilibrated matrix).
</pre>
<p> <i>LDAFB</i> </p>
<pre>
          LDAFB is INTEGER
          The leading dimension of the array AFB.  LDAFB &gt;= KD+1.
</pre>
<p> <i>EQUED</i> </p>
<pre>
          EQUED is CHARACTER*1
          Specifies the form of equilibration that was done.
          = 'N':  No equilibration (always true if FACT = 'N').
          = 'Y':  Equilibration was done, i.e., A has been replaced by
                  diag(S) * A * diag(S).
          EQUED is an input argument if FACT = 'F'; otherwise, it is an
          output argument.
</pre>
<p> <i>S</i> </p>
<pre><code>
          S is REAL array, dimension (N)
          The scale factors for A;
          not accessed if EQUED = 'N'.S is
                                      an input argument if FACT = 'F';
          otherwise, S is an output argument.If FACT = 'F' and EQUED = 'Y', each element of S must be positive.
</code></pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
          On entry, the N-by-NRHS right hand side matrix B.
          On exit, if EQUED = 'N', B is not modified; if EQUED = 'Y',
          B is overwritten by diag(S) * B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (LDX,NRHS)
          If INFO = 0 or INFO = N+1, the N-by-NRHS solution matrix X to
          the original system of equations.  Note that if EQUED = 'Y',
          A and B are modified on exit, and the solution to the
          equilibrated system is inv(diag(S))*X.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
          The estimate of the reciprocal condition number of the matrix
          A after equilibration (if done).  If RCOND is less than the
          machine precision (in particular, if RCOND = 0), the matrix
          is singular to working precision.  This condition is
          indicated by a return code of INFO &gt; 0.
</pre>
<p> <i>FERR</i> </p>
<pre>
          FERR is REAL array, dimension (NRHS)
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
          BERR is REAL array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (2*N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = i, and i is
                &lt;= N:  the leading minor of order i of A is
                       not positive definite, so the factorization
                       could not be completed, and the solution has not
                       been computed. RCOND = 0 is returned.
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The band storage scheme is illustrated by the following example, when
  N = 6, KD = 2, and UPLO = 'U':
  Two-dimensional storage of the Hermitian matrix A:
     a11  a12  a13
          a22  a23  a24
               a33  a34  a35
                    a44  a45  a46
                         a55  a56
     (aij=conjg(aji))         a66
  Band storage of the upper triangle of A:
      *    *   a13  a24  a35  a46
      *   a12  a23  a34  a45  a56
     a11  a22  a33  a44  a55  a66
  Similarly, if UPLO = 'L' the format of A is as follows:
     a11  a22  a33  a44  a55  a66
     a21  a32  a43  a54  a65   *
     a31  a42  a53  a64   *    *
  Array elements marked * are not used by the routine.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 341 of file cpbsvx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
