---
title: "dlaein(3)"
name: "dlaein"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaein/"
description: "dlaein.f –"
---

<h2 class="name">NAME</h2>
<p> dlaein.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaein</code> (RIGHTV, NOINIT, N, H, LDH, WR, WI, VR, VI, B, LDB, WORK, EPS3, SMLNUM, BIGNUM, INFO)<br />
 <i></i><code>DLAEIN</code> computes a specified right or left eigenvector of an upper Hessenberg matrix by inverse iteration.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaein (logicalRIGHTV, logicalNOINIT, integerN, double precision, dimension( ldh, * )H, integerLDH, double precisionWR, double precisionWI, double precision, dimension( * )VR, double precision, dimension( * )VI, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( * )WORK, double precisionEPS3, double precisionSMLNUM, double precisionBIGNUM, integerINFO)</h3>
<p> <code>DLAEIN</code> computes a specified right or left eigenvector of an upper Hessenberg matrix by inverse iteration. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAEIN uses inverse iteration to find a right or left eigenvector
 corresponding to the eigenvalue (WR,WI) of a real upper Hessenberg
 matrix H.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>RIGHTV</i> </p>
<pre>
          RIGHTV is LOGICAL
          = .TRUE. : compute right eigenvector;
          = .FALSE.: compute left eigenvector.
</pre>
<p> <i>NOINIT</i> </p>
<pre>
          NOINIT is LOGICAL
          = .TRUE. : no initial vector supplied in (VR,VI).
          = .FALSE.: initial vector supplied in (VR,VI).
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix H.  N &gt;= 0.
</pre>
<p> <i>H</i> </p>
<pre>
          H is DOUBLE PRECISION array, dimension (LDH,N)
          The upper Hessenberg matrix H.
</pre>
<p> <i>LDH</i> </p>
<pre>
          LDH is INTEGER
          The leading dimension of the array H.  LDH &gt;= max(1,N).
</pre>
<p> <i>WR</i> </p>
<pre>
          WR is DOUBLE PRECISION
</pre>
<p> <i>WI</i> </p>
<pre>
          WI is DOUBLE PRECISION
          The real and imaginary parts of the eigenvalue of H whose
          corresponding right or left eigenvector is to be computed.
</pre>
<p> <i>VR</i> </p>
<pre>
          VR is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>VI</i> </p>
<pre><code>
          VI is DOUBLE PRECISION array, dimension (N)
          On entry, if NOINIT = .FALSE. and WI = 0.0, VR must contain
          a real starting vector for inverse iteration using the real
          eigenvalue WR;
          if NOINIT = .FALSE. and WI.ne.0.0, VR and VI
          must contain the real and imaginary parts of a complex
          starting vector for inverse iteration using the complex
          eigenvalue (WR,WI);
          otherwise VR and VI need not be set.On exit, if WI = 0.0(real eigenvalue), VR contains the computed real eigenvector;
          if WI
              .ne .0.0(complex eigenvalue),
                  VR and VI contain the real and imaginary parts of the
                  computed complex eigenvector.The eigenvector is normalized
                  so that the component of largest magnitude has magnitude 1;
          here the magnitude of a complex number(x, y)
          is taken to be | x | + | y |.VI is not referenced if WI = 0.0.
</code></pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,N)
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= N+1.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>EPS3</i> </p>
<pre>
          EPS3 is DOUBLE PRECISION
          A small machine-dependent value which is used to perturb
          close eigenvalues, and to replace zero pivots.
</pre>
<p> <i>SMLNUM</i> </p>
<pre>
          SMLNUM is DOUBLE PRECISION
          A machine-dependent value close to the underflow threshold.
</pre>
<p> <i>BIGNUM</i> </p>
<pre>
          BIGNUM is DOUBLE PRECISION
          A machine-dependent value close to the overflow threshold.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          = 1:  inverse iteration did not converge; VR is set to the
                last iterate, and so is VI if WI.ne.0.0.
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
<p> Definition at line 172 of file dlaein.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
