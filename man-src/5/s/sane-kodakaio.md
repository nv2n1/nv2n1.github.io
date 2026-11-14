---
title: "sane-kodakaio(5)"
name: "sane-kodakaio"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-kodakaio/"
description: "sane-kodakaio – SANE backend for Kodak aio printer / scanners"
---

<p>sane-kodakaio &#8211; SANE backend for Kodak aio printer / scanners</p>
<h2>Description</h2>
<p>The <code>sane-kodakaio</code> library implements a SANE (Scanner Access Now Easy) backend which provides access to Kodak aio printer/scanners, like the ESP and Hero series. This document describes backend version 2.4, which is the first candidate for incorporation in sane-backends. </p>
<h2>Supported Hardware</h2>
<p>This version should support models of the Kodak ESP and Hero series, and possibly some Advent AiO scanners. The ESP 5250 and Hero 9.1 were used to develop the backend, but other models may work. Please see the supported devices list at <i><a rel="nofollow" href="http://www.sane-project.org/sane-backends.html#S-KODAKAIO">http://www.sane-project.org/sane-backends.html#S-KODAKAIO</a></i>. </p>
<p> If you have a model not on that list, or reported as &#8216;untested&#8217;: the best way to determine level of support is to test the scanner directly.</p>
<h2>Configuration File</h2>
<p>The configuration file <i>kodakaio.conf</i> is used to tell the backend how to look for scanners, and provide options controlling the operation of the backend. This file is read each time the frontend asks the backend for a list of scanners, generally only when the frontend starts.</p>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_KODAKAIO</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
</dl>
<h2>Known Issues</h2>
<p>Most hardware options are either not supported or not exposed for control by the user, including: multifeed detection, image compression etc.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7) </p>
<h2>Author</h2>
<p>P. Newall</p>
