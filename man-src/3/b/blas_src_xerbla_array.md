---
title: "blas_src_xerbla_array(3)"
name: "blas_src_xerbla_array"
section: "3"
letter: "b"
url: "/docs/linux/man/3-blas_src_xerbla_array/"
description: "xerbla_array.f –"
---

<p>xerbla_array.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>xerbla_array</code> (SRNAME_ARRAY, SRNAME_LEN, INFO)<br />
 <i></i><code>XERBLA_ARRAY</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine xerbla_array (<a href="/docs/linux/man/1-character/">character</a>(1), dimension(srname_len)SRNAME_ARRAY, integerSRNAME_LEN, integerINFO)</h3>
<p><code>XERBLA_ARRAY</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> XERBLA_ARRAY assists other languages in calling XERBLA, the LAPACK
 and BLAS error handler. Rather than taking a Fortran string argument
 as the function's name, XERBLA_ARRAY takes an array of single
 characters along with the array's length. XERBLA_ARRAY then copies
 up to 32 characters of that array into a Fortran string and passes
 that to XERBLA. If called with a non-positive SRNAME_LEN,
 XERBLA_ARRAY will call XERBLA with a string of all blank characters.
 Say some macro or other device makes XERBLA_ARRAY available to C99
 by a name lapack_xerbla and with a common Fortran calling convention.
 Then a C99 program could invoke XERBLA via:
 {
 int flen = strlen(__func__);
 lapack_xerbla(__func__, &amp;flen, &amp;info);
 }
 Providing XERBLA_ARRAY is not necessary for intercepting LAPACK
 errors. XERBLA_ARRAY calls XERBLA.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>SRNAME_ARRAY</i> </p>
<pre> SRNAME_ARRAY is <a href="//www.systutorials.com/docs/linux/man/1-CHARACTER/">CHARACTER</a>(1) array, dimension (SRNAME_LEN)
 The name of the routine which called XERBLA_ARRAY.</pre>
<p><i>SRNAME_LEN</i> </p>
<pre> SRNAME_LEN is INTEGER
 The length of the name in SRNAME_ARRAY.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 The position of the invalid parameter in the parameter list
 of the calling routine.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 81 of file BLAS/SRC/xerbla_array.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
