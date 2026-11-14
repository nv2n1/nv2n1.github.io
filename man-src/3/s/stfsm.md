---
title: "stfsm(3)"
name: "stfsm"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stfsm/"
description: "stfsm.f –"
---

<h2 class="name">NAME</h2>
<p> stfsm.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>stfsm</code> (TRANSR, SIDE, UPLO, TRANS, DIAG, M, N, ALPHA, A, B, LDB)<br />
 <i></i><code>STFSM</code> solves a matrix equation (one operand is a triangular matrix in RFP format).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stfsm (characterTRANSR, characterSIDE, characterUPLO, characterTRANS, characterDIAG, integerM, integerN, realALPHA, real, dimension( 0: * )A, real, dimension( 0: ldb-1, 0: * )B, integerLDB)</h3>
<p> <code>STFSM</code> solves a matrix equation (one operand is a triangular matrix in RFP format). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 Level 3 BLAS like routine for A in RFP Format.
 STFSM  solves the matrix equation
    op( A )*X = alpha*B  or  X*op( A ) = alpha*B
 where alpha is a scalar, X and B are m by n matrices, A is a unit, or
 non-unit,  upper or lower triangular matrix  and  op( A )  is one  of
    op( A ) = A   or   op( A ) = A**T.
 A is in Rectangular Full Packed (RFP) Format.
 The matrix X is overwritten on B.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANSR</i> </p>
<pre>
          TRANSR is CHARACTER*1
          = 'N':  The Normal Form of RFP A is stored;
          = 'T':  The Transpose Form of RFP A is stored.
</pre>
<p> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
           On entry, SIDE specifies whether op( A ) appears on the left
           or right of X as follows:
              SIDE = 'L' or 'l'   op( A )*X = alpha*B.
              SIDE = 'R' or 'r'   X*op( A ) = alpha*B.
           Unchanged on exit.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
           On entry, UPLO specifies whether the RFP matrix A came from
           an upper or lower triangular matrix as follows:
           UPLO = 'U' or 'u' RFP A came from an upper triangular matrix
           UPLO = 'L' or 'l' RFP A came from a  lower triangular matrix
           Unchanged on exit.
</pre>
<p> <i>TRANS</i> </p>
<pre>
          TRANS is CHARACTER*1
           On entry, TRANS  specifies the form of op( A ) to be used
           in the matrix multiplication as follows:
              TRANS  = 'N' or 'n'   op( A ) = A.
              TRANS  = 'T' or 't'   op( A ) = A'.
           Unchanged on exit.
</pre>
<p> <i>DIAG</i> </p>
<pre>
          DIAG is CHARACTER*1
           On entry, DIAG specifies whether or not RFP A is unit
           triangular as follows:
              DIAG = 'U' or 'u'   A is assumed to be unit triangular.
              DIAG = 'N' or 'n'   A is not assumed to be unit
                                  triangular.
           Unchanged on exit.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
           On entry, M specifies the number of rows of B. M must be at
           least zero.
           Unchanged on exit.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
           On entry, N specifies the number of columns of B.  N must be
           at least zero.
           Unchanged on exit.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is REAL
           On entry,  ALPHA specifies the scalar  alpha. When  alpha is
           zero then  A is not referenced and  B need not be set before
           entry.
           Unchanged on exit.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is REAL array, dimension(NT) NT = N * (N + 1) / 2. On entry, the matrix A in RFP Format.RFP Format is described by TRANSR, UPLO and N as follows : If TRANSR = 'N' then RFP A is(0
                                                                                                                                                                                   : N, 0
                                                                                                                                                                                   : K - 1) when N is even;
K = N / 2. RFP A is(0
                    : N - 1, 0
                    : K) when N is odd; K=N/2. If
           TRANSR = 'T' then RFP is the transpose of RFP A as
           defined when TRANSR = 'N'. The contents of RFP A are defined
           by UPLO as follows: If UPLO = 'U' the RFP A contains the NT
           elements of upper packed A either in normal or
           transpose Format. If UPLO = 'L' the RFP A contains
           the NT elements of lower packed A either in normal or
           transpose Format. The LDA of RFP A is (N+1)/2 when
           TRANSR = 'T'. When TRANSR is 'N' the LDA is N+1 when N is
           even and is N when is odd.
           See the Note below for more details. Unchanged on exit.
</code></pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, DIMENSION (LDB,N)
           Before entry,  the leading  m by n part of the array  B must
           contain  the  right-hand  side  matrix  B,  and  on exit  is
           overwritten by the solution matrix  X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
           On entry, LDB specifies the first dimension of B as declared
           in  the  calling  (sub)  program.   LDB  must  be  at  least
           max( 1, m ).
           Unchanged on exit.
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
<dd> September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  We first consider Rectangular Full Packed (RFP) Format when N is
  even. We give an example where N = 6.
      AP is Upper             AP is Lower
   00 01 02 03 04 05       00
      11 12 13 14 15       10 11
         22 23 24 25       20 21 22
            33 34 35       30 31 32 33
               44 45       40 41 42 43 44
                  55       50 51 52 53 54 55
  Let TRANSR = 'N'. RFP holds AP as follows:
  For UPLO = 'U' the upper trapezoid A(0:5,0:2) consists of the last
  three columns of AP upper. The lower triangle A(4:6,0:2) consists of
  the transpose of the first three columns of AP upper.
  For UPLO = 'L' the lower trapezoid A(1:6,0:2) consists of the first
  three columns of AP lower. The upper triangle A(0:2,0:2) consists of
  the transpose of the last three columns of AP lower.
  This covers the case N even and TRANSR = 'N'.
         RFP A                   RFP A
        03 04 05                33 43 53
        13 14 15                00 44 54
        23 24 25                10 11 55
        33 34 35                20 21 22
        00 44 45                30 31 32
        01 11 55                40 41 42
        02 12 22                50 51 52
  Now let TRANSR = 'T'. RFP A in both UPLO cases is just the
  transpose of RFP A above. One therefore gets:
           RFP A                   RFP A
     03 13 23 33 00 01 02    33 00 10 20 30 40 50
     04 14 24 34 44 11 12    43 44 11 21 31 41 51
     05 15 25 35 45 55 22    53 54 55 22 32 42 52
  We then consider Rectangular Full Packed (RFP) Format when N is
  odd. We give an example where N = 5.
     AP is Upper                 AP is Lower
   00 01 02 03 04              00
      11 12 13 14              10 11
         22 23 24              20 21 22
            33 34              30 31 32 33
               44              40 41 42 43 44
  Let TRANSR = 'N'. RFP holds AP as follows:
  For UPLO = 'U' the upper trapezoid A(0:4,0:2) consists of the last
  three columns of AP upper. The lower triangle A(3:4,0:1) consists of
  the transpose of the first two columns of AP upper.
  For UPLO = 'L' the lower trapezoid A(0:4,0:2) consists of the first
  three columns of AP lower. The upper triangle A(0:1,1:2) consists of
  the transpose of the last two columns of AP lower.
  This covers the case N odd and TRANSR = 'N'.
         RFP A                   RFP A
        02 03 04                00 33 43
        12 13 14                10 11 44
        22 23 24                20 21 22
        00 33 34                30 31 32
        01 11 44                40 41 42
  Now let TRANSR = 'T'. RFP A in both UPLO cases is just the
  transpose of RFP A above. One therefore gets:
           RFP A                   RFP A
     02 12 22 00 01             00 10 20 30 40 50
     03 13 23 33 11             33 11 21 31 41 51
     04 14 24 34 44             43 44 22 32 42 52
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 277 of file stfsm.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
