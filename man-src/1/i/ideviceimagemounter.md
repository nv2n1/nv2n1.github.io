---
title: "ideviceimagemounter(1)"
name: "ideviceimagemounter"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ideviceimagemounter/"
description: "ideviceimagemounter – Mount disk images on the device."
---

<h2>NAME</h2>
<p> ideviceimagemounter &#8211; Mount disk images on the device.</p>
<h2>SYNOPSIS</h2>
<p> <code>ideviceimagemounter</code> [OPTIONS] IMAGE_FILE IMAGE_SIGNATURE_FILE </p>
<h2>DESCRIPTION</h2>
<p> Mounts the specified disk image on the device. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable communication debugging.</p>
<dt><code>-u, &#8211;udid UDID</code></p>
<dd> target specific device by its 40-digit device UDID.</p>
<dt><code>-l, &#8211;list</code></p>
<dd> list mount information</p>
<dt><code>-t, &#8211;imagetype NAME</code></p>
<dd> the image type to use, default is &#8216;Developer&#8217;</p>
<dt><code>-x, &#8211;xml</code></p>
<dd> use XML output</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information</p>
<dt><code>IMAGE_FILE</code></p>
<dd> the image filename to mount</p>
<dt><code>IMAGE_SIGNATURE_FILE</code></p>
<dd> corresponding signature file for image filename </p>
</dl>
<h2>AUTHOR</h2>
<p> Nikias Bassen </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
<h2>Index</h2>
