---
title: "chsein(3)"
name: "chsein"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chsein/"
description: "chsein.f –"
---

<h2 class="name">NAME</h2>
<p> chsein.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chsein</code> (SIDE, EIGSRC, INITV, SELECT, N, H, LDH, W, VL, LDVL, VR, LDVR, MM, M, WORK, RWORK, IFAILL, IFAILR, INFO)<br />
 <i></i><code>CHSEIN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chsein (characterSIDE, characterEIGSRC, characterINITV, logical, dimension( * )SELECT, integerN, complex, dimension( ldh, * )H, integerLDH, complex, dimension( * )W, complex, dimension( ldvl, * )VL, integerLDVL, complex, dimension( ldvr, * )VR, integerLDVR, integerMM, integerM, complex, dimension( * )WORK, real, dimension( * )RWORK, integer, dimension( * )IFAILL, integer, dimension( * )IFAILR, integerINFO)</h3>
<p> <code>CHSEIN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHSEIN uses inverse iteration to find specified right and/or left
 eigenvectors of a complex upper Hessenberg matrix H.
 The right eigenvector x and the left eigenvector y of the matrix H
 corresponding to an eigenvalue w are defined by:
              H * x = w * x,     y**h * H = w * y**h
 where y**h denotes the conjugate transpose of the vector y.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          = 'R': compute right eigenvectors only;
          = 'L': compute left eigenvectors only;
          = 'B': compute both right and left eigenvectors.
</pre>
<p> <i>EIGSRC</i> </p>
<pre>
          EIGSRC is CHARACTER*1
          Specifies the source of eigenvalues supplied in W:
          = 'Q': the eigenvalues were found using CHSEQR; thus, if
                 H has zero subdiagonal elements, and so is
                 block-triangular, then the j-th eigenvalue can be
                 assumed to be an eigenvalue of the block containing
                 the j-th row/column.  This property allows CHSEIN to
                 perform inverse iteration on just one diagonal block.
          = 'N': no assumptions are made on the correspondence
                 between eigenvalues and diagonal blocks.  In this
                 case, CHSEIN must always perform inverse iteration
                 using the whole matrix H.
</pre>
<p> <i>INITV</i> </p>
<pre>
          INITV is CHARACTER*1
          = 'N': no initial vectors are supplied;
          = 'U': user-supplied initial vectors are stored in the arrays
                 VL and/or VR.
</pre>
<p> <i>SELECT</i> </p>
<pre>
          SELECT is LOGICAL array, dimension (N)
          Specifies the eigenvectors to be computed. To select the
          eigenvector corresponding to the eigenvalue W(j),
          SELECT(j) must be set to .TRUE..
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix H.  N &gt;= 0.
</pre>
<p> <i>H</i> </p>
<pre>
          H is COMPLEX array, dimension (LDH,N)
          The upper Hessenberg matrix H.
          If a NaN is detected in H, the routine will return with INFO=-6.
</pre>
<p> <i>LDH</i> </p>
<pre>
          LDH is INTEGER
          The leading dimension of the array H.  LDH &gt;= max(1,N).
</pre>
<p> <i>W</i> </p>
<pre>
          W is COMPLEX array, dimension (N)
          On entry, the eigenvalues of H.
          On exit, the real parts of W may have been altered since
          close eigenvalues are perturbed slightly in searching for
          independent eigenvectors.
</pre>
<p> <i>VL</i> </p>
<pre><code>
          VL is COMPLEX array, dimension (LDVL,MM)
          On entry, if INITV = 'U' and SIDE = 'L' or 'B', VL must
          contain starting vectors for the inverse iteration for the
          left eigenvectors; the starting vector for each eigenvector
          must be in the same column in which the eigenvector will be
          stored.
          On exit, if SIDE = 'L' or 'B', the left eigenvectors
          specified by SELECT will be stored consecutively in the
          columns of VL, in the same order as their eigenvalues.
          If SIDE = 'R', VL is not referenced.
</code></pre>
<p> <i>LDVL</i> </p>
<p>LDVL is INTEGER<br />
        The leading dimension of the array VL.LDVL &gt;= max(1, N) if SIDE = &#8216;L&#8217; or &#8216;B&#8217;;<br />
LDVL &gt;= 1 otherwise.</p>
<p> <i>VR</i> </p>
<p>          VR is COMPLEX array, dimension (LDVR,MM)<br />
          On entry, if INITV = &#8216;U&#8217; and SIDE = &#8216;R&#8217; or &#8216;B&#8217;, VR must<br />
          contain starting vectors for the inverse iteration for the<br />
          right eigenvectors; the starting vector for each eigenvector<br />
          must be in the same column in which the eigenvector will be<br />
          stored.<br />
          On exit, if SIDE = &#8216;R&#8217; or &#8216;B&#8217;, the right eigenvectors<br />
          specified by SELECT will be stored consecutively in the<br />
          columns of VR, in the same order as their eigenvalues.<br />
          If SIDE = &#8216;L&#8217;, VR is not referenced.</p>
<p> <i>LDVR</i> </p>
<p>LDVR is INTEGER<br />
        The leading dimension of the array VR.LDVR &gt;= max(1, N) if SIDE = &#8216;R&#8217; or &#8216;B&#8217;;<br />
LDVR &gt;= 1 otherwise.</p>
<p> <i>MM</i> </p>
<pre>
          MM is INTEGER
          The number of columns in the arrays VL and/or VR. MM &gt;= M.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of columns in the arrays VL and/or VR required to
          store the eigenvectors (= the number of .TRUE. elements in
          SELECT).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (N*N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N)
</pre>
<p> <i>IFAILL</i> </p>
<p>IFAILL is INTEGER array, dimension(MM) If SIDE = &#8216;L&#8217; or &#8216;B&#8217;, IFAILL(i) = j &gt; 0 if the left eigenvector in the i &#8211; th column of VL(corresponding to the eigenvalue w(j)) failed to converge;<br />
IFAILL(i) = 0 if the<br />
            eigenvector converged satisfactorily.If SIDE = &#8216;R&#8217;,<br />
                                                    IFAILL is not referenced.</p>
<p> <i>IFAILR</i> </p>
<p>IFAILR is INTEGER array, dimension(MM) If SIDE = &#8216;R&#8217; or &#8216;B&#8217;, IFAILR(i) = j &gt; 0 if the right eigenvector in the i &#8211; th column of VR(corresponding to the eigenvalue w(j)) failed to converge;<br />
IFAILR(i) = 0 if the<br />
            eigenvector converged satisfactorily.If SIDE = &#8216;L&#8217;,<br />
                                                    IFAILR is not referenced.</p>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : if INFO = i, i is the number of eigenvectors which failed to converge; see IFAILL and IFAILR for further
                details.
</code></pre>
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
<dd> November 2013</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Each eigenvector is normalized so that the element of largest
  magnitude has magnitude 1; here the magnitude of a complex number
  (x,y) is taken to be |x|+|y|.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 244 of file chsein.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
