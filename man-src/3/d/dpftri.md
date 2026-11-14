---
title: "dpftri(3)"
name: "dpftri"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpftri/"
description: "dpftri.f –"
---

<h2 class="name">NAME</h2>
<p> dpftri.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dpftri</code> (TRANSR, UPLO, N, A, INFO)<br />
 <i></i><code>DPFTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dpftri (characterTRANSR, characterUPLO, integerN, double precision, dimension( 0: * )A, integerINFO)</h3>
<p> <code>DPFTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DPFTRI computes the inverse of a (real) symmetric positive definite
 matrix A using the Cholesky factorization A = U**T*U or A = L*L**T
 computed by DPFTRF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANSR</i> </p>
<pre>
          TRANSR is CHARACTER*1
          = 'N':  The Normal TRANSR of RFP A is stored;
          = 'T':  The Transpose TRANSR of RFP A is stored.
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
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is DOUBLE PRECISION array, dimension(N *(N + 1) / 2) On entry, the symmetric matrix A in RFP format.RFP format is described by TRANSR, UPLO, and N as follows : If TRANSR = 'N' then RFP A is(0
                                                                                                                                                                                                : N, 0
                                                                                                                                                                                                : k - 1) when N is even;
k = N / 2. RFP A is(0
                    : N - 1, 0
                    : k) when N is odd; k=N/2. IF TRANSR = 'T' then RFP is
          the transpose of RFP A as defined when
          TRANSR = 'N'. The contents of RFP A are defined by UPLO as
          follows: If UPLO = 'U' the RFP A contains the nt elements of
          upper packed A. If UPLO = 'L' the RFP A contains the elements
          of lower packed A. The LDA of RFP A is (N+1)/2 when TRANSR =
          'T'. When TRANSR is 'N' the LDA is N+1 when N is even and N
          is odd. See the Note below for more details.
          On exit, the symmetric inverse of the original matrix, in the
          same storage format.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the (i,i) element of the factor U or L is
                zero, and the inverse could not be computed.
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
<p> Definition at line 192 of file dpftri.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
