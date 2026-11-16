---
title: "ideviceinfo(1)"
name: "ideviceinfo"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ideviceinfo/"
description: "ideviceinfo – Show information about the first connected device."
---

<h2>NAME</h2>
<p> ideviceinfo &#8211; Show information about the first connected device.</p>
<h2>SYNOPSIS</h2>
<p> <code>ideviceinfo</code> [OPTIONS] </p>
<h2>DESCRIPTION</h2>
<p> Show information about the first connected device. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;debug</code></dt>
<dd> enable communication debugging.</dd>
<dt><code>-u, &#8211;udid UDID</code></dt>
<dd> target specific device by its 40-digit device UDID.</dd>
<dt><code>-q, &#8211;domain NAME</code></dt>
<dd> set domain of query to NAME. Default: None.</dd>
<dt><code>-k, &#8211;key NAME</code></dt>
<dd> only query key specified by NAME. Default: All keys.</dd>
<dt><code>-x, &#8211;xml</code></dt>
<dd> output information as xml plist instead of key/value pairs.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> prints usage information </dd>
</dl>
<h2>AUTHOR</h2>
<p> Martin Szulecki </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
<h2>Index</h2>
