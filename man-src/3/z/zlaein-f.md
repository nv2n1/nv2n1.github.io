---
title: "zlaein-f(3)"
name: "zlaein-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaein-f/"
description: "zlaein.f –"
---

<p>zlaein.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaein</code> (RIGHTV, NOINIT, N, H, LDH, W, V, B, LDB, RWORK, EPS3, SMLNUM, INFO)<br />
 <i></i><code>ZLAEIN</code> computes a specified right or left eigenvector of an upper Hessenberg matrix by inverse iteration.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaein (logicalRIGHTV, logicalNOINIT, integerN, complex*16, dimension( ldh, * )H, integerLDH, complex*16W, complex*16, dimension( * )V, complex*16, dimension( ldb, * )B, integerLDB, double precision, dimension( * )RWORK, double precisionEPS3, double precisionSMLNUM, integerINFO)</h3>
<p><code>ZLAEIN</code> computes a specified right or left eigenvector of an upper Hessenberg matrix by inverse iteration. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAEIN uses inverse iteration to find a right or left eigenvector
 corresponding to the eigenvalue W of a complex upper Hessenberg
 matrix H.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>RIGHTV</i> </p>
<pre> RIGHTV is LOGICAL
 = .TRUE. : compute right eigenvector;
 = .FALSE.: compute left eigenvector.</pre>
<p><i>NOINIT</i> </p>
<pre> NOINIT is LOGICAL
 = .TRUE. : no initial vector supplied in V
 = .FALSE.: initial vector supplied in V.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix H. N &gt;= 0.</pre>
<p><i>H</i> </p>
<pre> H is COMPLEX*16 array, dimension (LDH,N)
 The upper Hessenberg matrix H.</pre>
<p><i>LDH</i> </p>
<pre> LDH is INTEGER
 The leading dimension of the array H. LDH &gt;= max(1,N).</pre>
<p><i>W</i> </p>
<pre> W is COMPLEX*16
 The eigenvalue of H whose corresponding right or left
 eigenvector is to be computed.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (N)
 On entry, if NOINIT = .FALSE., V must contain a starting
 vector for inverse iteration; otherwise V need not be set.
 On exit, V contains the computed eigenvector, normalized so
 that the component of largest magnitude has magnitude 1; here
 the magnitude of a complex number (x,y) is taken to be
 |x| + |y|.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>EPS3</i> </p>
<pre> EPS3 is DOUBLE PRECISION
 A small machine-dependent value which is used to perturb
 close eigenvalues, and to replace zero pivots.</pre>
<p><i>SMLNUM</i> </p>
<pre> SMLNUM is DOUBLE PRECISION
 A machine-dependent value close to the underflow threshold.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 = 1: inverse iteration did not converge; V is set to the
 last iterate.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 149 of file zlaein.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
