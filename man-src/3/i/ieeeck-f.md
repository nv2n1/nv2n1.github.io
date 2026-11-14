---
title: "ieeeck-f(3)"
name: "ieeeck-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieeeck-f/"
description: "ieeeck.f –"
---

<p>ieeeck.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>ieeeck</code> (ISPEC, ZERO, ONE)<br />
 <i></i><code>IEEECK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ieeeck (integerISPEC, realZERO, realONE)</h3>
<p><code>IEEECK</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> IEEECK is called from the ILAENV to verify that Infinity and
 possibly NaN arithmetic is safe (i.e. will not trap).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ISPEC</i> </p>
<pre> ISPEC is INTEGER
 Specifies whether to test just for inifinity arithmetic
 or whether to test for infinity and NaN arithmetic.
 = 0: Verify infinity arithmetic only.
 = 1: Verify infinity and NaN arithmetic.</pre>
<p><i>ZERO</i> </p>
<pre> ZERO is REAL
 Must contain the value 0.0
 This is passed to prevent the compiler from optimizing
 away this code.</pre>
<p><i>ONE</i> </p>
<pre> ONE is REAL
 Must contain the value 1.0
 This is passed to prevent the compiler from optimizing
 away this code.
 RETURN VALUE: INTEGER
 = 0: Arithmetic failed to produce the correct answers
 = 1: Arithmetic produced the correct answers</pre>
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
<p> Definition at line 83 of file ieeeck.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
