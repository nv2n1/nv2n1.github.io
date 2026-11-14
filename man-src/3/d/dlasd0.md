---
title: "dlasd0(3)"
name: "dlasd0"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasd0/"
description: "dlasd0.f –"
---

<h2 class="name">NAME</h2>
<p> dlasd0.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasd0</code> (N, SQRE, D, E, U, LDU, VT, LDVT, SMLSIZ, IWORK, WORK, INFO)<br />
 <i></i><code>DLASD0</code> computes the singular values of a real upper bidiagonal n-by-m matrix B with diagonal d and off-diagonal e. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasd0 (integerN, integerSQRE, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldu, * )U, integerLDU, double precision, dimension( ldvt, * )VT, integerLDVT, integerSMLSIZ, integer, dimension( * )IWORK, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DLASD0</code> computes the singular values of a real upper bidiagonal n-by-m matrix B with diagonal d and off-diagonal e. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 Using a divide and conquer approach, DLASD0 computes the singular
 value decomposition (SVD) of a real upper bidiagonal N-by-M
 matrix B with diagonal D and offdiagonal E, where M = N + SQRE.
 The algorithm computes orthogonal matrices U and VT such that
 B = U * S * VT. The singular values S are overwritten on D.
 A related subroutine, DLASDA, computes only the singular values,
 and optionally, the singular vectors in compact form.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
         On entry, the row dimension of the upper bidiagonal matrix.
         This is also the dimension of the main diagonal array D.
</pre>
<p> <i>SQRE</i> </p>
<pre>
          SQRE is INTEGER
         Specifies the column dimension of the bidiagonal matrix.
         = 0: The bidiagonal matrix has column dimension M = N;
         = 1: The bidiagonal matrix has column dimension M = N+1;
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
         On entry D contains the main diagonal of the bidiagonal
         matrix.
         On exit D, if INFO = 0, contains its singular values.
</pre>
<p> <i>E</i> </p>
<pre>
          E is DOUBLE PRECISION array, dimension (M-1)
         Contains the subdiagonal entries of the bidiagonal matrix.
         On exit, E has been destroyed.
</pre>
<p> <i>U</i> </p>
<pre>
          U is DOUBLE PRECISION array, dimension at least (LDQ, N)
         On exit, U contains the left singular vectors.
</pre>
<p> <i>LDU</i> </p>
<pre>
          LDU is INTEGER
         On entry, leading dimension of U.
</pre>
<p> <i>VT</i> </p>
<pre>
          VT is DOUBLE PRECISION array, dimension at least (LDVT, M)
         On exit, VT**T contains the right singular vectors.
</pre>
<p> <i>LDVT</i> </p>
<pre>
          LDVT is INTEGER
         On entry, leading dimension of VT.
</pre>
<p> <i>SMLSIZ</i> </p>
<pre>
          SMLSIZ is INTEGER
         On entry, maximum size of the subproblems at the
         bottom of the computation tree.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER work array.
         Dimension must be at least (8 * N)
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION work array.
         Dimension must be at least (3 * M**2 + 2 * M)
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
<p> Definition at line 152 of file dlasd0.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
