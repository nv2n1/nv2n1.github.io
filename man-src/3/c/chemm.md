---
title: "chemm(3)"
name: "chemm"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chemm/"
description: "chemm.f –"
---

<h2 class="name">NAME</h2>
<p> chemm.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chemm</code> (SIDE, UPLO, M, N, ALPHA, A, LDA, B, LDB, BETA, C, LDC)<br />
 <i></i><code>CHEMM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chemm (characterSIDE, characterUPLO, integerM, integerN, complexALPHA, complex, dimension(lda,*)A, integerLDA, complex, dimension(ldb,*)B, integerLDB, complexBETA, complex, dimension(ldc,*)C, integerLDC)</h3>
<p> <code>CHEMM</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHEMM  performs one of the matrix-matrix operations
    C := alpha*A*B + beta*C,
 or
    C := alpha*B*A + beta*C,
 where alpha and beta are scalars, A is an hermitian matrix and  B and
 C are m by n matrices.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
           On entry,  SIDE  specifies whether  the  hermitian matrix  A
           appears on the  left or right  in the  operation as follows:
              SIDE = 'L' or 'l'   C := alpha*A*B + beta*C,
              SIDE = 'R' or 'r'   C := alpha*B*A + beta*C,
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
           On  entry,   UPLO  specifies  whether  the  upper  or  lower
           triangular  part  of  the  hermitian  matrix   A  is  to  be
           referenced as follows:
              UPLO = 'U' or 'u'   Only the upper triangular part of the
                                  hermitian matrix is to be referenced.
              UPLO = 'L' or 'l'   Only the lower triangular part of the
                                  hermitian matrix is to be referenced.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
           On entry,  M  specifies the number of rows of the matrix  C.
           M  must be at least zero.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
           On entry, N specifies the number of columns of the matrix C.
           N  must be at least zero.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is COMPLEX
           On entry, ALPHA specifies the scalar alpha.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array of DIMENSION ( LDA, ka ), where ka is
           m  when  SIDE = 'L' or 'l'  and is n  otherwise.
           Before entry  with  SIDE = 'L' or 'l',  the  m by m  part of
           the array  A  must contain the  hermitian matrix,  such that
           when  UPLO = 'U' or 'u', the leading m by m upper triangular
           part of the array  A  must contain the upper triangular part
           of the  hermitian matrix and the  strictly  lower triangular
           part of  A  is not referenced,  and when  UPLO = 'L' or 'l',
           the leading  m by m  lower triangular part  of the  array  A
           must  contain  the  lower triangular part  of the  hermitian
           matrix and the  strictly upper triangular part of  A  is not
           referenced.
           Before entry  with  SIDE = 'R' or 'r',  the  n by n  part of
           the array  A  must contain the  hermitian matrix,  such that
           when  UPLO = 'U' or 'u', the leading n by n upper triangular
           part of the array  A  must contain the upper triangular part
           of the  hermitian matrix and the  strictly  lower triangular
           part of  A  is not referenced,  and when  UPLO = 'L' or 'l',
           the leading  n by n  lower triangular part  of the  array  A
           must  contain  the  lower triangular part  of the  hermitian
           matrix and the  strictly upper triangular part of  A  is not
           referenced.
           Note that the imaginary parts  of the diagonal elements need
           not be set, they are assumed to be zero.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
           On entry, LDA specifies the first dimension of A as declared
           in the  calling (sub) program. When  SIDE = 'L' or 'l'  then
           LDA must be at least  max( 1, m ), otherwise  LDA must be at
           least max( 1, n ).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array of DIMENSION ( LDB, n ).
           Before entry, the leading  m by n part of the array  B  must
           contain the matrix B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
           On entry, LDB specifies the first dimension of B as declared
           in  the  calling  (sub)  program.   LDB  must  be  at  least
           max( 1, m ).
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is COMPLEX
           On entry,  BETA  specifies the scalar  beta.  When  BETA  is
           supplied as zero then C need not be set on input.
</pre>
<p> <i>C</i> </p>
<pre>
          C is COMPLEX array of DIMENSION ( LDC, n ).
           Before entry, the leading  m by n  part of the array  C must
           contain the matrix  C,  except when  beta  is zero, in which
           case C need not be set on entry.
           On exit, the array  C  is overwritten by the  m by n updated
           matrix.
</pre>
<p> <i>LDC</i> </p>
<pre>
          LDC is INTEGER
           On entry, LDC specifies the first dimension of C as declared
           in  the  calling  (sub)  program.   LDC  must  be  at  least
           max( 1, m ).
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Level 3 Blas routine.
  -- Written on 8-February-1989.
     Jack Dongarra, Argonne National Laboratory.
     Iain Duff, AERE Harwell.
     Jeremy Du Croz, Numerical Algorithms Group Ltd.
     Sven Hammarling, Numerical Algorithms Group Ltd.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 192 of file chemm.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
