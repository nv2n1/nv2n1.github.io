---
title: "psblack(1)"
name: "psblack"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psblack/"
description: "psblack – PostScript filter."
---

<h2>NAME</h2>
<p> psblack &#8211; PostScript filter.</p>
<h2>SYNOPSIS</h2>
<p> <code>psblack</code> <i>&lt; input_PostScript_file</i> <i>&gt; output_PostScript_file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>psblack</code> is a filter which reads a PostScript file as input and writes a PostScript file as output. In the output file the filter forces a black background and scales the intensity values (values with R=G=B) so that any intensity greater than or equal to .8 is mapped to white. This filter works only on PostScript files produced by ctrans &#8211; the CGM translator in the NCAR Graphics software.</p>
<h2>SEE ALSO</h2>
<p> ctrans(1NCARG), pswhite(1NCARG)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
