---
title: "archdetect(1)"
name: "archdetect"
section: "1"
letter: "a"
url: "/docs/linux/man/1-archdetect/"
description: "archdetect – detect hardware architecture"
---

<h2 class="name">NAME</h2>
<p> <code>archdetect</code> &#8211; detect hardware architecture </p>
<h2>SYNOPSIS</h2>
<p> [-<code>g</code> ]</p>
<h2>DESCRIPTION</h2>
<p> displays the current machine architecture and subarchitecture. The architecture corresponds to that built into <code>dpkg</code> and describes the CPU (and possibly kernel) types; the subarchitecture distinguishes machines with different boot arrangements that require special handling. </p>
<p> The following option is available:</p>
<dl>
<dt><code>-g</code></p>
<dd> When bringing up new subarchitectures, may not yet have been taught about this specific machine. This option asks that try to guess a generic subarchitecture that may be compatible with this machine. This is only necessary on certain architectures, and simply has no effect elsewhere.</dl>
<h2>AUTHORS</h2>
<p> was written by the Debian Installer team. </p>
<h2>Index</h2>
