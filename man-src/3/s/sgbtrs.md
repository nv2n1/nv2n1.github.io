---
title: "sgbtrs(3)"
name: "sgbtrs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbtrs/"
---

<h2 class="name">NAME</h2>
 

 sgbtrs.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbtrs</b> (TRANS, N, KL, KU, NRHS, AB, LDAB, IPIV, B, LDB, INFO) 
 <i></i><b>SGBTRS</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbtrs (characterTRANS, integerN, integerKL, integerKU, integerNRHS, real, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, real, dimension( ldb, * )B, integerLDB, integerINFO)</h3>

 

 

 <b>SGBTRS</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBTRS solves a system of linear equations
    A * X = B  or  A**T * X = B
 with a general band matrix A using the LU factorization computed
 by SGBTRF.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>TRANS</i> 

 <pre>
          TRANS is CHARACTER*1
          Specifies the form of the system of equations.
          = 'N':  A * X = B  (No transpose)
          = 'T':  A**T* X = B  (Transpose)
          = 'C':  A**T* X = B  (Conjugate transpose = Transpose)
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
          of the matrix B.  NRHS &gt;= 0.
</pre> 

 
 <i>AB</i> 

 <pre>
          AB is REAL array, dimension (LDAB,N)
          Details of the LU factorization of the band matrix A, as
          computed by SGBTRF.  U is stored as an upper triangular band
          matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
          the multipliers used during the factorization are stored in
          rows KL+KU+2 to 2*KL+KU+1.
</pre> 

 
 <i>LDAB</i> 

 <pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= 2*KL+KU+1.
</pre> 

 
 <i>IPIV</i> 

 <pre><code>
IPIV is INTEGER array, dimension(N)
                           The pivot indices; for
1 &lt;= i &lt;= N, row i of the matrix was
                 interchanged with row
                 IPIV(i)
                     .
</code></pre> 

 
 <i>B</i> 

 <pre>
          B is REAL array, dimension (LDB,NRHS)
          On entry, the right hand side matrix B.
          On exit, the solution matrix X.
</pre> 

 
 <i>LDB</i> 

 <pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
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
 

 

 

 Definition at line 138 of file sgbtrs.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


