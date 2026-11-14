---
title: "ecryptfs-verify(1)"
name: "ecryptfs-verify"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-verify/"
description: "ecryptfs-verify – validate an eCryptfs encrypted home or encrypted private configuration"
---

<h2 class="name">NAME</h2>
<p> ecryptfs-verify &#8211; validate an eCryptfs encrypted home or encrypted private configuration</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-verify</code> [-h|&#8211;home] [-p|&#8211;private] [-e|&#8211;filenames-encrypted] [-n|&#8211;filenames-not-encrypted] [-u|&#8211;user USER] [&#8211;help] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;home</code></p>
<dd> True if HOME is correctly configured for encryption, False otherwise</p>
<dt><code>-p, &#8211;private</code></p>
<dd> True if a non-HOME directory is correctly configured for encryption, False otherwise</p>
<dt><code>-e, &#8211;filenames-encrypted</code></p>
<dd> True if filenames are set for encryption, False otherwise</p>
<dt><code>-n, &#8211;filenames-not-encrypted</code></p>
<dd> True if filenames are not encrypted, False otherwise</p>
<dt><code>-u, &#8211;user USER</code></p>
<dd> By default, the current user&#8217;s configuration is checked, override with this option</p>
<dt><code>&#8211;help</code></p>
<dd> This usage information </p>
</dl>
<h2>DESCRIPTION</h2>
<p> Note that options are additive. ALL checks must pass in order for this program to exit 0. Any failing check will cause this program to exit non-zero. </p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
