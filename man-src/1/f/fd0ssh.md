---
title: "fd0ssh(1)"
name: "fd0ssh"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fd0ssh/"
description: "fd0ssh — pipe for password-over-stdin support to ssh"
---

<h2>Name</h2>
<p> fd0ssh &#8212; pipe for password-over-stdin support to ssh</p>
<h2>Syntax</h2>
<p> <code>fd0ssh</code> <i>mount_command</i></p>
<h2>Description</h2>
<p> This is a wrapper for ssh which reads the password from stdin and sets things up so that ssh will recall the wrapper to get the password, which will be read from the parent process using a pipe. </p>
<p> It is used by <code><a href="/docs/linux/man/8-pam_mount/">pam_mount</a></code>(8) to mount SSH-based filesystems, such as ccgfs and sshfs.</p>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/7-hxtools/">hxtools</a></code>(7) </p>
<p> Idea by John S. Skogtvedt, <a rel="nofollow" href="http://www.debian-administration.org/articles/587">http://www.debian-administration.org/articles/587</a> </p>
<h2>Index</h2>
