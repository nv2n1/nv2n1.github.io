---
title: "dorcsd-f(3)"
name: "dorcsd-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dorcsd-f/"
description: "dorcsd.f –"
---

<p>dorcsd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>recursive subroutine <code>dorcsd</code> (JOBU1, JOBU2, JOBV1T, JOBV2T, TRANS, SIGNS, M, P, Q, X11, LDX11, X12, LDX12, X21, LDX21, X22, LDX22, THETA, U1, LDU1, U2, LDU2, V1T, LDV1T, V2T, LDV2T, WORK, LWORK, IWORK, INFO)<br />
 <i></i><code>DORCSD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>recursive subroutine dorcsd (characterJOBU1, characterJOBU2, characterJOBV1T, characterJOBV2T, characterTRANS, characterSIGNS, integerM, integerP, integerQ, double precision, dimension( ldx11, * )X11, integerLDX11, double precision, dimension( ldx12, * )X12, integerLDX12, double precision, dimension( ldx21, * )X21, integerLDX21, double precision, dimension( ldx22, * )X22, integerLDX22, double precision, dimension( * )THETA, double precision, dimension( ldu1, * )U1, integerLDU1, double precision, dimension( ldu2, * )U2, integerLDU2, double precision, dimension( ldv1t, * )V1T, integerLDV1T, double precision, dimension( ldv2t, * )V2T, integerLDV2T, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>DORCSD</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DORCSD computes the CS decomposition of an M-by-M partitioned
 orthogonal matrix X:
 [ I 0 0 | 0 0 0 ]
 [ 0 C 0 | 0 -S 0 ]
 [ X11 | X12 ] [ U1 | ] [ 0 0 0 | 0 0 -I ] [ V1 | ]**T
 X = [-----------] = [---------] [---------------------] [---------] .
 [ X21 | X22 ] [ | U2 ] [ 0 0 0 | I 0 0 ] [ | V2 ]
 [ 0 S 0 | 0 C 0 ]
 [ 0 0 I | 0 0 0 ]
 X11 is P-by-Q. The orthogonal matrices U1, U2, V1, and V2 are P-by-P,
 (M-P)-by-(M-P), Q-by-Q, and (M-Q)-by-(M-Q), respectively. C and S are
 R-by-R nonnegative diagonal matrices satisfying C^2 + S^2 = I, in
 which R = MIN(P,M-P,Q,M-Q).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBU1</i> </p>
<pre> JOBU1 is CHARACTER
 = 'Y': U1 is computed;
 otherwise: U1 is not computed.</pre>
<p><i>JOBU2</i> </p>
<pre> JOBU2 is CHARACTER
 = 'Y': U2 is computed;
 otherwise: U2 is not computed.</pre>
<p><i>JOBV1T</i> </p>
<pre> JOBV1T is CHARACTER
 = 'Y': V1T is computed;
 otherwise: V1T is not computed.</pre>
<p><i>JOBV2T</i> </p>
<pre> JOBV2T is CHARACTER
 = 'Y': V2T is computed;
 otherwise: V2T is not computed.</pre>
<p><i>TRANS</i> </p>
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
 The number of columns in X11 and X21. 0 &lt;= Q &lt;= M.</pre>
<p><i>X11</i> </p>
<pre> X11 is DOUBLE PRECISION array, dimension (LDX11,Q)
 On entry, part of the orthogonal matrix whose CSD is desired.</pre>
<p><i>LDX11</i> </p>
<pre> LDX11 is INTEGER
 The leading dimension of X11. LDX11 &gt;= MAX(1,P).</pre>
<p><i>X12</i> </p>
<pre> X12 is DOUBLE PRECISION array, dimension (LDX12,M-Q)
 On entry, part of the orthogonal matrix whose CSD is desired.</pre>
<p><i>LDX12</i> </p>
<pre> LDX12 is INTEGER
 The leading dimension of X12. LDX12 &gt;= MAX(1,P).</pre>
<p><i>X21</i> </p>
<pre> X21 is DOUBLE PRECISION array, dimension (LDX21,Q)
 On entry, part of the orthogonal matrix whose CSD is desired.</pre>
<p><i>LDX21</i> </p>
<pre> LDX21 is INTEGER
 The leading dimension of X11. LDX21 &gt;= MAX(1,M-P).</pre>
<p><i>X22</i> </p>
<pre> X22 is DOUBLE PRECISION array, dimension (LDX22,M-Q)
 On entry, part of the orthogonal matrix whose CSD is desired.</pre>
<p><i>LDX22</i> </p>
<pre> LDX22 is INTEGER
 The leading dimension of X11. LDX22 &gt;= MAX(1,M-P).</pre>
<p><i>THETA</i> </p>
<pre> THETA is DOUBLE PRECISION array, dimension (R), in which R =
 MIN(P,M-P,Q,M-Q).
 C = DIAG( COS(<a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1)), ... , COS(THETA(R)) ) and
 S = DIAG( SIN(<a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1)), ... , SIN(THETA(R)) ).</pre>
<p><i>U1</i> </p>
<pre> U1 is DOUBLE PRECISION array, dimension (P)
 If JOBU1 = 'Y', U1 contains the P-by-P orthogonal matrix U1.</pre>
<p><i>LDU1</i> </p>
<pre> LDU1 is INTEGER
 The leading dimension of U1. If JOBU1 = 'Y', LDU1 &gt;=
 MAX(1,P).</pre>
<p><i>U2</i> </p>
<pre> U2 is DOUBLE PRECISION array, dimension (M-P)
 If JOBU2 = 'Y', U2 contains the (M-P)-by-(M-P) orthogonal
 matrix U2.</pre>
<p><i>LDU2</i> </p>
<pre> LDU2 is INTEGER
 The leading dimension of U2. If JOBU2 = 'Y', LDU2 &gt;=
 MAX(1,M-P).</pre>
<p><i>V1T</i> </p>
<pre> V1T is DOUBLE PRECISION array, dimension (Q)
 If JOBV1T = 'Y', V1T contains the Q-by-Q matrix orthogonal
 matrix V1**T.</pre>
<p><i>LDV1T</i> </p>
<pre> LDV1T is INTEGER
 The leading dimension of V1T. If JOBV1T = 'Y', LDV1T &gt;=
 MAX(1,Q).</pre>
<p><i>V2T</i> </p>
<pre> V2T is DOUBLE PRECISION array, dimension (M-Q)
 If JOBV2T = 'Y', V2T contains the (M-Q)-by-(M-Q) orthogonal
 matrix V2**T.</pre>
<p><i>LDV2T</i> </p>
<pre> LDV2T is INTEGER
 The leading dimension of V2T. If JOBV2T = 'Y', LDV2T &gt;=
 MAX(1,M-Q).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
 If INFO &gt; 0 on exit, WORK(2:R) contains the values <a href="//www.systutorials.com/docs/linux/man/1-PHI/">PHI</a>(1),
 ..., PHI(R-1) that, together with <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(R),
 define the matrix in intermediate bidiagonal-block form
 remaining after nonconvergence. INFO specifies the number
 of nonzero PHI's.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the work array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (M-MIN(P, M-P, Q, M-Q))</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: DBBCSD did not converge. See the description of WORK
 above for details.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl COMPACT>
<dd>[1] Brian D. Sutton. Computing the complete CS decomposition. Numer. Algorithms, <a href="/docs/linux/man/1-50/">50</a>(1):33-65, 2009.</dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 297 of file dorcsd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
