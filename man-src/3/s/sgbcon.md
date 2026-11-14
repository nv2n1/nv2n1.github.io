---
title: "sgbcon(3)"
name: "sgbcon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbcon/"
---

<h2 class="name">NAME</h2>
 

 sgbcon.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbcon</b> (NORM, N, KL, KU, AB, LDAB, IPIV, ANORM, RCOND, WORK, IWORK, INFO) 
 <i></i><b>SGBCON</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbcon (characterNORM, integerN, integerKL, integerKU, real, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, realANORM, realRCOND, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>

 

 

 <b>SGBCON</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBCON estimates the reciprocal of the condition number of a real
 general band matrix A, in either the 1-norm or the infinity-norm,
 using the LU factorization computed by SGBTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as
    RCOND = 1 / ( norm(A) * norm(inv(A)) ).
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>NORM</i> 

 <pre>
          NORM is CHARACTER*1
          Specifies whether the 1-norm condition number or the
          infinity-norm condition number is required:
          = '1' or 'O':  1-norm;
          = 'I':         Infinity-norm.
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

 
 <i>ANORM</i> 

 <pre>
          ANORM is REAL
          If NORM = '1' or 'O', the 1-norm of the original matrix A.
          If NORM = 'I', the infinity-norm of the original matrix A.
</pre> 

 
 <i>RCOND</i> 

 <pre>
          RCOND is REAL
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(norm(A) * norm(inv(A))).
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
 

 

 

 Definition at line 146 of file sgbcon.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


