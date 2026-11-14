---
title: "afclosefile(3)"
name: "afclosefile"
section: "3"
letter: "a"
url: "/docs/linux/man/3-afclosefile/"
description: "afCloseFile – close an open audio file"
---

<p>afCloseFile &#8211; close an open audio file </p>
<h2>Synopsis</h2>
<pre>#include &lt;audiofile.h&gt;</pre>
<pre>int afCloseFile(AFfilehandle file);</pre>
<h2>Parameters</h2>
<p>file is a valid file handle created by <code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3).</p>
<h2>Description</h2>
<p>afCloseFile closes the audio file <i>file</i>, updating the file if it was opened for writing.</p>
<h2>Return Value</h2>
<p>afCloseFile returns 0 if the file was closed properly and -1 if an error occurred while closing the file.</p>
<h2>Errors</h2>
<p>afCloseFile can generate these possible errors: </p>
<dl COMPACT>
<dd>&bull; </p>
<p> AF_BAD_FILEHANDLE</dl>
<dl COMPACT>
<dd>&bull; </p>
<p> AF_BAD_LSEEK</dl>
<dl COMPACT>
<dd>&bull; </p>
<p> AF_BAD_WRITE</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-afopenfile/">afOpenFile</a></code>(3)</p>
<h2>Author</h2>
<p>Michael Pruett &lt;michael [at] 68k.org&gt;</p>
