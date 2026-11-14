---
title: "cupstestdsc(1)"
name: "cupstestdsc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cupstestdsc/"
description: "cupstestdsc – test conformance of postscript files (deprecated)"
---

<h2 class="name">NAME</h2>
<p> cupstestdsc &#8211; test conformance of postscript files (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> <code>cupstestdsc</code> [ <code>-h</code> ] <i>filename.ps</i> [ &#8230; <i>filenameN.ps</i> ]<br />
 <code>cupstestdsc</code> [ <code>-h</code> ] <code>&#8211;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>cupstestdsc</code> tests the conformance of PostScript files to the Adobe PostScript Language Document Structuring Conventions Specification version 3.0. The results of testing and any other output are sent to the standard output. The second form of the command reads PostScript from the standard input.</p>
<h2>NOTES</h2>
<p> <i>This program is deprecated and will be removed in a future release of CUPS.</i> </p>
<p> <code>cupstestdsc</code> only validates the DSC comments in a PostScript file and does not attempt to validate the PostScript code itself. Developers must ensure that the PostScript they generate follows the rules defined by Adobe. Specifically, all pages must be independent of each other, code outside page descriptions may not affect the graphics state (current font, color, transform matrix, etc.), and device-specific commands such as setpagedevice should not be used.</p>
<h2>SEE ALSO</h2>
<p> CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a>), Adobe PostScript Language Document Structuring Conventions Specification, Version 3.0.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2017 by Apple Inc. </p>
<h2>Index</h2>
