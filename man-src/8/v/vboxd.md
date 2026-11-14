---
title: "vboxd(8)"
name: "vboxd"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vboxd/"
description: "vboxd – isdn voice box daemon"
---

<p>vboxd &#8211; isdn voice box daemon</p>
<h2>Synopsis</h2>
<p><code>vboxd</code> <i>[OPTION] [OPTION] [&#8230;]</i></p>
<h2>Description</h2>
<p>Vboxd is a daemon which is accessed via tcp/ip and can give you the messages recorded with vboxgetty, or change them. </p>
<p> vboxd uses port 20012 (tcp and udp), as described in /etc/services.</p>
<h2>Options</h2>
<dl>
<dt><code>-f, &#8211;file FILE</code></p>
<dd>Config file to use. Default is the file &#8216;/etc/isdn/vboxd.conf&#8217;.</p>
<dt><code>-t, &#8211;timeout SECS</code></p>
<dd>Timeout for waiting for commands from the client. If no command is received within this time, the daemon exits. Default value is 600 seconds.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Show version of program.</dl>
<h2>Note</h2>
<p>After the start the timeout is set to 30 seconds. It will change after the first command to the value set with &#8211;timeout.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/vboxd.conf</code></p>
<dd>default config file</dl>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
