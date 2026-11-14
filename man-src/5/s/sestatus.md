---
title: "sestatus(5)"
name: "sestatus"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sestatus/"
description: "sestatus.conf – The"
---

<p>sestatus.conf &#8211; The <code></p>
<p><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8) configuration file. </p>
<h2>Description</h2>
<p>The <i>sestatus.conf</i> file is used by the <code><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8) command with the <code>-v</code> option to determine what file and process security contexts should be displayed. The fully qualified path name of the configuration file is:</p>
<dl>
<dd><i>/etc/sestatus.conf</i></dl>
<p> The file consists of two optional sections as described in the <code>FILE FORMAT</code> section. Whether these exist or not, the following will always be displayed:</p>
<dl>
<dd>The current process context<br />
 The init process context<br />
 The controlling terminal file context</dl>
<h2>File Format</h2>
<p>The format consists of two optional sections as follows:</p>
<dl>
<dd><code>[files]</code><br />
 <i>file_name</i><br />
 <i>[file_name]</i><br />
 <i>&#8230;</i> </p>
<p> <code>[process]</code><br />
 <i>executable_file_name</i><br />
 <i>[executable_file_name]</i><br />
 <i>&#8230;</i></dl>
<p> Where:</p>
<dl>
<dd><code>[files]</code></p>
<dl>
<dd>The start of the file list block.</dl>
<p> <i>file_name</i></p>
<dl>
<dd>One or more fully qualified file names, each on a new line will that will have its context displayed. If the file does not exist, then it is ignored. If the file is a symbolic link, then <code>sestatus -v</code> will also display the target file context.</dl>
<p> <code>[process]</code></p>
<dl>
<dd>The start of the process list block.</dl>
<p> <i>executable_file_name</i></p>
<dl>
<dd>One or more fully qualified executable file names that should it be an active process, have its context displayed. Each entry is on a new line.</dl>
</dl>
<h2>Example</h2>
<p># /etc/sestatus.conf<br />
 [files]<br />
 /etc/passwd<br />
 /etc/shadow<br />
 /bin/bash<br />
 /bin/login<br />
 /lib/libc.so.6<br />
 /lib/ld-linux.so.2<br />
 /lib/ld.so.1 [process]<br />
 /sbin/mingetty<br />
 /sbin/agetty<br />
 /usr/sbin/sshd </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/8-sestatus/">sestatus</a></code>(8) </p>
