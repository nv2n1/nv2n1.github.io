---
title: "claqr1(3)"
name: "claqr1"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claqr1/"
description: "claqr1.f –"
---

<h2 class="name">NAME</h2>
<p> claqr1.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>claqr1</code> (N, H, LDH, S1, S2, V)<br />
 <i></i><code>CLAQR1</code> sets a scalar multiple of the first column of the product of 2-by-2 or 3-by-3 matrix H and specified shifts.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claqr1 (integerN, complex, dimension( ldh, * )H, integerLDH, complexS1, complexS2, complex, dimension( * )V)</h3>
<p> <code>CLAQR1</code> sets a scalar multiple of the first column of the product of 2-by-2 or 3-by-3 matrix H and specified shifts. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
      Given a 2-by-2 or 3-by-3 matrix H, CLAQR1 sets v to a
      scalar multiple of the first column of the product
      (*)  K = (H - s1*I)*(H - s2*I)
      scaling to avoid overflows and most underflows.
      This is useful for starting double implicit shift bulges
      in the QR algorithm.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is integer
              Order of the matrix H. N must be either 2 or 3.
</pre>
<p> <i>H</i> </p>
<pre>
          H is COMPLEX array of dimension (LDH,N)
              The 2-by-2 or 3-by-3 matrix H in (*).
</pre>
<p> <i>LDH</i> </p>
<pre>
          LDH is integer
              The leading dimension of H as declared in
              the calling procedure.  LDH.GE.N
</pre>
<p> <i>S1</i> </p>
<pre>
          S1 is COMPLEX
</pre>
<p> <i>S2</i> </p>
<pre>
          S2 is COMPLEX
          S1 and S2 are the shifts defining K in (*) above.
</pre>
<p> <i>V</i> </p>
<pre>
          V is COMPLEX array of dimension N
              A scalar multiple of the first column of the
              matrix K in (*).
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Karen Braman and Ralph Byers, Department of Mathematics, University of Kansas, USA</dl>
<p> Definition at line 108 of file claqr1.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
