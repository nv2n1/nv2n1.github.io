---
title: "dlaeda(3)"
name: "dlaeda"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaeda/"
description: "dlaeda.f –"
---

<h2 class="name">NAME</h2>
<p> dlaeda.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaeda</code> (N, TLVLS, CURLVL, CURPBM, PRMPTR, PERM, GIVPTR, GIVCOL, GIVNUM, Q, QPTR, Z, ZTEMP, INFO)<br />
 <i></i><code>DLAEDA</code> used by sstedc. Computes the Z vector determining the rank-one modification of the diagonal matrix. Used when the original matrix is dense.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaeda (integerN, integerTLVLS, integerCURLVL, integerCURPBM, integer, dimension( * )PRMPTR, integer, dimension( * )PERM, integer, dimension( * )GIVPTR, integer, dimension( 2, * )GIVCOL, double precision, dimension( 2, * )GIVNUM, double precision, dimension( * )Q, integer, dimension( * )QPTR, double precision, dimension( * )Z, double precision, dimension( * )ZTEMP, integerINFO)</h3>
<p> <code>DLAEDA</code> used by sstedc. Computes the Z vector determining the rank-one modification of the diagonal matrix. Used when the original matrix is dense. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAEDA computes the Z vector corresponding to the merge step in the
 CURLVLth step of the merge process with TLVLS steps for the CURPBMth
 problem.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
         The dimension of the symmetric tridiagonal matrix.  N &gt;= 0.
</pre>
<p> <i>TLVLS</i> </p>
<pre>
          TLVLS is INTEGER
         The total number of merging levels in the overall divide and
         conquer tree.
</pre>
<p> <i>CURLVL</i> </p>
<pre>
          CURLVL is INTEGER
         The current level in the overall merge routine,
         0 &lt;= curlvl &lt;= tlvls.
</pre>
<p> <i>CURPBM</i> </p>
<pre>
          CURPBM is INTEGER
         The current problem in the current level in the overall
         merge routine (counting from upper left to lower right).
</pre>
<p> <i>PRMPTR</i> </p>
<pre>
          PRMPTR is INTEGER array, dimension (N lg N)
         Contains a list of pointers which indicate where in PERM a
         level's permutation is stored.  PRMPTR(i+1) - PRMPTR(i)
         indicates the size of the permutation and incidentally the
         size of the full, non-deflated problem.
</pre>
<p> <i>PERM</i> </p>
<pre>
          PERM is INTEGER array, dimension (N lg N)
         Contains the permutations (from deflation and sorting) to be
         applied to each eigenblock.
</pre>
<p> <i>GIVPTR</i> </p>
<pre>
          GIVPTR is INTEGER array, dimension (N lg N)
         Contains a list of pointers which indicate where in GIVCOL a
         level's Givens rotations are stored.  GIVPTR(i+1) - GIVPTR(i)
         indicates the number of Givens rotations.
</pre>
<p> <i>GIVCOL</i> </p>
<pre>
          GIVCOL is INTEGER array, dimension (2, N lg N)
         Each pair of numbers indicates a pair of columns to take place
         in a Givens rotation.
</pre>
<p> <i>GIVNUM</i> </p>
<pre>
          GIVNUM is DOUBLE PRECISION array, dimension (2, N lg N)
         Each number indicates the S value to be used in the
         corresponding Givens rotation.
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is DOUBLE PRECISION array, dimension (N**2)
         Contains the square eigenblocks from previous levels, the
         starting positions for blocks are given by QPTR.
</pre>
<p> <i>QPTR</i> </p>
<pre>
          QPTR is INTEGER array, dimension (N+2)
         Contains a list of pointers which indicate where in Q an
         eigenblock is stored.  SQRT( QPTR(i+1) - QPTR(i) ) indicates
         the size of the block.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension (N)
         On output this vector contains the updating vector (the last
         row of the first sub-eigenvector matrix and the first row of
         the second sub-eigenvector matrix).
</pre>
<p> <i>ZTEMP</i> </p>
<pre>
          ZTEMP is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
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
<dd> Jeff Rutter, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 166 of file dlaeda.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
