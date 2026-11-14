---
title: "pre2ncgm(1)"
name: "pre2ncgm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pre2ncgm/"
description: "pre2ncgm – convert a pre-CGM NCAR metafile to an NCAR CGM."
---

<h2>NAME</h2>
<p> pre2ncgm &#8211; convert a pre-CGM NCAR metafile to an NCAR CGM.</p>
<h2>SYNOPSIS</h2>
<p> <code>pre2ncgm</code> [<code>-n</code>]</p>
<h2>DESCRIPTION</h2>
<p> The &quot;pre2ncgm&quot; command reads a pre-CGM NCAR metafile from standard input and writes an NCAR CGM file to standard output. When plotted, the output file should have virtually the same appearance as the input file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code></p>
<dd> When this option appears, all text and header records which appear in the input file (created by PRSIM) are not copied to the output file.</dl>
<h2>EXAMPLES</h2>
<p> The command </p>
<p> <code>pre2ncgm</code> &lt; input-file &gt; output-file </p>
<p> causes &quot;input-file&quot; (which should be a pre-CGM NCAR metafile) to be read and the equivalent NCAR CGM file to be written to &quot;output-file&quot;).</p>
<h2>DIAGNOSTICS</h2>
<p> Various errors are detected by &quot;pre2ncgm&quot; and are written to /dev/tty.</p>
<h2>FILES</h2>
<p> /usr/local/bin/pre2ncgm.run</p>
<h2>VERSION</h2>
<p> 1.00 (1-Aug-90)</p>
<h2>SEE ALSO</h2>
<p> ctrans(1NCARG)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
