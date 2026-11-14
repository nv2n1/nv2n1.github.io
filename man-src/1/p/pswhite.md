---
title: "pswhite(1)"
name: "pswhite"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pswhite/"
description: "pswhite – PostScript filter."
---

<h2>NAME</h2>
<p> pswhite &#8211; PostScript filter.</p>
<h2>SYNOPSIS</h2>
<p> <code>pswhite</code> <i>&lt; input_PostScript_file</i> <i>&gt; output_PostScript_file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>pswhite</code> is a filter which reads a PostScript file as input and writes a PostScript file as output. In the output file the filter forces a white background and complements the intensity values (values with R=G=B) so that the default white foreground appears as black on the white background. This filter works only on PostScript files produced by ctrans &#8211; the CGM translator in the NCAR Graphics software.</p>
<h2>SEE ALSO</h2>
<p> ctrans(1NCARG), psblack(1NCARG)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
