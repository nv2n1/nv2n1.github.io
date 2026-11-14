---
title: "dsecnd_none-f(3)"
name: "dsecnd_none-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsecnd_none-f/"
description: "dsecnd_NONE.f –"
---

<p>dsecnd_NONE.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>dsecnd</code> ()<br />
 <i></i><code>DSECND</code> returns nothing</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dsecnd ()</h3>
<p><code>DSECND</code> returns nothing <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DSECND returns nothing instead of returning the user time for a process in seconds.
 If you are using that routine, it means that neither EXTERNAL ETIME,
 EXTERNAL ETIME_, INTERNAL ETIME, INTERNAL CPU_TIME is available on
 your machine.</pre>
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
<p> Definition at line 38 of file dsecnd_NONE.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
