---
title: "afnewfilesetup(3)"
name: "afnewfilesetup"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afnewfilesetup/"
description: "afNewFileSetup – create and initialize a new AFfilesetup structure"
---

<p>afNewFileSetup &#8211; create and initialize a new AFfilesetup structure </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>AFfilesetup afNewFileSetup(void);</pre>
<h2>Return Value</h2>
<p>afNewFileSetup returns, upon success, a valid AFfilesetup structure. </p>
<p> Upon failure, afNewFileSetup returns a null AFfilesetup. This case should only occur when no memory is available.</p>
<h2>Description</h2>
<p>The opaque AFfilesetup structure returned by afNewFileSetup can be used to specify parameters for a file to be opened for writing by <code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
