---
title: "cbbcsd-f(3)"
name: "cbbcsd-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cbbcsd-f/"
description: "cbbcsd.f –"
---

<p>cbbcsd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cbbcsd</code> (JOBU1, JOBU2, JOBV1T, JOBV2T, TRANS, M, P, Q, THETA, PHI, U1, LDU1, U2, LDU2, V1T, LDV1T, V2T, LDV2T, B11D, B11E, B12D, B12E, B21D, B21E, B22D, B22E, RWORK, LRWORK, INFO)<br />
 <i></i><code>CBBCSD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cbbcsd (characterJOBU1, characterJOBU2, characterJOBV1T, characterJOBV2T, characterTRANS, integerM, integerP, integerQ, real, dimension( * )THETA, real, dimension( * )PHI, complex, dimension( ldu1, * )U1, integerLDU1, complex, dimension( ldu2, * )U2, integerLDU2, complex, dimension( ldv1t, * )V1T, integerLDV1T, complex, dimension( ldv2t, * )V2T, integerLDV2T, real, dimension( * )B11D, real, dimension( * )B11E, real, dimension( * )B12D, real, dimension( * )B12E, real, dimension( * )B21D, real, dimension( * )B21E, real, dimension( * )B22D, real, dimension( * )B22E, real, dimension( * )RWORK, integerLRWORK, integerINFO)</h3>
<p><code>CBBCSD</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CBBCSD computes the CS decomposition of a unitary matrix in
 bidiagonal-block form,
 [ B11 | B12 0 0 ]
 [ 0 | 0 -I 0 ]
 X = [----------------]
 [ B21 | B22 0 0 ]
 [ 0 | 0 0 I ]
 [ C | -S 0 0 ]
 [ U1 | ] [ 0 | 0 -I 0 ] [ V1 | ]**H
 = [---------] [---------------] [---------] .
 [ | U2 ] [ S | C 0 0 ] [ | V2 ]
 [ 0 | 0 0 I ]
 X is M-by-M, its top-left block is P-by-Q, and Q must be no larger
 than P, M-P, or M-Q. (If Q is not the smallest index, then X must be
 transposed and/or permuted. This can be done in constant time using
 the TRANS and SIGNS options. See CUNCSD for details.)
 The bidiagonal matrices B11, B12, B21, and B22 are represented
 implicitly by angles THETA(1:Q) and PHI(1:Q-1).
 The unitary matrices U1, U2, V1T, and V2T are input/output.
 The input matrices are pre- or post-multiplied by the appropriate
 singular vector matrices.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBU1</i> </p>
<pre> JOBU1 is CHARACTER
 = 'Y': U1 is updated;
 otherwise: U1 is not updated.</pre>
<p><i>JOBU2</i> </p>
<pre> JOBU2 is CHARACTER
 = 'Y': U2 is updated;
 otherwise: U2 is not updated.</pre>
<p><i>JOBV1T</i> </p>
<pre> JOBV1T is CHARACTER
 = 'Y': V1T is updated;
 otherwise: V1T is not updated.</pre>
<p><i>JOBV2T</i> </p>
<pre> JOBV2T is CHARACTER
 = 'Y': V2T is updated;
 otherwise: V2T is not updated.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER
 = 'T': X, U1, U2, V1T, and V2T are stored in row-major
 order;
 otherwise: X, U1, U2, V1T, and V2T are stored in column-
 major order.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows and columns in X, the unitary matrix in
 bidiagonal-block form.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of rows in the top-left block of X. 0 &lt;= P &lt;= M.</pre>
<p><i>Q</i> </p>
<pre> Q is INTEGER
 The number of columns in the top-left block of X.
 0 &lt;= Q &lt;= MIN(P,M-P,M-Q).</pre>
<p><i>THETA</i> </p>
<pre> THETA is REAL array, dimension (Q)
 On entry, the angles <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1),...,THETA(Q) that, along with
 <a href="//www.systutorials.com/docs/linux/man/1-PHI/">PHI</a>(1), ...,PHI(Q-1), define the matrix in bidiagonal-block
 form. On exit, the angles whose cosines and sines define the
 diagonal blocks in the CS decomposition.</pre>
<p><i>PHI</i> </p>
<pre> PHI is REAL array, dimension (Q-1)
 The angles <a href="//www.systutorials.com/docs/linux/man/1-PHI/">PHI</a>(1),...,PHI(Q-1) that, along with <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1),...,
 THETA(Q), define the matrix in bidiagonal-block form.</pre>
<p><i>U1</i> </p>
<pre> U1 is COMPLEX array, dimension (LDU1,P)
 On entry, an LDU1-by-P matrix. On exit, U1 is postmultiplied
 by the left singular vector matrix common to [ B11 ; 0 ] and
 [ B12 0 0 ; 0 -I 0 0 ].</pre>
<p><i>LDU1</i> </p>
<pre> LDU1 is INTEGER
 The leading dimension of the array U1.</pre>
<p><i>U2</i> </p>
<pre> U2 is COMPLEX array, dimension (LDU2,M-P)
 On entry, an LDU2-by-(M-P) matrix. On exit, U2 is
 postmultiplied by the left singular vector matrix common to
 [ B21 ; 0 ] and [ B22 0 0 ; 0 0 I ].</pre>
<p><i>LDU2</i> </p>
<pre> LDU2 is INTEGER
 The leading dimension of the array U2.</pre>
<p><i>V1T</i> </p>
<pre> V1T is COMPLEX array, dimension (LDV1T,Q)
 On entry, a LDV1T-by-Q matrix. On exit, V1T is premultiplied
 by the conjugate transpose of the right singular vector
 matrix common to [ B11 ; 0 ] and [ B21 ; 0 ].</pre>
<p><i>LDV1T</i> </p>
<pre> LDV1T is INTEGER
 The leading dimension of the array V1T.</pre>
<p><i>V2T</i> </p>
<pre> V2T is COMPLEX array, dimenison (LDV2T,M-Q)
 On entry, a LDV2T-by-(M-Q) matrix. On exit, V2T is
 premultiplied by the conjugate transpose of the right
 singular vector matrix common to [ B12 0 0 ; 0 -I 0 ] and
 [ B22 0 0 ; 0 0 I ].</pre>
<p><i>LDV2T</i> </p>
<pre> LDV2T is INTEGER
 The leading dimension of the array V2T.</pre>
<p><i>B11D</i> </p>
<pre> B11D is REAL array, dimension (Q)
 When CBBCSD converges, B11D contains the cosines of <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1),
 ..., THETA(Q). If CBBCSD fails to converge, then B11D
 contains the diagonal of the partially reduced top-left
 block.</pre>
<p><i>B11E</i> </p>
<pre> B11E is REAL array, dimension (Q-1)
 When CBBCSD converges, B11E contains zeros. If CBBCSD fails
 to converge, then B11E contains the superdiagonal of the
 partially reduced top-left block.</pre>
<p><i>B12D</i> </p>
<pre> B12D is REAL array, dimension (Q)
 When CBBCSD converges, B12D contains the negative sines of
 <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(Q). If CBBCSD fails to converge, then
 B12D contains the diagonal of the partially reduced top-right
 block.</pre>
<p><i>B12E</i> </p>
<pre> B12E is REAL array, dimension (Q-1)
 When CBBCSD converges, B12E contains zeros. If CBBCSD fails
 to converge, then B12E contains the subdiagonal of the
 partially reduced top-right block.</pre>
<p><i>B21D</i> </p>
<pre> B21D is REAL array, dimension (Q)
 When CBBCSD converges, B21D contains the negative sines of
 <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(Q). If CBBCSD fails to converge, then
 B21D contains the diagonal of the partially reduced bottom-left
 block.</pre>
<p><i>B21E</i> </p>
<pre> B21E is REAL array, dimension (Q-1)
 When CBBCSD converges, B21E contains zeros. If CBBCSD fails
 to converge, then B21E contains the subdiagonal of the
 partially reduced bottom-left block.</pre>
<p><i>B22D</i> </p>
<pre> B22D is REAL array, dimension (Q)
 When CBBCSD converges, B22D contains the negative sines of
 <a href="//www.systutorials.com/docs/linux/man/1-THETA/">THETA</a>(1), ..., THETA(Q). If CBBCSD fails to converge, then
 B22D contains the diagonal of the partially reduced bottom-right
 block.</pre>
<p><i>B22E</i> </p>
<pre> B22E is REAL array, dimension (Q-1)
 When CBBCSD converges, B22E contains zeros. If CBBCSD fails
 to converge, then B22E contains the subdiagonal of the
 partially reduced bottom-right block.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LRWORK</i> </p>
<pre> LRWORK is INTEGER
 The dimension of the array RWORK. LRWORK &gt;= MAX(1,8*Q).
 If LRWORK = -1, then a workspace query is assumed; the
 routine only calculates the optimal size of the RWORK array,
 returns this value as the first entry of the work array, and
 no error message related to LRWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if CBBCSD did not converge, INFO specifies the number
 of nonzero entries in PHI, and B11D, B11E, etc.,
 contain the partially reduced matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl COMPACT>
<dd>
<pre> TOLMUL REAL, default = MAX(10,MIN(100,EPS**(-1/8)))
 TOLMUL controls the convergence criterion of the QR loop.
 Angles THETA(i), PHI(i) are rounded to 0 or PI/2 when they
 are within TOLMUL*EPS of either bound.</pre>
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
<p> Definition at line 330 of file cbbcsd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
