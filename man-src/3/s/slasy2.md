---
title: "slasy2(3)"
name: "slasy2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasy2/"
description: "slasy2.f –"
---

<h2 class="name">NAME</h2>
<p> slasy2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slasy2</code> (LTRANL, LTRANR, ISGN, N1, N2, TL, LDTL, TR, LDTR, B, LDB, SCALE, X, LDX, XNORM, INFO)<br />
 <i></i><code>SLASY2</code> solves the Sylvester matrix equation where the matrices are of order 1 or 2.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasy2 (logicalLTRANL, logicalLTRANR, integerISGN, integerN1, integerN2, real, dimension( ldtl, * )TL, integerLDTL, real, dimension( ldtr, * )TR, integerLDTR, real, dimension( ldb, * )B, integerLDB, realSCALE, real, dimension( ldx, * )X, integerLDX, realXNORM, integerINFO)</h3>
<p> <code>SLASY2</code> solves the Sylvester matrix equation where the matrices are of order 1 or 2. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLASY2 solves for the N1 by N2 matrix X, 1 &lt;= N1,N2 &lt;= 2, in
        op(TL)*X + ISGN*X*op(TR) = SCALE*B,
 where TL is N1 by N1, TR is N2 by N2, B is N1 by N2, and ISGN = 1 or
 -1.  op(T) = T or T**T, where T**T denotes the transpose of T.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>LTRANL</i> </p>
<pre>
          LTRANL is LOGICAL
          On entry, LTRANL specifies the op(TL):
             = .FALSE., op(TL) = TL,
             = .TRUE., op(TL) = TL**T.
</pre>
<p> <i>LTRANR</i> </p>
<pre>
          LTRANR is LOGICAL
          On entry, LTRANR specifies the op(TR):
            = .FALSE., op(TR) = TR,
            = .TRUE., op(TR) = TR**T.
</pre>
<p> <i>ISGN</i> </p>
<pre>
          ISGN is INTEGER
          On entry, ISGN specifies the sign of the equation
          as described before. ISGN may only be 1 or -1.
</pre>
<p> <i>N1</i> </p>
<pre>
          N1 is INTEGER
          On entry, N1 specifies the order of matrix TL.
          N1 may only be 0, 1 or 2.
</pre>
<p> <i>N2</i> </p>
<pre>
          N2 is INTEGER
          On entry, N2 specifies the order of matrix TR.
          N2 may only be 0, 1 or 2.
</pre>
<p> <i>TL</i> </p>
<pre>
          TL is REAL array, dimension (LDTL,2)
          On entry, TL contains an N1 by N1 matrix.
</pre>
<p> <i>LDTL</i> </p>
<pre>
          LDTL is INTEGER
          The leading dimension of the matrix TL. LDTL &gt;= max(1,N1).
</pre>
<p> <i>TR</i> </p>
<pre>
          TR is REAL array, dimension (LDTR,2)
          On entry, TR contains an N2 by N2 matrix.
</pre>
<p> <i>LDTR</i> </p>
<pre>
          LDTR is INTEGER
          The leading dimension of the matrix TR. LDTR &gt;= max(1,N2).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,2)
          On entry, the N1 by N2 matrix B contains the right-hand
          side of the equation.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the matrix B. LDB &gt;= max(1,N1).
</pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is REAL
          On exit, SCALE contains the scale factor. SCALE is chosen
          less than or equal to 1 to prevent the solution overflowing.
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension (LDX,2)
          On exit, X contains the N1 by N2 solution.
</pre>
<p> <i>LDX</i> </p>
<pre>
          LDX is INTEGER
          The leading dimension of the matrix X. LDX &gt;= max(1,N1).
</pre>
<p> <i>XNORM</i> </p>
<pre>
          XNORM is REAL
          On exit, XNORM is the infinity-norm of the solution.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          On exit, INFO is set to
             0: successful exit.
             1: TL and TR have too close eigenvalues, so TL or
                TR is perturbed to get a nonsingular equation.
          NOTE: In the interests of speed, this routine does not
                check the inputs for errors.
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
<p> Definition at line 174 of file slasy2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
