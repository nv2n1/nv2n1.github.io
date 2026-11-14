---
title: "dorbdb-f(3)"
name: "dorbdb-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dorbdb-f/"
description: "dorbdb.f –"
---

<p>dorbdb.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dorbdb</code> (TRANS, SIGNS, M, P, Q, X11, LDX11, X12, LDX12, X21, LDX21, X22, LDX22, THETA, PHI, TAUP1, TAUP2, TAUQ1, TAUQ2, WORK, LWORK, INFO)<br />
 <i></i><code>DORBDB</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dorbdb (characterTRANS, characterSIGNS, integerM, integerP, integerQ, double precision, dimension( ldx11, * )X11, integerLDX11, double precision, dimension( ldx12, * )X12, integerLDX12, double precision, dimension( ldx21, * )X21, integerLDX21, double precision, dimension( ldx22, * )X22, integerLDX22, double precision, dimension( * )THETA, double precision, dimension( * )PHI, double precision, dimension( * )TAUP1, double precision, dimension( * )TAUP2, double precision, dimension( * )TAUQ1, double precision, dimension( * )TAUQ2, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>DORBDB</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DORBDB simultaneously bidiagonalizes the blocks of an M-by-M
 partitioned orthogonal matrix X:
 [ B11 | B12 0 0 ]
 [ X11 | X12 ] [ P1 | ] [ 0 | 0 -I 0 ] [ Q1 | ]**T
 X = [-----------] = [---------] [----------------] [---------] .
 [ X21 | X22 ] [ | P2 ] [ B21 | B22 0 0 ] [ | Q2 ]
 [ 0 | 0 0 I ]
 X11 is P-by-Q. Q must be no larger than P, M-P, or M-Q. (If this is
 not the case, then X must be transposed and/or permuted. This can be
 done in constant time using the TRANS and SIGNS options. See DORCSD
 for details.)
 The orthogonal matrices P1, P2, Q1, and Q2 are P-by-P, (M-P)-by-
 (M-P), Q-by-Q, and (M-Q)-by-(M-Q), respectively. They are
 represented implicitly by Householder vectors.
 B11, B12, B21, and B22 are Q-by-Q bidiagonal matrices represented
 implicitly by angles THETA, PHI.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER
 = 'T': X, U1, U2, V1T, and V2T are stored in row-major
 order;
 otherwise: X, U1, U2, V1T, and V2T are stored in column-
 major order.</pre>
<p><i>SIGNS</i> </p>
<pre> SIGNS is CHARACTER
 = 'O': The lower-left block is made nonpositive (the
 &quot;other&quot; convention);
 otherwise: The upper-right block is made nonpositive (the
 &quot;default&quot; convention).</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows and columns in X.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of rows in X11 and X12. 0 &lt;= P &lt;= M.</pre>
<p><i>Q</i> </p>
<pre> Q is INTEGER
 The number of columns in X11 and X21. 0 &lt;= Q &lt;=
 MIN(P,M-P,M-Q).</pre>
<p><i>X11</i> </p>
<pre> X11 is DOUBLE PRECISION array, dimension (LDX11,Q)
 On entry, the top-left block of the orthogonal matrix to be
 reduced. On exit, the form depends on TRANS:
 If TRANS = 'N', then
 the columns of tril(X11) specify reflectors for P1,
 the rows of triu(X11,1) specify reflectors for Q1;
 else TRANS = 'T', and
 the rows of triu(X11) specify reflectors for P1,
 the columns of tril(X11,-1) specify reflectors for Q1.</pre>
<p><i>LDX11</i> </p>
<pre> LDX11 is INTEGER
 The leading dimension of X11. If TRANS = 'N', then LDX11 &gt;=
 P; else LDX11 &gt;= Q.</pre>
<p><i>X12</i> </p>
<pre> X12 is DOUBLE PRECISION array, dimension (LDX12,M-Q)
 On entry, the top-right block of the orthogonal matrix to
 be reduced. On exit, the form depends on TRANS:
 If TRANS = 'N', then
 the rows of triu(X12) specify the first P reflectors for
 Q2;
 else TRANS = 'T', and
 the columns of tril(X12) specify the first P reflectors
 for Q2.</pre>
<p><i>LDX12</i> </p>
<pre> LDX12 is INTEGER
 The leading dimension of X12. If TRANS = 'N', then LDX12 &gt;=
 P; else LDX11 &gt;= M-Q.</pre>
<p><i>X21</i> </p>
<pre> X21 is DOUBLE PRECISION array, dimension (LDX21,Q)
 On entry, the bottom-left block of the orthogonal matrix to
 be reduced. On exit, the form depends on TRANS:
 If TRANS = 'N', then
 the columns of tril(X21) specify reflectors for P2;
 else TRANS = 'T', and
 the rows of triu(X21) specify reflectors for P2.</pre>
<p><i>LDX21</i> </p>
<pre> LDX21 is INTEGER
 The leading dimension of X21. If TRANS = 'N', then LDX21 &gt;=
 M-P; else LDX21 &gt;= Q.</pre>
<p><i>X22</i> </p>
<pre> X22 is DOUBLE PRECISION array, dimension (LDX22,M-Q)
 On entry, the bottom-right block of the orthogonal matrix to
 be reduced. On exit, the form depends on TRANS:
 If TRANS = 'N', then
 the rows of triu(X22(Q+1:M-P,P+1:M-Q)) specify the last
 M-P-Q reflectors for Q2,
 else TRANS = 'T', and
 the columns of tril(X22(P+1:M-Q,Q+1:M-P)) specify the last
 M-P-Q reflectors for P2.</pre>
<p><i>LDX22</i> </p>
<pre> LDX22 is INTEGER
 The leading dimension of X22. If TRANS = 'N', then LDX22 &gt;=
 M-P; else LDX22 &gt;= M-Q.</pre>
<p><i>THETA</i> </p>
<pre> THETA is DOUBLE PRECISION array, dimension (Q)
 The entries of the bidiagonal blocks B11, B12, B21, B22 can
 be computed from the angles THETA and PHI. See Further
 Details.</pre>
<p><i>PHI</i> </p>
<pre> PHI is DOUBLE PRECISION array, dimension (Q-1)
 The entries of the bidiagonal blocks B11, B12, B21, B22 can
 be computed from the angles THETA and PHI. See Further
 Details.</pre>
<p><i>TAUP1</i> </p>
<pre> TAUP1 is DOUBLE PRECISION array, dimension (P)
 The scalar factors of the elementary reflectors that define
 P1.</pre>
<p><i>TAUP2</i> </p>
<pre> TAUP2 is DOUBLE PRECISION array, dimension (M-P)
 The scalar factors of the elementary reflectors that define
 P2.</pre>
<p><i>TAUQ1</i> </p>
<pre> TAUQ1 is DOUBLE PRECISION array, dimension (Q)
 The scalar factors of the elementary reflectors that define
 Q1.</pre>
<p><i>TAUQ2</i> </p>
<pre> TAUQ2 is DOUBLE PRECISION array, dimension (M-Q)
 The scalar factors of the elementary reflectors that define
 Q2.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (LWORK)</pre>
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
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> The bidiagonal blocks B11, B12, B21, and B22 are represented
 implicitly by angles <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(Q) and <a href="//www.systutorials.com/docs/linux/man/1-PHI/">PHI</a>(1), ...,
 PHI(Q-1). B11 and B21 are upper bidiagonal, while B21 and B22 are
 lower bidiagonal. Every entry in each bidiagonal band is a product
 of a sine or cosine of a THETA with a sine or cosine of a PHI. See
 [1] or DORCSD for details.
 P1, P2, Q1, and Q2 are represented as products of elementary
 reflectors. See DORCSD for details on generating P1, P2, Q1, and Q2
 using DORGQR and DORGLQ.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl COMPACT>
<dd>[1] Brian D. Sutton. Computing the complete CS decomposition. Numer. Algorithms, <a href="/docs/linux/man/1-50/">50</a>(1):33-65, 2009.</dl>
<p> Definition at line 286 of file dorbdb.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
