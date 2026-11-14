---
title: "idevicecrashreport(1)"
name: "idevicecrashreport"
section: "1"
letter: "i"
url: "/docs/linux/man/1-idevicecrashreport/"
description: "idevicecrashreport – Retrieve crash reports from a device."
---

<h2>NAME</h2>
<p> idevicecrashreport &#8211; Retrieve crash reports from a device.</p>
<h2>SYNOPSIS</h2>
<p> <code>idevicecrashreport</code> [OPTIONS] DIRECTORY </p>
<h2>DESCRIPTION</h2>
<p> Simple utility to move crash reports from a device to a local directory. </p>
<p> The utility outputs lines prefixed with either &quot;Link:&quot;, &quot;Copy:&quot; or &quot;Move:&quot; depending on whether a symlink was created, a file was copied or moved from the device to the target DIRECTORY. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e, &#8211;extract</code></p>
<dd> extract raw crash report into separate &#8216;.crash&#8217; files.</p>
<dt><code>-k, &#8211;keep</code></p>
<dd> copy but do not remove crash reports from device.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> enable communication debugging.</p>
<dt><code>-u, &#8211;udid UDID</code></p>
<dd> target specific device by its 40-digit device UDID.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> prints usage information. </p>
</dl>
<h2>AUTHOR</h2>
<p> Martin Szulecki </p>
<p> Nikias Bassen </p>
<h2>Index</h2>
