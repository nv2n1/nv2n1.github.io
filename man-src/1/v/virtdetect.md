---
title: "virtdetect(1)"
name: "virtdetect"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virtdetect/"
description: "virtdetect — Detect if this system is running as a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virtdetect &#8212; Detect if this system is running as a virtual machine </p>
<h2>SYNOPSIS</h2>
<p> virtdetect [ &#8211;verbose ] [ &#8211;detect-host ]</p>
<h2>DESCRIPTION</h2>
<p> Attempts to determine if this system is running under some form of virtualization. </p>
<p> If &#8211;verbose is enabled, each check will be output. Otherwise, only the result will be output. </p>
<p> if &#8211;detect-host is enabled, try and detect virtualization host (as opposed to guest) platforms</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd> Enable debug output</p>
<dt><code>&#8211;detect-host</code></p>
<dd> Try to detect virtualization host (as opposed to guest) platform.</p>
<dt><code>&#8211;help</code></p>
<dd> This help</p>
<dt><code>&#8211;man</code></p>
<dd> Full manpage</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt>&bull;</p>
<dd> 0 &#8211; No virtualization detected</p>
<dt>&bull;</p>
<dd> 1 &#8211; Virtualization detected</p>
<dt>&bull;</p>
<dd> 2 &#8211; More than one kind of virtualization detected</dl>
<h2>SEE ALSO</h2>
<p> Sys::Detect::Virtualization, &lt;<a rel="nofollow" href="http://www.dmo.ca/blog/detecting-virtualization-on-linux">http://www.dmo.ca/blog/detecting-virtualization-on-linux</a>&gt;</p>
<h2>LICENCE AND COPYRIGHT</h2>
<p> Copyright (C) 2009 Roaring Penguin Software Inc. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of either: the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; or the Artistic License. </p>
<h2>Index</h2>
