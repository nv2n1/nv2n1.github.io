---
title: "pt_chown(5)"
name: "pt_chown"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pt_chown/"
description: "pt_chown – helper function for grantpt(3), changes ownship and permissions of pseudotty"
---

<p>pt_chown &#8211; helper function for <a href="/docs/linux/man/3-grantpt/">grantpt</a>(3), changes ownship and permissions of pseudotty</p>
<h2>Synopsis</h2>
<p>/usr/lib/pt_chown </p>
<h2>Description</h2>
<p><code>pt_chown</code> is the helper program for the &#8216;grantpt&#8217; function. It is not intended to be run directly from the command line. pt_chown sets the owner, group and access permission of the slave pseudo terminal corresponding to the master pseudo terminal passed on file descriptor so that the pseudo terminal can be used by the calling process. This means programs like &#8216;xterm&#8217; and &#8216;screen&#8217; do not have to be setuid to get a pty. (There may be other reasons why they need privileges.) If you are using a 2.1 or newer Linux kernel with the &#8216;devptsfs&#8217; or `devfs&#8217; filesystems providing pty slaves, you don&#8217;t need this program; otherwise you do. The source for &#8216;pt_chown&#8217; is in &#8216;login/programs/pt_chown.c&#8217;. It is installed setuid root. </p>
<h2>Options</h2>
<p>pt_chown takes no arguments.</p>
<h2>Return Codes</h2>
<p><code>pt_chown</code> has the following return codes:</p>
<dl>
<dt>EBADF</p>
<dd>The file descriptor is not a valid master pseudo terminal. </p>
<dt>EINVAL</p>
<dd>The device is not a character device. </p>
<dt>EACCES</p>
<dd>Can&#8217;t change device owner and group or device permissions. </p>
<dt>0</p>
<dd>The owner, group, and permissions were successfully changed. </p>
</dl>
<h2>Bugs</h2>
<p>Report bugs using the glibcbug script to bugs [at] gnu.org </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3) </p>
