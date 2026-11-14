---
title: "slasd1(3)"
name: "slasd1"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasd1/"
description: "slasd1.f –"
---

<h2 class="name">NAME</h2>
<p> slasd1.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slasd1</code> (NL, NR, SQRE, D, ALPHA, BETA, U, LDU, VT, LDVT, IDXQ, IWORK, WORK, INFO)<br />
 <i></i><code>SLASD1</code> computes the SVD of an upper bidiagonal matrix B of the specified size. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasd1 (integerNL, integerNR, integerSQRE, real, dimension( * )D, realALPHA, realBETA, real, dimension( ldu, * )U, integerLDU, real, dimension( ldvt, * )VT, integerLDVT, integer, dimension( * )IDXQ, integer, dimension( * )IWORK, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SLASD1</code> computes the SVD of an upper bidiagonal matrix B of the specified size. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
SLASD1 computes the SVD of an upper bidiagonal N - by - M matrix B,
    where N = NL + NR + 1 and M = N + SQRE.SLASD1 is called from SLASD0.A related subroutine SLASD7 handles the case in which the singular
                                      values(and the singular vectors in factored form) are desired.SLASD1 computes the SVD as follows : (D1(in) 0 0 0)
                                                                                                                                             B = U(in) * (Z1 * *T a Z2 * *T b) * VT(in)(0 0 D2(in) 0) = U(out) * (D(out) 0) * VT(out)
where Z **T = (Z1 * *T a Z2 * *T b) = u * *T VT * *T, and u is a vector of dimension M
                                                                  with ALPHA and BETA in the NL +
                                                              1 and
                                                          NL + 2 th entries and zeros
                                                                   elsewhere; and the entry b is empty if SQRE = 0.
 The left singular vectors of the original matrix are stored in U, and
 the transpose of the right singular vectors are stored in VT, and the
 singular values are in D.  The algorithm consists of three stages:
    The first stage consists of deflating the size of the problem
    when there are multiple singular values or when there are zeros in
    the Z vector.  For each such occurence the dimension of the
    secular equation problem is reduced by one.  This stage is
    performed by the routine SLASD2.
    The second stage consists of calculating the updated
    singular values. This is done by finding the square roots of the
    roots of the secular equation via the routine SLASD4 (as called
    by SLASD3). This routine also calculates the singular vectors of
    the current problem.
    The final stage consists of computing the updated singular vectors
    directly using the updated singular values.  The singular vectors
    for the current problem are multiplied with the singular vectors
    from the overall problem.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>NL</i> </p>
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
          D is REAL array, dimension (NL+NR+1).
         N = NL+NR+1
         On entry D(1:NL,1:NL) contains the singular values of the
         upper block; and D(NL+2:N) contains the singular values of
         the lower block. On exit D(1:N) contains the singular values
         of the modified matrix.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is REAL
         Contains the diagonal element associated with the added row.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is REAL
         Contains the off-diagonal element associated with the added
         row.
</pre>
<p> <i>U</i> </p>
<pre>
          U is REAL array, dimension (LDU,N)
         On entry U(1:NL, 1:NL) contains the left singular vectors of
         the upper block; U(NL+2:N, NL+2:N) contains the left singular
         vectors of the lower block. On exit U contains the left
         singular vectors of the bidiagonal matrix.
</pre>
<p> <i>LDU</i> </p>
<pre>
          LDU is INTEGER
         The leading dimension of the array U.  LDU &gt;= max( 1, N ).
</pre>
<p> <i>VT</i> </p>
<pre>
          VT is REAL array, dimension (LDVT,M)
         where M = N + SQRE.
         On entry VT(1:NL+1, 1:NL+1)**T contains the right singular
         vectors of the upper block; VT(NL+2:M, NL+2:M)**T contains
         the right singular vectors of the lower block. On exit
         VT**T contains the right singular vectors of the
         bidiagonal matrix.
</pre>
<p> <i>LDVT</i> </p>
<pre>
          LDVT is INTEGER
         The leading dimension of the array VT.  LDVT &gt;= max( 1, M ).
</pre>
<p> <i>IDXQ</i> </p>
<pre>
          IDXQ is INTEGER array, dimension (N)
         This contains the permutation which will reintegrate the
         subproblem just solved back into sorted order, i.e.
         D( IDXQ( I = 1, N ) ) will be in ascending order.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (4*N)
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (3*M**2+2*M)
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
<p> Definition at line 204 of file slasd1.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
