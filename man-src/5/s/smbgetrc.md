---
title: "smbgetrc(5)"
name: "smbgetrc"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smbgetrc/"
description: "smbgetrc – configuration file for smbget"
---

<p>smbgetrc &#8211; configuration file for smbget</p>
<h2>Synopsis</h2>
<p>smbgetrc</p>
<h2>Description</h2>
<p>This manual page documents the format and options of the <i>smbgetrc</i> file. This is the configuration file used by the <code><a href="/docs/linux/man/1-smbget/">smbget</a></code>(1) utility. The file contains of key-value pairs, one pair on each line. The key and value should be separated by a space. </p>
<p> By default, smbget reads its configuration from <i>$HOME/.smbgetrc</i>, though other locations can be specified using the command-line options.</p>
<h2>Options</h2>
<p>The following keys can be set: </p>
<p> resume on|off</p>
<dl>
<dd>Whether aborted downloads should be automatically resumed.</dl>
<p> recursive on|off</p>
<dl>
<dd>Whether directories should be downloaded recursively</dl>
<p> user <i>name[%password]</i></p>
<dl>
<dd>Username (and password) to use when logging in to the remote server. Use an empty string for anonymous access.</dl>
<p> workgroup <i>wg</i></p>
<dl>
<dd>Workgroup to use when logging in</dl>
<p> nonprompt on|off</p>
<dl>
<dd>Turns off asking for username and password. Useful for scripts.</dl>
<p> debuglevel <i>int</i></p>
<dl>
<dd>(Samba) debuglevel to run at. Useful for tracking down protocol level problems.</dl>
<p> dots on|off</p>
<dl>
<dd>Whether a single dot should be printed for each block that has been downloaded, instead of the default progress indicator.</dl>
<p> blocksize <i>int</i></p>
<dl>
<dd>Number of bytes to put in a block.</dl>
<h2>Version</h2>
<p>This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-smbget/">smbget</a></code>(1) and <code><a href="/docs/linux/man/7-samba/">Samba</a></code>(7).</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> This manual page was written by Jelmer Vernooij</p>
