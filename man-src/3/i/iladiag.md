---
title: "iladiag(3)"
name: "iladiag"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iladiag/"
description: "iladiag.f –"
---

<h2 class="name">NAME</h2>
<p> iladiag.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>iladiag</code> (DIAG)<br />
 <i></i><code>ILADIAG</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function iladiag (characterDIAG)</h3>
<p> <code>ILADIAG</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 This subroutine translated from a character string specifying if a
 matrix has unit diagonal or not to the relevant BLAST-specified
 integer constant.
 ILADIAG returns an INTEGER.  If ILADIAG &lt; 0, then the input is not a
 character indicating a unit or non-unit diagonal.  Otherwise ILADIAG
 returns the constant value corresponding to DIAG.
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
<p> Definition at line 59 of file iladiag.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
