---
title: "slasd7-f(3)"
name: "slasd7-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasd7-f/"
description: "slasd7.f –"
---

<p>slasd7.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasd7</code> (ICOMPQ, NL, NR, SQRE, K, D, Z, ZW, VF, VFW, VL, VLW, ALPHA, BETA, DSIGMA, IDX, IDXP, IDXQ, PERM, GIVPTR, GIVCOL, LDGCOL, GIVNUM, LDGNUM, C, S, INFO)<br />
 <i></i><code>SLASD7</code> merges the two sets of singular values together into a single sorted set. Then it tries to deflate the size of the problem. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasd7 (integerICOMPQ, integerNL, integerNR, integerSQRE, integerK, real, dimension( * )D, real, dimension( * )Z, real, dimension( * )ZW, real, dimension( * )VF, real, dimension( * )VFW, real, dimension( * )VL, real, dimension( * )VLW, realALPHA, realBETA, real, dimension( * )DSIGMA, integer, dimension( * )IDX, integer, dimension( * )IDXP, integer, dimension( * )IDXQ, integer, dimension( * )PERM, integerGIVPTR, integer, dimension( ldgcol, * )GIVCOL, integerLDGCOL, real, dimension( ldgnum, * )GIVNUM, integerLDGNUM, realC, realS, integerINFO)</h3>
<p><code>SLASD7</code> merges the two sets of singular values together into a single sorted set. Then it tries to deflate the size of the problem. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASD7 merges the two sets of singular values together into a single
 sorted set. Then it tries to deflate the size of the problem. There
 are two ways in which deflation can occur: when two or more singular
 values are close together or if there is a tiny entry in the Z
 vector. For each such occurrence the order of the related
 secular equation problem is reduced by one.
 SLASD7 is called from SLASD6.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>ICOMPQ</i> </p>
<pre> ICOMPQ is INTEGER
 Specifies whether singular vectors are to be computed
 in compact form, as follows:
 = 0: Compute singular values only.
 = 1: Compute singular vectors of upper
 bidiagonal matrix in compact form.</pre>
<p><i>NL</i> </p>
<pre> NL is INTEGER
 The row dimension of the upper block. NL &gt;= 1.</pre>
<p><i>NR</i> </p>
<pre> NR is INTEGER
 The row dimension of the lower block. NR &gt;= 1.</pre>
<p><i>SQRE</i> </p>
<pre> SQRE is INTEGER
 = 0: the lower block is an NR-by-NR square matrix.
 = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
 The bidiagonal matrix has
 N = NL + NR + 1 rows and
 M = N + SQRE &gt;= N columns.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 Contains the dimension of the non-deflated matrix, this is
 the order of the related secular equation. 1 &lt;= K &lt;=N.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension ( N )
 On entry D contains the singular values of the two submatrices
 to be combined. On exit D contains the trailing (N-K) updated
 singular values (those which were deflated) sorted into
 increasing order.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension ( M )
 On exit Z contains the updating row vector in the secular
 equation.</pre>
<p><i>ZW</i> </p>
<pre> ZW is REAL array, dimension ( M )
 Workspace for Z.</pre>
<p><i>VF</i> </p>
<pre> VF is REAL array, dimension ( M )
 On entry, VF(1:NL+1) contains the first components of all
 right singular vectors of the upper block; and VF(NL+2:M)
 contains the first components of all right singular vectors
 of the lower block. On exit, VF contains the first components
 of all right singular vectors of the bidiagonal matrix.</pre>
<p><i>VFW</i> </p>
<pre> VFW is REAL array, dimension ( M )
 Workspace for VF.</pre>
<p><i>VL</i> </p>
<pre> VL is REAL array, dimension ( M )
 On entry, VL(1:NL+1) contains the last components of all
 right singular vectors of the upper block; and VL(NL+2:M)
 contains the last components of all right singular vectors
 of the lower block. On exit, VL contains the last components
 of all right singular vectors of the bidiagonal matrix.</pre>
<p><i>VLW</i> </p>
<pre> VLW is REAL array, dimension ( M )
 Workspace for VL.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is REAL
 Contains the diagonal element associated with the added row.</pre>
<p><i>BETA</i> </p>
<pre> BETA is REAL
 Contains the off-diagonal element associated with the added
 row.</pre>
<p><i>DSIGMA</i> </p>
<pre> DSIGMA is REAL array, dimension ( N )
 Contains a copy of the diagonal elements (K-1 singular values
 and one zero) in the secular equation.</pre>
<p><i>IDX</i> </p>
<pre> IDX is INTEGER array, dimension ( N )
 This will contain the permutation used to sort the contents of
 D into ascending order.</pre>
<p><i>IDXP</i> </p>
<pre> IDXP is INTEGER array, dimension ( N )
 This will contain the permutation used to place deflated
 values of D at the end of the array. On output IDXP(2:K)
 points to the nondeflated D-values and IDXP(K+1:N)
 points to the deflated singular values.</pre>
<p><i>IDXQ</i> </p>
<pre> IDXQ is INTEGER array, dimension ( N )
 This contains the permutation which separately sorts the two
 sub-problems in D into ascending order. Note that entries in
 the first half of this permutation must first be moved one
 position backward; and entries in the second half
 must first have NL+1 added to their values.</pre>
<p><i>PERM</i> </p>
<pre> PERM is INTEGER array, dimension ( N )
 The permutations (from deflation and sorting) to be applied
 to each singular block. Not referenced if ICOMPQ = 0.</pre>
<p><i>GIVPTR</i> </p>
<pre> GIVPTR is INTEGER
 The number of Givens rotations which took place in this
 subproblem. Not referenced if ICOMPQ = 0.</pre>
<p><i>GIVCOL</i> </p>
<pre> GIVCOL is INTEGER array, dimension ( LDGCOL, 2 )
 Each pair of numbers indicates a pair of columns to take place
 in a Givens rotation. Not referenced if ICOMPQ = 0.</pre>
<p><i>LDGCOL</i> </p>
<pre> LDGCOL is INTEGER
 The leading dimension of GIVCOL, must be at least N.</pre>
<p><i>GIVNUM</i> </p>
<pre> GIVNUM is REAL array, dimension ( LDGNUM, 2 )
 Each number indicates the C or S value to be used in the
 corresponding Givens rotation. Not referenced if ICOMPQ = 0.</pre>
<p><i>LDGNUM</i> </p>
<pre> LDGNUM is INTEGER
 The leading dimension of GIVNUM, must be at least N.</pre>
<p><i>C</i> </p>
<pre> C is REAL
 C contains garbage if SQRE =0 and the C-value of a Givens
 rotation related to the right null space if SQRE = 1.</pre>
<p><i>S</i> </p>
<pre> S is REAL
 S contains garbage if SQRE =0 and the S-value of a Givens
 rotation related to the right null space if SQRE = 1.</pre>
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
<p> Definition at line 278 of file slasd7.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
