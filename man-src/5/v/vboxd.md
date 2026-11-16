---
title: "vboxd(5)"
name: "vboxd"
section: "5"
letter: "v"
url: "/docs/linux/man/5-vboxd/"
description: "vboxd.conf – config file for vboxd (the daemon)"
---

<p>vboxd.conf &#8211; config file for vboxd (the daemon)</p>
<h2>Description</h2>
<p>This file is used to configure who may access which voice box folders. Everything after &quot;#&quot; is ignored, as are empty lines. All arguments must be separated by whitespace (spaces, tabs). Arguments may not contain whitespace.</p>
<dl>
<dt><code>Login lines</code></dt>
<dd>The login lines set who may connect to the vbox daemon. Hosts that are not in this list are not allowed to connect. <code>Format : L:HOSTPATTERN:ACCESS</code></dd>
<dl>
<dd>
</dd><dl>
<dt><code>HOSTPATTERN</code></dt>
<dd>UN*X pattern of a hostname or ip address.</dd>
<dt><code>ACCESS</code></dt>
<dd>&quot;Y&quot; means access is granted, &quot;N&quot; means access is denied.</dd></dl>
</dl>
<dt><code>Access lines</code></dt>
<dd>The access lines set the password for each user and what rights he or she has. </dd>
<pre><code>Format : A:HOSTPATTERN:MODE:NAME:PASSWORD:SPOOLDIR:INCOMINGDIR</code></pre>
<dl>
<dd>
</dd><dl>
<dt><code>HOSTPATTERN</code></dt>
<dd>UN*X pattern of a hostname or ip address.</dd>
<dt><code>MODE</code></dt>
<dd>Name to use with LOGIN.</dd>
<dt><code>PASSWORD</code></dt>
<dd>Password for LOGIN.</dd>
<dt><code>SPOOLDIR</code></dt>
<dd>Spool directory for this user. You must give the whole path.</dd>
<dt><code>INCOMINGDIR</code></dt>
<dd>Directory with messages for this user. You may give a full path or a path relative to SPOOLDIR.</dd></dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/isdn/vboxd.conf</code></dt>
<dd>this configuration file </dd>
<dt><code>/usr/doc/isdnutils/examples/vboxd.conf</code></dt>
<dd>an example </dd>
</dl>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux.</p>
</dl>