---
title: "fstobdf(1)"
name: "fstobdf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fstobdf/"
description: "fstobdf – generate BDF font from X font server"
---

<h2 class="name">NAME</h2>
<p> fstobdf &#8211; generate BDF font from X font server </p>
<h2>SYNOPSIS</h2>
<p> <code>fstobdf</code> [ <code>-server</code> <i>servername</i> ] <code>-fn</code> <i>fontname</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>fstobdf</i> program reads a font from a font server and prints a BDF file on the standard output that may be used to recreate the font. This is useful in testing servers, debugging font metrics, and reproducing lost BDF files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-server </code><i>servername</i></dt>
<dd> This option specifies the server from which the font should be read. <i>servername</i> must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7). If not specified, the server name in the <code>FONTSERVER</code> environment variable is used.</dd>
<dt><code>-fn </code><i>fontname</i></dt>
<dd> This option specifies the font for which a BDF file should be generated.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FONTSERVER</code></dt>
<dd> The default server to use. The server name must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7).</dd></dl>
<h2>SEE ALSO</h2>
<p> xfs(1), <a href="/docs/linux/man/1-bdftopcf/">bdftopcf</a>(1), <a href="/docs/linux/man/1-showfont/">showfont</a>(1), <a href="/docs/linux/man/1-fslsfonts/">fslsfonts</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>AUTHOR</h2>
<p> Olaf Brandt, Network Computing Devices<br />
 Dave Lemke, Network Computing Devices </p>
<p> Jim Fulton, MIT X Consortium </p>
