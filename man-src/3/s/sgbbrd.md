---
title: "sgbbrd(3)"
name: "sgbbrd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgbbrd/"
---

<h2 class="name">NAME</h2>
 

 sgbbrd.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgbbrd</b> (VECT, M, N, NCC, KL, KU, AB, LDAB, D, E, Q, LDQ, PT, LDPT, C, LDC, WORK, INFO) 
 <i></i><b>SGBBRD</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgbbrd (characterVECT, integerM, integerN, integerNCC, integerKL, integerKU, real, dimension( ldab, * )AB, integerLDAB, real, dimension( * )D, real, dimension( * )E, real, dimension( ldq, * )Q, integerLDQ, real, dimension( ldpt, * )PT, integerLDPT, real, dimension( ldc, * )C, integerLDC, real, dimension( * )WORK, integerINFO)</h3>

 

 

 <b>SGBBRD</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGBBRD reduces a real general m-by-n band matrix A to upper
 bidiagonal form B by an orthogonal transformation: Q**T * A * P = B.
 The routine computes B, and optionally forms Q or P**T, or computes
 Q**T*C for a given matrix C.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>VECT</i> 

 <pre>
          VECT is CHARACTER*1
          Specifies whether or not the matrices Q and P**T are to be
          formed.
          = 'N': do not form Q or P**T;
          = 'Q': form Q only;
          = 'P': form P**T only;
          = 'B': form both.
</pre> 

 
 <i>M</i> 

 <pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre> 

 
 <i>N</i> 

 <pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
</pre> 

 
 <i>NCC</i> 

 <pre>
          NCC is INTEGER
          The number of columns of the matrix C.  NCC &gt;= 0.
</pre> 

 
 <i>KL</i> 

 <pre>
          KL is INTEGER
          The number of subdiagonals of the matrix A. KL &gt;= 0.
</pre> 

 
 <i>KU</i> 

 <pre>
          KU is INTEGER
          The number of superdiagonals of the matrix A. KU &gt;= 0.
</pre> 

 
 <i>AB</i> 

 <pre>
          AB is REAL array, dimension (LDAB,N)
          On entry, the m-by-n band matrix A, stored in rows 1 to
          KL+KU+1. The j-th column of A is stored in the j-th column of
          the array AB as follows:
          AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl).
          On exit, A is overwritten by values generated during the
          reduction.
</pre> 

 
 <i>LDAB</i> 

 <pre>
          LDAB is INTEGER
          The leading dimension of the array A. LDAB &gt;= KL+KU+1.
</pre> 

 
 <i>D</i> 

 <pre>
          D is REAL array, dimension (min(M,N))
          The diagonal elements of the bidiagonal matrix B.
</pre> 

 
 <i>E</i> 

 <pre>
          E is REAL array, dimension (min(M,N)-1)
          The superdiagonal elements of the bidiagonal matrix B.
</pre> 

 
 <i>Q</i> 

 <pre>
          Q is REAL array, dimension (LDQ,M)
          If VECT = 'Q' or 'B', the m-by-m orthogonal matrix Q.
          If VECT = 'N' or 'P', the array Q is not referenced.
</pre> 

 
 <i>LDQ</i> 

 <pre><code>
LDQ is INTEGER
        The leading dimension of the array Q.LDQ &gt;= max(1, M) if VECT = 'Q' or 'B';
LDQ &gt;= 1 otherwise.
</code></pre> 

 
 <i>PT</i> 

 <pre>
          PT is REAL array, dimension (LDPT,N)
          If VECT = 'P' or 'B', the n-by-n orthogonal matrix P'.
          If VECT = 'N' or 'Q', the array PT is not referenced.
</pre> 

 
 <i>LDPT</i> 

 
LDPT is INTEGER
        The leading dimension of the array PT.LDPT &gt;= max(1, N) if VECT = 'P' or 'B';
LDPT &gt;= 1 otherwise.
 

 
 <i>C</i> 

 <pre>
          C is REAL array, dimension (LDC,NCC)
          On entry, an m-by-ncc matrix C.
          On exit, C is overwritten by Q**T*C.
          C is not referenced if NCC = 0.
</pre> 

 
 <i>LDC</i> 

 <pre><code>
LDC is INTEGER
        The leading dimension of the array C.LDC &gt;= max(1, M) if NCC
    &gt; 0;
LDC &gt;= 1 if NCC = 0.
</code></pre> 

 
 <i>WORK</i> 

 <pre>
          WORK is REAL array, dimension (2*max(M,N))
</pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
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
 

 

 

 Definition at line 187 of file sgbbrd.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


