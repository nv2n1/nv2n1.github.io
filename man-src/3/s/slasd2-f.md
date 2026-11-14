---
title: "slasd2-f(3)"
name: "slasd2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasd2-f/"
description: "slasd2.f –"
---

<p>slasd2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasd2</code> (NL, NR, SQRE, K, D, Z, ALPHA, BETA, U, LDU, VT, LDVT, DSIGMA, U2, LDU2, VT2, LDVT2, IDXP, IDX, IDXC, IDXQ, COLTYP, INFO)<br />
 <i></i><code>SLASD2</code> merges the two sets of singular values together into a single sorted set. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasd2 (integerNL, integerNR, integerSQRE, integerK, real, dimension( * )D, real, dimension( * )Z, realALPHA, realBETA, real, dimension( ldu, * )U, integerLDU, real, dimension( ldvt, * )VT, integerLDVT, real, dimension( * )DSIGMA, real, dimension( ldu2, * )U2, integerLDU2, real, dimension( ldvt2, * )VT2, integerLDVT2, integer, dimension( * )IDXP, integer, dimension( * )IDX, integer, dimension( * )IDXC, integer, dimension( * )IDXQ, integer, dimension( * )COLTYP, integerINFO)</h3>
<p><code>SLASD2</code> merges the two sets of singular values together into a single sorted set. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASD2 merges the two sets of singular values together into a single
 sorted set. Then it tries to deflate the size of the problem.
 There are two ways in which deflation can occur: when two or more
 singular values are close together or if there is a tiny entry in the
 Z vector. For each such occurrence the order of the related secular
 equation problem is reduced by one.
 SLASD2 is called from SLASD1.</pre>
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
 Contains the dimension of the non-deflated matrix,
 This is the order of the related secular equation. 1 &lt;= K &lt;=N.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry D contains the singular values of the two submatrices
 to be combined. On exit D contains the trailing (N-K) updated
 singular values (those which were deflated) sorted into
 increasing order.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (N)
 On exit Z contains the updating row vector in the secular
 equation.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is REAL
 Contains the diagonal element associated with the added row.</pre>
<p><i>BETA</i> </p>
<pre> BETA is REAL
 Contains the off-diagonal element associated with the added
 row.</pre>
<p><i>U</i> </p>
<pre> U is REAL array, dimension (LDU,N)
 On entry U contains the left singular vectors of two
 submatrices in the two square blocks with corners at (1,1),
 (NL, NL), and (NL+2, NL+2), (N,N).
 On exit U contains the trailing (N-K) updated left singular
 vectors (those which were deflated) in its last N-K columns.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= N.</pre>
<p><i>VT</i> </p>
<pre> VT is REAL array, dimension (LDVT,M)
 On entry VT**T contains the right singular vectors of two
 submatrices in the two square blocks with corners at (1,1),
 (NL+1, NL+1), and (NL+2, NL+2), (M,M).
 On exit VT**T contains the trailing (N-K) updated right singular
 vectors (those which were deflated) in its last N-K columns.
 In case SQRE =1, the last row of VT spans the right null
 space.</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 The leading dimension of the array VT. LDVT &gt;= M.</pre>
<p><i>DSIGMA</i> </p>
<pre> DSIGMA is REAL array, dimension (N)
 Contains a copy of the diagonal elements (K-1 singular values
 and one zero) in the secular equation.</pre>
<p><i>U2</i> </p>
<pre> U2 is REAL array, dimension (LDU2,N)
 Contains a copy of the first K-1 left singular vectors which
 will be used by SLASD3 in a matrix multiply (SGEMM) to solve
 for the new left singular vectors. U2 is arranged into four
 blocks. The first block contains a column with 1 at NL+1 and
 zero everywhere else; the second block contains non-zero
 entries only at and above NL; the third contains non-zero
 entries only below NL+1; and the fourth is dense.</pre>
<p><i>LDU2</i> </p>
<pre> LDU2 is INTEGER
 The leading dimension of the array U2. LDU2 &gt;= N.</pre>
<p><i>VT2</i> </p>
<pre> VT2 is REAL array, dimension (LDVT2,N)
 VT2**T contains a copy of the first K right singular vectors
 which will be used by SLASD3 in a matrix multiply (SGEMM) to
 solve for the new right singular vectors. VT2 is arranged into
 three blocks. The first block contains a row that corresponds
 to the special 0 diagonal element in SIGMA; the second block
 contains non-zeros only at and before NL +1; the third block
 contains non-zeros only at and after NL +2.</pre>
<p><i>LDVT2</i> </p>
<pre> LDVT2 is INTEGER
 The leading dimension of the array VT2. LDVT2 &gt;= M.</pre>
<p><i>IDXP</i> </p>
<pre> IDXP is INTEGER array, dimension (N)
 This will contain the permutation used to place deflated
 values of D at the end of the array. On output IDXP(2:K)
 points to the nondeflated D-values and IDXP(K+1:N)
 points to the deflated singular values.</pre>
<p><i>IDX</i> </p>
<pre> IDX is INTEGER array, dimension (N)
 This will contain the permutation used to sort the contents of
 D into ascending order.</pre>
<p><i>IDXC</i> </p>
<pre> IDXC is INTEGER array, dimension (N)
 This will contain the permutation used to arrange the columns
 of the deflated U matrix into three groups: the first group
 contains non-zero entries only at and above NL, the second
 contains non-zero entries only below NL+2, and the third is
 dense.</pre>
<p><i>IDXQ</i> </p>
<pre> IDXQ is INTEGER array, dimension (N)
 This contains the permutation which separately sorts the two
 sub-problems in D into ascending order. Note that entries in
 the first hlaf of this permutation must first be moved one
 position backward; and entries in the second half
 must first have NL+1 added to their values.</pre>
<p><i>COLTYP</i> </p>
<pre> COLTYP is INTEGER array, dimension (N)
 As workspace, this will contain a label which will indicate
 which of the following types a column in the U2 matrix or a
 row in the VT2 matrix is:
 1 : non-zero in the upper half only
 2 : non-zero in the lower half only
 3 : dense
 4 : deflated
 On exit, it is an array of dimension 4, with COLTYP(I) being
 the dimension of the I-th type columns.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
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
<p> Definition at line 268 of file slasd2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
