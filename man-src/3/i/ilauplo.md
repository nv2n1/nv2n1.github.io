---
title: "ilauplo(3)"
name: "ilauplo"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilauplo/"
description: "ilauplo.f –"
---

<h2 class="name">NAME</h2>
<p> ilauplo.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>ilauplo</code> (UPLO)<br />
 <i></i><code>ILAUPLO</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilauplo (characterUPLO)</h3>
<p> <code>ILAUPLO</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 This subroutine translated from a character string specifying a
 upper- or lower-triangular matrix to the relevant BLAST-specified
 integer constant.
 ILAUPLO returns an INTEGER.  If ILAUPLO &lt; 0, then the input is not
 a character indicating an upper- or lower-triangular matrix.
 Otherwise ILAUPLO returns the constant value corresponding to UPLO.
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
<p> Definition at line 59 of file ilauplo.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
