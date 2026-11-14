---
title: "vboxd-conf(5)"
name: "vboxd-conf"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vboxd-conf/"
description: "vboxd.conf – config file for vboxd (the daemon)"
---

<p>vboxd.conf &#8211; config file for vboxd (the daemon)</p>
<h2>Description</h2>
<p>This file is used to configure who may access which voice box folders. Everything after &quot;#&quot; is ignored, as are empty lines. All arguments must be separated by whitespace (spaces, tabs). Arguments may not contain whitespace.</p>
<dl>
<dt><code>Login lines</code></p>
<dd>The login lines set who may connect to the vbox daemon. Hosts that are not in this list are not allowed to connect. <code>Format : L:HOSTPATTERN:ACCESS</code></p>
<dl>
<dd>
<dl>
<dt><code>HOSTPATTERN</code></p>
<dd>UN*X pattern of a hostname or ip address.</p>
<dt><code>ACCESS</code></p>
<dd>&quot;Y&quot; means access is granted, &quot;N&quot; means access is denied.</dl>
</dl>
<dt><code>Access lines</code></p>
<dd>The access lines set the password for each user and what rights he or she has. </p>
<pre><code>Format : A:HOSTPATTERN:MODE:NAME:PASSWORD:SPOOLDIR:INCOMINGDIR</code></pre>
<dl>
<dd>
<dl>
<dt><code>HOSTPATTERN</code></p>
<dd>UN*X pattern of a hostname or ip address.</p>
<dt><code>MODE</code></p>
<dd>Name to use with LOGIN.</p>
<dt><code>PASSWORD</code></p>
<dd>Password for LOGIN.</p>
<dt><code>SPOOLDIR</code></p>
<dd>Spool directory for this user. You must give the whole path.</p>
<dt><code>INCOMINGDIR</code></p>
<dd>Directory with messages for this user. You may give a full path or a path relative to SPOOLDIR.</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/vboxd.conf</code></p>
<dd>this configuration file </p>
<dt><code>/usr/doc/isdnutils/examples/vboxd.conf</code></p>
<dd>an example </p>
</dl>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
