---
title: "ilaprec-f(3)"
name: "ilaprec-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilaprec-f/"
description: "ilaprec.f –"
---

<p>ilaprec.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>ilaprec</code> (PREC)<br />
 <i></i><code>ILAPREC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilaprec (characterPREC)</h3>
<p><code>ILAPREC</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> This subroutine translated from a character string specifying an
 intermediate precision to the relevant BLAST-specified integer
 constant.
 ILAPREC returns an INTEGER. If ILAPREC &lt; 0, then the input is not a
 character indicating a supported intermediate precision. Otherwise
 ILAPREC returns the constant value corresponding to PREC.</pre>
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
<p> Definition at line 59 of file ilaprec.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
