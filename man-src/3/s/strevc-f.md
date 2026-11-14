---
title: "strevc-f(3)"
name: "strevc-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strevc-f/"
description: "strevc.f –"
---

<p>strevc.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>strevc</code> (SIDE, HOWMNY, SELECT, N, T, LDT, VL, LDVL, VR, LDVR, MM, M, WORK, INFO)<br />
 <i></i><code>STREVC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine strevc (characterSIDE, characterHOWMNY, logical, dimension( * )SELECT, integerN, real, dimension( ldt, * )T, integerLDT, real, dimension( ldvl, * )VL, integerLDVL, real, dimension( ldvr, * )VR, integerLDVR, integerMM, integerM, real, dimension( * )WORK, integerINFO)</h3>
<p><code>STREVC</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STREVC computes some or all of the right and/or left eigenvectors of
 a real upper quasi-triangular matrix T.
 Matrices of this type are produced by the Schur factorization of
 a real general matrix: A = Q*T*Q**T, as computed by SHSEQR.
 
 The right eigenvector x and the left eigenvector y of T corresponding
 to an eigenvalue w are defined by:
 
 T*x = w*x, (y**T)*T = w*(y**T)
 
 where y**T denotes the transpose of y.
 The eigenvalues are not input to this routine, but are read directly
 from the diagonal blocks of T.
 
 This routine returns the matrices X and/or Y of right and left
 eigenvectors of T, or the products Q*X and/or Q*Y, where Q is an
 input matrix. If Q is the orthogonal factor that reduces a matrix
 A to Schur form T, then Q*X and Q*Y are the matrices of right and
 left eigenvectors of A.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'R': compute right eigenvectors only;
 = 'L': compute left eigenvectors only;
 = 'B': compute both right and left eigenvectors.</pre>
<p><i>HOWMNY</i> </p>
<pre> HOWMNY is CHARACTER*1
 = 'A': compute all right and/or left eigenvectors;
 = 'B': compute all right and/or left eigenvectors,
 backtransformed by the matrices in VR and/or VL;
 = 'S': compute selected right and/or left eigenvectors,
 as indicated by the logical array SELECT.</pre>
<p><i>SELECT</i> </p>
<pre> SELECT is LOGICAL array, dimension (N)
 If HOWMNY = 'S', SELECT specifies the eigenvectors to be
 computed.
 If w(j) is a real eigenvalue, the corresponding real
 eigenvector is computed if SELECT(j) is .TRUE..
 If w(j) and w(j+1) are the real and imaginary parts of a
 complex eigenvalue, the corresponding complex eigenvector is
 computed if either SELECT(j) or SELECT(j+1) is .TRUE., and
 on exit SELECT(j) is set to .TRUE. and SELECT(j+1) is set to
 .FALSE..
 Not referenced if HOWMNY = 'A' or 'B'.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix T. N &gt;= 0.</pre>
<p><i>T</i> </p>
<pre> T is REAL array, dimension (LDT,N)
 The upper quasi-triangular matrix T in Schur canonical form.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= max(1,N).</pre>
<p><i>VL</i> </p>
<pre> VL is REAL array, dimension (LDVL,MM)
 On entry, if SIDE = 'L' or 'B' and HOWMNY = 'B', VL must
 contain an N-by-N matrix Q (usually the orthogonal matrix Q
 of Schur vectors returned by SHSEQR).
 On exit, if SIDE = 'L' or 'B', VL contains:
 if HOWMNY = 'A', the matrix Y of left eigenvectors of T;
 if HOWMNY = 'B', the matrix Q*Y;
 if HOWMNY = 'S', the left eigenvectors of T specified by
 SELECT, stored consecutively in the columns
 of VL, in the same order as their
 eigenvalues.
 A complex eigenvector corresponding to a complex eigenvalue
 is stored in two consecutive columns, the first holding the
 real part, and the second the imaginary part.
 Not referenced if SIDE = 'R'.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the array VL. LDVL &gt;= 1, and if
 SIDE = 'L' or 'B', LDVL &gt;= N.</pre>
<p><i>VR</i> </p>
<pre> VR is REAL array, dimension (LDVR,MM)
 On entry, if SIDE = 'R' or 'B' and HOWMNY = 'B', VR must
 contain an N-by-N matrix Q (usually the orthogonal matrix Q
 of Schur vectors returned by SHSEQR).
 On exit, if SIDE = 'R' or 'B', VR contains:
 if HOWMNY = 'A', the matrix X of right eigenvectors of T;
 if HOWMNY = 'B', the matrix Q*X;
 if HOWMNY = 'S', the right eigenvectors of T specified by
 SELECT, stored consecutively in the columns
 of VR, in the same order as their
 eigenvalues.
 A complex eigenvector corresponding to a complex eigenvalue
 is stored in two consecutive columns, the first holding the
 real part and the second the imaginary part.
 Not referenced if SIDE = 'L'.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the array VR. LDVR &gt;= 1, and if
 SIDE = 'R' or 'B', LDVR &gt;= N.</pre>
<p><i>MM</i> </p>
<pre> MM is INTEGER
 The number of columns in the arrays VL and/or VR. MM &gt;= M.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns in the arrays VL and/or VR actually
 used to store the eigenvectors.
 If HOWMNY = 'A' or 'B', M is set to N.
 Each selected real eigenvector occupies one column and each
 selected complex eigenvector occupies two columns.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (3*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The algorithm used in this program is basically backward (forward)
 substitution, with scaling to make the the code robust against
 possible overflow.
 Each eigenvector is normalized so that the element of largest
 magnitude has magnitude 1; here the magnitude of a complex number
 (x,y) is taken to be |x| + |y|.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 222 of file strevc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
