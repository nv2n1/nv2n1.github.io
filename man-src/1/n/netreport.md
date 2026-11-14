---
title: "netreport(1)"
name: "netreport"
section: "1"
letter: "n"
url: "/docs/linux/man/1-netreport/"
description: "netreport – request notification of network interface changes"
---

<h2>NAME</h2>
<p> netreport &#8211; request notification of network interface changes</p>
<h2>SYNOPSIS</h2>
<p> <code>netreport</code> <i>[</i>-r<i>]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>netreport</code> tells the network management scripts to send a SIGIO signal to the process which called netreport when any network interface status changes occur.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> Remove the current request (if any) for the calling process.</dl>
<h2>NOTES</h2>
<p> If a program does not call netreport with the <code>-r</code> option before it exits, and another process is created with the same PID before any changes take place in interface status, it is possible that the new process will receive a spurious SIGIO. </p>
<h2>Index</h2>
