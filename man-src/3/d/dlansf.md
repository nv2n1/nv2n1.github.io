---
title: "dlansf(3)"
name: "dlansf"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlansf/"
description: "dlansf.f –"
---

<h2 class="name">NAME</h2>
<p> dlansf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dlansf</code> (NORM, TRANSR, UPLO, N, A, WORK)<br />
 <i></i><code>DLANSF</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a symmetric matrix in RFP format.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dlansf (characterNORM, characterTRANSR, characterUPLO, integerN, double precision, dimension( 0: * )A, double precision, dimension( 0: * )WORK)</h3>
<p> <code>DLANSF</code> returns the value of the 1-norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a symmetric matrix in RFP format. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLANSF returns the value of the one norm, or the Frobenius norm, or
 the infinity norm, or the element of largest absolute value of a
 real symmetric matrix A in RFP format.
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> DLANSF </p>
<pre>
    DLANSF = ( max(abs(A(i,j))), NORM = 'M' or 'm'
             (
             ( norm1(A),         NORM = '1', 'O' or 'o'
             (
             ( normI(A),         NORM = 'I' or 'i'
             (
             ( normF(A),         NORM = 'F', 'f', 'E' or 'e'
 where  norm1  denotes the  one norm of a matrix (maximum column sum),
 normI  denotes the  infinity norm  of a matrix  (maximum row sum) and
 normF  denotes the  Frobenius norm of a matrix (square root of sum of
 squares).  Note that  max(abs(A(i,j)))  is not a  matrix norm.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>NORM</i> </p>
<pre>
          NORM is CHARACTER*1
          Specifies the value to be returned in DLANSF as described
          above.
</pre>
<p> <i>TRANSR</i> </p>
<pre>
          TRANSR is CHARACTER*1
          Specifies whether the RFP format of A is normal or
          transposed format.
          = 'N':  RFP format is Normal;
          = 'T':  RFP format is Transpose.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
           On entry, UPLO specifies whether the RFP matrix A came from
           an upper or lower triangular matrix as follows:
           = 'U': RFP A came from an upper triangular matrix;
           = 'L': RFP A came from a lower triangular matrix.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A. N &gt;= 0. When N = 0, DLANSF is
          set to zero.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is DOUBLE PRECISION array, dimension(N *(N + 1) / 2);
          On entry, the upper (if UPLO = 'U') or lower (if UPLO = 'L')
          part of the symmetric matrix A stored in RFP format. See the
          "Notes" below for more details.
          Unchanged on exit.
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)),
          where LWORK &gt;= N when NORM = 'I' or '1' or 'O'; otherwise,
          WORK is not referenced.
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
<p> Definition at line 210 of file dlansf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
