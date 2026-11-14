---
title: "svdrpsend(1)"
name: "svdrpsend"
section: "1"
letter: "s"
url: "/docs/linux/man/1-svdrpsend/"
description: "svdrpsend – sends commands to VDR"
---

<h2>NAME</h2>
<p> svdrpsend &#8211; sends commands to VDR</p>
<h2>SYNOPSIS</h2>
<p> svdrpsend [<i>options</i>] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> This program sends commands to VDR (the Video Disk Recorder) and displays the result. A list of available commands can be shown by sending the HELP command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> <i>hostname</i></p>
<dd> Accesses the VDR at the specified <i>hostname</i> (default is localhost).</p>
<dt><code>-p</code> <i>port</i></p>
<dd> Uses the SVDRP port number <i>port</i> (default is 6419).</dl>
<h2>EXAMPLES</h2>
<p> To request the available commands from the VDR running on the local host: </p>
<p> svdrpsend HELP</p>
<h2>AUTHORS</h2>
<p> Written by Tobias Grimm &lt;tg [at] e-tobi.net&gt; </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-vdr/">vdr</a>(1), <a href="/docs/linux/man/5-vdr/">vdr</a>(5) </p>
<h2>Index</h2>
