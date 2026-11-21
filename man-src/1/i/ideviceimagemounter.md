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
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-l, &#8211;list</code></dt>
<dd> list mount information</dd>
<dt><code>-t, &#8211;imagetype NAME</code></dt>
<dd> the image type to use, default is &#8216;Developer&#8217;</dd>
<dt><code>-x, &#8211;xml</code></dt>
<dd> use XML output</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information</dd>
<dt><code>IMAGE_FILE</code></dt>
<dd> the image filename to mount</dd>
<dt><code>IMAGE_SIGNATURE_FILE</code></dt>
<dd> corresponding signature file for image filename </dd>
</dl>
<h2>AUTHOR</h2>
<p> Nikias Bassen </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
