---
title: "drv(7)"
name: "drv"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drv/"
description: "drv – cups driver interface for ppd compiler files"
---

<p>drv &#8211; cups driver interface for ppd compiler files</p>
<h2>Synopsis</h2>
<p><code>drv list</code><br />
 <code>drv cat</code> <i><a href="drv:///filename.drv/pcfilename">drv:///filename.drv/pcfilename</a></i></p>
<h2>Description</h2>
<p><i>drv</i> lists and compiles PPDC source files installed in the /usr/share/cups/drv and (on Mac OS X) /Library/Printers/PPDs/Contents/Resources directories on behalf of the scheduler, <i><a href="/docs/linux/man/8-cupsd/">cupsd</a>(8)</i>. </p>
<p> The first form of the command lists all of the PPD files that can be produced by the driver information files in the two directories. </p>
<p> The second form of the command compiles the requested PPD and sends it to the standard output.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ppdc/">ppdc</a>(1), <a href="/docs/linux/man/1-ppdhtml/">ppdhtml</a>(1), <a href="/docs/linux/man/1-ppdi/">ppdi</a>(1), <a href="/docs/linux/man/1-ppdmerge/">ppdmerge</a>(1), <a href="/docs/linux/man/1-ppdpo/">ppdpo</a>(1), <a href="/docs/linux/man/5-ppdcfile/">ppdcfile</a>(5)<br />
 <a rel="nofollow" href="http://localhost:631/help">http://localhost:631/help</a></p>
<h2>Copyright</h2>
<p>Copyright 2008-2009 by Apple Inc.</p>
