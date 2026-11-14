---
title: "dlatdf(3)"
name: "dlatdf"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlatdf/"
description: "dlatdf.f –"
---

<h2 class="name">NAME</h2>
<p> dlatdf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlatdf</code> (IJOB, N, Z, LDZ, RHS, RDSUM, RDSCAL, IPIV, JPIV)<br />
 <i></i><code>DLATDF</code> uses the LU factorization of the n-by-n matrix computed by sgetc2 and computes a contribution to the reciprocal Dif-estimate.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlatdf (integerIJOB, integerN, double precision, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )RHS, double precisionRDSUM, double precisionRDSCAL, integer, dimension( * )IPIV, integer, dimension( * )JPIV)</h3>
<p> <code>DLATDF</code> uses the LU factorization of the n-by-n matrix computed by sgetc2 and computes a contribution to the reciprocal Dif-estimate. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLATDF uses the LU factorization of the n-by-n matrix Z computed by
 DGETC2 and computes a contribution to the reciprocal Dif-estimate
 by solving Z * x = b for x, and choosing the r.h.s. b such that
 the norm of x is as large as possible. On entry RHS = b holds the
 contribution from earlier solved sub-systems, and on return RHS = x.
 The factorization of Z returned by DGETC2 has the form Z = P*L*U*Q,
 where P and Q are permutation matrices. L is lower triangular with
 unit diagonal elements and U is upper triangular.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>IJOB</i> </p>
<pre>
          IJOB is INTEGER
          IJOB = 2: First compute an approximative null-vector e
              of Z using DGECON, e is normalized and solve for
              Zx = +-e - f with the sign giving the greater value
              of 2-norm(x). About 5 times as expensive as Default.
          IJOB .ne. 2: Local look ahead strategy where all entries of
              the r.h.s. b is choosen as either +1 or -1 (Default).
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix Z.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension (LDZ, N)
          On entry, the LU part of the factorization of the n-by-n
          matrix Z computed by DGETC2:  Z = P * L * U * Q
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDA &gt;= max(1, N).
</pre>
<p> <i>RHS</i> </p>
<pre>
          RHS is DOUBLE PRECISION array, dimension (N)
          On entry, RHS contains contributions from other subsystems.
          On exit, RHS contains the solution of the subsystem with
          entries acoording to the value of IJOB (see above).
</pre>
<p> <i>RDSUM</i> </p>
<pre>
          RDSUM is DOUBLE PRECISION
          On entry, the sum of squares of computed contributions to
          the Dif-estimate under computation by DTGSYL, where the
          scaling factor RDSCAL (see below) has been factored out.
          On exit, the corresponding sum of squares updated with the
          contributions from the current sub-system.
          If TRANS = 'T' RDSUM is not touched.
          NOTE: RDSUM only makes sense when DTGSY2 is called by STGSYL.
</pre>
<p> <i>RDSCAL</i> </p>
<pre>
          RDSCAL is DOUBLE PRECISION
          On entry, scaling factor used to prevent overflow in RDSUM.
          On exit, RDSCAL is updated w.r.t. the current contributions
          in RDSUM.
          If TRANS = 'T', RDSCAL is not touched.
          NOTE: RDSCAL only makes sense when DTGSY2 is called by
                DTGSYL.
</pre>
<p> <i>IPIV</i> </p>
<pre><code>
IPIV is INTEGER array, dimension(N).The pivot indices; for
1 &lt;= i &lt;= N, row i of the
                 matrix has been interchanged with row
                 IPIV(i)
                     .
</code></pre>
<p> <i>JPIV</i> </p>
<p>JPIV is INTEGER array, dimension(N).The pivot indices; for<br />
1 &lt;= j &lt;= N, column j of the<br />
                 matrix has been interchanged with column<br />
                 JPIV(j)<br />
                     .</p>
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
<dd> This routine is a further developed implementation of algorithm BSOLVE in [1] using complete pivoting in the LU factorization.</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd>
<pre><code>
  [1] Bo Kagstrom and Lars Westin,
      Generalized Schur Methods with Condition Estimators for
      Solving the Generalized Sylvester Equation, IEEE Transactions
      on Automatic Control, Vol. 34, No. 7, July 1989, pp 745-751.
  [2] Peter Poromaa,
      On Efficient and Robust Estimators for the Separation
      between two Regular Matrix Pairs with Applications in
      Condition Estimation. Report IMINF-95.05, Departement of
      Computing Science, Umea University, S-901 87 Umea, Sweden, 1995.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 171 of file dlatdf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
