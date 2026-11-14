---
title: "libwacom-list-devices(1)"
name: "libwacom-list-devices"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libwacom-list-devices/"
description: "libwacom-list-devices – utility to list supported tablet devices"
---

<h2 class="name">NAME</h2>
<p> libwacom-list-devices &#8211; utility to list supported tablet devices</p>
<h2>SYNOPSIS</h2>
<p> <code>libwacom-list-devices [&#8211;format=yaml|datafile]</code> </p>
<h2>DESCRIPTION</h2>
<p> libwacom-list-devices is a debug utility to list all supported tablet devices identified by libwacom. It is usually used to check whether a libwacom installation is correct after adding custom data files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;format=yaml|datafile</code></p>
<dd> Sets the output format to be used. If <i>yaml</i>, the output format is YAML comprising the bus type, vendor and product ID and the device name. If <i>datafile</i>, the output format matches the tablet data files. The default is <i>yaml</i>. </p>
</dl>
<h2>Index</h2>
