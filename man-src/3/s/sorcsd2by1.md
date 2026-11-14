---
title: "sorcsd2by1(3)"
name: "sorcsd2by1"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorcsd2by1/"
description: "sorcsd2by1.f –"
---

<p>sorcsd2by1.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sorcsd2by1</code> (JOBU1, JOBU2, JOBV1T, M, P, Q, X11, LDX11, X21, LDX21, THETA, U1, LDU1, U2, LDU2, V1T, LDV1T, WORK, LWORK, IWORK, INFO)<br />
 <i></i><code>SORCSD2BY1</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sorcsd2by1 (characterJOBU1, characterJOBU2, characterJOBV1T, integerM, integerP, integerQ, real, dimension(ldx11,*)X11, integerLDX11, real, dimension(ldx21,*)X21, integerLDX21, real, dimension(*)THETA, real, dimension(ldu1,*)U1, integerLDU1, real, dimension(ldu2,*)U2, integerLDU2, real, dimension(ldv1t,*)V1T, integerLDV1T, real, dimension(*)WORK, integerLWORK, integer, dimension(*)IWORK, integerINFO)</h3>
<p><code>SORCSD2BY1</code> .SH &quot;Purpose:&quot; </p>
<pre> SORCSD2BY1 computes the CS decomposition of an M-by-Q matrix X with
 orthonormal columns that has been partitioned into a 2-by-1 block
 structure:
 [ I 0 0 ]
 [ 0 C 0 ]
 [ X11 ] [ U1 | ] [ 0 0 0 ]
 X = [-----] = [---------] [----------] V1**T .
 [ X21 ] [ | U2 ] [ 0 0 0 ]
 [ 0 S 0 ]
 [ 0 0 I ]
 
 X11 is P-by-Q. The orthogonal matrices U1, U2, V1, and V2 are P-by-P,
 (M-P)-by-(M-P), Q-by-Q, and (M-Q)-by-(M-Q), respectively. C and S are
 R-by-R nonnegative diagonal matrices satisfying C^2 + S^2 = I, in
 which R = MIN(P,M-P,Q,M-Q)..fi
 
<code>Parameters:</code>
<dl><dt><dd><i>JOBU1</i> 
 JOBU1 is CHARACTER
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
<pre> X11 is REAL array, dimension (LDX11,Q)
 On entry, part of the orthogonal matrix whose CSD is
 desired.</pre>
<p><i>LDX11</i> </p>
<pre> LDX11 is INTEGER
 The leading dimension of X11. LDX11 &gt;= MAX(1,P).</pre>
<p><i>X21</i> </p>
<pre> X21 is REAL array, dimension (LDX21,Q)
 On entry, part of the orthogonal matrix whose CSD is
 desired.</pre>
<p><i>LDX21</i> </p>
<pre> LDX21 is INTEGER
 The leading dimension of X21. LDX21 &gt;= MAX(1,M-P).</pre>
<p><i>THETA</i> </p>
<pre> THETA is REAL array, dimension (R), in which R =
 MIN(P,M-P,Q,M-Q).
 C = DIAG( COS(<a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1)), ... , COS(THETA(R)) ) and
 S = DIAG( SIN(<a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1)), ... , SIN(THETA(R)) ).</pre>
<p><i>U1</i> </p>
<pre> U1 is REAL array, dimension (P)
 If JOBU1 = 'Y', U1 contains the P-by-P orthogonal matrix U1.</pre>
<p><i>LDU1</i> </p>
<pre> LDU1 is INTEGER
 The leading dimension of U1. If JOBU1 = 'Y', LDU1 &gt;=
 MAX(1,P).</pre>
<p><i>U2</i> </p>
<pre> U2 is REAL array, dimension (M-P)
 If JOBU2 = 'Y', U2 contains the (M-P)-by-(M-P) orthogonal
 matrix U2.</pre>
<p><i>LDU2</i> </p>
<pre> LDU2 is INTEGER
 The leading dimension of U2. If JOBU2 = 'Y', LDU2 &gt;=
 MAX(1,M-P).</pre>
<p><i>V1T</i> </p>
<pre> V1T is REAL array, dimension (Q)
 If JOBV1T = 'Y', V1T contains the Q-by-Q matrix orthogonal
 matrix V1**T.</pre>
<p><i>LDV1T</i> </p>
<pre> LDV1T is INTEGER
 The leading dimension of V1T. If JOBV1T = 'Y', LDV1T &gt;=
 MAX(1,Q).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
 If INFO &gt; 0 on exit, WORK(2:R) contains the values <a href="//www.systutorials.com/docs/linux/man/1-PHI/">PHI</a>(1),
 ..., PHI(R-1) that, together with <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(R),
 define the matrix in intermediate bidiagonal-block form
 remaining after nonconvergence. INFO specifies the number
 of nonzero PHI's.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.</pre>
<p>&nbsp;<wbr> </p>
<pre> If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the work array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p>&nbsp;<wbr><br />
 <i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (M-MIN(P,M-P,Q,M-Q))</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: SBBCSD did not converge. See the description of WORK
 above for details.</pre>
</dl>
<p> <code>Reference: [1] Brian D. Sutton. Computing the complete CS decomposition. Numer.</code></p>
<dl>
<dd>Algorithms, <a href="/docs/linux/man/1-50/">50</a>(1):33-65, 2009.</dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>July 2012</dl>
<p> Definition at line 232 of file sorcsd2by1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
