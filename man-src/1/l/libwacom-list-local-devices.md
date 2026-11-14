---
title: "libwacom-list-local-devices(1)"
name: "libwacom-list-local-devices"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libwacom-list-local-devices/"
description: "libwacom-list-local-devices – utility to list tablet devices"
---

<h2 class="name">NAME</h2>
<p> libwacom-list-local-devices &#8211; utility to list tablet devices</p>
<h2>SYNOPSIS</h2>
<p> <code>libwacom-list-local-devices [&#8211;format=oneline|datafile] [&#8211;database /path/to/datadir]</code> </p>
<h2>DESCRIPTION</h2>
<p> libwacom-list-local-devices is a debug utility to list connected tablet devices identified by libwacom. It is usually used to check whether a libwacom data file is correct, present and/or applies to a specific device.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;format=oneline|datafile</code></p>
<dd> Sets the output format to be used. If <i>oneline</i>, the output format is a one-line format comprising the device name and the event nodes. If <i>datafile</i>, the output format matches the tablet data files. The default is <i>oneline</i>.</p>
<dt><code>&#8211;database /path/do/datadir</code></p>
<dd> Sets the data directory path to be used. This is only useful when testing against a modified data path. Only libwacom developers need this option.</dl>
<h2>NOTES</h2>
<p> The Linux kernel provides separate <i>/dev/input/event*</i> nodes for the stylus, the pad and the touch part of the tablet. These devices nodes are listed as part of this tool&#8217;s output. </p>
<p> This tool is unable to distinguish between multiple identical devices. Only one such device will be listed, with all event nodes from all devices that are of the same type. </p>
<h2>Index</h2>
