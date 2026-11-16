---
title: "vboxputty(8)"
name: "vboxputty"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vboxputty/"
description: "vboxputty – a self-dialing/-calling vboxgetty"
---

<p>vboxputty &#8211; a self-dialing/-calling vboxgetty</p>
<h2>Synopsis</h2>
<p><code>vboxputty </code> <code>-d</code> <i>device</i> [<code>-f</code> <i>config-file</i>] [<code>-c</code> <i>phonenumber</i>] [<code>-s</code> <i>ring-timeout</i>] [<code>-w</code> <i>wait</i>] [<code>-t</code> <i>redial</i>] [<code>-r</code> <i>redial-pause</i>] </p>
<p> <code>vboxputty </code> [-<code>hv</code>]</p>
<h2>Description</h2>
<p><i>vboxputty</i> is a vboxgetty, not waiting for, but triggering a call. After connect, vboxputty is acting exactly like vboxgetty. <i>vboxputty</i> exits with 0 if a connection was established, 99 on BUSY. </p>
<h2>Options</h2>
<dl>
<dt>-h</dt>
<dd>display a short help</dd>
<dt>-v</dt>
<dd>display the version information</dd>
<dt>-f config-file</dt>
<dd>use <i>config-file</i> instead of the default vboxgetty.conf</dd>
<dt>-d device</dt>
<dd>use <i>device</i> (/dev/ttyI*) for dialout</dd>
<dt>-c phonenumber</dt>
<dd>the phonenumber to be called</dd>
<dt>-s ring-timeout</dt>
<dd>vboxputty will dial the <i>phonenumber</i> and wait <i>ring-timeout</i> seconds for the called party to accept the call, if <i>ring-timeout</i> seconds are ellapsed before connect, vboxputty will hangup.</dd>
<dt>-w wait</dt>
<dd>after the connection is established, vboxputty will wait <i>wait</i> seconds before starting the tcl-script</dd>
<dt>-t redial</dt>
<dd>if the called party is BUSY, vboxputty will try <i>redial</i> times to get a connect</dd>
<dt>-r redial-pause</dt>
<dd>vboxputty waits <i>redial-pause</i> seconds between BUSY-redials</dd></dl>
<h2>Files</h2>
<p><i>/usr/local/vbox/etc/vboxgetty.conf</i></p>
<h2>Author</h2>
<p>Gerrit Pape &lt;pape [at] innominate.de&gt;</p>
<h2>See Also</h2>
<p><code>the vbox-documentation</code> </p>
