---
title: "showconsolefont(8)"
name: "showconsolefont"
section: "8"
letter: "s"
url: "/docs/linux/man/8-showconsolefont/"
description: "showconsolefont – Show the current EGA/VGA console screen font"
---

<p>showconsolefont &#8211; Show the current EGA/VGA console screen font</p>
<h2>Synopsis</h2>
<p><code>showconsolefont</code> [ <code>-V | &#8211;version</code> ] [ <code>-v</code> ] [ <code>-i</code> ] [ <code>-C</code> <i>console</i> ] </p>
<h2>Description</h2>
<p>The <code>showconsolefont</code> command outputs the current console font to stdout. The option <code>-v</code> prints additional information, while the option <code>-V</code> prints the program version number. The option <code>-i</code> doesn&#8217;t print out the font table, just shows ROWSxCOLSxCOUNT and exits. On Linux 2.6.1 and later, the option <code>-C</code> allows one to indicate the console involved. Its argument is a pathname. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8) </p>
