---
title: "ncargrun(1)"
name: "ncargrun"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncargrun/"
description: "ncargrun – to run a user program and redirect the metafile output"
---

<h2>NAME</h2>
<p> ncargrun &#8211; to run a user program and redirect the metafile output</p>
<h2>SYNOPSIS</h2>
<p> <code>ncargrun</code> <code>program-name</code> [<code>-t</code>] [<code>-o metafile-name</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>ncargrun</i> is a script that invokes &quot;program-name&quot;, which uses the NCAR GKS library, and applies the specified options. </p>
<p> Prior to running your program, this script sets the environment variables NCARG_GKS_OUTPUT, NCARG_GKS_PSOUTPUT, and NCARG_GKS_PDFOUTPUT to produce the desired effect.</p>
<h2>OPTIONS</h2>
<p> <code>-o</code><i> </i><code>filename</code> </p>
<p> specifies the name of the output metafile or PostScript file. If filename is replaced by &quot;| translator-name&quot;, the effect is to pipe the metafile to the named translator. </p>
<p> <code>-t</code><i> </i> specifies that metafile output should be piped to the default translator &quot;ctrans&quot;. </p>
<h2>SEE ALSO</h2>
<p> <code>ncarg_gks(1NCARG),</code> <code>ncarg_env(5NCARG),</code> <code>ncargintro(5NCARG)</code></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
