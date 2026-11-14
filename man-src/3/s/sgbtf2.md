---
title: "sgbtf2(3)"
name: "sgbtf2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbtf2/"
---

<h2 class="name">NAME</h2>
 

 sgbtf2.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbtf2</b> (M, N, KL, KU, AB, LDAB, IPIV, INFO) 
 <i></i><b>SGBTF2</b> computes the LU factorization of a general band matrix using the unblocked version of the algorithm.

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbtf2 (integerM, integerN, integerKL, integerKU, real, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, integerINFO)</h3>

 

 

 <b>SGBTF2</b> computes the LU factorization of a general band matrix using the unblocked version of the algorithm. 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBTF2 computes an LU factorization of a real m-by-n band matrix A
 using partial pivoting with row interchanges.
 This is the unblocked version of the algorithm, calling Level 2 BLAS.
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

 <pre><code>
AB is REAL array, dimension(LDAB, N) On entry, the matrix A in band storage, in rows KL + 1 to 2 * KL + KU + 1; rows 1 to KL of the array need not be set.
          The j-th column of A is stored in the j-th column of the
          array AB as follows:
          AB(kl+ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl)
          On exit, details of the factorization: U is stored as an
          upper triangular band matrix with KL+KU superdiagonals in
          rows 1 to KL+KU+1, and the multipliers used during the
          factorization are stored in rows KL+KU+2 to 2*KL+KU+1.
          See below for further details.
</code></pre> 

 
 <i>LDAB</i> 

 <pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= 2*KL+KU+1.
</pre> 

 
 <i>IPIV</i> 

 <pre><code>
IPIV is INTEGER array, dimension(min(M, N))
                           The pivot indices; for
1 &lt;= i &lt;= min(M, N), row i of the
                     matrix was interchanged with row IPIV(i)
                         .
</code></pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = +i, U(i,i) is exactly zero. The factorization
               has been completed, but the factor U is exactly
               singular, and division by zero will occur if it is used
               to solve a system of equations.
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
<dd> September 2012</dl>
 

 <b>Further Details: </b>
<dl>
<dt>
<dd> 

 

 <pre>
  The band storage scheme is illustrated by the following example, when
  M = N = 6, KL = 2, KU = 1:
  On entry:                       On exit:
      *    *    *    +    +    +       *    *    *   u14  u25  u36
      *    *    +    +    +    +       *    *   u13  u24  u35  u46
      *   a12  a23  a34  a45  a56      *   u12  u23  u34  u45  u56
     a11  a22  a33  a44  a55  a66     u11  u22  u33  u44  u55  u66
     a21  a32  a43  a54  a65   *      m21  m32  m43  m54  m65   *
     a31  a42  a53  a64   *    *      m31  m42  m53  m64   *    *
  Array elements marked * are not used by the routine; elements marked
  + need not be set on entry, but are required by the routine to store
  elements of U, because of fill-in resulting from the row
  interchanges.
</pre> 

 
&nbsp;<wbr></dl>
 

 

 

 Definition at line 146 of file sgbtf2.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


