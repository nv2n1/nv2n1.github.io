---
title: "sgbequ(3)"
name: "sgbequ"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbequ/"
---

<h2 class="name">NAME</h2>
 

 sgbequ.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbequ</b> (M, N, KL, KU, AB, LDAB, R, C, ROWCND, COLCND, AMAX, INFO) 
 <i></i><b>SGBEQU</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbequ (integerM, integerN, integerKL, integerKU, real, dimension( ldab, * )AB, integerLDAB, real, dimension( * )R, real, dimension( * )C, realROWCND, realCOLCND, realAMAX, integerINFO)</h3>

 

 

 <b>SGBEQU</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBEQU computes row and column scalings intended to equilibrate an
 M-by-N band matrix A and reduce its condition number.  R returns the
 row scale factors and C the column scale factors, chosen to try to
 make the largest element in each row and column of the matrix B with
 elements B(i,j)=R(i)*A(i,j)*C(j) have absolute value 1.
 R(i) and C(j) are restricted to be between SMLNUM = smallest safe
 number and BIGNUM = largest safe number.  Use of these scaling
 factors is not guaranteed to reduce the condition number of A but
 works well in practice.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>M</i> 

 <pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre> 

 
 <i>N</i> 

 <pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
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
          The band matrix A, stored in rows 1 to KL+KU+1.  The j-th
          column of A is stored in the j-th column of the array AB as
          follows:
          AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl).
</pre> 

 
 <i>LDAB</i> 

 <pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KL+KU+1.
</pre> 

 
 <i>R</i> 

 <pre>
          R is REAL array, dimension (M)
          If INFO = 0, or INFO &gt; M, R contains the row scale factors
          for A.
</pre> 

 
 <i>C</i> 

 <pre>
          C is REAL array, dimension (N)
          If INFO = 0, C contains the column scale factors for A.
</pre> 

 
 <i>ROWCND</i> 

 <pre>
          ROWCND is REAL
          If INFO = 0 or INFO &gt; M, ROWCND contains the ratio of the
          smallest R(i) to the largest R(i).  If ROWCND &gt;= 0.1 and
          AMAX is neither too large nor too small, it is not worth
          scaling by R.
</pre> 

 
 <i>COLCND</i> 

 <pre>
          COLCND is REAL
          If INFO = 0, COLCND contains the ratio of the smallest
          C(i) to the largest C(i).  If COLCND &gt;= 0.1, it is not
          worth scaling by C.
</pre> 

 
 <i>AMAX</i> 

 <pre>
          AMAX is REAL
          Absolute value of largest matrix element.  If AMAX is very
          close to overflow or very close to underflow, the matrix
          should be scaled.
</pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, and i is
                &lt;= M:  the i-th row of A is exactly zero
                &gt;  M:  the (i-M)-th column of A is exactly zero
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
 

 

 

 Definition at line 153 of file sgbequ.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


