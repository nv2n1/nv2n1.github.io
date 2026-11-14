---
title: "font2c(1)"
name: "font2c"
section: "1"
letter: "f"
url: "/docs/linux/man/1-font2c/"
description: "font2c – Write PostScript Type 0 or Type 1 font as C code"
---

<h2>NAME</h2>
<p> font2c &#8211; Write PostScript Type 0 or Type 1 font as C code</p>
<h2>SYNOPSIS</h2>
<p> <code>font2c</code> <i>fontnames</i></p>
<h2>DESCRIPTION</h2>
<p> This script invokes <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) with the following options: </p>
<p> <center> <code>-q -dNODISPLAY -dWRITESYSTEMDICT</code><br />
 </center> </p>
<p> followed by the arguments from the command line. This will write out a PostScript Type 0 or Type 1 font as C code that can be linked with the interpreter.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1)</p>
<h2>VERSION</h2>
<p> This document was last revised for Ghostscript version 9.07.</p>
<h2>AUTHOR</h2>
<p> Artifex Software, Inc. are the primary maintainers of Ghostscript. This manpage by George Ferguson. </p>
<h2>Index</h2>
