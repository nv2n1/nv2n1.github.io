---
title: "dlasd6(3)"
name: "dlasd6"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasd6/"
description: "dlasd6.f –"
---

<h2 class="name">NAME</h2>
<p> dlasd6.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasd6</code> (ICOMPQ, NL, NR, SQRE, D, VF, VL, ALPHA, BETA, IDXQ, PERM, GIVPTR, GIVCOL, LDGCOL, GIVNUM, LDGNUM, POLES, DIFL, DIFR, Z, K, C, S, WORK, IWORK, INFO)<br />
 <i></i><code>DLASD6</code> computes the SVD of an updated upper bidiagonal matrix obtained by merging two smaller ones by appending a row. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasd6 (integerICOMPQ, integerNL, integerNR, integerSQRE, double precision, dimension( * )D, double precision, dimension( * )VF, double precision, dimension( * )VL, double precisionALPHA, double precisionBETA, integer, dimension( * )IDXQ, integer, dimension( * )PERM, integerGIVPTR, integer, dimension( ldgcol, * )GIVCOL, integerLDGCOL, double precision, dimension( ldgnum, * )GIVNUM, integerLDGNUM, double precision, dimension( ldgnum, * )POLES, double precision, dimension( * )DIFL, double precision, dimension( * )DIFR, double precision, dimension( * )Z, integerK, double precisionC, double precisionS, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DLASD6</code> computes the SVD of an updated upper bidiagonal matrix obtained by merging two smaller ones by appending a row. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DLASD6 computes the SVD of an updated upper bidiagonal matrix B
 obtained by merging two smaller ones by appending a row. This
 routine is used only for the problem which requires all singular
 values and optionally singular vector matrices in factored form.
 B is an N-by-M matrix with N = NL + NR + 1 and M = N + SQRE.
 A related subroutine, DLASD1, handles the case in which all singular
 values and singular vectors of the bidiagonal matrix are desired.
 DLASD6 computes the SVD as follows:
               ( D1(in)    0    0       0 )
   B = U(in) * (   Z1**T   a   Z2**T    b ) * VT(in)
               (   0       0   D2(in)   0 )
     = U(out) * ( D(out) 0) * VT(out)
 where Z **T = (Z1 * *T a Z2 * *T b) = u * *T VT * *T, and u is a vector of dimension M
                                                                   with ALPHA and BETA in the NL +
                                                               1 and
                                                           NL + 2 th entries and zeros
                                                                    elsewhere;
 and the entry b is empty if SQRE = 0. The singular values of B can be computed using D1, D2, the first components of all the right singular vectors of the lower block, and the last components of all the right singular vectors of the upper block.These components are stored and updated in VF and VL,
                             respectively, in DLASD6.Hence U and VT are not explicitly referenced.The singular values are stored in D.The algorithm consists of two stages : The first stage consists of deflating the size of the problem when there are multiple singular values or if there is a zero in the Z vector.For each such occurence the dimension of the secular equation problem is reduced by one.This stage is performed by the routine DLASD7.The second stage consists of calculating the updated singular values.This is done by finding the roots of the secular equation via the routine DLASD4(as called by DLASD8).This routine also updates VF and VL and computes the distances between the updated singular values and the old singular values.DLASD6 is called from DLASDA.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ICOMPQ</i> </p>
<pre>
          ICOMPQ is INTEGER
         Specifies whether singular vectors are to be computed in
         factored form:
         = 0: Compute singular values only.
         = 1: Compute singular vectors in factored form as well.
</pre>
<p> <i>NL</i> </p>
<pre>
          NL is INTEGER
         The row dimension of the upper block.  NL &gt;= 1.
</pre>
<p> <i>NR</i> </p>
<pre>
          NR is INTEGER
         The row dimension of the lower block.  NR &gt;= 1.
</pre>
<p> <i>SQRE</i> </p>
<pre>
          SQRE is INTEGER
         = 0: the lower block is an NR-by-NR square matrix.
         = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
         The bidiagonal matrix has row dimension N = NL + NR + 1,
         and column dimension M = N + SQRE.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension ( NL+NR+1 ).
         On entry D(1:NL,1:NL) contains the singular values of the
         upper block, and D(NL+2:N) contains the singular values
         of the lower block. On exit D(1:N) contains the singular
         values of the modified matrix.
</pre>
<p> <i>VF</i> </p>
<pre>
          VF is DOUBLE PRECISION array, dimension ( M )
         On entry, VF(1:NL+1) contains the first components of all
         right singular vectors of the upper block; and VF(NL+2:M)
         contains the first components of all right singular vectors
         of the lower block. On exit, VF contains the first components
         of all right singular vectors of the bidiagonal matrix.
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is DOUBLE PRECISION array, dimension ( M )
         On entry, VL(1:NL+1) contains the  last components of all
         right singular vectors of the upper block; and VL(NL+2:M)
         contains the last components of all right singular vectors of
         the lower block. On exit, VL contains the last components of
         all right singular vectors of the bidiagonal matrix.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is DOUBLE PRECISION
         Contains the diagonal element associated with the added row.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is DOUBLE PRECISION
         Contains the off-diagonal element associated with the added
         row.
</pre>
<p> <i>IDXQ</i> </p>
<pre>
          IDXQ is INTEGER array, dimension ( N )
         This contains the permutation which will reintegrate the
         subproblem just solved back into sorted order, i.e.
         D( IDXQ( I = 1, N ) ) will be in ascending order.
</pre>
<p> <i>PERM</i> </p>
<pre>
          PERM is INTEGER array, dimension ( N )
         The permutations (from deflation and sorting) to be applied
         to each block. Not referenced if ICOMPQ = 0.
</pre>
<p> <i>GIVPTR</i> </p>
<pre>
          GIVPTR is INTEGER
         The number of Givens rotations which took place in this
         subproblem. Not referenced if ICOMPQ = 0.
</pre>
<p> <i>GIVCOL</i> </p>
<pre>
          GIVCOL is INTEGER array, dimension ( LDGCOL, 2 )
         Each pair of numbers indicates a pair of columns to take place
         in a Givens rotation. Not referenced if ICOMPQ = 0.
</pre>
<p> <i>LDGCOL</i> </p>
<pre>
          LDGCOL is INTEGER
         leading dimension of GIVCOL, must be at least N.
</pre>
<p> <i>GIVNUM</i> </p>
<pre>
          GIVNUM is DOUBLE PRECISION array, dimension ( LDGNUM, 2 )
         Each number indicates the C or S value to be used in the
         corresponding Givens rotation. Not referenced if ICOMPQ = 0.
</pre>
<p> <i>LDGNUM</i> </p>
<pre>
          LDGNUM is INTEGER
         The leading dimension of GIVNUM and POLES, must be at least N.
</pre>
<p> <i>POLES</i> </p>
<pre>
          POLES is DOUBLE PRECISION array, dimension ( LDGNUM, 2 )
         On exit, POLES(1,*) is an array containing the new singular
         values obtained from solving the secular equation, and
         POLES(2,*) is an array containing the poles in the secular
         equation. Not referenced if ICOMPQ = 0.
</pre>
<p> <i>DIFL</i> </p>
<pre>
          DIFL is DOUBLE PRECISION array, dimension ( N )
         On exit, DIFL(I) is the distance between I-th updated
         (undeflated) singular value and the I-th (undeflated) old
         singular value.
</pre>
<p> <i>DIFR</i> </p>
<pre><code>
DIFR is DOUBLE PRECISION array,
    dimension(LDGNUM, 2) if ICOMPQ = 1 and
                                     dimension(N) if ICOMPQ = 0. On exit,
                            DIFR(I, 1) is the distance between I - th updated(undeflated) singular value and the I+1-th (undeflated) old
         singular value.
         If ICOMPQ = 1, DIFR(1:K,2) is an array containing the
         normalizing factors for the right singular vector matrix.
         See DLASD8 for details on DIFL and DIFR.
</code></pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension ( M )
         The first elements of this array contain the components
         of the deflation-adjusted updating row vector.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
         Contains the dimension of the non-deflated matrix,
         This is the order of the related secular equation. 1 &lt;= K &lt;=N.
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION
         C contains garbage if SQRE =0 and the C-value of a Givens
         rotation related to the right null space if SQRE = 1.
</pre>
<p> <i>S</i> </p>
<pre>
          S is DOUBLE PRECISION
         S contains garbage if SQRE =0 and the S-value of a Givens
         rotation related to the right null space if SQRE = 1.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension ( 4 * M )
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension ( 3 * N )
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  if INFO = 1, a singular value did not converge
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 312 of file dlasd6.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
