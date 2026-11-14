---
title: "afpfsd(1)"
name: "afpfsd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afpfsd/"
description: "afpfsd – Daemon to manage AFP sessions for the afpfs-ng FUSE client."
---

<h2>NAME</h2>
<p> afpfsd &#8211; Daemon to manage AFP sessions for the afpfs-ng FUSE client.</p>
<h2>SYNOPSIS</h2>
<p> <i>afpfsd</i> [<code>-l|logmethod=method</code> [f|&#8211;foreground [d|&#8211;debug </p>
<h2>DESCRIPTION</h2>
<p> afpfsd is a daemon that manages AFP sessions. Functions (like mounting, getting status, etc) can be performed using the <a href="/docs/linux/man/1-afp_client/">afp_client</a>(1) tool. This client communicates with the daemon over a named pipe. </p>
<p> afpfsd will not start if another instance is already running. There needs to be one copy of afpfsd running per user. </p>
<h2>OPTIONS</h2>
<p> <code>-l|&#8211;logmethod</code> sets the method used to log; values are stdout or syslog </p>
<p> <code>-f|&#8211;foreground</code> doesn&#8217;t fork the daemon </p>
<p> <code>-f|&#8211;debug</code> puts the daemon in the foreground and dumps logs to stdout </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-afp_client/">afp_client</a></code>(1), <code><a href="/docs/linux/man/1-mount_afp/">mount_afp</a></code>(1) </p>
<h2>Index</h2>
