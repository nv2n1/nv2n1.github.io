---
title: "ctrsyl(3)"
name: "ctrsyl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctrsyl/"
description: "ctrsyl.f –"
---

<h2 class="name">NAME</h2>
<p> ctrsyl.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctrsyl</code> (TRANA, TRANB, ISGN, M, N, A, LDA, B, LDB, C, LDC, SCALE, INFO)<br />
 <i></i><code>CTRSYL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctrsyl (characterTRANA, characterTRANB, integerISGN, integerM, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldc, * )C, integerLDC, realSCALE, integerINFO)</h3>
<p> <code>CTRSYL</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTRSYL solves the complex Sylvester matrix equation:
    op(A)*X + X*op(B) = scale*C or
    op(A)*X - X*op(B) = scale*C,
 where op(A) = A or A**H, and A and B are both upper triangular. A is
 M-by-M and B is N-by-N; the right hand side C and the solution X are
 M-by-N; and scale is an output scale factor, set &lt;= 1 to avoid
 overflow in X.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANA</i> </p>
<pre>
          TRANA is CHARACTER*1
          Specifies the option op(A):
          = 'N': op(A) = A    (No transpose)
          = 'C': op(A) = A**H (Conjugate transpose)
</pre>
<p> <i>TRANB</i> </p>
<pre>
          TRANB is CHARACTER*1
          Specifies the option op(B):
          = 'N': op(B) = B    (No transpose)
          = 'C': op(B) = B**H (Conjugate transpose)
</pre>
<p> <i>ISGN</i> </p>
<pre>
          ISGN is INTEGER
          Specifies the sign in the equation:
          = +1: solve op(A)*X + X*op(B) = scale*C
          = -1: solve op(A)*X - X*op(B) = scale*C
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The order of the matrix A, and the number of rows in the
          matrices X and C. M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix B, and the number of columns in the
          matrices X and C. N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,M)
          The upper triangular matrix A.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,N)
          The upper triangular matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,N).
</pre>
<p> <i>C</i> </p>
<pre>
          C is COMPLEX array, dimension (LDC,N)
          On entry, the M-by-N right hand side matrix C.
          On exit, C is overwritten by the solution matrix X.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1,M)
</pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is REAL
          The scale factor, scale, set &lt;= 1 to avoid overflow in X.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          = 1: A and B have common or very close eigenvalues; perturbed
               values were used to solve the equation (but the matrices
               A and B are unchanged).
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
<p> Definition at line 157 of file ctrsyl.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
