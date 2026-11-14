---
title: "zlaesy(3)"
name: "zlaesy"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaesy/"
description: "zlaesy.f –"
---

<p>zlaesy.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaesy</code> (A, B, C, RT1, RT2, EVSCAL, CS1, SN1)<br />
 <i></i><code>ZLAESY</code> computes the eigenvalues and eigenvectors of a 2-by-2 complex symmetric matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaesy (complex*16A, complex*16B, complex*16C, complex*16RT1, complex*16RT2, complex*16EVSCAL, complex*16CS1, complex*16SN1)</h3>
<p><code>ZLAESY</code> computes the eigenvalues and eigenvectors of a 2-by-2 complex symmetric matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAESY computes the eigendecomposition of a 2-by-2 symmetric matrix
 ( ( A, B );( B, C ) )
 provided the norm of the matrix of eigenvectors is larger than
 some threshold value.
 RT1 is the eigenvalue of larger absolute value, and RT2 of
 smaller absolute value. If the eigenvectors are computed, then
 on return ( CS1, SN1 ) is the unit eigenvector for RT1, hence
 [ CS1 SN1 ] . [ A B ] . [ CS1 -SN1 ] = [ RT1 0 ]
 [ -SN1 CS1 ] [ B C ] [ SN1 CS1 ] [ 0 RT2 ]</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>A</i> </p>
<pre> A is COMPLEX*16
 The ( 1, 1 ) element of input matrix.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16
 The ( 1, 2 ) element of input matrix. The ( 2, 1 ) element
 is also given by B, since the 2-by-2 matrix is symmetric.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16
 The ( 2, 2 ) element of input matrix.</pre>
<p><i>RT1</i> </p>
<pre> RT1 is COMPLEX*16
 The eigenvalue of larger modulus.</pre>
<p><i>RT2</i> </p>
<pre> RT2 is COMPLEX*16
 The eigenvalue of smaller modulus.</pre>
<p><i>EVSCAL</i> </p>
<pre> EVSCAL is COMPLEX*16
 The complex value by which the eigenvector matrix was scaled
 to make it orthonormal. If EVSCAL is zero, the eigenvectors
 were not computed. This means one of two things: the 2-by-2
 matrix could not be diagonalized, or the norm of the matrix
 of eigenvectors before scaling was larger than the threshold
 value THRESH (set below).</pre>
<p><i>CS1</i> </p>
<pre> CS1 is COMPLEX*16</pre>
<p><i>SN1</i> </p>
<pre> SN1 is COMPLEX*16
 If EVSCAL .NE. 0, ( CS1, SN1 ) is the unit right eigenvector
 for RT1.</pre>
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
<p> Definition at line 116 of file zlaesy.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
