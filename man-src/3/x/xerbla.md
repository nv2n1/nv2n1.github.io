---
title: "xerbla(3)"
name: "xerbla"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xerbla/"
description: "xerbla.f –"
---

<h2 class="name">NAME</h2>
<p> xerbla.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>xerbla</code> (SRNAME, INFO)<br />
 <i></i><code>XERBLA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine xerbla (character*(*)SRNAME, integerINFO)</h3>
<p> <code>XERBLA</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 XERBLA  is an error handler for the LAPACK routines.
 It is called by an LAPACK routine if an input parameter has an
 invalid value.  A message is printed and execution stops.
 Installers may consider modifying the STOP statement in order to
 call system-specific exception-handling facilities.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SRNAME</i> </p>
<pre>
          SRNAME is CHARACTER*(*)
          The name of the routine which called XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          The position of the invalid parameter in the parameter list
          of the calling routine.
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
<dd> November 2011</dl>
<p> Definition at line 71 of file SRC/xerbla.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
