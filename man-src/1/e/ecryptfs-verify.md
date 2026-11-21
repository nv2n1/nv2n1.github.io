---

title: "ecryptfs-verify(1)"
name: "ecryptfs-verify"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-verify/"
description: "ecryptfs-verify – validate an eCryptfs encrypted home or encrypted private configuration"
---

<p> <code>ecryptfs-verify</code> [-h|&#8211;home] [-p|&#8211;private] [-e|&#8211;filenames-encrypted] [-n|&#8211;filenames-not-encrypted] [-u|&#8211;user USER] [&#8211;help] </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;home</code></dt>
<dd> True if HOME is correctly configured for encryption, False otherwise</dd>
<dt><code>-p, &#8211;private</code></dt>
<dd> True if a non-HOME directory is correctly configured for encryption, False otherwise</dd>
<dt><code>-e, &#8211;filenames-encrypted</code></dt>
<dd> True if filenames are set for encryption, False otherwise</dd>
<dt><code>-n, &#8211;filenames-not-encrypted</code></dt>
<dd> True if filenames are not encrypted, False otherwise</dd>
<dt><code>-u, &#8211;user USER</code></dt>
<dd> By default, the current user&#8217;s configuration is checked, override with this option</dd>
<dt><code>&#8211;help</code></dt>
<dd> This usage information </dd>
</dl>
<p> Note that options are additive. ALL checks must pass in order for this program to exit 0. Any failing check will cause this program to exit non-zero. </p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
