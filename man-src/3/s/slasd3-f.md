---
title: "slasd3-f(3)"
name: "slasd3-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasd3-f/"
description: "slasd3.f –"
---

<p>slasd3.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasd3</code> (NL, NR, SQRE, K, D, Q, LDQ, DSIGMA, U, LDU, U2, LDU2, VT, LDVT, VT2, LDVT2, IDXC, CTOT, Z, INFO)<br />
 <i></i><code>SLASD3</code> finds all square roots of the roots of the secular equation, as defined by the values in D and Z, and then updates the singular vectors by matrix multiplication. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasd3 (integerNL, integerNR, integerSQRE, integerK, real, dimension( * )D, real, dimension( ldq, * )Q, integerLDQ, real, dimension( * )DSIGMA, real, dimension( ldu, * )U, integerLDU, real, dimension( ldu2, * )U2, integerLDU2, real, dimension( ldvt, * )VT, integerLDVT, real, dimension( ldvt2, * )VT2, integerLDVT2, integer, dimension( * )IDXC, integer, dimension( * )CTOT, real, dimension( * )Z, integerINFO)</h3>
<p><code>SLASD3</code> finds all square roots of the roots of the secular equation, as defined by the values in D and Z, and then updates the singular vectors by matrix multiplication. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASD3 finds all the square roots of the roots of the secular
 equation, as defined by the values in D and Z. It makes the
 appropriate calls to SLASD4 and then updates the singular
 vectors by matrix multiplication.
 This code makes very mild assumptions about floating point
 arithmetic. It will work on machines with a guard digit in
 add/subtract, or on those binary machines without guard digits
 which subtract like the Cray XMP, Cray YMP, Cray C 90, or Cray 2.
 It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.
 SLASD3 is called from SLASD1.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>NL</i> </p>
<pre> NL is INTEGER
 The row dimension of the upper block. NL &gt;= 1.</pre>
<p><i>NR</i> </p>
<pre> NR is INTEGER
 The row dimension of the lower block. NR &gt;= 1.</pre>
<p><i>SQRE</i> </p>
<pre> SQRE is INTEGER
 = 0: the lower block is an NR-by-NR square matrix.
 = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
 The bidiagonal matrix has N = NL + NR + 1 rows and
 M = N + SQRE &gt;= N columns.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 The size of the secular equation, 1 =&lt; K = &lt; N.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension(K)
 On exit the square roots of the roots of the secular equation,
 in ascending order.</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array,
 dimension at least (LDQ,K).</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= K.</pre>
<p><i>DSIGMA</i> </p>
<pre> DSIGMA is REAL array, dimension(K)
 The first K elements of this array contain the old roots
 of the deflated updating problem. These are the poles
 of the secular equation.</pre>
<p><i>U</i> </p>
<pre> U is REAL array, dimension (LDU, N)
 The last N - K columns of this matrix contain the deflated
 left singular vectors.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= N.</pre>
<p><i>U2</i> </p>
<pre> U2 is REAL array, dimension (LDU2, N)
 The first K columns of this matrix contain the non-deflated
 left singular vectors for the split problem.</pre>
<p><i>LDU2</i> </p>
<pre> LDU2 is INTEGER
 The leading dimension of the array U2. LDU2 &gt;= N.</pre>
<p><i>VT</i> </p>
<pre> VT is REAL array, dimension (LDVT, M)
 The last M - K columns of VT**T contain the deflated
 right singular vectors.</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 The leading dimension of the array VT. LDVT &gt;= N.</pre>
<p><i>VT2</i> </p>
<pre> VT2 is REAL array, dimension (LDVT2, N)
 The first K columns of VT2**T contain the non-deflated
 right singular vectors for the split problem.</pre>
<p><i>LDVT2</i> </p>
<pre> LDVT2 is INTEGER
 The leading dimension of the array VT2. LDVT2 &gt;= N.</pre>
<p><i>IDXC</i> </p>
<pre> IDXC is INTEGER array, dimension (N)
 The permutation used to arrange the columns of U (and rows of
 VT) into three groups: the first group contains non-zero
 entries only at and above (or before) NL +1; the second
 contains non-zero entries only at and below (or after) NL+2;
 and the third is dense. The first column of U and the row of
 VT are treated separately, however.
 The rows of the singular vectors found by SLASD4
 must be likewise permuted before the matrix multiplies can
 take place.</pre>
<p><i>CTOT</i> </p>
<pre> CTOT is INTEGER array, dimension (4)
 A count of the total number of the various types of columns
 in U (or rows in VT), as described in IDXC. The fourth column
 type is any column which has been deflated.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (K)
 The first K elements of this array contain the components
 of the deflation-adjusted updating row vector.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = 1, a singular value did not converge</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 224 of file slasd3.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
