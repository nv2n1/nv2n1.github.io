---
title: "ilatrans(3)"
name: "ilatrans"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilatrans/"
description: "ilatrans.f –"
---

<h2 class="name">NAME</h2>
<p> ilatrans.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>ilatrans</code> (TRANS)<br />
 <i></i><code>ILATRANS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilatrans (characterTRANS)</h3>
<p> <code>ILATRANS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 This subroutine translates from a character string specifying a
 transposition operation to the relevant BLAST-specified integer
 constant.
 ILATRANS returns an INTEGER.  If ILATRANS &lt; 0, then the input is not
 a character indicating a transposition operator.  Otherwise ILATRANS
 returns the constant value corresponding to TRANS.
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
<p> Definition at line 59 of file ilatrans.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
