---
title: "ecryptfs-recover-private(1)"
name: "ecryptfs-recover-private"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-recover-private/"
description: "ecryptfs-recover-private – find and mount any encrypted private directories"
---

<h2 class="name">NAME</h2>
<p> <code>ecryptfs-recover-private</code> &#8211; find and mount any encrypted private directories</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-recover-private</code> [&#8211;rw] [encrypted private dir] </p>
<h2>DESCRIPTION</h2>
<p> This utility is intended to help eCryptfs recover data from their encrypted home or encrypted private partitions. It is useful to run this from a LiveISO or a recovery image. It must run under <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) or with root permission, in order to search the filesystem and perform the mounts. </p>
<p> The program can take a target encrypted directory on the command line. If unspecified, the utility will search the entire system looking for encrypted private directories, as configured by <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a></code>(1). </p>
<p> If an encrypted directory and a <i>wrapped-passphrase</i> file are found, the user is prompted for the login (wrapping) passphrase, the keys are inserted into the keyring, and the data is decrypted and mounted. </p>
<p> If no <i>wrapped-passphrase</i> file is found, the user will be prompted for their mount passphrase. This passphrase is typically 32 characters of [0-9a-f]. All users are prompted to urgently record this randomly generated passphrase when they first setup their encrypted private directory. </p>
<p> The destination mount of the decrypted data is a temporary directory, in the form of <i>/tmp/ecryptfs.XXXXXXXX</i>. </p>
<p> By default, the mount will be read-only. To mount with read and write permission, add the &#8211;rw parameter. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a></code>(1), <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) </p>
<p> <i><a rel="nofollow" href="http://blog.dustinkirkland.com/2009/03/mounting-your-encrypted-home-from.html">http://blog.dustinkirkland.com/2009/03/mounting-your-encrypted-home-from.html</a></i> </p>
<dl>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
