---
title: "shadowconfig(8)"
name: "shadowconfig"
section: "8"
letter: "s"
url: "/docs/linux/man/8-shadowconfig/"
description: "shadowconfig – toggle shadow passwords on and off"
---

<p>shadowconfig &#8211; toggle shadow passwords on and off</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>shadowconfig</code> <i>on</i> | <i>off</i> </p>
<h2>Description</h2>
<p><code>shadowconfig</code> on will turn shadow passwords on; <i>shadowconfig off</i> will turn shadow passwords off. <code>shadowconfig</code> will print an error message and exit with a nonzero code if it finds anything awry. If that happens, you should correct the error and run it again. Turning shadow passwords on when they are already on, or off when they are already off, is harmless.</p>
<dd>Read <i>/usr/share/doc/passwd/README.Debian</i> for a brief introduction to shadow passwords and related features. Note that turning shadow passwords off and on again will lose all password aging information. </p>
