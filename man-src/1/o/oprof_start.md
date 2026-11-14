---
title: "oprof_start(1)"
name: "oprof_start"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oprof_start/"
description: "oprof_start – A GUI interface for OProfile"
---

<h2 class="name">NAME</h2>
<p> oprof_start &#8211; A GUI interface for OProfile </p>
<h2>SYNOPSIS</h2>
<p> <code>oprof_start</code> [ <i>options</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>oprof_start</code> application provides a GUI interface to control the operation of OProfile. Running <code>oprof_start</code> requires root privileges and does not support <code>operf</code> due to <code>oprof_start</code> using the older <code>opcontrol</code> script. </p>
<h2>ENVIRONMENT</h2>
<p> No special environment variables are recognised by oprof_start. </p>
<h2>FILES</h2>
<dl>
<dt><i>/root/.oprofile/daemonrc</i></p>
<dd> Configuration file for opcontrol</p>
<dt><i>/var/lib/oprofile/samples/</i></p>
<dd> The location of the generated sample files. </p>
</dl>
<h2>VERSION</h2>
<dl>
<dt>This man page is current for oprofile-0.9.9.</p>
<dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>/usr/share/doc/oprofile/,</code> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a>(1)</code> </p>
<h2>Index</h2>
