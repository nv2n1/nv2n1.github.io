---
title: "shsein-f(3)"
name: "shsein-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-shsein-f/"
description: "shsein.f –"
---

<p>shsein.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>shsein</code> (SIDE, EIGSRC, INITV, SELECT, N, H, LDH, WR, WI, VL, LDVL, VR, LDVR, MM, M, WORK, IFAILL, IFAILR, INFO)<br />
 <i></i><code>SHSEIN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine shsein (characterSIDE, characterEIGSRC, characterINITV, logical, dimension( * )SELECT, integerN, real, dimension( ldh, * )H, integerLDH, real, dimension( * )WR, real, dimension( * )WI, real, dimension( ldvl, * )VL, integerLDVL, real, dimension( ldvr, * )VR, integerLDVR, integerMM, integerM, real, dimension( * )WORK, integer, dimension( * )IFAILL, integer, dimension( * )IFAILR, integerINFO)</h3>
<p><code>SHSEIN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SHSEIN uses inverse iteration to find specified right and/or left
 eigenvectors of a real upper Hessenberg matrix H.
 The right eigenvector x and the left eigenvector y of the matrix H
 corresponding to an eigenvalue w are defined by:
 H * x = w * x, y**h * H = w * y**h
 where y**h denotes the conjugate transpose of the vector y.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'R': compute right eigenvectors only;
 = 'L': compute left eigenvectors only;
 = 'B': compute both right and left eigenvectors.</pre>
<p><i>EIGSRC</i> </p>
<pre> EIGSRC is CHARACTER*1
 Specifies the source of eigenvalues supplied in (WR,WI):
 = 'Q': the eigenvalues were found using SHSEQR; thus, if
 H has zero subdiagonal elements, and so is
 block-triangular, then the j-th eigenvalue can be
 assumed to be an eigenvalue of the block containing
 the j-th row/column. This property allows SHSEIN to
 perform inverse iteration on just one diagonal block.
 = 'N': no assumptions are made on the correspondence
 between eigenvalues and diagonal blocks. In this
 case, SHSEIN must always perform inverse iteration
 using the whole matrix H.</pre>
<p><i>INITV</i> </p>
<pre> INITV is CHARACTER*1
 = 'N': no initial vectors are supplied;
 = 'U': user-supplied initial vectors are stored in the arrays
 VL and/or VR.</pre>
<p><i>SELECT</i> </p>
<pre> SELECT is LOGICAL array, dimension (N)
 Specifies the eigenvectors to be computed. To select the
 real eigenvector corresponding to a real eigenvalue WR(j),
 SELECT(j) must be set to .TRUE.. To select the complex
 eigenvector corresponding to a complex eigenvalue
 (WR(j),WI(j)), with complex conjugate (WR(j+1),WI(j+1)),
 either SELECT(j) or SELECT(j+1) or both must be set to
 .TRUE.; then on exit SELECT(j) is .TRUE. and SELECT(j+1) is
 .FALSE..</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix H. N &gt;= 0.</pre>
<p><i>H</i> </p>
<pre> H is REAL array, dimension (LDH,N)
 The upper Hessenberg matrix H.</pre>
<p><i>LDH</i> </p>
<pre> LDH is INTEGER
 The leading dimension of the array H. LDH &gt;= max(1,N).</pre>
<p><i>WR</i> </p>
<pre> WR is REAL array, dimension (N)</pre>
<p><i>WI</i> </p>
<pre> WI is REAL array, dimension (N)
 On entry, the real and imaginary parts of the eigenvalues of
 H; a complex conjugate pair of eigenvalues must be stored in
 consecutive elements of WR and WI.
 On exit, WR may have been altered since close eigenvalues
 are perturbed slightly in searching for independent
 eigenvectors.</pre>
<p><i>VL</i> </p>
<pre> VL is REAL array, dimension (LDVL,MM)
 On entry, if INITV = 'U' and SIDE = 'L' or 'B', VL must
 contain starting vectors for the inverse iteration for the
 left eigenvectors; the starting vector for each eigenvector
 must be in the same column(s) in which the eigenvector will
 be stored.
 On exit, if SIDE = 'L' or 'B', the left eigenvectors
 specified by SELECT will be stored consecutively in the
 columns of VL, in the same order as their eigenvalues. A
 complex eigenvector corresponding to a complex eigenvalue is
 stored in two consecutive columns, the first holding the real
 part and the second the imaginary part.
 If SIDE = 'R', VL is not referenced.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the array VL.
 LDVL &gt;= max(1,N) if SIDE = 'L' or 'B'; LDVL &gt;= 1 otherwise.</pre>
<p><i>VR</i> </p>
<pre> VR is REAL array, dimension (LDVR,MM)
 On entry, if INITV = 'U' and SIDE = 'R' or 'B', VR must
 contain starting vectors for the inverse iteration for the
 right eigenvectors; the starting vector for each eigenvector
 must be in the same column(s) in which the eigenvector will
 be stored.
 On exit, if SIDE = 'R' or 'B', the right eigenvectors
 specified by SELECT will be stored consecutively in the
 columns of VR, in the same order as their eigenvalues. A
 complex eigenvector corresponding to a complex eigenvalue is
 stored in two consecutive columns, the first holding the real
 part and the second the imaginary part.
 If SIDE = 'L', VR is not referenced.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the array VR.
 LDVR &gt;= max(1,N) if SIDE = 'R' or 'B'; LDVR &gt;= 1 otherwise.</pre>
<p><i>MM</i> </p>
<pre> MM is INTEGER
 The number of columns in the arrays VL and/or VR. MM &gt;= M.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns in the arrays VL and/or VR required to
 store the eigenvectors; each selected real eigenvector
 occupies one column and each selected complex eigenvector
 occupies two columns.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension ((N+2)*N)</pre>
<p><i>IFAILL</i> </p>
<pre> IFAILL is INTEGER array, dimension (MM)
 If SIDE = 'L' or 'B', IFAILL(i) = j &gt; 0 if the left
 eigenvector in the i-th column of VL (corresponding to the
 eigenvalue w(j)) failed to converge; IFAILL(i) = 0 if the
 eigenvector converged satisfactorily. If the i-th and (i+1)th
 columns of VL hold a complex eigenvector, then IFAILL(i) and
 IFAILL(i+1) are set to the same value.
 If SIDE = 'R', IFAILL is not referenced.</pre>
<p><i>IFAILR</i> </p>
<pre> IFAILR is INTEGER array, dimension (MM)
 If SIDE = 'R' or 'B', IFAILR(i) = j &gt; 0 if the right
 eigenvector in the i-th column of VR (corresponding to the
 eigenvalue w(j)) failed to converge; IFAILR(i) = 0 if the
 eigenvector converged satisfactorily. If the i-th and (i+1)th
 columns of VR hold a complex eigenvector, then IFAILR(i) and
 IFAILR(i+1) are set to the same value.
 If SIDE = 'L', IFAILR is not referenced.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, i is the number of eigenvectors which
 failed to converge; see IFAILL and IFAILR for further
 details.</pre>
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
<pre> Each eigenvector is normalized so that the element of largest
 magnitude has magnitude 1; here the magnitude of a complex number
 (x,y) is taken to be |x|+|y|.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 261 of file shsein.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
