---
title: "xfsinfo(1)"
name: "xfsinfo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfsinfo/"
description: "xfsinfo – X font server information utility"
---

<h2 class="name">NAME</h2>
<p> xfsinfo &#8211; X font server information utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xfsinfo</code> [-server <i>servername</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xfsinfo</i> is a utility for displaying information about an X font server. It is used to examine the capabilities of a server, the predefined values for various parameters used in communicating between clients and the server, and the font catalogues and alternate servers that are available.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-server </code><i>servername</i></p>
<dd> This option specifies the X font server to contact. <i>servername</i> must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7). If not specified, the server name in the <code>FONTSERVER</code> environment variable is used.</dl>
<h2>HISTORY</h2>
<p> <i>Xfsinfo</i> was originally called <i>fsinfo.</i> It was renamed to avoid a clash with the <i>fsinfo</i> utility from the Berkeley automounter <i>amd.</i></p>
<h2>EXAMPLE</h2>
<p> The following shows a sample produced by <i>xfsinfo</i>. </p>
<pre>
example% xfsinfo -server hansen:7100
name of server: hansen:7100
version number: 1
vendor string:  Font Server Prototype
vendor release number:  17
maximum request size:   16384 longwords (65536 bytes)
number of catalogues:   1
        all
Number of alternate servers: 2
    #0  hansen:7101
    #1  hansen:7102
number of extensions:   0
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>FONTSERVER</code></p>
<dd> To get the default fontserver. The server name must be specified in one of the formats defined in the <i>Font Server Names</i> section of <a href="/docs/linux/man/7-x/">X</a>(7).</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xfs/">xfs</a>(1), <a href="/docs/linux/man/1-fslsfonts/">fslsfonts</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<h2>AUTHOR</h2>
<p> Dave Lemke, Network Computing Devices, Inc </p>
<h2>Index</h2>
