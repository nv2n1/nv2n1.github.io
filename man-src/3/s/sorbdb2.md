---
title: "sorbdb2(3)"
name: "sorbdb2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorbdb2/"
description: "sorbdb2.f –"
---

<p>sorbdb2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sorbdb2</code> (M, P, Q, X11, LDX11, X21, LDX21, THETA, PHI, TAUP1, TAUP2, TAUQ1, WORK, LWORK, INFO)<br />
 <i></i><code>SORBDB2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sorbdb2 (integerM, integerP, integerQ, real, dimension(ldx11,*)X11, integerLDX11, real, dimension(ldx21,*)X21, integerLDX21, real, dimension(*)THETA, real, dimension(*)PHI, real, dimension(*)TAUP1, real, dimension(*)TAUP2, real, dimension(*)TAUQ1, real, dimension(*)WORK, integerLWORK, integerINFO)</h3>
<p><code>SORBDB2</code> .SH &quot;Purpose:&quot; </p>
<pre> SORBDB2 simultaneously bidiagonalizes the blocks of a tall and skinny
 matrix X with orthonomal columns:
 [ B11 ]
 [ X11 ] [ P1 | ] [ 0 ]
 [-----] = [---------] [-----] Q1**T .
 [ X21 ] [ | P2 ] [ B21 ]
 [ 0 ]
 X11 is P-by-Q, and X21 is (M-P)-by-Q. P must be no larger than M-P,
 Q, or M-Q. Routines SORBDB1, SORBDB3, and SORBDB4 handle cases in
 which P is not the minimum dimension.
 The orthogonal matrices P1, P2, and Q1 are P-by-P, (M-P)-by-(M-P),
 and (M-Q)-by-(M-Q), respectively. They are represented implicitly by
 Householder vectors.
 B11 and B12 are P-by-P bidiagonal matrices represented implicitly by
 angles THETA, PHI..fi
 
<code>Parameters:</code>
<dl><dt><dd><i>M</i> 
 M is INTEGER
 The number of rows X11 plus the number of rows in X21.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of rows in X11. 0 &lt;= P &lt;= min(M-P,Q,M-Q).</pre>
<p><i>Q</i> </p>
<pre> Q is INTEGER
 The number of columns in X11 and X21. 0 &lt;= Q &lt;= M.</pre>
<p><i>X11</i> </p>
<pre> X11 is REAL array, dimension (LDX11,Q)
 On entry, the top block of the matrix X to be reduced. On
 exit, the columns of tril(X11) specify reflectors for P1 and
 the rows of triu(X11,1) specify reflectors for Q1.</pre>
<p><i>LDX11</i> </p>
<pre> LDX11 is INTEGER
 The leading dimension of X11. LDX11 &gt;= P.</pre>
<p><i>X21</i> </p>
<pre> X21 is REAL array, dimension (LDX21,Q)
 On entry, the bottom block of the matrix X to be reduced. On
 exit, the columns of tril(X21) specify reflectors for P2.</pre>
<p><i>LDX21</i> </p>
<pre> LDX21 is INTEGER
 The leading dimension of X21. LDX21 &gt;= M-P.</pre>
<p><i>THETA</i> </p>
<pre> THETA is REAL array, dimension (Q)
 The entries of the bidiagonal blocks B11, B21 are defined by
 THETA and PHI. See Further Details.</pre>
<p><i>PHI</i> </p>
<pre> PHI is REAL array, dimension (Q-1)
 The entries of the bidiagonal blocks B11, B21 are defined by
 THETA and PHI. See Further Details.</pre>
<p><i>TAUP1</i> </p>
<pre> TAUP1 is REAL array, dimension (P)
 The scalar factors of the elementary reflectors that define
 P1.</pre>
<p><i>TAUP2</i> </p>
<pre> TAUP2 is REAL array, dimension (M-P)
 The scalar factors of the elementary reflectors that define
 P2.</pre>
<p><i>TAUQ1</i> </p>
<pre> TAUQ1 is REAL array, dimension (Q)
 The scalar factors of the elementary reflectors that define
 Q1.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (LWORK)</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= M-Q.
 
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
<dd>July 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The upper-bidiagonal blocks B11, B21 are represented implicitly by
 angles <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(Q) and <a href="//www.systutorials.com/docs/linux/man/1-PHI/">PHI</a>(1), ..., PHI(Q-1). Every entry
 in each bidiagonal band is a product of a sine or cosine of a THETA
 with a sine or cosine of a PHI. See [1] or SORCSD for details.
 P1, P2, and Q1 are represented as products of elementary reflectors.
 See SORCSD2BY1 for details on generating P1, P2, and Q1 using SORGQR
 and SORGLQ.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl>
<dd>[1] Brian D. Sutton. Computing the complete CS decomposition. Numer. Algorithms, <a href="/docs/linux/man/1-50/">50</a>(1):33-65, 2009.</dl>
<p> Definition at line 201 of file sorbdb2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
