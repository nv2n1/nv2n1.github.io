---
title: "sgbrfs(3)"
name: "sgbrfs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbrfs/"
---

<h2 class="name">NAME</h2>
 

 sgbrfs.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbrfs</b> (TRANS, N, KL, KU, NRHS, AB, LDAB, AFB, LDAFB, IPIV, B, LDB, X, LDX, FERR, BERR, WORK, IWORK, INFO) 
 <i></i><b>SGBRFS</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbrfs (characterTRANS, integerN, integerKL, integerKU, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, real, dimension( ldafb, * )AFB, integerLDAFB, integer, dimension( * )IPIV, real, dimension( ldb, * )B, integerLDB, real, dimension( ldx, * )X, integerLDX, real, dimension( * )FERR, real, dimension( * )BERR, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>

 

 

 <b>SGBRFS</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBRFS improves the computed solution to a system of linear
 equations when the coefficient matrix is banded, and provides
 error bounds and backward error estimates for the solution.
</pre> 

 
&nbsp;<wbr></dl>
 

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
          AB is REAL array, dimension (LDAB,N)
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
          AFB is REAL array, dimension (LDAFB,N)
          Details of the LU factorization of the band matrix A, as
          computed by SGBTRF.  U is stored as an upper triangular band
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

 <pre><code>
IPIV is INTEGER array, dimension(N)
                           The pivot indices from SGBTRF; for
1 &lt;= i &lt;= N, row i of the
                 matrix was interchanged with row
                 IPIV(i)
                     .
</code></pre> 

 
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
          On entry, the solution matrix X, as computed by SGBTRS.
          On exit, the improved solution matrix X.
</pre> 

 
 <i>LDX</i> 

 <pre>
          LDX is INTEGER
          The leading dimension of the array X.  LDX &gt;= max(1,N).
</pre> 

 
 <i>FERR</i> 

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

 
 <i>BERR</i> 

 <pre>
          BERR is REAL array, dimension (NRHS)
          The componentwise relative backward error of each solution
          vector X(j) (i.e., the smallest relative change in
          any element of A or B that makes X(j) an exact solution).
</pre> 

 
 <i>WORK</i> 

 <pre>
          WORK is REAL array, dimension (3*N)
</pre> 

 
 <i>IWORK</i> 

 <pre>
          IWORK is INTEGER array, dimension (N)
</pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Internal Parameters: </b>
<dl>
<dt>
<dd> 

 

 <pre>
  ITMAX is the maximum number of steps of iterative refinement.
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
<dd> November 2011</dl>
 

 

 

 Definition at line 204 of file sgbrfs.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


